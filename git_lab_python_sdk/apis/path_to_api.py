import typing_extensions

from git_lab_python_sdk.paths import PathValues
from git_lab_python_sdk.apis.paths.api_v4_groups_id_badges_badge_id import ApiV4GroupsIdBadgesBadgeId
from git_lab_python_sdk.apis.paths.api_v4_groups_id_badges import ApiV4GroupsIdBadges
from git_lab_python_sdk.apis.paths.api_v4_groups_id_badges_render import ApiV4GroupsIdBadgesRender
from git_lab_python_sdk.apis.paths.api_v4_groups_id_access_requests_user_id import ApiV4GroupsIdAccessRequestsUserId
from git_lab_python_sdk.apis.paths.api_v4_groups_id_access_requests_user_id_approve import ApiV4GroupsIdAccessRequestsUserIdApprove
from git_lab_python_sdk.apis.paths.api_v4_groups_id_access_requests import ApiV4GroupsIdAccessRequests
from git_lab_python_sdk.apis.paths.api_v4_projects_id_repository_merged_branches import ApiV4ProjectsIdRepositoryMergedBranches
from git_lab_python_sdk.apis.paths.api_v4_projects_id_repository_branches_branch import ApiV4ProjectsIdRepositoryBranchesBranch
from git_lab_python_sdk.apis.paths.api_v4_projects_id_repository_branches import ApiV4ProjectsIdRepositoryBranches
from git_lab_python_sdk.apis.paths.api_v4_projects_id_repository_branches_branch_unprotect import ApiV4ProjectsIdRepositoryBranchesBranchUnprotect
from git_lab_python_sdk.apis.paths.api_v4_projects_id_repository_branches_branch_protect import ApiV4ProjectsIdRepositoryBranchesBranchProtect
from git_lab_python_sdk.apis.paths.api_v4_projects_id_badges_badge_id import ApiV4ProjectsIdBadgesBadgeId
from git_lab_python_sdk.apis.paths.api_v4_projects_id_badges import ApiV4ProjectsIdBadges
from git_lab_python_sdk.apis.paths.api_v4_projects_id_badges_render import ApiV4ProjectsIdBadgesRender
from git_lab_python_sdk.apis.paths.api_v4_projects_id_access_requests_user_id import ApiV4ProjectsIdAccessRequestsUserId
from git_lab_python_sdk.apis.paths.api_v4_projects_id_access_requests_user_id_approve import ApiV4ProjectsIdAccessRequestsUserIdApprove
from git_lab_python_sdk.apis.paths.api_v4_projects_id_access_requests import ApiV4ProjectsIdAccessRequests
from git_lab_python_sdk.apis.paths.api_v4_projects_id_alert_management_alerts_alert_iid_metric_images_metric_image_id import ApiV4ProjectsIdAlertManagementAlertsAlertIidMetricImagesMetricImageId
from git_lab_python_sdk.apis.paths.api_v4_projects_id_alert_management_alerts_alert_iid_metric_images import ApiV4ProjectsIdAlertManagementAlertsAlertIidMetricImages
from git_lab_python_sdk.apis.paths.api_v4_projects_id_alert_management_alerts_alert_iid_metric_images_authorize import ApiV4ProjectsIdAlertManagementAlertsAlertIidMetricImagesAuthorize
from git_lab_python_sdk.apis.paths.api_v4_admin_batched_background_migrations_id import ApiV4AdminBatchedBackgroundMigrationsId
from git_lab_python_sdk.apis.paths.api_v4_admin_batched_background_migrations import ApiV4AdminBatchedBackgroundMigrations
from git_lab_python_sdk.apis.paths.api_v4_admin_batched_background_migrations_id_resume import ApiV4AdminBatchedBackgroundMigrationsIdResume
from git_lab_python_sdk.apis.paths.api_v4_admin_batched_background_migrations_id_pause import ApiV4AdminBatchedBackgroundMigrationsIdPause
from git_lab_python_sdk.apis.paths.api_v4_admin_ci_variables_key import ApiV4AdminCiVariablesKey
from git_lab_python_sdk.apis.paths.api_v4_admin_ci_variables import ApiV4AdminCiVariables
from git_lab_python_sdk.apis.paths.api_v4_admin_databases_database_name_dictionary_tables_table_name import ApiV4AdminDatabasesDatabaseNameDictionaryTablesTableName
from git_lab_python_sdk.apis.paths.api_v4_admin_clusters_cluster_id import ApiV4AdminClustersClusterId
from git_lab_python_sdk.apis.paths.api_v4_admin_clusters_add import ApiV4AdminClustersAdd
from git_lab_python_sdk.apis.paths.api_v4_admin_clusters import ApiV4AdminClusters
from git_lab_python_sdk.apis.paths.api_v4_admin_migrations_timestamp_mark import ApiV4AdminMigrationsTimestampMark
from git_lab_python_sdk.apis.paths.api_v4_applications_id import ApiV4ApplicationsId
from git_lab_python_sdk.apis.paths.api_v4_applications import ApiV4Applications
from git_lab_python_sdk.apis.paths.api_v4_avatar import ApiV4Avatar
from git_lab_python_sdk.apis.paths.api_v4_broadcast_messages_id import ApiV4BroadcastMessagesId
from git_lab_python_sdk.apis.paths.api_v4_broadcast_messages import ApiV4BroadcastMessages
from git_lab_python_sdk.apis.paths.api_v4_bulk_imports_import_id_entities_entity_id import ApiV4BulkImportsImportIdEntitiesEntityId
from git_lab_python_sdk.apis.paths.api_v4_bulk_imports_import_id_entities import ApiV4BulkImportsImportIdEntities
from git_lab_python_sdk.apis.paths.api_v4_bulk_imports_import_id import ApiV4BulkImportsImportId
from git_lab_python_sdk.apis.paths.api_v4_bulk_imports_entities import ApiV4BulkImportsEntities
from git_lab_python_sdk.apis.paths.api_v4_bulk_imports import ApiV4BulkImports
from git_lab_python_sdk.apis.paths.api_v4_application_appearance import ApiV4ApplicationAppearance
from git_lab_python_sdk.apis.paths.api_v4_application_plan_limits import ApiV4ApplicationPlanLimits
from git_lab_python_sdk.apis.paths.api_v4_metadata import ApiV4Metadata
from git_lab_python_sdk.apis.paths.api_v4_version import ApiV4Version
from git_lab_python_sdk.apis.paths.api_v4_projects_id_jobs import ApiV4ProjectsIdJobs
from git_lab_python_sdk.apis.paths.api_v4_projects_id_jobs_job_id import ApiV4ProjectsIdJobsJobId
from git_lab_python_sdk.apis.paths.api_v4_projects_id_jobs_job_id_play import ApiV4ProjectsIdJobsJobIdPlay

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.API_V4_GROUPS_ID_BADGES_BADGE_ID: ApiV4GroupsIdBadgesBadgeId,
        PathValues.API_V4_GROUPS_ID_BADGES: ApiV4GroupsIdBadges,
        PathValues.API_V4_GROUPS_ID_BADGES_RENDER: ApiV4GroupsIdBadgesRender,
        PathValues.API_V4_GROUPS_ID_ACCESS_REQUESTS_USER_ID: ApiV4GroupsIdAccessRequestsUserId,
        PathValues.API_V4_GROUPS_ID_ACCESS_REQUESTS_USER_ID_APPROVE: ApiV4GroupsIdAccessRequestsUserIdApprove,
        PathValues.API_V4_GROUPS_ID_ACCESS_REQUESTS: ApiV4GroupsIdAccessRequests,
        PathValues.API_V4_PROJECTS_ID_REPOSITORY_MERGED_BRANCHES: ApiV4ProjectsIdRepositoryMergedBranches,
        PathValues.API_V4_PROJECTS_ID_REPOSITORY_BRANCHES_BRANCH: ApiV4ProjectsIdRepositoryBranchesBranch,
        PathValues.API_V4_PROJECTS_ID_REPOSITORY_BRANCHES: ApiV4ProjectsIdRepositoryBranches,
        PathValues.API_V4_PROJECTS_ID_REPOSITORY_BRANCHES_BRANCH_UNPROTECT: ApiV4ProjectsIdRepositoryBranchesBranchUnprotect,
        PathValues.API_V4_PROJECTS_ID_REPOSITORY_BRANCHES_BRANCH_PROTECT: ApiV4ProjectsIdRepositoryBranchesBranchProtect,
        PathValues.API_V4_PROJECTS_ID_BADGES_BADGE_ID: ApiV4ProjectsIdBadgesBadgeId,
        PathValues.API_V4_PROJECTS_ID_BADGES: ApiV4ProjectsIdBadges,
        PathValues.API_V4_PROJECTS_ID_BADGES_RENDER: ApiV4ProjectsIdBadgesRender,
        PathValues.API_V4_PROJECTS_ID_ACCESS_REQUESTS_USER_ID: ApiV4ProjectsIdAccessRequestsUserId,
        PathValues.API_V4_PROJECTS_ID_ACCESS_REQUESTS_USER_ID_APPROVE: ApiV4ProjectsIdAccessRequestsUserIdApprove,
        PathValues.API_V4_PROJECTS_ID_ACCESS_REQUESTS: ApiV4ProjectsIdAccessRequests,
        PathValues.API_V4_PROJECTS_ID_ALERT_MANAGEMENT_ALERTS_ALERT_IID_METRIC_IMAGES_METRIC_IMAGE_ID: ApiV4ProjectsIdAlertManagementAlertsAlertIidMetricImagesMetricImageId,
        PathValues.API_V4_PROJECTS_ID_ALERT_MANAGEMENT_ALERTS_ALERT_IID_METRIC_IMAGES: ApiV4ProjectsIdAlertManagementAlertsAlertIidMetricImages,
        PathValues.API_V4_PROJECTS_ID_ALERT_MANAGEMENT_ALERTS_ALERT_IID_METRIC_IMAGES_AUTHORIZE: ApiV4ProjectsIdAlertManagementAlertsAlertIidMetricImagesAuthorize,
        PathValues.API_V4_ADMIN_BATCHED_BACKGROUND_MIGRATIONS_ID: ApiV4AdminBatchedBackgroundMigrationsId,
        PathValues.API_V4_ADMIN_BATCHED_BACKGROUND_MIGRATIONS: ApiV4AdminBatchedBackgroundMigrations,
        PathValues.API_V4_ADMIN_BATCHED_BACKGROUND_MIGRATIONS_ID_RESUME: ApiV4AdminBatchedBackgroundMigrationsIdResume,
        PathValues.API_V4_ADMIN_BATCHED_BACKGROUND_MIGRATIONS_ID_PAUSE: ApiV4AdminBatchedBackgroundMigrationsIdPause,
        PathValues.API_V4_ADMIN_CI_VARIABLES_KEY: ApiV4AdminCiVariablesKey,
        PathValues.API_V4_ADMIN_CI_VARIABLES: ApiV4AdminCiVariables,
        PathValues.API_V4_ADMIN_DATABASES_DATABASE_NAME_DICTIONARY_TABLES_TABLE_NAME: ApiV4AdminDatabasesDatabaseNameDictionaryTablesTableName,
        PathValues.API_V4_ADMIN_CLUSTERS_CLUSTER_ID: ApiV4AdminClustersClusterId,
        PathValues.API_V4_ADMIN_CLUSTERS_ADD: ApiV4AdminClustersAdd,
        PathValues.API_V4_ADMIN_CLUSTERS: ApiV4AdminClusters,
        PathValues.API_V4_ADMIN_MIGRATIONS_TIMESTAMP_MARK: ApiV4AdminMigrationsTimestampMark,
        PathValues.API_V4_APPLICATIONS_ID: ApiV4ApplicationsId,
        PathValues.API_V4_APPLICATIONS: ApiV4Applications,
        PathValues.API_V4_AVATAR: ApiV4Avatar,
        PathValues.API_V4_BROADCAST_MESSAGES_ID: ApiV4BroadcastMessagesId,
        PathValues.API_V4_BROADCAST_MESSAGES: ApiV4BroadcastMessages,
        PathValues.API_V4_BULK_IMPORTS_IMPORT_ID_ENTITIES_ENTITY_ID: ApiV4BulkImportsImportIdEntitiesEntityId,
        PathValues.API_V4_BULK_IMPORTS_IMPORT_ID_ENTITIES: ApiV4BulkImportsImportIdEntities,
        PathValues.API_V4_BULK_IMPORTS_IMPORT_ID: ApiV4BulkImportsImportId,
        PathValues.API_V4_BULK_IMPORTS_ENTITIES: ApiV4BulkImportsEntities,
        PathValues.API_V4_BULK_IMPORTS: ApiV4BulkImports,
        PathValues.API_V4_APPLICATION_APPEARANCE: ApiV4ApplicationAppearance,
        PathValues.API_V4_APPLICATION_PLAN_LIMITS: ApiV4ApplicationPlanLimits,
        PathValues.API_V4_METADATA: ApiV4Metadata,
        PathValues.API_V4_VERSION: ApiV4Version,
        PathValues.API_V4_PROJECTS_ID_JOBS: ApiV4ProjectsIdJobs,
        PathValues.API_V4_PROJECTS_ID_JOBS_JOB_ID: ApiV4ProjectsIdJobsJobId,
        PathValues.API_V4_PROJECTS_ID_JOBS_JOB_ID_PLAY: ApiV4ProjectsIdJobsJobIdPlay,
    }
)

