# coding: utf-8

"""
    GitLab API

    An OpenAPI definition for the GitLab REST API. Few API resources or endpoints are currently included. The intent is to expand this to match the entire Markdown documentation of the API: <https://docs.gitlab.com/ee/api/>. Contributions are welcome.  When viewing this on gitlab.com, you can test API calls directly from the browser against the `gitlab.com` instance, if you are logged in. The feature uses the current [GitLab session cookie](https://docs.gitlab.com/ee/api/index.html#session-cookie), so each request is made using your account.  Instructions for using this tool can be found in [Interactive API Documentation](https://docs.gitlab.com/ee/api/openapi/openapi_interactive.html) 

    The version of the OpenAPI document: v4
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING


class RequiredPlanlimitsModifyLimitsRequest(TypedDict):
    # Name of the plan to update
    plan_name: str

class OptionalPlanlimitsModifyLimitsRequest(TypedDict, total=False):
    # Maximum number of jobs in a single pipeline
    ci_pipeline_size: int

    # Total number of jobs in currently active pipelines
    ci_active_jobs: int

    # Maximum number of pipeline subscriptions to and from a project
    ci_project_subscriptions: int

    # Maximum number of pipeline schedules
    ci_pipeline_schedules: int

    # Maximum number of DAG dependencies that a job can have
    ci_needs_size_limit: int

    # Maximum number of runners registered per group
    ci_registered_group_runners: int

    # Maximum number of runners registered per project
    ci_registered_project_runners: int

    # Maximum Conan package file size in bytes
    conan_max_file_size: int

    # Maximum storage size for the root namespace enforcement in MiB
    enforcement_limit: int

    # Maximum generic package file size in bytes
    generic_packages_max_file_size: int

    # Maximum Helm chart file size in bytes
    helm_max_file_size: int

    # Maximum Maven package file size in bytes
    maven_max_file_size: int

    # Maximum storage size for the root namespace notifications in MiB
    notification_limit: int

    # Maximum NPM package file size in bytes
    npm_max_file_size: int

    # Maximum NuGet package file size in bytes
    nuget_max_file_size: int

    # Maximum PyPI package file size in bytes
    pypi_max_file_size: int

    # Maximum Terraform Module package file size in bytes
    terraform_module_max_file_size: int

    # Maximum storage size for the root namespace in MiB
    storage_size_limit: int

    # Maximum number of downstream pipelines in a pipeline's hierarchy tree
    pipeline_hierarchy_size: int

class PlanlimitsModifyLimitsRequest(RequiredPlanlimitsModifyLimitsRequest, OptionalPlanlimitsModifyLimitsRequest):
    pass
