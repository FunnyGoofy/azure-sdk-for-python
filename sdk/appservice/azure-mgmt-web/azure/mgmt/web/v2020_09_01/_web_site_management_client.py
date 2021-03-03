# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    from azure.core.credentials import TokenCredential

from ._configuration import WebSiteManagementClientConfiguration
from .operations import AppServiceCertificateOrdersOperations
from .operations import CertificateRegistrationProviderOperations
from .operations import DomainsOperations
from .operations import TopLevelDomainsOperations
from .operations import DomainRegistrationProviderOperations
from .operations import CertificatesOperations
from .operations import DeletedWebAppsOperations
from .operations import DiagnosticsOperations
from .operations import ProviderOperations
from .operations import RecommendationsOperations
from .operations import WebSiteManagementClientOperationsMixin
from .operations import WebAppsOperations
from .operations import StaticSitesOperations
from .operations import AppServiceEnvironmentsOperations
from .operations import AppServicePlansOperations
from .operations import ResourceHealthMetadataOperations
from . import models


class WebSiteManagementClient(WebSiteManagementClientOperationsMixin):
    """WebSite Management Client.

    :ivar app_service_certificate_orders: AppServiceCertificateOrdersOperations operations
    :vartype app_service_certificate_orders: azure.mgmt.web.v2020_09_01.operations.AppServiceCertificateOrdersOperations
    :ivar certificate_registration_provider: CertificateRegistrationProviderOperations operations
    :vartype certificate_registration_provider: azure.mgmt.web.v2020_09_01.operations.CertificateRegistrationProviderOperations
    :ivar domains: DomainsOperations operations
    :vartype domains: azure.mgmt.web.v2020_09_01.operations.DomainsOperations
    :ivar top_level_domains: TopLevelDomainsOperations operations
    :vartype top_level_domains: azure.mgmt.web.v2020_09_01.operations.TopLevelDomainsOperations
    :ivar domain_registration_provider: DomainRegistrationProviderOperations operations
    :vartype domain_registration_provider: azure.mgmt.web.v2020_09_01.operations.DomainRegistrationProviderOperations
    :ivar certificates: CertificatesOperations operations
    :vartype certificates: azure.mgmt.web.v2020_09_01.operations.CertificatesOperations
    :ivar deleted_web_apps: DeletedWebAppsOperations operations
    :vartype deleted_web_apps: azure.mgmt.web.v2020_09_01.operations.DeletedWebAppsOperations
    :ivar diagnostics: DiagnosticsOperations operations
    :vartype diagnostics: azure.mgmt.web.v2020_09_01.operations.DiagnosticsOperations
    :ivar provider: ProviderOperations operations
    :vartype provider: azure.mgmt.web.v2020_09_01.operations.ProviderOperations
    :ivar recommendations: RecommendationsOperations operations
    :vartype recommendations: azure.mgmt.web.v2020_09_01.operations.RecommendationsOperations
    :ivar web_apps: WebAppsOperations operations
    :vartype web_apps: azure.mgmt.web.v2020_09_01.operations.WebAppsOperations
    :ivar static_sites: StaticSitesOperations operations
    :vartype static_sites: azure.mgmt.web.v2020_09_01.operations.StaticSitesOperations
    :ivar app_service_environments: AppServiceEnvironmentsOperations operations
    :vartype app_service_environments: azure.mgmt.web.v2020_09_01.operations.AppServiceEnvironmentsOperations
    :ivar app_service_plans: AppServicePlansOperations operations
    :vartype app_service_plans: azure.mgmt.web.v2020_09_01.operations.AppServicePlansOperations
    :ivar resource_health_metadata: ResourceHealthMetadataOperations operations
    :vartype resource_health_metadata: azure.mgmt.web.v2020_09_01.operations.ResourceHealthMetadataOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        subscription_id,  # type: str
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = WebSiteManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.app_service_certificate_orders = AppServiceCertificateOrdersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.certificate_registration_provider = CertificateRegistrationProviderOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.domains = DomainsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.top_level_domains = TopLevelDomainsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.domain_registration_provider = DomainRegistrationProviderOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.certificates = CertificatesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.deleted_web_apps = DeletedWebAppsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.diagnostics = DiagnosticsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.provider = ProviderOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.recommendations = RecommendationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.web_apps = WebAppsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.static_sites = StaticSitesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.app_service_environments = AppServiceEnvironmentsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.app_service_plans = AppServicePlansOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.resource_health_metadata = ResourceHealthMetadataOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> WebSiteManagementClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)