# coding: utf-8

"""
    GitLab API

    An OpenAPI definition for the GitLab REST API. Few API resources or endpoints are currently included. The intent is to expand this to match the entire Markdown documentation of the API: <https://docs.gitlab.com/ee/api/>. Contributions are welcome.  When viewing this on gitlab.com, you can test API calls directly from the browser against the `gitlab.com` instance, if you are logged in. The feature uses the current [GitLab session cookie](https://docs.gitlab.com/ee/api/index.html#session-cookie), so each request is made using your account.  Instructions for using this tool can be found in [Interactive API Documentation](https://docs.gitlab.com/ee/api/openapi/openapi_interactive.html) 

    The version of the OpenAPI document: v4
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from git_lab_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from git_lab_python_sdk.api_response import AsyncGeneratorResponse
from git_lab_python_sdk import api_client, exceptions
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

from git_lab_python_sdk.model.api_entities_bulk_import import APIEntitiesBulkImport as APIEntitiesBulkImportSchema
from git_lab_python_sdk.model.bulkimports_start_new_migration_request import BulkimportsStartNewMigrationRequest as BulkimportsStartNewMigrationRequestSchema

from git_lab_python_sdk.type.api_entities_bulk_import import APIEntitiesBulkImport
from git_lab_python_sdk.type.bulkimports_start_new_migration_request import BulkimportsStartNewMigrationRequest

from ...api_client import Dictionary
from git_lab_python_sdk.pydantic.api_entities_bulk_import import APIEntitiesBulkImport as APIEntitiesBulkImportPydantic
from git_lab_python_sdk.pydantic.bulkimports_start_new_migration_request import BulkimportsStartNewMigrationRequest as BulkimportsStartNewMigrationRequestPydantic

# body param
SchemaForRequestBodyApplicationXWwwFormUrlencoded = BulkimportsStartNewMigrationRequestSchema


request_body_bulkimports_start_new_migration_request = api_client.RequestBody(
    content={
        'application/x-www-form-urlencoded': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationXWwwFormUrlencoded),
    },
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = APIEntitiesBulkImportSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: APIEntitiesBulkImport


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: APIEntitiesBulkImport


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: 


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: 


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
)


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: 


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: 


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
)


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: 


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: 


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
)


@dataclass
class ApiResponseFor422(api_client.ApiResponse):
    body: 


@dataclass
class ApiResponseFor422Async(api_client.AsyncApiResponse):
    body: 


_response_for_422 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor422,
    response_cls_async=ApiResponseFor422Async,
)


@dataclass
class ApiResponseFor503(api_client.ApiResponse):
    body: 


@dataclass
class ApiResponseFor503Async(api_client.AsyncApiResponse):
    body: 


_response_for_503 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor503,
    response_cls_async=ApiResponseFor503Async,
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _start_new_migration_mapped_args(
        self,
        configuration_url: str,
        configuration_access_token: str,
        entities_source_type: typing.List[str],
        entities_source_full_path: typing.List[str],
        entities_destination_namespace: typing.List[str],
        entities_destination_slug: typing.Optional[typing.List[str]] = None,
        entities_destination_name: typing.Optional[typing.List[str]] = None,
        entities_migrate_projects: typing.Optional[typing.List[bool]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if configuration_url is not None:
            _body["configuration[url]"] = configuration_url
        if configuration_access_token is not None:
            _body["configuration[access_token]"] = configuration_access_token
        if entities_source_type is not None:
            _body["entities[source_type]"] = entities_source_type
        if entities_source_full_path is not None:
            _body["entities[source_full_path]"] = entities_source_full_path
        if entities_destination_namespace is not None:
            _body["entities[destination_namespace]"] = entities_destination_namespace
        if entities_destination_slug is not None:
            _body["entities[destination_slug]"] = entities_destination_slug
        if entities_destination_name is not None:
            _body["entities[destination_name]"] = entities_destination_name
        if entities_migrate_projects is not None:
            _body["entities[migrate_projects]"] = entities_migrate_projects
        args.body = _body
        return args

    async def _astart_new_migration_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/x-www-form-urlencoded',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Start a new GitLab Migration
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v4/bulk_imports',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_bulkimports_start_new_migration_request.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _start_new_migration_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/x-www-form-urlencoded',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Start a new GitLab Migration
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v4/bulk_imports',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_bulkimports_start_new_migration_request.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class StartNewMigrationRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def astart_new_migration(
        self,
        configuration_url: str,
        configuration_access_token: str,
        entities_source_type: typing.List[str],
        entities_source_full_path: typing.List[str],
        entities_destination_namespace: typing.List[str],
        entities_destination_slug: typing.Optional[typing.List[str]] = None,
        entities_destination_name: typing.Optional[typing.List[str]] = None,
        entities_migrate_projects: typing.Optional[typing.List[bool]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._start_new_migration_mapped_args(
            body=body,
            configuration_url=configuration_url,
            configuration_access_token=configuration_access_token,
            entities_source_type=entities_source_type,
            entities_source_full_path=entities_source_full_path,
            entities_destination_namespace=entities_destination_namespace,
            entities_destination_slug=entities_destination_slug,
            entities_destination_name=entities_destination_name,
            entities_migrate_projects=entities_migrate_projects,
        )
        return await self._astart_new_migration_oapg(
            body=args.body,
            **kwargs,
        )
    
    def start_new_migration(
        self,
        configuration_url: str,
        configuration_access_token: str,
        entities_source_type: typing.List[str],
        entities_source_full_path: typing.List[str],
        entities_destination_namespace: typing.List[str],
        entities_destination_slug: typing.Optional[typing.List[str]] = None,
        entities_destination_name: typing.Optional[typing.List[str]] = None,
        entities_migrate_projects: typing.Optional[typing.List[bool]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._start_new_migration_mapped_args(
            body=body,
            configuration_url=configuration_url,
            configuration_access_token=configuration_access_token,
            entities_source_type=entities_source_type,
            entities_source_full_path=entities_source_full_path,
            entities_destination_namespace=entities_destination_namespace,
            entities_destination_slug=entities_destination_slug,
            entities_destination_name=entities_destination_name,
            entities_migrate_projects=entities_migrate_projects,
        )
        return self._start_new_migration_oapg(
            body=args.body,
        )

class StartNewMigration(BaseApi):

    async def astart_new_migration(
        self,
        configuration_url: str,
        configuration_access_token: str,
        entities_source_type: typing.List[str],
        entities_source_full_path: typing.List[str],
        entities_destination_namespace: typing.List[str],
        entities_destination_slug: typing.Optional[typing.List[str]] = None,
        entities_destination_name: typing.Optional[typing.List[str]] = None,
        entities_migrate_projects: typing.Optional[typing.List[bool]] = None,
        validate: bool = False,
        **kwargs,
    ) -> APIEntitiesBulkImportPydantic:
        raw_response = await self.raw.astart_new_migration(
            body=body,
            configuration_url=configuration_url,
            configuration_access_token=configuration_access_token,
            entities_source_type=entities_source_type,
            entities_source_full_path=entities_source_full_path,
            entities_destination_namespace=entities_destination_namespace,
            entities_destination_slug=entities_destination_slug,
            entities_destination_name=entities_destination_name,
            entities_migrate_projects=entities_migrate_projects,
            **kwargs,
        )
        if validate:
            return APIEntitiesBulkImportPydantic(**raw_response.body)
        return api_client.construct_model_instance(APIEntitiesBulkImportPydantic, raw_response.body)
    
    
    def start_new_migration(
        self,
        configuration_url: str,
        configuration_access_token: str,
        entities_source_type: typing.List[str],
        entities_source_full_path: typing.List[str],
        entities_destination_namespace: typing.List[str],
        entities_destination_slug: typing.Optional[typing.List[str]] = None,
        entities_destination_name: typing.Optional[typing.List[str]] = None,
        entities_migrate_projects: typing.Optional[typing.List[bool]] = None,
        validate: bool = False,
    ) -> APIEntitiesBulkImportPydantic:
        raw_response = self.raw.start_new_migration(
            body=body,
            configuration_url=configuration_url,
            configuration_access_token=configuration_access_token,
            entities_source_type=entities_source_type,
            entities_source_full_path=entities_source_full_path,
            entities_destination_namespace=entities_destination_namespace,
            entities_destination_slug=entities_destination_slug,
            entities_destination_name=entities_destination_name,
            entities_migrate_projects=entities_migrate_projects,
        )
        if validate:
            return APIEntitiesBulkImportPydantic(**raw_response.body)
        return api_client.construct_model_instance(APIEntitiesBulkImportPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        configuration_url: str,
        configuration_access_token: str,
        entities_source_type: typing.List[str],
        entities_source_full_path: typing.List[str],
        entities_destination_namespace: typing.List[str],
        entities_destination_slug: typing.Optional[typing.List[str]] = None,
        entities_destination_name: typing.Optional[typing.List[str]] = None,
        entities_migrate_projects: typing.Optional[typing.List[bool]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._start_new_migration_mapped_args(
            body=body,
            configuration_url=configuration_url,
            configuration_access_token=configuration_access_token,
            entities_source_type=entities_source_type,
            entities_source_full_path=entities_source_full_path,
            entities_destination_namespace=entities_destination_namespace,
            entities_destination_slug=entities_destination_slug,
            entities_destination_name=entities_destination_name,
            entities_migrate_projects=entities_migrate_projects,
        )
        return await self._astart_new_migration_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        configuration_url: str,
        configuration_access_token: str,
        entities_source_type: typing.List[str],
        entities_source_full_path: typing.List[str],
        entities_destination_namespace: typing.List[str],
        entities_destination_slug: typing.Optional[typing.List[str]] = None,
        entities_destination_name: typing.Optional[typing.List[str]] = None,
        entities_migrate_projects: typing.Optional[typing.List[bool]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._start_new_migration_mapped_args(
            body=body,
            configuration_url=configuration_url,
            configuration_access_token=configuration_access_token,
            entities_source_type=entities_source_type,
            entities_source_full_path=entities_source_full_path,
            entities_destination_namespace=entities_destination_namespace,
            entities_destination_slug=entities_destination_slug,
            entities_destination_name=entities_destination_name,
            entities_migrate_projects=entities_migrate_projects,
        )
        return self._start_new_migration_oapg(
            body=args.body,
        )

