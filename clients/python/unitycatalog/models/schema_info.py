# coding: utf-8

"""
    Unity Catalog API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class SchemaInfo(BaseModel):
    """
    SchemaInfo
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="Name of schema, relative to parent catalog.")
    catalog_name: Optional[StrictStr] = Field(default=None, description="Name of parent catalog.")
    comment: Optional[StrictStr] = Field(default=None, description="User-provided free-form text description.")
    properties: Optional[Dict[str, StrictStr]] = Field(default=None, description="A map of key-value properties attached to the securable.")
    full_name: Optional[StrictStr] = Field(default=None, description="Full name of schema, in form of __catalog_name__.__schema_name__.")
    created_at: Optional[StrictInt] = Field(default=None, description="Time at which this schema was created, in epoch milliseconds.")
    updated_at: Optional[StrictInt] = Field(default=None, description="Time at which this schema was last modified, in epoch milliseconds.")
    schema_id: Optional[StrictStr] = Field(default=None, description="Unique identifier for the schema.")
    __properties: ClassVar[List[str]] = ["name", "catalog_name", "comment", "properties", "full_name", "created_at", "updated_at", "schema_id"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of SchemaInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SchemaInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "catalog_name": obj.get("catalog_name"),
            "comment": obj.get("comment"),
            "properties": obj.get("properties"),
            "full_name": obj.get("full_name"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "schema_id": obj.get("schema_id")
        })
        return _obj


