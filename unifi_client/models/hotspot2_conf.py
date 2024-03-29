# coding: utf-8

"""
    Unifi API

    Unifi Controller API

    The version of the OpenAPI document: 8.0.26
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from pydantic import Field
from unifi_client.models.hotspot2_conf_capab import Hotspot2ConfCapab
from unifi_client.models.hotspot2_conf_cellular_network_list import Hotspot2ConfCellularNetworkList
from unifi_client.models.hotspot2_conf_friendly_name import Hotspot2ConfFriendlyName
from unifi_client.models.hotspot2_conf_icons import Hotspot2ConfIcons
from unifi_client.models.hotspot2_conf_nai_realm_list import Hotspot2ConfNaiRealmList
from unifi_client.models.hotspot2_conf_osu import Hotspot2ConfOsu
from unifi_client.models.hotspot2_conf_qos_map_dcsp import Hotspot2ConfQOSMapDcsp
from unifi_client.models.hotspot2_conf_qos_map_exceptions import Hotspot2ConfQOSMapExceptions
from unifi_client.models.hotspot2_conf_roaming_consortium_list import Hotspot2ConfRoamingConsortiumList
from unifi_client.models.hotspot2_conf_venue_name import Hotspot2ConfVenueName
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Hotspot2Conf(BaseModel):
    """
    Hotspot2Conf
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, alias="_id")
    anqp_domain_id: Optional[StrictInt] = None
    attr_hidden: Optional[StrictBool] = None
    attr_hidden_id: Optional[StrictStr] = None
    attr_no_delete: Optional[StrictBool] = None
    attr_no_edit: Optional[StrictBool] = None
    capab: Optional[List[Hotspot2ConfCapab]] = None
    cellular_network_list: Optional[List[Hotspot2ConfCellularNetworkList]] = None
    deauth_req_timeout: Optional[StrictInt] = None
    disable_dgaf: Optional[StrictBool] = None
    domain_name_list: Optional[List[StrictStr]] = None
    friendly_name: Optional[List[Hotspot2ConfFriendlyName]] = None
    gas_advanced: Optional[StrictBool] = None
    gas_comeback_delay: Optional[StrictInt] = None
    gas_frag_limit: Optional[StrictInt] = None
    hessid: Optional[StrictStr] = None
    hessid_used: Optional[StrictBool] = None
    icons: Optional[List[Hotspot2ConfIcons]] = None
    ipaddr_type_avail_v4: Optional[StrictInt] = None
    ipaddr_type_avail_v6: Optional[StrictInt] = None
    metrics_downlink_load: Optional[StrictInt] = None
    metrics_downlink_load_set: Optional[StrictBool] = None
    metrics_downlink_speed: Optional[StrictInt] = None
    metrics_downlink_speed_set: Optional[StrictBool] = None
    metrics_info_at_capacity: Optional[StrictBool] = None
    metrics_info_link_status: Optional[StrictStr] = None
    metrics_info_symmetric: Optional[StrictBool] = None
    metrics_measurement: Optional[StrictInt] = None
    metrics_measurement_set: Optional[StrictBool] = None
    metrics_status: Optional[StrictBool] = None
    metrics_uplink_load: Optional[StrictInt] = None
    metrics_uplink_load_set: Optional[StrictBool] = None
    metrics_uplink_speed: Optional[StrictInt] = None
    metrics_uplink_speed_set: Optional[StrictBool] = None
    nai_realm_list: Optional[List[Hotspot2ConfNaiRealmList]] = None
    name: Optional[StrictStr] = None
    network_access_asra: Optional[StrictBool] = None
    network_access_esr: Optional[StrictBool] = None
    network_access_internet: Optional[StrictBool] = None
    network_access_uesa: Optional[StrictBool] = None
    network_auth_type: Optional[StrictInt] = None
    network_auth_url: Optional[StrictStr] = None
    network_type: Optional[StrictInt] = None
    osu: Optional[List[Hotspot2ConfOsu]] = None
    osu_ssid: Optional[StrictStr] = None
    qos_map_dcsp: Optional[List[Hotspot2ConfQOSMapDcsp]] = None
    qos_map_exceptions: Optional[List[Hotspot2ConfQOSMapExceptions]] = None
    qos_map_status: Optional[StrictBool] = None
    roaming_consortium_list: Optional[List[Hotspot2ConfRoamingConsortiumList]] = None
    save_timestamp: Optional[StrictStr] = None
    site_id: Optional[StrictStr] = None
    t_c_filename: Optional[StrictStr] = None
    t_c_timestamp: Optional[StrictInt] = None
    venue_group: Optional[StrictInt] = None
    venue_name: Optional[List[Hotspot2ConfVenueName]] = None
    venue_type: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["_id", "anqp_domain_id", "attr_hidden", "attr_hidden_id", "attr_no_delete", "attr_no_edit", "capab", "cellular_network_list", "deauth_req_timeout", "disable_dgaf", "domain_name_list", "friendly_name", "gas_advanced", "gas_comeback_delay", "gas_frag_limit", "hessid", "hessid_used", "icons", "ipaddr_type_avail_v4", "ipaddr_type_avail_v6", "metrics_downlink_load", "metrics_downlink_load_set", "metrics_downlink_speed", "metrics_downlink_speed_set", "metrics_info_at_capacity", "metrics_info_link_status", "metrics_info_symmetric", "metrics_measurement", "metrics_measurement_set", "metrics_status", "metrics_uplink_load", "metrics_uplink_load_set", "metrics_uplink_speed", "metrics_uplink_speed_set", "nai_realm_list", "name", "network_access_asra", "network_access_esr", "network_access_internet", "network_access_uesa", "network_auth_type", "network_auth_url", "network_type", "osu", "osu_ssid", "qos_map_dcsp", "qos_map_exceptions", "qos_map_status", "roaming_consortium_list", "save_timestamp", "site_id", "t_c_filename", "t_c_timestamp", "venue_group", "venue_name", "venue_type"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Hotspot2Conf from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in capab (list)
        _items = []
        if self.capab:
            for _item in self.capab:
                if _item:
                    _items.append(_item.to_dict())
            _dict['capab'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in cellular_network_list (list)
        _items = []
        if self.cellular_network_list:
            for _item in self.cellular_network_list:
                if _item:
                    _items.append(_item.to_dict())
            _dict['cellular_network_list'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in friendly_name (list)
        _items = []
        if self.friendly_name:
            for _item in self.friendly_name:
                if _item:
                    _items.append(_item.to_dict())
            _dict['friendly_name'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in icons (list)
        _items = []
        if self.icons:
            for _item in self.icons:
                if _item:
                    _items.append(_item.to_dict())
            _dict['icons'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in nai_realm_list (list)
        _items = []
        if self.nai_realm_list:
            for _item in self.nai_realm_list:
                if _item:
                    _items.append(_item.to_dict())
            _dict['nai_realm_list'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in osu (list)
        _items = []
        if self.osu:
            for _item in self.osu:
                if _item:
                    _items.append(_item.to_dict())
            _dict['osu'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in qos_map_dcsp (list)
        _items = []
        if self.qos_map_dcsp:
            for _item in self.qos_map_dcsp:
                if _item:
                    _items.append(_item.to_dict())
            _dict['qos_map_dcsp'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in qos_map_exceptions (list)
        _items = []
        if self.qos_map_exceptions:
            for _item in self.qos_map_exceptions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['qos_map_exceptions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in roaming_consortium_list (list)
        _items = []
        if self.roaming_consortium_list:
            for _item in self.roaming_consortium_list:
                if _item:
                    _items.append(_item.to_dict())
            _dict['roaming_consortium_list'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in venue_name (list)
        _items = []
        if self.venue_name:
            for _item in self.venue_name:
                if _item:
                    _items.append(_item.to_dict())
            _dict['venue_name'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Hotspot2Conf from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_id": obj.get("_id"),
            "anqp_domain_id": obj.get("anqp_domain_id"),
            "attr_hidden": obj.get("attr_hidden"),
            "attr_hidden_id": obj.get("attr_hidden_id"),
            "attr_no_delete": obj.get("attr_no_delete"),
            "attr_no_edit": obj.get("attr_no_edit"),
            "capab": [Hotspot2ConfCapab.from_dict(_item) for _item in obj.get("capab")] if obj.get("capab") is not None else None,
            "cellular_network_list": [Hotspot2ConfCellularNetworkList.from_dict(_item) for _item in obj.get("cellular_network_list")] if obj.get("cellular_network_list") is not None else None,
            "deauth_req_timeout": obj.get("deauth_req_timeout"),
            "disable_dgaf": obj.get("disable_dgaf"),
            "domain_name_list": obj.get("domain_name_list"),
            "friendly_name": [Hotspot2ConfFriendlyName.from_dict(_item) for _item in obj.get("friendly_name")] if obj.get("friendly_name") is not None else None,
            "gas_advanced": obj.get("gas_advanced"),
            "gas_comeback_delay": obj.get("gas_comeback_delay"),
            "gas_frag_limit": obj.get("gas_frag_limit"),
            "hessid": obj.get("hessid"),
            "hessid_used": obj.get("hessid_used"),
            "icons": [Hotspot2ConfIcons.from_dict(_item) for _item in obj.get("icons")] if obj.get("icons") is not None else None,
            "ipaddr_type_avail_v4": obj.get("ipaddr_type_avail_v4"),
            "ipaddr_type_avail_v6": obj.get("ipaddr_type_avail_v6"),
            "metrics_downlink_load": obj.get("metrics_downlink_load"),
            "metrics_downlink_load_set": obj.get("metrics_downlink_load_set"),
            "metrics_downlink_speed": obj.get("metrics_downlink_speed"),
            "metrics_downlink_speed_set": obj.get("metrics_downlink_speed_set"),
            "metrics_info_at_capacity": obj.get("metrics_info_at_capacity"),
            "metrics_info_link_status": obj.get("metrics_info_link_status"),
            "metrics_info_symmetric": obj.get("metrics_info_symmetric"),
            "metrics_measurement": obj.get("metrics_measurement"),
            "metrics_measurement_set": obj.get("metrics_measurement_set"),
            "metrics_status": obj.get("metrics_status"),
            "metrics_uplink_load": obj.get("metrics_uplink_load"),
            "metrics_uplink_load_set": obj.get("metrics_uplink_load_set"),
            "metrics_uplink_speed": obj.get("metrics_uplink_speed"),
            "metrics_uplink_speed_set": obj.get("metrics_uplink_speed_set"),
            "nai_realm_list": [Hotspot2ConfNaiRealmList.from_dict(_item) for _item in obj.get("nai_realm_list")] if obj.get("nai_realm_list") is not None else None,
            "name": obj.get("name"),
            "network_access_asra": obj.get("network_access_asra"),
            "network_access_esr": obj.get("network_access_esr"),
            "network_access_internet": obj.get("network_access_internet"),
            "network_access_uesa": obj.get("network_access_uesa"),
            "network_auth_type": obj.get("network_auth_type"),
            "network_auth_url": obj.get("network_auth_url"),
            "network_type": obj.get("network_type"),
            "osu": [Hotspot2ConfOsu.from_dict(_item) for _item in obj.get("osu")] if obj.get("osu") is not None else None,
            "osu_ssid": obj.get("osu_ssid"),
            "qos_map_dcsp": [Hotspot2ConfQOSMapDcsp.from_dict(_item) for _item in obj.get("qos_map_dcsp")] if obj.get("qos_map_dcsp") is not None else None,
            "qos_map_exceptions": [Hotspot2ConfQOSMapExceptions.from_dict(_item) for _item in obj.get("qos_map_exceptions")] if obj.get("qos_map_exceptions") is not None else None,
            "qos_map_status": obj.get("qos_map_status"),
            "roaming_consortium_list": [Hotspot2ConfRoamingConsortiumList.from_dict(_item) for _item in obj.get("roaming_consortium_list")] if obj.get("roaming_consortium_list") is not None else None,
            "save_timestamp": obj.get("save_timestamp"),
            "site_id": obj.get("site_id"),
            "t_c_filename": obj.get("t_c_filename"),
            "t_c_timestamp": obj.get("t_c_timestamp"),
            "venue_group": obj.get("venue_group"),
            "venue_name": [Hotspot2ConfVenueName.from_dict(_item) for _item in obj.get("venue_name")] if obj.get("venue_name") is not None else None,
            "venue_type": obj.get("venue_type")
        })
        return _obj


