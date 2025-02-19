# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from git_lab_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    BADGES = "badges"
    BRANCHES = "branches"
    ACCESS_REQUESTS = "access_requests"
    BULK_IMPORTS = "bulk_imports"
    ALERT_MANAGEMENT = "alert_management"
    BROADCAST_MESSAGES = "broadcast_messages"
    CI_VARIABLES = "ci_variables"
    CLUSTERS = "clusters"
    BATCHED_BACKGROUND_MIGRATIONS = "batched_background_migrations"
    APPLICATIONS = "applications"
    JOBS = "jobs"
    APPLICATION = "application"
    METADATA = "metadata"
    PLAN_LIMITS = "plan_limits"
    ADMIN = "admin"
    MIGRATIONS = "migrations"
    AVATAR = "avatar"
    CI_LINT = "ci_lint"
    CI_RESOURCE_GROUPS = "ci_resource_groups"
    CLUSTER_AGENTS = "cluster_agents"
    COMPOSER_PACKAGES = "composer_packages"
    CONAN_PACKAGES = "conan_packages"
    CONTAINER_REGISTRY = "container_registry"
    CONTAINER_REGISTRY_EVENT = "container_registry_event"
    DASHBOARD_ANNOTATIONS = "dashboard_annotations"
    DEBIAN_DISTRIBUTION = "debian_distribution"
    DEBIAN_PACKAGES = "debian_packages"
    DEPENDENCY_PROXY = "dependency_proxy"
    DEPLOY_KEYS = "deploy_keys"
    DEPLOY_TOKENS = "deploy_tokens"
    DEPLOYMENTS = "deployments"
    DORA_METRICS = "dora_metrics"
    ENVIRONMENTS = "environments"
    ERROR_TRACKING_CLIENT_KEYS = "error_tracking_client_keys"
    ERROR_TRACKING_PROJECT_SETTINGS = "error_tracking_project_settings"
    FEATURE_FLAGS_USER_LISTS = "feature_flags_user_lists"
    FEATURE_FLAGS = "feature_flags"
    FEATURES = "features"
    FREEZE_PERIODS = "freeze_periods"
    GENERIC_PACKAGES = "generic_packages"
    GEO = "geo"
    GEO_NODES = "geo_nodes"
    GO_PROXY = "go_proxy"
    GROUP_EXPORT = "group_export"
    GROUP_IMPORT = "group_import"
    GROUP_PACKAGES = "group_packages"
    HELM_PACKAGES = "helm_packages"
    INTEGRATIONS = "integrations"
    ISSUE_LINKS = "issue_links"
    JIRA_CONNECT_SUBSCRIPTIONS = "jira_connect_subscriptions"
    MAVEN_PACKAGES = "maven_packages"
    MERGE_REQUESTS = "merge_requests"
    METRICS_USER_STARRED_DASHBOARDS = "metrics_user_starred_dashboards"
    ML_MODEL_REGISTRY = "ml_model_registry"
    NPM_PACKAGES = "npm_packages"
    NUGET_PACKAGES = "nuget_packages"
    PACKAGE_FILES = "package_files"
    PROJECT_EXPORT = "project_export"
    PROJECT_HOOKS = "project_hooks"
    PROJECT_IMPORT = "project_import"
    PROJECT_IMPORT_BITBUCKET = "project_import_bitbucket"
    PROJECT_IMPORT_GITHUB = "project_import_github"
    PROJECT_PACKAGES = "project_packages"
    PROJECTS = "projects"
    PROTECTED_ENVIRONMENTS = "protected environments"
    PYPI_PACKAGES = "pypi_packages"
    RELEASE_LINKS = "release_links"
    RELEASES = "releases"
    RESOURCE_MILESTONE_EVENTS = "resource_milestone_events"
    RPM_PACKAGES = "rpm_packages"
    RUBYGEM_PACKAGES = "rubygem_packages"
    SUGGESTIONS = "suggestions"
    SYSTEM_HOOKS = "system_hooks"
    TERRAFORM_STATE = "terraform_state"
    TERRAFORM_REGISTRY = "terraform_registry"
    UNLEASH_API = "unleash_api"
