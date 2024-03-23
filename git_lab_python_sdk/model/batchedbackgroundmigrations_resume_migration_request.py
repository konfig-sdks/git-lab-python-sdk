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


class BatchedbackgroundmigrationsResumeMigrationRequest(
    schemas.AnyTypeSchema,
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class database(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "main": "MAIN",
                        "ci": "CI",
                        "embedding": "EMBEDDING",
                        "main_clusterwide": "MAIN_CLUSTERWIDE",
                        "geo": "GEO",
                    }
                
                @schemas.classproperty
                def MAIN(cls):
                    return cls("main")
                
                @schemas.classproperty
                def CI(cls):
                    return cls("ci")
                
                @schemas.classproperty
                def EMBEDDING(cls):
                    return cls("embedding")
                
                @schemas.classproperty
                def MAIN_CLUSTERWIDE(cls):
                    return cls("main_clusterwide")
                
                @schemas.classproperty
                def GEO(cls):
                    return cls("geo")
            __annotations__ = {
                "database": database,
            }

    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["database"]) -> MetaOapg.properties.database: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["database", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["database"]) -> typing.Union[MetaOapg.properties.database, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["database", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        database: typing.Union[MetaOapg.properties.database, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BatchedbackgroundmigrationsResumeMigrationRequest':
        return super().__new__(
            cls,
            *args,
            database=database,
            _configuration=_configuration,
            **kwargs,
        )
