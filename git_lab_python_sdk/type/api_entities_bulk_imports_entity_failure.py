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


class RequiredAPIEntitiesBulkImportsEntityFailure(TypedDict):
    pass

class OptionalAPIEntitiesBulkImportsEntityFailure(TypedDict, total=False):
    relation: str

    step: str

    exception_message: str

    exception_class: str

    correlation_id_value: str

    created_at: datetime

    pipeline_class: str

    pipeline_step: str

class APIEntitiesBulkImportsEntityFailure(RequiredAPIEntitiesBulkImportsEntityFailure, OptionalAPIEntitiesBulkImportsEntityFailure):
    pass
