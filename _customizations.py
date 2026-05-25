# coding: utf-8

from __future__ import annotations

import warnings
from collections.abc import Mapping
from typing import Any, Optional

warnings.filterwarnings(
    "ignore",
    message='Field name "register" in "TldPricingInfo" shadows an attribute in parent "BaseModel"',
)


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

    return cls.model_construct(
        result=obj.get("result"),
        message=obj.get("message"),
        clientid=obj.get("clientid"),
        domainid=obj.get("domainid"),
        totalresults=obj.get("totalresults"),
        startnumber=obj.get("startnumber"),
        numreturned=obj.get("numreturned"),
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
    from whmcs_client.models.domain_info import DomainInfo
    from whmcs_client.models.get_clients_domains_response import GetClientsDomainsResponse

    GetClientsDomainsResponse.from_dict = classmethod(_get_clients_domains_response_from_dict)
    GetClientsDomainsResponse.to_dict = _get_clients_domains_response_to_dict
