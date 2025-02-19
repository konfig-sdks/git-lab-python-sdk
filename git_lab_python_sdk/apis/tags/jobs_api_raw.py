# coding: utf-8

"""
    GitLab API

    An OpenAPI definition for the GitLab REST API. Few API resources or endpoints are currently included. The intent is to expand this to match the entire Markdown documentation of the API: <https://docs.gitlab.com/ee/api/>. Contributions are welcome.  When viewing this on gitlab.com, you can test API calls directly from the browser against the `gitlab.com` instance, if you are logged in. The feature uses the current [GitLab session cookie](https://docs.gitlab.com/ee/api/index.html#session-cookie), so each request is made using your account.  Instructions for using this tool can be found in [Interactive API Documentation](https://docs.gitlab.com/ee/api/openapi/openapi_interactive.html) 

    The version of the OpenAPI document: v4
    Generated by: https://konfigthis.com
"""

from git_lab_python_sdk.paths.api_v4_projects_id_jobs_job_id.get import GetSingleByIdRaw
from git_lab_python_sdk.paths.api_v4_projects_id_jobs.get import ListForProjectRaw
from git_lab_python_sdk.paths.api_v4_projects_id_jobs_job_id_play.post import RunManualJobRaw


class JobsApiRaw(
    GetSingleByIdRaw,
    ListForProjectRaw,
    RunManualJobRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
