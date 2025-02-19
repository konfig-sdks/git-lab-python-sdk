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

from git_lab_python_sdk.model.broadcastmessages_create_message_request import BroadcastmessagesCreateMessageRequest as BroadcastmessagesCreateMessageRequestSchema
from git_lab_python_sdk.model.api_entities_broadcast_message import APIEntitiesBroadcastMessage as APIEntitiesBroadcastMessageSchema

from git_lab_python_sdk.type.api_entities_broadcast_message import APIEntitiesBroadcastMessage
from git_lab_python_sdk.type.broadcastmessages_create_message_request import BroadcastmessagesCreateMessageRequest

from ...api_client import Dictionary
from git_lab_python_sdk.pydantic.broadcastmessages_create_message_request import BroadcastmessagesCreateMessageRequest as BroadcastmessagesCreateMessageRequestPydantic
from git_lab_python_sdk.pydantic.api_entities_broadcast_message import APIEntitiesBroadcastMessage as APIEntitiesBroadcastMessagePydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = BroadcastmessagesCreateMessageRequestSchema


request_body_broadcastmessages_create_message_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
_auth = [
    'ApiKeyAuth',
]
SchemaFor201ResponseBodyApplicationJson = APIEntitiesBroadcastMessageSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: APIEntitiesBroadcastMessage


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: APIEntitiesBroadcastMessage


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '201': _response_for_201,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_message_mapped_args(
        self,
        message: str,
        starts_at: typing.Optional[datetime] = None,
        ends_at: typing.Optional[datetime] = None,
        color: typing.Optional[str] = None,
        font: typing.Optional[str] = None,
        target_access_levels: typing.Optional[typing.List[int]] = None,
        target_path: typing.Optional[str] = None,
        broadcast_type: typing.Optional[str] = None,
        dismissable: typing.Optional[bool] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if message is not None:
            _body["message"] = message
        if starts_at is not None:
            _body["starts_at"] = starts_at
        if ends_at is not None:
            _body["ends_at"] = ends_at
        if color is not None:
            _body["color"] = color
        if font is not None:
            _body["font"] = font
        if target_access_levels is not None:
            _body["target_access_levels"] = target_access_levels
        if target_path is not None:
            _body["target_path"] = target_path
        if broadcast_type is not None:
            _body["broadcast_type"] = broadcast_type
        if dismissable is not None:
            _body["dismissable"] = dismissable
        args.body = _body
        return args

    async def _acreate_message_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Create a broadcast message
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
            path_template='/api/v4/broadcast_messages',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_broadcastmessages_create_message_request.serialize(body, content_type)
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


    def _create_message_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Create a broadcast message
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
            path_template='/api/v4/broadcast_messages',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_broadcastmessages_create_message_request.serialize(body, content_type)
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


class CreateMessageRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_message(
        self,
        message: str,
        starts_at: typing.Optional[datetime] = None,
        ends_at: typing.Optional[datetime] = None,
        color: typing.Optional[str] = None,
        font: typing.Optional[str] = None,
        target_access_levels: typing.Optional[typing.List[int]] = None,
        target_path: typing.Optional[str] = None,
        broadcast_type: typing.Optional[str] = None,
        dismissable: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_message_mapped_args(
            body=body,
            message=message,
            starts_at=starts_at,
            ends_at=ends_at,
            color=color,
            font=font,
            target_access_levels=target_access_levels,
            target_path=target_path,
            broadcast_type=broadcast_type,
            dismissable=dismissable,
        )
        return await self._acreate_message_oapg(
            body=args.body,
            **kwargs,
        )
    
    def create_message(
        self,
        message: str,
        starts_at: typing.Optional[datetime] = None,
        ends_at: typing.Optional[datetime] = None,
        color: typing.Optional[str] = None,
        font: typing.Optional[str] = None,
        target_access_levels: typing.Optional[typing.List[int]] = None,
        target_path: typing.Optional[str] = None,
        broadcast_type: typing.Optional[str] = None,
        dismissable: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_message_mapped_args(
            body=body,
            message=message,
            starts_at=starts_at,
            ends_at=ends_at,
            color=color,
            font=font,
            target_access_levels=target_access_levels,
            target_path=target_path,
            broadcast_type=broadcast_type,
            dismissable=dismissable,
        )
        return self._create_message_oapg(
            body=args.body,
        )

class CreateMessage(BaseApi):

    async def acreate_message(
        self,
        message: str,
        starts_at: typing.Optional[datetime] = None,
        ends_at: typing.Optional[datetime] = None,
        color: typing.Optional[str] = None,
        font: typing.Optional[str] = None,
        target_access_levels: typing.Optional[typing.List[int]] = None,
        target_path: typing.Optional[str] = None,
        broadcast_type: typing.Optional[str] = None,
        dismissable: typing.Optional[bool] = None,
        validate: bool = False,
        **kwargs,
    ) -> APIEntitiesBroadcastMessagePydantic:
        raw_response = await self.raw.acreate_message(
            body=body,
            message=message,
            starts_at=starts_at,
            ends_at=ends_at,
            color=color,
            font=font,
            target_access_levels=target_access_levels,
            target_path=target_path,
            broadcast_type=broadcast_type,
            dismissable=dismissable,
            **kwargs,
        )
        if validate:
            return APIEntitiesBroadcastMessagePydantic(**raw_response.body)
        return api_client.construct_model_instance(APIEntitiesBroadcastMessagePydantic, raw_response.body)
    
    
    def create_message(
        self,
        message: str,
        starts_at: typing.Optional[datetime] = None,
        ends_at: typing.Optional[datetime] = None,
        color: typing.Optional[str] = None,
        font: typing.Optional[str] = None,
        target_access_levels: typing.Optional[typing.List[int]] = None,
        target_path: typing.Optional[str] = None,
        broadcast_type: typing.Optional[str] = None,
        dismissable: typing.Optional[bool] = None,
        validate: bool = False,
    ) -> APIEntitiesBroadcastMessagePydantic:
        raw_response = self.raw.create_message(
            body=body,
            message=message,
            starts_at=starts_at,
            ends_at=ends_at,
            color=color,
            font=font,
            target_access_levels=target_access_levels,
            target_path=target_path,
            broadcast_type=broadcast_type,
            dismissable=dismissable,
        )
        if validate:
            return APIEntitiesBroadcastMessagePydantic(**raw_response.body)
        return api_client.construct_model_instance(APIEntitiesBroadcastMessagePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        message: str,
        starts_at: typing.Optional[datetime] = None,
        ends_at: typing.Optional[datetime] = None,
        color: typing.Optional[str] = None,
        font: typing.Optional[str] = None,
        target_access_levels: typing.Optional[typing.List[int]] = None,
        target_path: typing.Optional[str] = None,
        broadcast_type: typing.Optional[str] = None,
        dismissable: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_message_mapped_args(
            body=body,
            message=message,
            starts_at=starts_at,
            ends_at=ends_at,
            color=color,
            font=font,
            target_access_levels=target_access_levels,
            target_path=target_path,
            broadcast_type=broadcast_type,
            dismissable=dismissable,
        )
        return await self._acreate_message_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        message: str,
        starts_at: typing.Optional[datetime] = None,
        ends_at: typing.Optional[datetime] = None,
        color: typing.Optional[str] = None,
        font: typing.Optional[str] = None,
        target_access_levels: typing.Optional[typing.List[int]] = None,
        target_path: typing.Optional[str] = None,
        broadcast_type: typing.Optional[str] = None,
        dismissable: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_message_mapped_args(
            body=body,
            message=message,
            starts_at=starts_at,
            ends_at=ends_at,
            color=color,
            font=font,
            target_access_levels=target_access_levels,
            target_path=target_path,
            broadcast_type=broadcast_type,
            dismissable=dismissable,
        )
        return self._create_message_oapg(
            body=args.body,
        )

