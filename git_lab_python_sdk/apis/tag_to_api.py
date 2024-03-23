import typing_extensions

from git_lab_python_sdk.apis.tags import TagValues
from git_lab_python_sdk.apis.tags.badges_api import BadgesApi
from git_lab_python_sdk.apis.tags.branches_api import BranchesApi
from git_lab_python_sdk.apis.tags.access_requests_api import AccessRequestsApi
from git_lab_python_sdk.apis.tags.bulk_imports_api import BulkImportsApi
from git_lab_python_sdk.apis.tags.alert_management_api import AlertManagementApi
from git_lab_python_sdk.apis.tags.broadcast_messages_api import BroadcastMessagesApi
from git_lab_python_sdk.apis.tags.ci_variables_api import CiVariablesApi
from git_lab_python_sdk.apis.tags.clusters_api import ClustersApi
from git_lab_python_sdk.apis.tags.batched_background_migrations_api import BatchedBackgroundMigrationsApi
from git_lab_python_sdk.apis.tags.applications_api import ApplicationsApi
from git_lab_python_sdk.apis.tags.jobs_api import JobsApi
from git_lab_python_sdk.apis.tags.application_api import ApplicationApi
from git_lab_python_sdk.apis.tags.metadata_api import MetadataApi
from git_lab_python_sdk.apis.tags.plan_limits_api import PlanLimitsApi
from git_lab_python_sdk.apis.tags.admin_api import AdminApi
from git_lab_python_sdk.apis.tags.migrations_api import MigrationsApi
from git_lab_python_sdk.apis.tags.avatar_api import AvatarApi
from git_lab_python_sdk.apis.tags.ci_lint_api import CiLintApi
from git_lab_python_sdk.apis.tags.ci_resource_groups_api import CiResourceGroupsApi
from git_lab_python_sdk.apis.tags.cluster_agents_api import ClusterAgentsApi
from git_lab_python_sdk.apis.tags.composer_packages_api import ComposerPackagesApi
from git_lab_python_sdk.apis.tags.conan_packages_api import ConanPackagesApi
from git_lab_python_sdk.apis.tags.container_registry_api import ContainerRegistryApi
from git_lab_python_sdk.apis.tags.container_registry_event_api import ContainerRegistryEventApi
from git_lab_python_sdk.apis.tags.dashboard_annotations_api import DashboardAnnotationsApi
from git_lab_python_sdk.apis.tags.debian_distribution_api import DebianDistributionApi
from git_lab_python_sdk.apis.tags.debian_packages_api import DebianPackagesApi
from git_lab_python_sdk.apis.tags.dependency_proxy_api import DependencyProxyApi
from git_lab_python_sdk.apis.tags.deploy_keys_api import DeployKeysApi
from git_lab_python_sdk.apis.tags.deploy_tokens_api import DeployTokensApi
from git_lab_python_sdk.apis.tags.deployments_api import DeploymentsApi
from git_lab_python_sdk.apis.tags.dora_metrics_api import DoraMetricsApi
from git_lab_python_sdk.apis.tags.environments_api import EnvironmentsApi
from git_lab_python_sdk.apis.tags.error_tracking_client_keys_api import ErrorTrackingClientKeysApi
from git_lab_python_sdk.apis.tags.error_tracking_project_settings_api import ErrorTrackingProjectSettingsApi
from git_lab_python_sdk.apis.tags.feature_flags_user_lists_api import FeatureFlagsUserListsApi
from git_lab_python_sdk.apis.tags.feature_flags_api import FeatureFlagsApi
from git_lab_python_sdk.apis.tags.features_api import FeaturesApi
from git_lab_python_sdk.apis.tags.freeze_periods_api import FreezePeriodsApi
from git_lab_python_sdk.apis.tags.generic_packages_api import GenericPackagesApi
from git_lab_python_sdk.apis.tags.geo_api import GeoApi
from git_lab_python_sdk.apis.tags.geo_nodes_api import GeoNodesApi
from git_lab_python_sdk.apis.tags.go_proxy_api import GoProxyApi
from git_lab_python_sdk.apis.tags.group_export_api import GroupExportApi
from git_lab_python_sdk.apis.tags.group_import_api import GroupImportApi
from git_lab_python_sdk.apis.tags.group_packages_api import GroupPackagesApi
from git_lab_python_sdk.apis.tags.helm_packages_api import HelmPackagesApi
from git_lab_python_sdk.apis.tags.integrations_api import IntegrationsApi
from git_lab_python_sdk.apis.tags.issue_links_api import IssueLinksApi
from git_lab_python_sdk.apis.tags.jira_connect_subscriptions_api import JiraConnectSubscriptionsApi
from git_lab_python_sdk.apis.tags.maven_packages_api import MavenPackagesApi
from git_lab_python_sdk.apis.tags.merge_requests_api import MergeRequestsApi
from git_lab_python_sdk.apis.tags.metrics_user_starred_dashboards_api import MetricsUserStarredDashboardsApi
from git_lab_python_sdk.apis.tags.ml_model_registry_api import MlModelRegistryApi
from git_lab_python_sdk.apis.tags.npm_packages_api import NpmPackagesApi
from git_lab_python_sdk.apis.tags.nuget_packages_api import NugetPackagesApi
from git_lab_python_sdk.apis.tags.package_files_api import PackageFilesApi
from git_lab_python_sdk.apis.tags.project_export_api import ProjectExportApi
from git_lab_python_sdk.apis.tags.project_hooks_api import ProjectHooksApi
from git_lab_python_sdk.apis.tags.project_import_api import ProjectImportApi
from git_lab_python_sdk.apis.tags.project_import_bitbucket_api import ProjectImportBitbucketApi
from git_lab_python_sdk.apis.tags.project_import_github_api import ProjectImportGithubApi
from git_lab_python_sdk.apis.tags.project_packages_api import ProjectPackagesApi
from git_lab_python_sdk.apis.tags.projects_api import ProjectsApi
from git_lab_python_sdk.apis.tags.protected_environments_api import ProtectedEnvironmentsApi
from git_lab_python_sdk.apis.tags.pypi_packages_api import PypiPackagesApi
from git_lab_python_sdk.apis.tags.release_links_api import ReleaseLinksApi
from git_lab_python_sdk.apis.tags.releases_api import ReleasesApi
from git_lab_python_sdk.apis.tags.resource_milestone_events_api import ResourceMilestoneEventsApi
from git_lab_python_sdk.apis.tags.rpm_packages_api import RpmPackagesApi
from git_lab_python_sdk.apis.tags.rubygem_packages_api import RubygemPackagesApi
from git_lab_python_sdk.apis.tags.suggestions_api import SuggestionsApi
from git_lab_python_sdk.apis.tags.system_hooks_api import SystemHooksApi
from git_lab_python_sdk.apis.tags.terraform_state_api import TerraformStateApi
from git_lab_python_sdk.apis.tags.terraform_registry_api import TerraformRegistryApi
from git_lab_python_sdk.apis.tags.unleash_api_api import UnleashApiApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.BADGES: BadgesApi,
        TagValues.BRANCHES: BranchesApi,
        TagValues.ACCESS_REQUESTS: AccessRequestsApi,
        TagValues.BULK_IMPORTS: BulkImportsApi,
        TagValues.ALERT_MANAGEMENT: AlertManagementApi,
        TagValues.BROADCAST_MESSAGES: BroadcastMessagesApi,
        TagValues.CI_VARIABLES: CiVariablesApi,
        TagValues.CLUSTERS: ClustersApi,
        TagValues.BATCHED_BACKGROUND_MIGRATIONS: BatchedBackgroundMigrationsApi,
        TagValues.APPLICATIONS: ApplicationsApi,
        TagValues.JOBS: JobsApi,
        TagValues.APPLICATION: ApplicationApi,
        TagValues.METADATA: MetadataApi,
        TagValues.PLAN_LIMITS: PlanLimitsApi,
        TagValues.ADMIN: AdminApi,
        TagValues.MIGRATIONS: MigrationsApi,
        TagValues.AVATAR: AvatarApi,
        TagValues.CI_LINT: CiLintApi,
        TagValues.CI_RESOURCE_GROUPS: CiResourceGroupsApi,
        TagValues.CLUSTER_AGENTS: ClusterAgentsApi,
        TagValues.COMPOSER_PACKAGES: ComposerPackagesApi,
        TagValues.CONAN_PACKAGES: ConanPackagesApi,
        TagValues.CONTAINER_REGISTRY: ContainerRegistryApi,
        TagValues.CONTAINER_REGISTRY_EVENT: ContainerRegistryEventApi,
        TagValues.DASHBOARD_ANNOTATIONS: DashboardAnnotationsApi,
        TagValues.DEBIAN_DISTRIBUTION: DebianDistributionApi,
        TagValues.DEBIAN_PACKAGES: DebianPackagesApi,
        TagValues.DEPENDENCY_PROXY: DependencyProxyApi,
        TagValues.DEPLOY_KEYS: DeployKeysApi,
        TagValues.DEPLOY_TOKENS: DeployTokensApi,
        TagValues.DEPLOYMENTS: DeploymentsApi,
        TagValues.DORA_METRICS: DoraMetricsApi,
        TagValues.ENVIRONMENTS: EnvironmentsApi,
        TagValues.ERROR_TRACKING_CLIENT_KEYS: ErrorTrackingClientKeysApi,
        TagValues.ERROR_TRACKING_PROJECT_SETTINGS: ErrorTrackingProjectSettingsApi,
        TagValues.FEATURE_FLAGS_USER_LISTS: FeatureFlagsUserListsApi,
        TagValues.FEATURE_FLAGS: FeatureFlagsApi,
        TagValues.FEATURES: FeaturesApi,
        TagValues.FREEZE_PERIODS: FreezePeriodsApi,
        TagValues.GENERIC_PACKAGES: GenericPackagesApi,
        TagValues.GEO: GeoApi,
        TagValues.GEO_NODES: GeoNodesApi,
        TagValues.GO_PROXY: GoProxyApi,
        TagValues.GROUP_EXPORT: GroupExportApi,
        TagValues.GROUP_IMPORT: GroupImportApi,
        TagValues.GROUP_PACKAGES: GroupPackagesApi,
        TagValues.HELM_PACKAGES: HelmPackagesApi,
        TagValues.INTEGRATIONS: IntegrationsApi,
        TagValues.ISSUE_LINKS: IssueLinksApi,
        TagValues.JIRA_CONNECT_SUBSCRIPTIONS: JiraConnectSubscriptionsApi,
        TagValues.MAVEN_PACKAGES: MavenPackagesApi,
        TagValues.MERGE_REQUESTS: MergeRequestsApi,
        TagValues.METRICS_USER_STARRED_DASHBOARDS: MetricsUserStarredDashboardsApi,
        TagValues.ML_MODEL_REGISTRY: MlModelRegistryApi,
        TagValues.NPM_PACKAGES: NpmPackagesApi,
        TagValues.NUGET_PACKAGES: NugetPackagesApi,
        TagValues.PACKAGE_FILES: PackageFilesApi,
        TagValues.PROJECT_EXPORT: ProjectExportApi,
        TagValues.PROJECT_HOOKS: ProjectHooksApi,
        TagValues.PROJECT_IMPORT: ProjectImportApi,
        TagValues.PROJECT_IMPORT_BITBUCKET: ProjectImportBitbucketApi,
        TagValues.PROJECT_IMPORT_GITHUB: ProjectImportGithubApi,
        TagValues.PROJECT_PACKAGES: ProjectPackagesApi,
        TagValues.PROJECTS: ProjectsApi,
        TagValues.PROTECTED_ENVIRONMENTS: ProtectedEnvironmentsApi,
        TagValues.PYPI_PACKAGES: PypiPackagesApi,
        TagValues.RELEASE_LINKS: ReleaseLinksApi,
        TagValues.RELEASES: ReleasesApi,
        TagValues.RESOURCE_MILESTONE_EVENTS: ResourceMilestoneEventsApi,
        TagValues.RPM_PACKAGES: RpmPackagesApi,
        TagValues.RUBYGEM_PACKAGES: RubygemPackagesApi,
        TagValues.SUGGESTIONS: SuggestionsApi,
        TagValues.SYSTEM_HOOKS: SystemHooksApi,
        TagValues.TERRAFORM_STATE: TerraformStateApi,
        TagValues.TERRAFORM_REGISTRY: TerraformRegistryApi,
        TagValues.UNLEASH_API: UnleashApiApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.BADGES: BadgesApi,
        TagValues.BRANCHES: BranchesApi,
        TagValues.ACCESS_REQUESTS: AccessRequestsApi,
        TagValues.BULK_IMPORTS: BulkImportsApi,
        TagValues.ALERT_MANAGEMENT: AlertManagementApi,
        TagValues.BROADCAST_MESSAGES: BroadcastMessagesApi,
        TagValues.CI_VARIABLES: CiVariablesApi,
        TagValues.CLUSTERS: ClustersApi,
        TagValues.BATCHED_BACKGROUND_MIGRATIONS: BatchedBackgroundMigrationsApi,
        TagValues.APPLICATIONS: ApplicationsApi,
        TagValues.JOBS: JobsApi,
        TagValues.APPLICATION: ApplicationApi,
        TagValues.METADATA: MetadataApi,
        TagValues.PLAN_LIMITS: PlanLimitsApi,
        TagValues.ADMIN: AdminApi,
        TagValues.MIGRATIONS: MigrationsApi,
        TagValues.AVATAR: AvatarApi,
        TagValues.CI_LINT: CiLintApi,
        TagValues.CI_RESOURCE_GROUPS: CiResourceGroupsApi,
        TagValues.CLUSTER_AGENTS: ClusterAgentsApi,
        TagValues.COMPOSER_PACKAGES: ComposerPackagesApi,
        TagValues.CONAN_PACKAGES: ConanPackagesApi,
        TagValues.CONTAINER_REGISTRY: ContainerRegistryApi,
        TagValues.CONTAINER_REGISTRY_EVENT: ContainerRegistryEventApi,
        TagValues.DASHBOARD_ANNOTATIONS: DashboardAnnotationsApi,
        TagValues.DEBIAN_DISTRIBUTION: DebianDistributionApi,
        TagValues.DEBIAN_PACKAGES: DebianPackagesApi,
        TagValues.DEPENDENCY_PROXY: DependencyProxyApi,
        TagValues.DEPLOY_KEYS: DeployKeysApi,
        TagValues.DEPLOY_TOKENS: DeployTokensApi,
        TagValues.DEPLOYMENTS: DeploymentsApi,
        TagValues.DORA_METRICS: DoraMetricsApi,
        TagValues.ENVIRONMENTS: EnvironmentsApi,
        TagValues.ERROR_TRACKING_CLIENT_KEYS: ErrorTrackingClientKeysApi,
        TagValues.ERROR_TRACKING_PROJECT_SETTINGS: ErrorTrackingProjectSettingsApi,
        TagValues.FEATURE_FLAGS_USER_LISTS: FeatureFlagsUserListsApi,
        TagValues.FEATURE_FLAGS: FeatureFlagsApi,
        TagValues.FEATURES: FeaturesApi,
        TagValues.FREEZE_PERIODS: FreezePeriodsApi,
        TagValues.GENERIC_PACKAGES: GenericPackagesApi,
        TagValues.GEO: GeoApi,
        TagValues.GEO_NODES: GeoNodesApi,
        TagValues.GO_PROXY: GoProxyApi,
        TagValues.GROUP_EXPORT: GroupExportApi,
        TagValues.GROUP_IMPORT: GroupImportApi,
        TagValues.GROUP_PACKAGES: GroupPackagesApi,
        TagValues.HELM_PACKAGES: HelmPackagesApi,
        TagValues.INTEGRATIONS: IntegrationsApi,
        TagValues.ISSUE_LINKS: IssueLinksApi,
        TagValues.JIRA_CONNECT_SUBSCRIPTIONS: JiraConnectSubscriptionsApi,
        TagValues.MAVEN_PACKAGES: MavenPackagesApi,
        TagValues.MERGE_REQUESTS: MergeRequestsApi,
        TagValues.METRICS_USER_STARRED_DASHBOARDS: MetricsUserStarredDashboardsApi,
        TagValues.ML_MODEL_REGISTRY: MlModelRegistryApi,
        TagValues.NPM_PACKAGES: NpmPackagesApi,
        TagValues.NUGET_PACKAGES: NugetPackagesApi,
        TagValues.PACKAGE_FILES: PackageFilesApi,
        TagValues.PROJECT_EXPORT: ProjectExportApi,
        TagValues.PROJECT_HOOKS: ProjectHooksApi,
        TagValues.PROJECT_IMPORT: ProjectImportApi,
        TagValues.PROJECT_IMPORT_BITBUCKET: ProjectImportBitbucketApi,
        TagValues.PROJECT_IMPORT_GITHUB: ProjectImportGithubApi,
        TagValues.PROJECT_PACKAGES: ProjectPackagesApi,
        TagValues.PROJECTS: ProjectsApi,
        TagValues.PROTECTED_ENVIRONMENTS: ProtectedEnvironmentsApi,
        TagValues.PYPI_PACKAGES: PypiPackagesApi,
        TagValues.RELEASE_LINKS: ReleaseLinksApi,
        TagValues.RELEASES: ReleasesApi,
        TagValues.RESOURCE_MILESTONE_EVENTS: ResourceMilestoneEventsApi,
        TagValues.RPM_PACKAGES: RpmPackagesApi,
        TagValues.RUBYGEM_PACKAGES: RubygemPackagesApi,
        TagValues.SUGGESTIONS: SuggestionsApi,
        TagValues.SYSTEM_HOOKS: SystemHooksApi,
        TagValues.TERRAFORM_STATE: TerraformStateApi,
        TagValues.TERRAFORM_REGISTRY: TerraformRegistryApi,
        TagValues.UNLEASH_API: UnleashApiApi,
    }
)