path_to_api = PathToApi(
    {
        PathValues.API_V4_GROUPS_ID_BADGES_BADGE_ID: ApiV4GroupsIdBadgesBadgeId,
        PathValues.API_V4_GROUPS_ID_BADGES: ApiV4GroupsIdBadges,
        PathValues.API_V4_GROUPS_ID_BADGES_RENDER: ApiV4GroupsIdBadgesRender,
        PathValues.API_V4_GROUPS_ID_ACCESS_REQUESTS_USER_ID: ApiV4GroupsIdAccessRequestsUserId,
        PathValues.API_V4_GROUPS_ID_ACCESS_REQUESTS_USER_ID_APPROVE: ApiV4GroupsIdAccessRequestsUserIdApprove,
        PathValues.API_V4_GROUPS_ID_ACCESS_REQUESTS: ApiV4GroupsIdAccessRequests,
        PathValues.API_V4_PROJECTS_ID_REPOSITORY_MERGED_BRANCHES: ApiV4ProjectsIdRepositoryMergedBranches,
        PathValues.API_V4_PROJECTS_ID_REPOSITORY_BRANCHES_BRANCH: ApiV4ProjectsIdRepositoryBranchesBranch,
        PathValues.API_V4_PROJECTS_ID_REPOSITORY_BRANCHES: ApiV4ProjectsIdRepositoryBranches,
        PathValues.API_V4_PROJECTS_ID_REPOSITORY_BRANCHES_BRANCH_UNPROTECT: ApiV4ProjectsIdRepositoryBranchesBranchUnprotect,
        PathValues.API_V4_PROJECTS_ID_REPOSITORY_BRANCHES_BRANCH_PROTECT: ApiV4ProjectsIdRepositoryBranchesBranchProtect,
        PathValues.API_V4_PROJECTS_ID_BADGES_BADGE_ID: ApiV4ProjectsIdBadgesBadgeId,
        PathValues.API_V4_PROJECTS_ID_BADGES: ApiV4ProjectsIdBadges,
        PathValues.API_V4_PROJECTS_ID_BADGES_RENDER: ApiV4ProjectsIdBadgesRender,
        PathValues.API_V4_PROJECTS_ID_ACCESS_REQUESTS_USER_ID: ApiV4ProjectsIdAccessRequestsUserId,
        PathValues.API_V4_PROJECTS_ID_ACCESS_REQUESTS_USER_ID_APPROVE: ApiV4ProjectsIdAccessRequestsUserIdApprove,
        PathValues.API_V4_PROJECTS_ID_ACCESS_REQUESTS: ApiV4ProjectsIdAccessRequests,
        PathValues.API_V4_PROJECTS_ID_ALERT_MANAGEMENT_ALERTS_ALERT_IID_METRIC_IMAGES_METRIC_IMAGE_ID: ApiV4ProjectsIdAlertManagementAlertsAlertIidMetricImagesMetricImageId,
        PathValues.API_V4_PROJECTS_ID_ALERT_MANAGEMENT_ALERTS_ALERT_IID_METRIC_IMAGES: ApiV4ProjectsIdAlertManagementAlertsAlertIidMetricImages,
        PathValues.API_V4_PROJECTS_ID_ALERT_MANAGEMENT_ALERTS_ALERT_IID_METRIC_IMAGES_AUTHORIZE: ApiV4ProjectsIdAlertManagementAlertsAlertIidMetricImagesAuthorize,
        PathValues.API_V4_ADMIN_BATCHED_BACKGROUND_MIGRATIONS_ID: ApiV4AdminBatchedBackgroundMigrationsId,
        PathValues.API_V4_ADMIN_BATCHED_BACKGROUND_MIGRATIONS: ApiV4AdminBatchedBackgroundMigrations,
        PathValues.API_V4_ADMIN_BATCHED_BACKGROUND_MIGRATIONS_ID_RESUME: ApiV4AdminBatchedBackgroundMigrationsIdResume,
        PathValues.API_V4_ADMIN_BATCHED_BACKGROUND_MIGRATIONS_ID_PAUSE: ApiV4AdminBatchedBackgroundMigrationsIdPause,
        PathValues.API_V4_ADMIN_CI_VARIABLES_KEY: ApiV4AdminCiVariablesKey,
        PathValues.API_V4_ADMIN_CI_VARIABLES: ApiV4AdminCiVariables,
        PathValues.API_V4_ADMIN_DATABASES_DATABASE_NAME_DICTIONARY_TABLES_TABLE_NAME: ApiV4AdminDatabasesDatabaseNameDictionaryTablesTableName,
        PathValues.API_V4_ADMIN_CLUSTERS_CLUSTER_ID: ApiV4AdminClustersClusterId,
        PathValues.API_V4_ADMIN_CLUSTERS_ADD: ApiV4AdminClustersAdd,
        PathValues.API_V4_ADMIN_CLUSTERS: ApiV4AdminClusters,
        PathValues.API_V4_ADMIN_MIGRATIONS_TIMESTAMP_MARK: ApiV4AdminMigrationsTimestampMark,
        PathValues.API_V4_APPLICATIONS_ID: ApiV4ApplicationsId,
        PathValues.API_V4_APPLICATIONS: ApiV4Applications,
        PathValues.API_V4_AVATAR: ApiV4Avatar,
        PathValues.API_V4_BROADCAST_MESSAGES_ID: ApiV4BroadcastMessagesId,
        PathValues.API_V4_BROADCAST_MESSAGES: ApiV4BroadcastMessages,
        PathValues.API_V4_BULK_IMPORTS_IMPORT_ID_ENTITIES_ENTITY_ID: ApiV4BulkImportsImportIdEntitiesEntityId,
        PathValues.API_V4_BULK_IMPORTS_IMPORT_ID_ENTITIES: ApiV4BulkImportsImportIdEntities,
        PathValues.API_V4_BULK_IMPORTS_IMPORT_ID: ApiV4BulkImportsImportId,
        PathValues.API_V4_BULK_IMPORTS_ENTITIES: ApiV4BulkImportsEntities,
        PathValues.API_V4_BULK_IMPORTS: ApiV4BulkImports,
        PathValues.API_V4_APPLICATION_APPEARANCE: ApiV4ApplicationAppearance,
        PathValues.API_V4_APPLICATION_PLAN_LIMITS: ApiV4ApplicationPlanLimits,
        PathValues.API_V4_METADATA: ApiV4Metadata,
        PathValues.API_V4_VERSION: ApiV4Version,
        PathValues.API_V4_PROJECTS_ID_JOBS: ApiV4ProjectsIdJobs,
        PathValues.API_V4_PROJECTS_ID_JOBS_JOB_ID: ApiV4ProjectsIdJobsJobId,
        PathValues.API_V4_PROJECTS_ID_JOBS_JOB_ID_PLAY: ApiV4ProjectsIdJobsJobIdPlay,
    }
)
