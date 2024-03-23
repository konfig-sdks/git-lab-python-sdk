# coding: utf-8

"""
    GitLab API

    An OpenAPI definition for the GitLab REST API. Few API resources or endpoints are currently included. The intent is to expand this to match the entire Markdown documentation of the API: <https://docs.gitlab.com/ee/api/>. Contributions are welcome.  When viewing this on gitlab.com, you can test API calls directly from the browser against the `gitlab.com` instance, if you are logged in. The feature uses the current [GitLab session cookie](https://docs.gitlab.com/ee/api/index.html#session-cookie), so each request is made using your account.  Instructions for using this tool can be found in [Interactive API Documentation](https://docs.gitlab.com/ee/api/openapi/openapi_interactive.html) 

    The version of the OpenAPI document: v4
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from git_lab_python_sdk import schemas  # noqa: F401


class APIEntitiesCiVariable(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    API_Entities_Ci_Variable model
    """


    class MetaOapg:
        
        class properties:
            variable_type = schemas.StrSchema
            key = schemas.StrSchema
            value = schemas.StrSchema
            protected = schemas.BoolSchema
            masked = schemas.BoolSchema
            raw = schemas.BoolSchema
            environment_scope = schemas.StrSchema
            __annotations__ = {
                "variable_type": variable_type,
                "key": key,
                "value": value,
                "protected": protected,
                "masked": masked,
                "raw": raw,
                "environment_scope": environment_scope,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["variable_type"]) -> MetaOapg.properties.variable_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["key"]) -> MetaOapg.properties.key: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["protected"]) -> MetaOapg.properties.protected: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["masked"]) -> MetaOapg.properties.masked: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["raw"]) -> MetaOapg.properties.raw: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["environment_scope"]) -> MetaOapg.properties.environment_scope: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["variable_type", "key", "value", "protected", "masked", "raw", "environment_scope", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["variable_type"]) -> typing.Union[MetaOapg.properties.variable_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["key"]) -> typing.Union[MetaOapg.properties.key, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["value"]) -> typing.Union[MetaOapg.properties.value, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["protected"]) -> typing.Union[MetaOapg.properties.protected, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["masked"]) -> typing.Union[MetaOapg.properties.masked, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["raw"]) -> typing.Union[MetaOapg.properties.raw, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["environment_scope"]) -> typing.Union[MetaOapg.properties.environment_scope, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["variable_type", "key", "value", "protected", "masked", "raw", "environment_scope", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        variable_type: typing.Union[MetaOapg.properties.variable_type, str, schemas.Unset] = schemas.unset,
        key: typing.Union[MetaOapg.properties.key, str, schemas.Unset] = schemas.unset,
        value: typing.Union[MetaOapg.properties.value, str, schemas.Unset] = schemas.unset,
        protected: typing.Union[MetaOapg.properties.protected, bool, schemas.Unset] = schemas.unset,
        masked: typing.Union[MetaOapg.properties.masked, bool, schemas.Unset] = schemas.unset,
        raw: typing.Union[MetaOapg.properties.raw, bool, schemas.Unset] = schemas.unset,
        environment_scope: typing.Union[MetaOapg.properties.environment_scope, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'APIEntitiesCiVariable':
        return super().__new__(
            cls,
            *args,
            variable_type=variable_type,
            key=key,
            value=value,
            protected=protected,
            masked=masked,
            raw=raw,
            environment_scope=environment_scope,
            _configuration=_configuration,
            **kwargs,
        )
