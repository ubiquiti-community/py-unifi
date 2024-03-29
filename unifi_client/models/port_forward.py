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
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class PortForward(BaseModel):
    """
    PortForward
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, alias="_id")
    attr_hidden: Optional[StrictBool] = None
    attr_hidden_id: Optional[StrictStr] = None
    attr_no_delete: Optional[StrictBool] = None
    attr_no_edit: Optional[StrictBool] = None
    destination_ip: Optional[StrictStr] = None
    dst_port: Optional[StrictStr] = None
    enabled: Optional[StrictBool] = None
    fwd: Optional[StrictStr] = None
    fwd_port: Optional[StrictStr] = None
    log: Optional[StrictBool] = None
    name: Optional[StrictStr] = None
    pfwd_interface: Optional[StrictStr] = None
    proto: Optional[StrictStr] = None
    site_id: Optional[StrictStr] = None
    src: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["_id", "attr_hidden", "attr_hidden_id", "attr_no_delete", "attr_no_edit", "destination_ip", "dst_port", "enabled", "fwd", "fwd_port", "log", "name", "pfwd_interface", "proto", "site_id", "src"]

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
        """Create an instance of PortForward from a JSON string"""
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
        """Create an instance of PortForward from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_id": obj.get("_id"),
            "attr_hidden": obj.get("attr_hidden"),
            "attr_hidden_id": obj.get("attr_hidden_id"),
            "attr_no_delete": obj.get("attr_no_delete"),
            "attr_no_edit": obj.get("attr_no_edit"),
            "destination_ip": obj.get("destination_ip"),
            "dst_port": obj.get("dst_port"),
            "enabled": obj.get("enabled"),
            "fwd": obj.get("fwd"),
            "fwd_port": obj.get("fwd_port"),
            "log": obj.get("log"),
            "name": obj.get("name"),
            "pfwd_interface": obj.get("pfwd_interface"),
            "proto": obj.get("proto"),
            "site_id": obj.get("site_id"),
            "src": obj.get("src")
        })
        return _obj


