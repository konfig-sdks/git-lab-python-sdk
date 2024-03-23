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

from git_lab_python_sdk.model.clusters_update_instance_cluster_request import ClustersUpdateInstanceClusterRequest as ClustersUpdateInstanceClusterRequestSchema
from git_lab_python_sdk.model.api_entities_cluster import APIEntitiesCluster as APIEntitiesClusterSchema

from git_lab_python_sdk.type.api_entities_cluster import APIEntitiesCluster
from git_lab_python_sdk.type.clusters_update_instance_cluster_request import ClustersUpdateInstanceClusterRequest

from ...api_client import Dictionary
from git_lab_python_sdk.pydantic.clusters_update_instance_cluster_request import ClustersUpdateInstanceClusterRequest as ClustersUpdateInstanceClusterRequestPydantic
from git_lab_python_sdk.pydantic.api_entities_cluster import APIEntitiesCluster as APIEntitiesClusterPydantic

# Path params
ClusterIdSchema = schemas.Int32Schema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'cluster_id': typing.Union[ClusterIdSchema, decimal.Decimal, int, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_cluster_id = api_client.PathParameter(
    name="cluster_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ClusterIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = ClustersUpdateInstanceClusterRequestSchema


request_body_clusters_update_instance_cluster_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor200ResponseBodyApplicationJson = APIEntitiesClusterSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: APIEntitiesCluster


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: APIEntitiesCluster


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
class ApiResponseFor403(api_client.ApiResponse):
    body: 


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: 


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
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
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _update_instance_cluster_mapped_args(
        self,
        cluster_id: int,
        name: typing.Optional[str] = None,
        enabled: typing.Optional[bool] = None,
        environment_scope: typing.Optional[str] = None,
        namespace_per_environment: typing.Optional[bool] = None,
        domain: typing.Optional[str] = None,
        management_project_id: typing.Optional[int] = None,
        managed: typing.Optional[bool] = None,
        platform_kubernetes_attributes_api_url: typing.Optional[str] = None,
        platform_kubernetes_attributes_token: typing.Optional[str] = None,
        platform_kubernetes_attributes_ca_cert: typing.Optional[str] = None,
        platform_kubernetes_attributes_namespace: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if name is not None:
            _body["name"] = name
        if enabled is not None:
            _body["enabled"] = enabled
        if environment_scope is not None:
            _body["environment_scope"] = environment_scope
        if namespace_per_environment is not None:
            _body["namespace_per_environment"] = namespace_per_environment
        if domain is not None:
            _body["domain"] = domain
        if management_project_id is not None:
            _body["management_project_id"] = management_project_id
        if managed is not None:
            _body["managed"] = managed
        if platform_kubernetes_attributes_api_url is not None:
            _body["platform_kubernetes_attributes[api_url]"] = platform_kubernetes_attributes_api_url
        if platform_kubernetes_attributes_token is not None:
            _body["platform_kubernetes_attributes[token]"] = platform_kubernetes_attributes_token
        if platform_kubernetes_attributes_ca_cert is not None:
            _body["platform_kubernetes_attributes[ca_cert]"] = platform_kubernetes_attributes_ca_cert
        if platform_kubernetes_attributes_namespace is not None:
            _body["platform_kubernetes_attributes[namespace]"] = platform_kubernetes_attributes_namespace
        args.body = _body
        if cluster_id is not None:
            _path_params["cluster_id"] = cluster_id
        args.path = _path_params
        return args

    async def _aupdate_instance_cluster_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Edit instance cluster
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_cluster_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'put'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v4/admin/clusters/{cluster_id}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_clusters_update_instance_cluster_request.serialize(body, content_type)
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


    def _update_instance_cluster_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Edit instance cluster
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_cluster_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'put'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v4/admin/clusters/{cluster_id}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_clusters_update_instance_cluster_request.serialize(body, content_type)
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


class UpdateInstanceClusterRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_instance_cluster(
        self,
        cluster_id: int,
        name: typing.Optional[str] = None,
        enabled: typing.Optional[bool] = None,
        environment_scope: typing.Optional[str] = None,
        namespace_per_environment: typing.Optional[bool] = None,
        domain: typing.Optional[str] = None,
        management_project_id: typing.Optional[int] = None,
        managed: typing.Optional[bool] = None,
        platform_kubernetes_attributes_api_url: typing.Optional[str] = None,
        platform_kubernetes_attributes_token: typing.Optional[str] = None,
        platform_kubernetes_attributes_ca_cert: typing.Optional[str] = None,
        platform_kubernetes_attributes_namespace: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_instance_cluster_mapped_args(
            body=body,
            cluster_id=cluster_id,
            name=name,
            enabled=enabled,
            environment_scope=environment_scope,
            namespace_per_environment=namespace_per_environment,
            domain=domain,
            management_project_id=management_project_id,
            managed=managed,
            platform_kubernetes_attributes_api_url=platform_kubernetes_attributes_api_url,
            platform_kubernetes_attributes_token=platform_kubernetes_attributes_token,
            platform_kubernetes_attributes_ca_cert=platform_kubernetes_attributes_ca_cert,
            platform_kubernetes_attributes_namespace=platform_kubernetes_attributes_namespace,
        )
        return await self._aupdate_instance_cluster_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def update_instance_cluster(
        self,
        cluster_id: int,
        name: typing.Optional[str] = None,
        enabled: typing.Optional[bool] = None,
        environment_scope: typing.Optional[str] = None,
        namespace_per_environment: typing.Optional[bool] = None,
        domain: typing.Optional[str] = None,
        management_project_id: typing.Optional[int] = None,
        managed: typing.Optional[bool] = None,
        platform_kubernetes_attributes_api_url: typing.Optional[str] = None,
        platform_kubernetes_attributes_token: typing.Optional[str] = None,
        platform_kubernetes_attributes_ca_cert: typing.Optional[str] = None,
        platform_kubernetes_attributes_namespace: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_instance_cluster_mapped_args(
            body=body,
            cluster_id=cluster_id,
            name=name,
            enabled=enabled,
            environment_scope=environment_scope,
            namespace_per_environment=namespace_per_environment,
            domain=domain,
            management_project_id=management_project_id,
            managed=managed,
            platform_kubernetes_attributes_api_url=platform_kubernetes_attributes_api_url,
            platform_kubernetes_attributes_token=platform_kubernetes_attributes_token,
            platform_kubernetes_attributes_ca_cert=platform_kubernetes_attributes_ca_cert,
            platform_kubernetes_attributes_namespace=platform_kubernetes_attributes_namespace,
        )
        return self._update_instance_cluster_oapg(
            body=args.body,
            path_params=args.path,
        )

class UpdateInstanceCluster(BaseApi):

    async def aupdate_instance_cluster(
        self,
        cluster_id: int,
        name: typing.Optional[str] = None,
        enabled: typing.Optional[bool] = None,
        environment_scope: typing.Optional[str] = None,
        namespace_per_environment: typing.Optional[bool] = None,
        domain: typing.Optional[str] = None,
        management_project_id: typing.Optional[int] = None,
        managed: typing.Optional[bool] = None,
        platform_kubernetes_attributes_api_url: typing.Optional[str] = None,
        platform_kubernetes_attributes_token: typing.Optional[str] = None,
        platform_kubernetes_attributes_ca_cert: typing.Optional[str] = None,
        platform_kubernetes_attributes_namespace: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> APIEntitiesClusterPydantic:
        raw_response = await self.raw.aupdate_instance_cluster(
            body=body,
            cluster_id=cluster_id,
            name=name,
            enabled=enabled,
            environment_scope=environment_scope,
            namespace_per_environment=namespace_per_environment,
            domain=domain,
            management_project_id=management_project_id,
            managed=managed,
            platform_kubernetes_attributes_api_url=platform_kubernetes_attributes_api_url,
            platform_kubernetes_attributes_token=platform_kubernetes_attributes_token,
            platform_kubernetes_attributes_ca_cert=platform_kubernetes_attributes_ca_cert,
            platform_kubernetes_attributes_namespace=platform_kubernetes_attributes_namespace,
            **kwargs,
        )
        if validate:
            return APIEntitiesClusterPydantic(**raw_response.body)
        return api_client.construct_model_instance(APIEntitiesClusterPydantic, raw_response.body)
    
    
    def update_instance_cluster(
        self,
        cluster_id: int,
        name: typing.Optional[str] = None,
        enabled: typing.Optional[bool] = None,
        environment_scope: typing.Optional[str] = None,
        namespace_per_environment: typing.Optional[bool] = None,
        domain: typing.Optional[str] = None,
        management_project_id: typing.Optional[int] = None,
        managed: typing.Optional[bool] = None,
        platform_kubernetes_attributes_api_url: typing.Optional[str] = None,
        platform_kubernetes_attributes_token: typing.Optional[str] = None,
        platform_kubernetes_attributes_ca_cert: typing.Optional[str] = None,
        platform_kubernetes_attributes_namespace: typing.Optional[str] = None,
        validate: bool = False,
    ) -> APIEntitiesClusterPydantic:
        raw_response = self.raw.update_instance_cluster(
            body=body,
            cluster_id=cluster_id,
            name=name,
            enabled=enabled,
            environment_scope=environment_scope,
            namespace_per_environment=namespace_per_environment,
            domain=domain,
            management_project_id=management_project_id,
            managed=managed,
            platform_kubernetes_attributes_api_url=platform_kubernetes_attributes_api_url,
            platform_kubernetes_attributes_token=platform_kubernetes_attributes_token,
            platform_kubernetes_attributes_ca_cert=platform_kubernetes_attributes_ca_cert,
            platform_kubernetes_attributes_namespace=platform_kubernetes_attributes_namespace,
        )
        if validate:
            return APIEntitiesClusterPydantic(**raw_response.body)
        return api_client.construct_model_instance(APIEntitiesClusterPydantic, raw_response.body)


class ApiForput(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aput(
        self,
        cluster_id: int,
        name: typing.Optional[str] = None,
        enabled: typing.Optional[bool] = None,
        environment_scope: typing.Optional[str] = None,
        namespace_per_environment: typing.Optional[bool] = None,
        domain: typing.Optional[str] = None,
        management_project_id: typing.Optional[int] = None,
        managed: typing.Optional[bool] = None,
        platform_kubernetes_attributes_api_url: typing.Optional[str] = None,
        platform_kubernetes_attributes_token: typing.Optional[str] = None,
        platform_kubernetes_attributes_ca_cert: typing.Optional[str] = None,
        platform_kubernetes_attributes_namespace: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_instance_cluster_mapped_args(
            body=body,
            cluster_id=cluster_id,
            name=name,
            enabled=enabled,
            environment_scope=environment_scope,
            namespace_per_environment=namespace_per_environment,
            domain=domain,
            management_project_id=management_project_id,
            managed=managed,
            platform_kubernetes_attributes_api_url=platform_kubernetes_attributes_api_url,
            platform_kubernetes_attributes_token=platform_kubernetes_attributes_token,
            platform_kubernetes_attributes_ca_cert=platform_kubernetes_attributes_ca_cert,
            platform_kubernetes_attributes_namespace=platform_kubernetes_attributes_namespace,
        )
        return await self._aupdate_instance_cluster_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def put(
        self,
        cluster_id: int,
        name: typing.Optional[str] = None,
        enabled: typing.Optional[bool] = None,
        environment_scope: typing.Optional[str] = None,
        namespace_per_environment: typing.Optional[bool] = None,
        domain: typing.Optional[str] = None,
        management_project_id: typing.Optional[int] = None,
        managed: typing.Optional[bool] = None,
        platform_kubernetes_attributes_api_url: typing.Optional[str] = None,
        platform_kubernetes_attributes_token: typing.Optional[str] = None,
        platform_kubernetes_attributes_ca_cert: typing.Optional[str] = None,
        platform_kubernetes_attributes_namespace: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_instance_cluster_mapped_args(
            body=body,
            cluster_id=cluster_id,
            name=name,
            enabled=enabled,
            environment_scope=environment_scope,
            namespace_per_environment=namespace_per_environment,
            domain=domain,
            management_project_id=management_project_id,
            managed=managed,
            platform_kubernetes_attributes_api_url=platform_kubernetes_attributes_api_url,
            platform_kubernetes_attributes_token=platform_kubernetes_attributes_token,
            platform_kubernetes_attributes_ca_cert=platform_kubernetes_attributes_ca_cert,
            platform_kubernetes_attributes_namespace=platform_kubernetes_attributes_namespace,
        )
        return self._update_instance_cluster_oapg(
            body=args.body,
            path_params=args.path,
        )

