# coding: utf-8

"""Runtime customizations for generated WHMCS models."""

from __future__ import annotations

import warnings
from collections.abc import Mapping
import re
from types import NoneType, UnionType
from typing import Annotated, Any, Optional, Union, get_args, get_origin

warnings.filterwarnings(
    "ignore",
    message='Field name "register" in "TldPricingInfo" shadows an attribute in parent "BaseModel"',
)


_INT_PATTERN = re.compile(r"^[+-]?\d+$")


def _unwrap_annotation(annotation: Any) -> Any:
    origin = get_origin(annotation)
    if origin is Annotated:
        return _unwrap_annotation(get_args(annotation)[0])

    if origin in (Union, UnionType):
        args = [arg for arg in get_args(annotation) if arg is not NoneType]
        if len(args) == 1:
            return _unwrap_annotation(args[0])

    return annotation


def _normalize_value(annotation: Any, value: Any) -> Any:
    if value is None:
        return None

    annotation = _unwrap_annotation(annotation)
    origin = get_origin(annotation)

    if isinstance(annotation, type) and hasattr(annotation, "model_fields"):
        if isinstance(value, Mapping):
            return _normalize_model_payload(annotation, value)
        return value

    if origin is list:
        item_annotation = get_args(annotation)[0] if get_args(annotation) else Any
        if isinstance(value, list):
            return [_normalize_value(item_annotation, item) for item in value]
        return value

    if origin is dict:
        value_args = get_args(annotation)
        item_annotation = value_args[1] if len(value_args) > 1 else Any
        if isinstance(value, Mapping):
            return {
                key: _normalize_value(item_annotation, item)
                for key, item in value.items()
            }
        return value

    if annotation is int and isinstance(value, str):
        stripped = value.strip()
        if stripped == "":
            return None

        if _INT_PATTERN.fullmatch(stripped):
            return int(stripped)

    return value


def _normalize_model_payload(model_cls: Any, payload: Mapping[str, Any]) -> dict[str, Any]:
    normalized = dict(payload)
    field_map: dict[str, Any] = {}

    for field_name, field in model_cls.model_fields.items():
        field_map[field_name] = field
        field_alias = getattr(field, "alias", None)
        if field_alias:
            field_map[field_alias] = field

    for key, value in list(normalized.items()):
        field = field_map.get(key)
        if field is None:
            continue

        normalized[key] = _normalize_value(field.annotation, value)

    return normalized


def _patch_from_dict(model_cls: Any) -> None:
    def _from_dict(cls, obj):
        if obj is None:
            return None

        if not isinstance(obj, Mapping):
            return cls.model_validate(obj)

        return cls.model_validate(_normalize_model_payload(cls, obj))

    model_cls.from_dict = classmethod(_from_dict)


def _should_patch_model(model_cls: Any) -> bool:
    if not isinstance(model_cls, type) or not hasattr(model_cls, "model_fields"):
        return False

    model_fields = getattr(model_cls, "model_fields", {})
    if "actual_instance" in model_fields:
        return False

    if "additional_properties" in model_fields:
        return False

    return True


def _coerce_bool(value: Any) -> Any:
    if value in (None, ""):
        return value

    if isinstance(value, bool):
        return value

    if isinstance(value, (int, float)):
        return bool(value)

    if isinstance(value, str):
        lowered = value.strip().lower()
        if lowered in {"1", "true", "yes", "on"}:
            return True
        if lowered in {"0", "false", "no", "off"}:
            return False

    return value


def _normalize_domain_row(raw_domain: Mapping[str, Any]) -> dict[str, Any]:
    normalized = dict(raw_domain)

    for key in ("id", "userid", "orderid", "regperiod", "promoid"):
        value = normalized.get(key)
        if isinstance(value, str) and value.isdigit():
            normalized[key] = int(value)

    for key in ("firstpaymentamount", "recurringamount"):
        value = normalized.get(key)
        if isinstance(value, str) and value != "":
            normalized[key] = float(value)

    for key in ("dnsmanagement", "emailforwarding", "idprotection", "donotrenew"):
        normalized[key] = _coerce_bool(normalized.get(key))

    if normalized.get("expirydate") == "0000-00-00":
        normalized["expirydate"] = None

    return normalized


def _normalize_domains(raw_domains: Any) -> Optional[list[Any]]:
    if raw_domains is None:
        return None

    if raw_domains == "":
        return []

    if isinstance(raw_domains, Mapping):
        raw_domains = raw_domains.get("domain")
        if raw_domains is None:
            return []

    if isinstance(raw_domains, list):
        # pylint: disable=import-outside-toplevel
        from whmcs_client.models.domain_info import DomainInfo

        normalized_domains = []
        for item in raw_domains:
            if isinstance(item, Mapping):
                normalized_domains.append(DomainInfo.from_dict(_normalize_domain_row(item)))
            else:
                normalized_domains.append(item)
        return normalized_domains

    return raw_domains


def _get_clients_domains_response_from_dict(cls, obj):
    if obj is None:
        return None

    if not isinstance(obj, dict):
        return cls.model_validate(obj)

    normalized = _normalize_model_payload(cls, obj)

    return cls.model_construct(
        result=normalized.get("result"),
        message=normalized.get("message"),
        clientid=normalized.get("clientid"),
        domainid=normalized.get("domainid"),
        totalresults=normalized.get("totalresults"),
        startnumber=normalized.get("startnumber"),
        numreturned=normalized.get("numreturned"),
        domains=_normalize_domains(obj.get("domains")),
    )


def _get_clients_domains_response_to_dict(self):
    output = {}

    if self.result is not None:
        output["result"] = self.result
    if self.message is not None:
        output["message"] = self.message
    if self.clientid is not None:
        output["clientid"] = self.clientid
    if self.domainid is not None:
        output["domainid"] = self.domainid
    if self.totalresults is not None:
        output["totalresults"] = self.totalresults
    if self.startnumber is not None:
        output["startnumber"] = self.startnumber
    if self.numreturned is not None:
        output["numreturned"] = self.numreturned

    domains = self.domains
    if domains is not None:
        if isinstance(domains, list):
            output["domains"] = [
                item.to_dict() if hasattr(item, "to_dict") and callable(item.to_dict) else item
                for item in domains
            ]
        elif hasattr(domains, "to_dict") and callable(domains.to_dict):
            output["domains"] = domains.to_dict()
        else:
            output["domains"] = domains

    return output


def apply_customizations():
    """Apply runtime customizations to generated models."""

    # pylint: disable=import-outside-toplevel
    import whmcs_client.models as models_package
    from whmcs_client.models.get_clients_domains_response import GetClientsDomainsResponse

    for model_name in dir(models_package):
        model_cls = getattr(models_package, model_name)
        if _should_patch_model(model_cls):
            _patch_from_dict(model_cls)

    GetClientsDomainsResponse.from_dict = classmethod(_get_clients_domains_response_from_dict)
    GetClientsDomainsResponse.to_dict = _get_clients_domains_response_to_dict
