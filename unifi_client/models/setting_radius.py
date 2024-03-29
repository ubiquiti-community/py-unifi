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
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class SettingRadius(BaseModel):
    """
    SettingRadius
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, alias="_id")
    accounting_enabled: Optional[StrictBool] = None
    acct_port: Optional[StrictInt] = None
    attr_hidden: Optional[StrictBool] = None
    attr_hidden_id: Optional[StrictStr] = None
    attr_no_delete: Optional[StrictBool] = None
    attr_no_edit: Optional[StrictBool] = None
    auth_port: Optional[StrictInt] = None
    configure_whole_network: Optional[StrictBool] = None
    enabled: Optional[StrictBool] = None
    interim_update_interval: Optional[StrictInt] = None
    key: Optional[StrictStr] = None
    site_id: Optional[StrictStr] = None
    tunneled_reply: Optional[StrictBool] = None
    x_secret: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["_id", "accounting_enabled", "acct_port", "attr_hidden", "attr_hidden_id", "attr_no_delete", "attr_no_edit", "auth_port", "configure_whole_network", "enabled", "interim_update_interval", "key", "site_id", "tunneled_reply", "x_secret"]

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
        """Create an instance of SettingRadius from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of SettingRadius from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_id": obj.get("_id"),
            "accounting_enabled": obj.get("accounting_enabled"),
            "acct_port": obj.get("acct_port"),
            "attr_hidden": obj.get("attr_hidden"),
            "attr_hidden_id": obj.get("attr_hidden_id"),
            "attr_no_delete": obj.get("attr_no_delete"),
            "attr_no_edit": obj.get("attr_no_edit"),
            "auth_port": obj.get("auth_port"),
            "configure_whole_network": obj.get("configure_whole_network"),
            "enabled": obj.get("enabled"),
            "interim_update_interval": obj.get("interim_update_interval"),
            "key": obj.get("key"),
            "site_id": obj.get("site_id"),
            "tunneled_reply": obj.get("tunneled_reply"),
            "x_secret": obj.get("x_secret")
        })
        return _obj


