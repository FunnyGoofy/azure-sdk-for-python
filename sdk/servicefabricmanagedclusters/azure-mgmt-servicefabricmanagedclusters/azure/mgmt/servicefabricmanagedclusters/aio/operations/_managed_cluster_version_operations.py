# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, List, Optional, TypeVar, Union

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._managed_cluster_version_operations import build_get_by_environment_request, build_get_request, build_list_by_environment_request, build_list_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class ManagedClusterVersionOperations:
    """ManagedClusterVersionOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.servicefabricmanagedclusters.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace_async
    async def get(
        self,
        location: str,
        cluster_version: str,
        **kwargs: Any
    ) -> "_models.ManagedClusterCodeVersionResult":
        """Gets information about a Service Fabric managed cluster code version available in the specified
        location.

        Gets information about an available Service Fabric managed cluster code version.

        :param location: The location for the cluster code versions. This is different from cluster
         location.
        :type location: str
        :param cluster_version: The cluster code version.
        :type cluster_version: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ManagedClusterCodeVersionResult, or the result of cls(response)
        :rtype: ~azure.mgmt.servicefabricmanagedclusters.models.ManagedClusterCodeVersionResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ManagedClusterCodeVersionResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2022-02-01-preview")  # type: str

        
        request = build_get_request(
            location=location,
            subscription_id=self._config.subscription_id,
            cluster_version=cluster_version,
            api_version=api_version,
            template_url=self.get.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorModel, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ManagedClusterCodeVersionResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': "/subscriptions/{subscriptionId}/providers/Microsoft.ServiceFabric/locations/{location}/managedClusterVersions/{clusterVersion}"}  # type: ignore


    @distributed_trace_async
    async def get_by_environment(
        self,
        location: str,
        environment: Union[str, "_models.ManagedClusterVersionEnvironment"],
        cluster_version: str,
        **kwargs: Any
    ) -> "_models.ManagedClusterCodeVersionResult":
        """Gets information about a Service Fabric cluster code version available for the specified
        environment.

        Gets information about an available Service Fabric cluster code version by environment.

        :param location: The location for the cluster code versions. This is different from cluster
         location.
        :type location: str
        :param environment: The operating system of the cluster. The default means all.
        :type environment: str or
         ~azure.mgmt.servicefabricmanagedclusters.models.ManagedClusterVersionEnvironment
        :param cluster_version: The cluster code version.
        :type cluster_version: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ManagedClusterCodeVersionResult, or the result of cls(response)
        :rtype: ~azure.mgmt.servicefabricmanagedclusters.models.ManagedClusterCodeVersionResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ManagedClusterCodeVersionResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2022-02-01-preview")  # type: str

        
        request = build_get_by_environment_request(
            location=location,
            environment=environment,
            subscription_id=self._config.subscription_id,
            cluster_version=cluster_version,
            api_version=api_version,
            template_url=self.get_by_environment.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorModel, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ManagedClusterCodeVersionResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_by_environment.metadata = {'url': "/subscriptions/{subscriptionId}/providers/Microsoft.ServiceFabric/locations/{location}/environments/{environment}/managedClusterVersions/{clusterVersion}"}  # type: ignore


    @distributed_trace_async
    async def list(
        self,
        location: str,
        **kwargs: Any
    ) -> List["_models.ManagedClusterCodeVersionResult"]:
        """Gets the list of Service Fabric cluster code versions available for the specified location.

        Gets all available code versions for Service Fabric cluster resources by location.

        :param location: The location for the cluster code versions. This is different from cluster
         location.
        :type location: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of ManagedClusterCodeVersionResult, or the result of cls(response)
        :rtype: list[~azure.mgmt.servicefabricmanagedclusters.models.ManagedClusterCodeVersionResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["_models.ManagedClusterCodeVersionResult"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2022-02-01-preview")  # type: str

        
        request = build_list_request(
            location=location,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.list.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorModel, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('[ManagedClusterCodeVersionResult]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list.metadata = {'url': "/subscriptions/{subscriptionId}/providers/Microsoft.ServiceFabric/locations/{location}/managedClusterVersions"}  # type: ignore


    @distributed_trace_async
    async def list_by_environment(
        self,
        location: str,
        environment: Union[str, "_models.ManagedClusterVersionEnvironment"],
        **kwargs: Any
    ) -> List["_models.ManagedClusterCodeVersionResult"]:
        """Gets the list of Service Fabric cluster code versions available for the specified environment.

        Gets all available code versions for Service Fabric cluster resources by environment.

        :param location: The location for the cluster code versions. This is different from cluster
         location.
        :type location: str
        :param environment: The operating system of the cluster. The default means all.
        :type environment: str or
         ~azure.mgmt.servicefabricmanagedclusters.models.ManagedClusterVersionEnvironment
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of ManagedClusterCodeVersionResult, or the result of cls(response)
        :rtype: list[~azure.mgmt.servicefabricmanagedclusters.models.ManagedClusterCodeVersionResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["_models.ManagedClusterCodeVersionResult"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2022-02-01-preview")  # type: str

        
        request = build_list_by_environment_request(
            location=location,
            environment=environment,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.list_by_environment.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorModel, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('[ManagedClusterCodeVersionResult]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list_by_environment.metadata = {'url': "/subscriptions/{subscriptionId}/providers/Microsoft.ServiceFabric/locations/{location}/environments/{environment}/managedClusterVersions"}  # type: ignore

