# coding: utf-8

"""
    GitLab API

    An OpenAPI definition for the GitLab REST API. Few API resources or endpoints are currently included. The intent is to expand this to match the entire Markdown documentation of the API: <https://docs.gitlab.com/ee/api/>. Contributions are welcome.  When viewing this on gitlab.com, you can test API calls directly from the browser against the `gitlab.com` instance, if you are logged in. The feature uses the current [GitLab session cookie](https://docs.gitlab.com/ee/api/index.html#session-cookie), so each request is made using your account.  Instructions for using this tool can be found in [Interactive API Documentation](https://docs.gitlab.com/ee/api/openapi/openapi_interactive.html) 

    The version of the OpenAPI document: v4
    Generated by: https://konfigthis.com
"""

from git_lab_python_sdk.paths.api_v4_admin_databases_database_name_dictionary_tables_table_name.get import GetDictionaryDetails
from git_lab_python_sdk.apis.tags.admin_api_raw import AdminApiRaw


class AdminApi(
    GetDictionaryDetails,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: AdminApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = AdminApiRaw(api_client)
