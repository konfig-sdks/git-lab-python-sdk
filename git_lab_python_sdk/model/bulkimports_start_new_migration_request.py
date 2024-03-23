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


class BulkimportsStartNewMigrationRequest(
    schemas.AnyTypeSchema,
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "entities[destination_namespace]",
            "configuration[access_token]",
            "configuration[url]",
            "entities[source_full_path]",
            "entities[source_type]",
        }
        
        class properties:
            configuration_url = schemas.StrSchema
            configuration_access_token = schemas.StrSchema
            
            
            class entities_source_type(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "group_entity": "GROUP_ENTITY",
                                "project_entity": "PROJECT_ENTITY",
                            }
                        
                        @schemas.classproperty
                        def GROUP_ENTITY(cls):
                            return cls("group_entity")
                        
                        @schemas.classproperty
                        def PROJECT_ENTITY(cls):
                            return cls("project_entity")
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'entities_source_type':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class entities_source_full_path(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'entities_source_full_path':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class entities_destination_namespace(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'entities_destination_namespace':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class entities_destination_slug(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'entities_destination_slug':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class entities_destination_name(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'entities_destination_name':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class entities_migrate_projects(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.BoolSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, bool, ]], typing.List[typing.Union[MetaOapg.items, bool, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'entities_migrate_projects':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "configuration[url]": configuration_url,
                "configuration[access_token]": configuration_access_token,
                "entities[source_type]": entities_source_type,
                "entities[source_full_path]": entities_source_full_path,
                "entities[destination_namespace]": entities_destination_namespace,
                "entities[destination_slug]": entities_destination_slug,
                "entities[destination_name]": entities_destination_name,
                "entities[migrate_projects]": entities_migrate_projects,
            }

    
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["configuration[url]"]) -> MetaOapg.properties.configuration_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["configuration[access_token]"]) -> MetaOapg.properties.configuration_access_token: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["entities[source_type]"]) -> MetaOapg.properties.entities_source_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["entities[source_full_path]"]) -> MetaOapg.properties.entities_source_full_path: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["entities[destination_namespace]"]) -> MetaOapg.properties.entities_destination_namespace: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["entities[destination_slug]"]) -> MetaOapg.properties.entities_destination_slug: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["entities[destination_name]"]) -> MetaOapg.properties.entities_destination_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["entities[migrate_projects]"]) -> MetaOapg.properties.entities_migrate_projects: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["configuration[url]", "configuration[access_token]", "entities[source_type]", "entities[source_full_path]", "entities[destination_namespace]", "entities[destination_slug]", "entities[destination_name]", "entities[migrate_projects]", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["configuration[url]"]) -> MetaOapg.properties.configuration_url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["configuration[access_token]"]) -> MetaOapg.properties.configuration_access_token: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["entities[source_type]"]) -> MetaOapg.properties.entities_source_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["entities[source_full_path]"]) -> MetaOapg.properties.entities_source_full_path: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["entities[destination_namespace]"]) -> MetaOapg.properties.entities_destination_namespace: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["entities[destination_slug]"]) -> typing.Union[MetaOapg.properties.entities_destination_slug, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["entities[destination_name]"]) -> typing.Union[MetaOapg.properties.entities_destination_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["entities[migrate_projects]"]) -> typing.Union[MetaOapg.properties.entities_migrate_projects, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["configuration[url]", "configuration[access_token]", "entities[source_type]", "entities[source_full_path]", "entities[destination_namespace]", "entities[destination_slug]", "entities[destination_name]", "entities[migrate_projects]", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BulkimportsStartNewMigrationRequest':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )
