operation_parameter_map = {
    '/api/v4/groups/{id}/access_requests/{user_id}/approve-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'access_level'
            },
        ]
    },
    '/api/v4/projects/{id}/access_requests/{user_id}/approve-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'access_level'
            },
        ]
    },
    '/api/v4/groups/{id}/access_requests/{user_id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/api/v4/projects/{id}/access_requests/{user_id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/api/v4/groups/{id}/access_requests-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
        ]
    },
    '/api/v4/projects/{id}/access_requests-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
        ]
    },
    '/api/v4/groups/{id}/access_requests-POST': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/api/v4/projects/{id}/access_requests-POST': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/api/v4/admin/databases/{database_name}/dictionary/tables/{table_name}-GET': {
        'parameters': [
            {
                'name': 'database_name'
            },
            {
                'name': 'table_name'
            },
        ]
    },
    '/api/v4/projects/{id}/alert_management_alerts/{alert_iid}/metric_images/authorize-POST': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'alert_iid'
            },
        ]
    },
    '/api/v4/projects/{id}/alert_management_alerts/{alert_iid}/metric_images-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'alert_iid'
            },
        ]
    },
    '/api/v4/projects/{id}/alert_management_alerts/{alert_iid}/metric_images/{metric_image_id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'alert_iid'
            },
            {
                'name': 'metric_image_id'
            },
        ]
    },
    '/api/v4/projects/{id}/alert_management_alerts/{alert_iid}/metric_images/{metric_image_id}-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'alert_iid'
            },
            {
                'name': 'metric_image_id'
            },
            {
                'name': 'url'
            },
            {
                'name': 'url_text'
            },
        ]
    },
    '/api/v4/projects/{id}/alert_management_alerts/{alert_iid}/metric_images-POST': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'alert_iid'
            },
            {
                'name': 'file'
            },
            {
                'name': 'url'
            },
            {
                'name': 'url_text'
            },
        ]
    },
    '/api/v4/application/appearance-GET': {
        'parameters': [
        ]
    },
    '/api/v4/application/appearance-PUT': {
        'parameters': [
            {
                'name': 'title'
            },
            {
                'name': 'description'
            },
            {
                'name': 'pwa_name'
            },
            {
                'name': 'pwa_short_name'
            },
            {
                'name': 'pwa_description'
            },
            {
                'name': 'logo'
            },
            {
                'name': 'pwa_icon'
            },
            {
                'name': 'header_logo'
            },
            {
                'name': 'favicon'
            },
            {
                'name': 'new_project_guidelines'
            },
            {
                'name': 'profile_image_guidelines'
            },
            {
                'name': 'header_message'
            },
            {
                'name': 'footer_message'
            },
            {
                'name': 'message_background_color'
            },
            {
                'name': 'message_font_color'
            },
            {
                'name': 'email_header_and_footer_enabled'
            },
        ]
    },
    '/api/v4/applications-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'redirect_uri'
            },
            {
                'name': 'scopes'
            },
            {
                'name': 'confidential'
            },
        ]
    },
    '/api/v4/applications/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/api/v4/applications-GET': {
        'parameters': [
        ]
    },
    '/api/v4/avatar-GET': {
        'parameters': [
            {
                'name': 'email'
            },
            {
                'name': 'size'
            },
        ]
    },
    '/api/v4/groups/{id}/badges-POST': {
        'parameters': [
            {
                'name': 'link_url'
            },
            {
                'name': 'image_url'
            },
            {
                'name': 'id'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/api/v4/projects/{id}/badges-POST': {
        'parameters': [
            {
                'name': 'link_url'
            },
            {
                'name': 'image_url'
            },
            {
                'name': 'id'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/api/v4/groups/{id}/badges/{badge_id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'badge_id'
            },
        ]
    },
    '/api/v4/groups/{id}/badges-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/api/v4/projects/{id}/badges/{badge_id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'badge_id'
            },
        ]
    },
    '/api/v4/projects/{id}/badges-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/api/v4/groups/{id}/badges/render-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'link_url'
            },
            {
                'name': 'image_url'
            },
        ]
    },
    '/api/v4/groups/{id}/badges/{badge_id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'badge_id'
            },
        ]
    },
    '/api/v4/projects/{id}/badges/{badge_id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'badge_id'
            },
        ]
    },
    '/api/v4/projects/{id}/badges/render-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'link_url'
            },
            {
                'name': 'image_url'
            },
        ]
    },
    '/api/v4/groups/{id}/badges/{badge_id}-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'badge_id'
            },
            {
                'name': 'link_url'
            },
            {
                'name': 'image_url'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/api/v4/projects/{id}/badges/{badge_id}-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'badge_id'
            },
            {
                'name': 'link_url'
            },
            {
                'name': 'image_url'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/api/v4/admin/batched_background_migrations/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'database'
            },
        ]
    },
    '/api/v4/admin/batched_background_migrations-GET': {
        'parameters': [
            {
                'name': 'database'
            },
        ]
    },
    '/api/v4/admin/batched_background_migrations/{id}/pause-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'database'
            },
        ]
    },
    '/api/v4/admin/batched_background_migrations/{id}/resume-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'database'
            },
        ]
    },
    '/api/v4/projects/{id}/repository/branches/{branch}-HEAD': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'branch'
            },
        ]
    },
    '/api/v4/projects/{id}/repository/branches-POST': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'branch'
            },
            {
                'name': 'ref'
            },
        ]
    },
    '/api/v4/projects/{id}/repository/branches/{branch}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'branch'
            },
        ]
    },
    '/api/v4/projects/{id}/repository/merged_branches-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/api/v4/projects/{id}/repository/branches-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'search'
            },
            {
                'name': 'regex'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'page_token'
            },
        ]
    },
    '/api/v4/projects/{id}/repository/branches/{branch}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'branch'
            },
        ]
    },
    '/api/v4/projects/{id}/repository/branches/{branch}/protect-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'branch'
            },
            {
                'name': 'developers_can_push'
            },
            {
                'name': 'developers_can_merge'
            },
        ]
    },
    '/api/v4/projects/{id}/repository/branches/{branch}/unprotect-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'branch'
            },
        ]
    },
    '/api/v4/broadcast_messages-POST': {
        'parameters': [
            {
                'name': 'message'
            },
            {
                'name': 'starts_at'
            },
            {
                'name': 'ends_at'
            },
            {
                'name': 'color'
            },
            {
                'name': 'font'
            },
            {
                'name': 'target_access_levels'
            },
            {
                'name': 'target_path'
            },
            {
                'name': 'broadcast_type'
            },
            {
                'name': 'dismissable'
            },
        ]
    },
    '/api/v4/broadcast_messages/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/api/v4/broadcast_messages/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/api/v4/broadcast_messages-GET': {
        'parameters': [
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
        ]
    },
    '/api/v4/broadcast_messages/{id}-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'message'
            },
            {
                'name': 'starts_at'
            },
            {
                'name': 'ends_at'
            },
            {
                'name': 'color'
            },
            {
                'name': 'font'
            },
            {
                'name': 'target_access_levels'
            },
            {
                'name': 'target_path'
            },
            {
                'name': 'broadcast_type'
            },
            {
                'name': 'dismissable'
            },
        ]
    },
    '/api/v4/bulk_imports/{import_id}/entities/{entity_id}-GET': {
        'parameters': [
            {
                'name': 'import_id'
            },
            {
                'name': 'entity_id'
            },
        ]
    },
    '/api/v4/bulk_imports/{import_id}-GET': {
        'parameters': [
            {
                'name': 'import_id'
            },
        ]
    },
    '/api/v4/bulk_imports/{import_id}/entities-GET': {
        'parameters': [
            {
                'name': 'import_id'
            },
            {
                'name': 'status'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
        ]
    },
    '/api/v4/bulk_imports/entities-GET': {
        'parameters': [
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'status'
            },
        ]
    },
    '/api/v4/bulk_imports-GET': {
        'parameters': [
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'status'
            },
        ]
    },
    '/api/v4/bulk_imports-POST': {
        'parameters': [
            {
                'name': 'configuration[url]'
            },
            {
                'name': 'configuration[access_token]'
            },
            {
                'name': 'entities[source_type]'
            },
            {
                'name': 'entities[source_full_path]'
            },
            {
                'name': 'entities[destination_namespace]'
            },
            {
                'name': 'entities[destination_slug]'
            },
            {
                'name': 'entities[destination_name]'
            },
            {
                'name': 'entities[migrate_projects]'
            },
        ]
    },
    '/api/v4/admin/ci/variables-POST': {
        'parameters': [
            {
                'name': 'key'
            },
            {
                'name': 'value'
            },
            {
                'name': 'protected'
            },
            {
                'name': 'masked'
            },
            {
                'name': 'raw'
            },
            {
                'name': 'variable_type'
            },
        ]
    },
    '/api/v4/admin/ci/variables/{key}-DELETE': {
        'parameters': [
            {
                'name': 'key'
            },
        ]
    },
    '/api/v4/admin/ci/variables/{key}-GET': {
        'parameters': [
            {
                'name': 'key'
            },
        ]
    },
    '/api/v4/admin/ci/variables-GET': {
        'parameters': [
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
        ]
    },
    '/api/v4/admin/ci/variables/{key}-PUT': {
        'parameters': [
            {
                'name': 'key'
            },
            {
                'name': 'value'
            },
            {
                'name': 'protected'
            },
            {
                'name': 'masked'
            },
            {
                'name': 'raw'
            },
            {
                'name': 'variable_type'
            },
        ]
    },
    '/api/v4/admin/clusters/add-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'platform_kubernetes_attributes[api_url]'
            },
            {
                'name': 'platform_kubernetes_attributes[token]'
            },
            {
                'name': 'enabled'
            },
            {
                'name': 'environment_scope'
            },
            {
                'name': 'namespace_per_environment'
            },
            {
                'name': 'domain'
            },
            {
                'name': 'management_project_id'
            },
            {
                'name': 'managed'
            },
            {
                'name': 'platform_kubernetes_attributes[ca_cert]'
            },
            {
                'name': 'platform_kubernetes_attributes[namespace]'
            },
            {
                'name': 'platform_kubernetes_attributes[authorization_type]'
            },
        ]
    },
    '/api/v4/admin/clusters/{cluster_id}-DELETE': {
        'parameters': [
            {
                'name': 'cluster_id'
            },
        ]
    },
    '/api/v4/admin/clusters/{cluster_id}-GET': {
        'parameters': [
            {
                'name': 'cluster_id'
            },
        ]
    },
    '/api/v4/admin/clusters-GET': {
        'parameters': [
        ]
    },
    '/api/v4/admin/clusters/{cluster_id}-PUT': {
        'parameters': [
            {
                'name': 'cluster_id'
            },
            {
                'name': 'name'
            },
            {
                'name': 'enabled'
            },
            {
                'name': 'environment_scope'
            },
            {
                'name': 'namespace_per_environment'
            },
            {
                'name': 'domain'
            },
            {
                'name': 'management_project_id'
            },
            {
                'name': 'managed'
            },
            {
                'name': 'platform_kubernetes_attributes[api_url]'
            },
            {
                'name': 'platform_kubernetes_attributes[token]'
            },
            {
                'name': 'platform_kubernetes_attributes[ca_cert]'
            },
            {
                'name': 'platform_kubernetes_attributes[namespace]'
            },
        ]
    },
    '/api/v4/projects/{id}/jobs/{job_id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'job_id'
            },
        ]
    },
    '/api/v4/projects/{id}/jobs-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'scope'
            },
        ]
    },
    '/api/v4/projects/{id}/jobs/{job_id}/play-POST': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'job_id'
            },
            {
                'name': 'job_variables_attributes'
            },
        ]
    },
    '/api/v4/metadata-GET': {
        'parameters': [
        ]
    },
    '/api/v4/version-GET': {
        'parameters': [
        ]
    },
    '/api/v4/admin/migrations/{timestamp}/mark-POST': {
        'parameters': [
            {
                'name': 'timestamp'
            },
            {
                'name': 'database'
            },
        ]
    },
    '/api/v4/application/plan_limits-GET': {
        'parameters': [
            {
                'name': 'plan_name'
            },
        ]
    },
    '/api/v4/application/plan_limits-PUT': {
        'parameters': [
            {
                'name': 'plan_name'
            },
            {
                'name': 'ci_pipeline_size'
            },
            {
                'name': 'ci_active_jobs'
            },
            {
                'name': 'ci_project_subscriptions'
            },
            {
                'name': 'ci_pipeline_schedules'
            },
            {
                'name': 'ci_needs_size_limit'
            },
            {
                'name': 'ci_registered_group_runners'
            },
            {
                'name': 'ci_registered_project_runners'
            },
            {
                'name': 'conan_max_file_size'
            },
            {
                'name': 'enforcement_limit'
            },
            {
                'name': 'generic_packages_max_file_size'
            },
            {
                'name': 'helm_max_file_size'
            },
            {
                'name': 'maven_max_file_size'
            },
            {
                'name': 'notification_limit'
            },
            {
                'name': 'npm_max_file_size'
            },
            {
                'name': 'nuget_max_file_size'
            },
            {
                'name': 'pypi_max_file_size'
            },
            {
                'name': 'terraform_module_max_file_size'
            },
            {
                'name': 'storage_size_limit'
            },
            {
                'name': 'pipeline_hierarchy_size'
            },
        ]
    },
};