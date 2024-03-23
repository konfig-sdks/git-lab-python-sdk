<div align="left">

[![Visit Gitlab](./header.png)](https://gitlab.com)

# Gitlab<a id="gitlab"></a>

An OpenAPI definition for the GitLab REST API.
Few API resources or endpoints are currently included.
The intent is to expand this to match the entire Markdown documentation of the API:
<https://docs.gitlab.com/ee/api/>. Contributions are welcome.

When viewing this on gitlab.com, you can test API calls directly from the browser
against the `gitlab.com` instance, if you are logged in.
The feature uses the current [GitLab session cookie](https://docs.gitlab.com/ee/api/index.html#session-cookie),
so each request is made using your account.

Instructions for using this tool can be found in [Interactive API Documentation](https://docs.gitlab.com/ee/api/openapi/openapi_interactive.html)



</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`gitlab.access_requests.approve_for_user`](#gitlabaccess_requestsapprove_for_user)
  * [`gitlab.access_requests.approve_for_user_0`](#gitlabaccess_requestsapprove_for_user_0)
  * [`gitlab.access_requests.deny_access_to_user`](#gitlabaccess_requestsdeny_access_to_user)
  * [`gitlab.access_requests.deny_access_to_user_0`](#gitlabaccess_requestsdeny_access_to_user_0)
  * [`gitlab.access_requests.get_list`](#gitlabaccess_requestsget_list)
  * [`gitlab.access_requests.get_list_0`](#gitlabaccess_requestsget_list_0)
  * [`gitlab.access_requests.request_access_to_group`](#gitlabaccess_requestsrequest_access_to_group)
  * [`gitlab.access_requests.request_access_to_project`](#gitlabaccess_requestsrequest_access_to_project)
  * [`gitlab.admin.get_dictionary_details`](#gitlabadminget_dictionary_details)
  * [`gitlab.alert_management.authorize_metric_image_upload`](#gitlabalert_managementauthorize_metric_image_upload)
  * [`gitlab.alert_management.get_metric_images_for_alert`](#gitlabalert_managementget_metric_images_for_alert)
  * [`gitlab.alert_management.remove_metric_image`](#gitlabalert_managementremove_metric_image)
  * [`gitlab.alert_management.update_metric_image`](#gitlabalert_managementupdate_metric_image)
  * [`gitlab.alert_management.upload_metric_image`](#gitlabalert_managementupload_metric_image)
  * [`gitlab.application.get_current_appearance`](#gitlabapplicationget_current_appearance)
  * [`gitlab.application.modify_appearance`](#gitlabapplicationmodify_appearance)
  * [`gitlab.applications.create_new_application`](#gitlabapplicationscreate_new_application)
  * [`gitlab.applications.delete_specific_application`](#gitlabapplicationsdelete_specific_application)
  * [`gitlab.applications.list_all_registered`](#gitlabapplicationslist_all_registered)
  * [`gitlab.avatar.get_url_for_user`](#gitlabavatarget_url_for_user)
  * [`gitlab.badges.add_badge_to_group`](#gitlabbadgesadd_badge_to_group)
  * [`gitlab.badges.add_project_badge`](#gitlabbadgesadd_project_badge)
  * [`gitlab.badges.get_group_badge`](#gitlabbadgesget_group_badge)
  * [`gitlab.badges.get_list`](#gitlabbadgesget_list)
  * [`gitlab.badges.get_project_badge`](#gitlabbadgesget_project_badge)
  * [`gitlab.badges.list_viewable_by_authenticated_user`](#gitlabbadgeslist_viewable_by_authenticated_user)
  * [`gitlab.badges.preview_badge_from_group`](#gitlabbadgespreview_badge_from_group)
  * [`gitlab.badges.remove_from_group`](#gitlabbadgesremove_from_group)
  * [`gitlab.badges.remove_from_project`](#gitlabbadgesremove_from_project)
  * [`gitlab.badges.render_preview_from_project`](#gitlabbadgesrender_preview_from_project)
  * [`gitlab.badges.update_group_badge`](#gitlabbadgesupdate_group_badge)
  * [`gitlab.badges.update_project_badge`](#gitlabbadgesupdate_project_badge)
  * [`gitlab.batched_background_migrations.get_migration`](#gitlabbatched_background_migrationsget_migration)
  * [`gitlab.batched_background_migrations.list`](#gitlabbatched_background_migrationslist)
  * [`gitlab.batched_background_migrations.pause_migration`](#gitlabbatched_background_migrationspause_migration)
  * [`gitlab.batched_background_migrations.resume_migration`](#gitlabbatched_background_migrationsresume_migration)
  * [`gitlab.branches.check_if_exists`](#gitlabbranchescheck_if_exists)
  * [`gitlab.branches.create_branch`](#gitlabbranchescreate_branch)
  * [`gitlab.branches.delete_branch`](#gitlabbranchesdelete_branch)
  * [`gitlab.branches.delete_merged`](#gitlabbranchesdelete_merged)
  * [`gitlab.branches.get_all`](#gitlabbranchesget_all)
  * [`gitlab.branches.get_single_branch`](#gitlabbranchesget_single_branch)
  * [`gitlab.branches.protect_branch`](#gitlabbranchesprotect_branch)
  * [`gitlab.branches.unprotect_branch`](#gitlabbranchesunprotect_branch)
  * [`gitlab.broadcast_messages.create_message`](#gitlabbroadcast_messagescreate_message)
  * [`gitlab.broadcast_messages.delete_message`](#gitlabbroadcast_messagesdelete_message)
  * [`gitlab.broadcast_messages.get_specific_message`](#gitlabbroadcast_messagesget_specific_message)
  * [`gitlab.broadcast_messages.list_all`](#gitlabbroadcast_messageslist_all)
  * [`gitlab.broadcast_messages.update_message`](#gitlabbroadcast_messagesupdate_message)
  * [`gitlab.bulk_imports.get_entity_details`](#gitlabbulk_importsget_entity_details)
  * [`gitlab.bulk_imports.get_migration_details`](#gitlabbulk_importsget_migration_details)
  * [`gitlab.bulk_imports.list_entities`](#gitlabbulk_importslist_entities)
  * [`gitlab.bulk_imports.list_entities_0`](#gitlabbulk_importslist_entities_0)
  * [`gitlab.bulk_imports.list_migrations`](#gitlabbulk_importslist_migrations)
  * [`gitlab.bulk_imports.start_new_migration`](#gitlabbulk_importsstart_new_migration)
  * [`gitlab.ci_variables.create_new_instance_variable`](#gitlabci_variablescreate_new_instance_variable)
  * [`gitlab.ci_variables.delete_instance_variable`](#gitlabci_variablesdelete_instance_variable)
  * [`gitlab.ci_variables.get_specific_instance_variable`](#gitlabci_variablesget_specific_instance_variable)
  * [`gitlab.ci_variables.list_instance_variables`](#gitlabci_variableslist_instance_variables)
  * [`gitlab.ci_variables.update_instance_variable`](#gitlabci_variablesupdate_instance_variable)
  * [`gitlab.clusters.add_existing_kubernetes_instance_cluster`](#gitlabclustersadd_existing_kubernetes_instance_cluster)
  * [`gitlab.clusters.delete_instance_cluster`](#gitlabclustersdelete_instance_cluster)
  * [`gitlab.clusters.get_single_instance_cluster`](#gitlabclustersget_single_instance_cluster)
  * [`gitlab.clusters.list_instance_clusters`](#gitlabclusterslist_instance_clusters)
  * [`gitlab.clusters.update_instance_cluster`](#gitlabclustersupdate_instance_cluster)
  * [`gitlab.jobs.get_single_by_id`](#gitlabjobsget_single_by_id)
  * [`gitlab.jobs.list_for_project`](#gitlabjobslist_for_project)
  * [`gitlab.jobs.run_manual_job`](#gitlabjobsrun_manual_job)
  * [`gitlab.metadata.get_information`](#gitlabmetadataget_information)
  * [`gitlab.metadata.get_version_information`](#gitlabmetadataget_version_information)
  * [`gitlab.migrations.mark_as_executed`](#gitlabmigrationsmark_as_executed)
  * [`gitlab.plan_limits.get_current_limits`](#gitlabplan_limitsget_current_limits)
  * [`gitlab.plan_limits.modify_limits`](#gitlabplan_limitsmodify_limits)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=GitLab&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from git_lab_python_sdk import GitLab, ApiException

gitlab = GitLab(
    api_key_auth="YOUR_API_KEY",
)

try:
    # Approves an access request for the given user.
    approve_for_user_response = gitlab.access_requests.approve_for_user(
        body=None,
        id="id_example",
        user_id=1,
        access_level=30,
    )
    print(approve_for_user_response)
except ApiException as e:
    print("Exception when calling AccessRequestsApi.approve_for_user: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from git_lab_python_sdk import GitLab, ApiException

gitlab = GitLab(
    api_key_auth="YOUR_API_KEY",
)


async def main():
    try:
        # Approves an access request for the given user.
        approve_for_user_response = await gitlab.access_requests.aapprove_for_user(
            body=None,
            id="id_example",
            user_id=1,
            access_level=30,
        )
        print(approve_for_user_response)
    except ApiException as e:
        print("Exception when calling AccessRequestsApi.approve_for_user: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from git_lab_python_sdk import GitLab, ApiException

gitlab = GitLab(
    api_key_auth="YOUR_API_KEY",
)

try:
    # Approves an access request for the given user.
    approve_for_user_response = gitlab.access_requests.raw.approve_for_user(
        body=None,
        id="id_example",
        user_id=1,
        access_level=30,
    )
    pprint(approve_for_user_response.body)
    pprint(approve_for_user_response.body["id"])
    pprint(approve_for_user_response.body["username"])
    pprint(approve_for_user_response.body["name"])
    pprint(approve_for_user_response.body["state"])
    pprint(approve_for_user_response.body["avatar_url"])
    pprint(approve_for_user_response.body["avatar_path"])
    pprint(approve_for_user_response.body["custom_attributes"])
    pprint(approve_for_user_response.body["web_url"])
    pprint(approve_for_user_response.body["email"])
    pprint(approve_for_user_response.body["requested_at"])
    pprint(approve_for_user_response.headers)
    pprint(approve_for_user_response.status)
    pprint(approve_for_user_response.round_trip_time)
except ApiException as e:
    print("Exception when calling AccessRequestsApi.approve_for_user: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `gitlab.access_requests.approve_for_user`<a id="gitlabaccess_requestsapprove_for_user"></a>

This feature was introduced in GitLab 8.11.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
approve_for_user_response = gitlab.access_requests.approve_for_user(
    body=None,
    id="id_example",
    user_id=1,
    access_level=30,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID or URL-encoded path of the group owned by the authenticated user

##### user_id: `int`<a id="user_id-int"></a>

The user ID of the access requester

##### access_level: `int`<a id="access_level-int"></a>

A valid access level (defaults: `30`, the Developer role)

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AccessrequestsApproveForUserRequest`](./git_lab_python_sdk/type/accessrequests_approve_for_user_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`APIEntitiesAccessRequester`](./git_lab_python_sdk/pydantic/api_entities_access_requester.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/groups/{id}/access_requests/{user_id}/approve` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.access_requests.approve_for_user_0`<a id="gitlabaccess_requestsapprove_for_user_0"></a>

This feature was introduced in GitLab 8.11.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
approve_for_user_0_response = gitlab.access_requests.approve_for_user_0(
    body=None,
    id="id_example",
    user_id=1,
    access_level=30,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID or URL-encoded path of the project owned by the authenticated user

##### user_id: `int`<a id="user_id-int"></a>

The user ID of the access requester

##### access_level: `int`<a id="access_level-int"></a>

A valid access level (defaults: `30`, the Developer role)

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AccessrequestsApproveForUserRequest1`](./git_lab_python_sdk/type/accessrequests_approve_for_user_request1.py)
#### 🔄 Return<a id="🔄-return"></a>

[`APIEntitiesAccessRequester`](./git_lab_python_sdk/pydantic/api_entities_access_requester.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/projects/{id}/access_requests/{user_id}/approve` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.access_requests.deny_access_to_user`<a id="gitlabaccess_requestsdeny_access_to_user"></a>

This feature was introduced in GitLab 8.11.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
gitlab.access_requests.deny_access_to_user(
    id="id_example",
    user_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID or URL-encoded path of the group owned by the authenticated user

##### user_id: `int`<a id="user_id-int"></a>

The user ID of the access requester

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/groups/{id}/access_requests/{user_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.access_requests.deny_access_to_user_0`<a id="gitlabaccess_requestsdeny_access_to_user_0"></a>

This feature was introduced in GitLab 8.11.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
gitlab.access_requests.deny_access_to_user_0(
    id="id_example",
    user_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID or URL-encoded path of the project owned by the authenticated user

##### user_id: `int`<a id="user_id-int"></a>

The user ID of the access requester

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/projects/{id}/access_requests/{user_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.access_requests.get_list`<a id="gitlabaccess_requestsget_list"></a>

This feature was introduced in GitLab 8.11.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_response = gitlab.access_requests.get_list(
    id="id_example",
    page=1,
    per_page=20,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID or URL-encoded path of the group owned by the authenticated user

##### page: `int`<a id="page-int"></a>

Current page number

##### per_page: `int`<a id="per_page-int"></a>

Number of items per page

#### 🔄 Return<a id="🔄-return"></a>

[`APIEntitiesAccessRequester`](./git_lab_python_sdk/pydantic/api_entities_access_requester.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/groups/{id}/access_requests` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.access_requests.get_list_0`<a id="gitlabaccess_requestsget_list_0"></a>

This feature was introduced in GitLab 8.11.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_0_response = gitlab.access_requests.get_list_0(
    id="id_example",
    page=1,
    per_page=20,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID or URL-encoded path of the project owned by the authenticated user

##### page: `int`<a id="page-int"></a>

Current page number

##### per_page: `int`<a id="per_page-int"></a>

Number of items per page

#### 🔄 Return<a id="🔄-return"></a>

[`APIEntitiesAccessRequester`](./git_lab_python_sdk/pydantic/api_entities_access_requester.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/projects/{id}/access_requests` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.access_requests.request_access_to_group`<a id="gitlabaccess_requestsrequest_access_to_group"></a>

This feature was introduced in GitLab 8.11.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
request_access_to_group_response = gitlab.access_requests.request_access_to_group(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID or URL-encoded path of the group owned by the authenticated user

#### 🔄 Return<a id="🔄-return"></a>

[`APIEntitiesAccessRequester`](./git_lab_python_sdk/pydantic/api_entities_access_requester.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/groups/{id}/access_requests` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.access_requests.request_access_to_project`<a id="gitlabaccess_requestsrequest_access_to_project"></a>

This feature was introduced in GitLab 8.11.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
request_access_to_project_response = gitlab.access_requests.request_access_to_project(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID or URL-encoded path of the project owned by the authenticated user

#### 🔄 Return<a id="🔄-return"></a>

[`APIEntitiesAccessRequester`](./git_lab_python_sdk/pydantic/api_entities_access_requester.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/projects/{id}/access_requests` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.admin.get_dictionary_details`<a id="gitlabadminget_dictionary_details"></a>

Retrieve dictionary details

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_dictionary_details_response = gitlab.admin.get_dictionary_details(
    database_name="main",
    table_name="table_name_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### database_name: `str`<a id="database_name-str"></a>

The database name

##### table_name: `str`<a id="table_name-str"></a>

The table name

#### 🔄 Return<a id="🔄-return"></a>

[`APIEntitiesDictionaryTable`](./git_lab_python_sdk/pydantic/api_entities_dictionary_table.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/admin/databases/{database_name}/dictionary/tables/{table_name}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.alert_management.authorize_metric_image_upload`<a id="gitlabalert_managementauthorize_metric_image_upload"></a>

Workhorse authorize metric image file upload

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
gitlab.alert_management.authorize_metric_image_upload(
    id="id_example",
    alert_iid=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID or URL-encoded path of the project

##### alert_iid: `int`<a id="alert_iid-int"></a>

The IID of the Alert

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/projects/{id}/alert_management_alerts/{alert_iid}/metric_images/authorize` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.alert_management.get_metric_images_for_alert`<a id="gitlabalert_managementget_metric_images_for_alert"></a>

Metric Images for alert

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_metric_images_for_alert_response = (
    gitlab.alert_management.get_metric_images_for_alert(
        id="id_example",
        alert_iid=1,
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID or URL-encoded path of the project

##### alert_iid: `int`<a id="alert_iid-int"></a>

The IID of the Alert

#### 🔄 Return<a id="🔄-return"></a>

[`AlertmanagementGetMetricImagesForAlertResponse`](./git_lab_python_sdk/pydantic/alertmanagement_get_metric_images_for_alert_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/projects/{id}/alert_management_alerts/{alert_iid}/metric_images` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.alert_management.remove_metric_image`<a id="gitlabalert_managementremove_metric_image"></a>

Remove a metric image for an alert

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_metric_image_response = gitlab.alert_management.remove_metric_image(
    id="id_example",
    alert_iid=1,
    metric_image_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID or URL-encoded path of the project

##### alert_iid: `int`<a id="alert_iid-int"></a>

The IID of the Alert

##### metric_image_id: `int`<a id="metric_image_id-int"></a>

The ID of metric image

#### 🔄 Return<a id="🔄-return"></a>

[`APIEntitiesMetricImage`](./git_lab_python_sdk/pydantic/api_entities_metric_image.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/projects/{id}/alert_management_alerts/{alert_iid}/metric_images/{metric_image_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.alert_management.update_metric_image`<a id="gitlabalert_managementupdate_metric_image"></a>

Update a metric image for an alert

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_metric_image_response = gitlab.alert_management.update_metric_image(
    body=None,
    id="id_example",
    alert_iid=1,
    metric_image_id=1,
    url="string_example",
    url_text="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID or URL-encoded path of the project

##### alert_iid: `int`<a id="alert_iid-int"></a>

The IID of the Alert

##### metric_image_id: `int`<a id="metric_image_id-int"></a>

The ID of metric image

##### url: `str`<a id="url-str"></a>

The url to view more metric info

##### url_text: `str`<a id="url_text-str"></a>

A description of the image or URL

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AlertmanagementUpdateMetricImageRequest`](./git_lab_python_sdk/type/alertmanagement_update_metric_image_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`APIEntitiesMetricImage`](./git_lab_python_sdk/pydantic/api_entities_metric_image.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/projects/{id}/alert_management_alerts/{alert_iid}/metric_images/{metric_image_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.alert_management.upload_metric_image`<a id="gitlabalert_managementupload_metric_image"></a>

Upload a metric image for an alert

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
upload_metric_image_response = gitlab.alert_management.upload_metric_image(
    body=None,
    id="id_example",
    alert_iid=1,
    file=open("/path/to/file", "rb"),
    url="string_example",
    url_text="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID or URL-encoded path of the project

##### alert_iid: `int`<a id="alert_iid-int"></a>

The IID of the Alert

##### file: `IO`<a id="file-io"></a>

The image file to be uploaded

##### url: `str`<a id="url-str"></a>

The url to view more metric info

##### url_text: `str`<a id="url_text-str"></a>

A description of the image or URL

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AlertmanagementUploadMetricImageRequest`](./git_lab_python_sdk/type/alertmanagement_upload_metric_image_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`APIEntitiesMetricImage`](./git_lab_python_sdk/pydantic/api_entities_metric_image.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/projects/{id}/alert_management_alerts/{alert_iid}/metric_images` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.application.get_current_appearance`<a id="gitlabapplicationget_current_appearance"></a>

Get the current appearance

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_current_appearance_response = gitlab.application.get_current_appearance()
```

#### 🔄 Return<a id="🔄-return"></a>

[`APIEntitiesAppearance`](./git_lab_python_sdk/pydantic/api_entities_appearance.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/application/appearance` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.application.modify_appearance`<a id="gitlabapplicationmodify_appearance"></a>

Modify appearance

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
modify_appearance_response = gitlab.application.modify_appearance(
    body=None,
    title="string_example",
    description="string_example",
    pwa_name="string_example",
    pwa_short_name="string_example",
    pwa_description="string_example",
    logo=open("/path/to/file", "rb"),
    pwa_icon=open("/path/to/file", "rb"),
    header_logo=open("/path/to/file", "rb"),
    favicon=open("/path/to/file", "rb"),
    new_project_guidelines="string_example",
    profile_image_guidelines="string_example",
    header_message="string_example",
    footer_message="string_example",
    message_background_color="string_example",
    message_font_color="string_example",
    email_header_and_footer_enabled=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### title: `str`<a id="title-str"></a>

Instance title on the sign in / sign up page

##### description: `str`<a id="description-str"></a>

Markdown text shown on the sign in / sign up page

##### pwa_name: `str`<a id="pwa_name-str"></a>

Name of the Progressive Web App

##### pwa_short_name: `str`<a id="pwa_short_name-str"></a>

Optional, short name for Progressive Web App

##### pwa_description: `str`<a id="pwa_description-str"></a>

An explanation of what the Progressive Web App does

##### logo: `IO`<a id="logo-io"></a>

Instance image used on the sign in / sign up page

##### pwa_icon: `IO`<a id="pwa_icon-io"></a>

Icon used for Progressive Web App

##### header_logo: `IO`<a id="header_logo-io"></a>

Instance image used for the main navigation bar

##### favicon: `IO`<a id="favicon-io"></a>

Instance favicon in .ico/.png format

##### new_project_guidelines: `str`<a id="new_project_guidelines-str"></a>

Markdown text shown on the new project page

##### profile_image_guidelines: `str`<a id="profile_image_guidelines-str"></a>

Markdown text shown on the profile page below Public Avatar

##### header_message: `str`<a id="header_message-str"></a>

Message within the system header bar

##### footer_message: `str`<a id="footer_message-str"></a>

Message within the system footer bar

##### message_background_color: `str`<a id="message_background_color-str"></a>

Background color for the system header / footer bar

##### message_font_color: `str`<a id="message_font_color-str"></a>

Font color for the system header / footer bar

##### email_header_and_footer_enabled: `bool`<a id="email_header_and_footer_enabled-bool"></a>

Add header and footer to all outgoing emails if enabled

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ApplicationModifyAppearanceRequest`](./git_lab_python_sdk/type/application_modify_appearance_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`APIEntitiesAppearance`](./git_lab_python_sdk/pydantic/api_entities_appearance.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/application/appearance` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.applications.create_new_application`<a id="gitlabapplicationscreate_new_application"></a>

This feature was introduced in GitLab 10.5

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_application_response = gitlab.applications.create_new_application(
    body=None,
    name="string_example",
    redirect_uri="string_example",
    scopes="string_example",
    confidential=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Name of the application.

##### redirect_uri: `str`<a id="redirect_uri-str"></a>

Redirect URI of the application.

##### scopes: `str`<a id="scopes-str"></a>

Scopes of the application. You can specify multiple scopes by separating\\\\                                  each scope using a space

##### confidential: `bool`<a id="confidential-bool"></a>

The application is used where the client secret can be kept confidential. Native mobile apps \\\\                         and Single Page Apps are considered non-confidential. Defaults to true if not supplied

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ApplicationsCreateNewApplicationRequest`](./git_lab_python_sdk/type/applications_create_new_application_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`APIEntitiesApplicationWithSecret`](./git_lab_python_sdk/pydantic/api_entities_application_with_secret.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/applications` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.applications.delete_specific_application`<a id="gitlabapplicationsdelete_specific_application"></a>

Delete a specific application

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
gitlab.applications.delete_specific_application(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

The ID of the application (not the application_id)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/applications/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.applications.list_all_registered`<a id="gitlabapplicationslist_all_registered"></a>

List all registered applications

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_registered_response = gitlab.applications.list_all_registered()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ApplicationsListAllRegisteredResponse`](./git_lab_python_sdk/pydantic/applications_list_all_registered_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/applications` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.avatar.get_url_for_user`<a id="gitlabavatarget_url_for_user"></a>

Return avatar url for a user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_url_for_user_response = gitlab.avatar.get_url_for_user(
    email="email_example",
    size=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### email: `str`<a id="email-str"></a>

Public email address of the user

##### size: `int`<a id="size-int"></a>

Single pixel dimension for Gravatar images

#### 🔄 Return<a id="🔄-return"></a>

[`APIEntitiesAvatar`](./git_lab_python_sdk/pydantic/api_entities_avatar.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/avatar` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.badges.add_badge_to_group`<a id="gitlabbadgesadd_badge_to_group"></a>

This feature was introduced in GitLab 10.6.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_badge_to_group_response = gitlab.badges.add_badge_to_group(
    body=None,
    link_url="string_example",
    image_url="string_example",
    id="id_example",
    name="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### link_url: `str`<a id="link_url-str"></a>

URL of the badge link

##### image_url: `str`<a id="image_url-str"></a>

URL of the badge image

##### id: `str`<a id="id-str"></a>

The ID or URL-encoded path of the group owned by the authenticated user.

##### name: `str`<a id="name-str"></a>

Name for the badge

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BadgesAddBadgeToGroupRequest`](./git_lab_python_sdk/type/badges_add_badge_to_group_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`APIEntitiesBadge`](./git_lab_python_sdk/pydantic/api_entities_badge.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/groups/{id}/badges` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.badges.add_project_badge`<a id="gitlabbadgesadd_project_badge"></a>

This feature was introduced in GitLab 10.6.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_project_badge_response = gitlab.badges.add_project_badge(
    body=None,
    link_url="string_example",
    image_url="string_example",
    id="id_example",
    name="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### link_url: `str`<a id="link_url-str"></a>

URL of the badge link

##### image_url: `str`<a id="image_url-str"></a>

URL of the badge image

##### id: `str`<a id="id-str"></a>

The ID or URL-encoded path of the project owned by the authenticated user.

##### name: `str`<a id="name-str"></a>

Name for the badge

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BadgesAddProjectBadgeRequest`](./git_lab_python_sdk/type/badges_add_project_badge_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`APIEntitiesBadge`](./git_lab_python_sdk/pydantic/api_entities_badge.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/projects/{id}/badges` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.badges.get_group_badge`<a id="gitlabbadgesget_group_badge"></a>

This feature was introduced in GitLab 10.6.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_group_badge_response = gitlab.badges.get_group_badge(
    id="id_example",
    badge_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID or URL-encoded path of the group owned by the authenticated user.

##### badge_id: `int`<a id="badge_id-int"></a>

The badge ID

#### 🔄 Return<a id="🔄-return"></a>

[`APIEntitiesBadge`](./git_lab_python_sdk/pydantic/api_entities_badge.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/groups/{id}/badges/{badge_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.badges.get_list`<a id="gitlabbadgesget_list"></a>

This feature was introduced in GitLab 10.6.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_response = gitlab.badges.get_list(
    id="id_example",
    page=1,
    per_page=20,
    name="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID or URL-encoded path of the group owned by the authenticated user.

##### page: `int`<a id="page-int"></a>

Current page number

##### per_page: `int`<a id="per_page-int"></a>

Number of items per page

##### name: `str`<a id="name-str"></a>

Name for the badge

#### 🔄 Return<a id="🔄-return"></a>

[`BadgesGetListResponse`](./git_lab_python_sdk/pydantic/badges_get_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/groups/{id}/badges` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.badges.get_project_badge`<a id="gitlabbadgesget_project_badge"></a>

This feature was introduced in GitLab 10.6.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_project_badge_response = gitlab.badges.get_project_badge(
    id="id_example",
    badge_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID or URL-encoded path of the project owned by the authenticated user.

##### badge_id: `int`<a id="badge_id-int"></a>

The badge ID

#### 🔄 Return<a id="🔄-return"></a>

[`APIEntitiesBadge`](./git_lab_python_sdk/pydantic/api_entities_badge.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/projects/{id}/badges/{badge_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.badges.list_viewable_by_authenticated_user`<a id="gitlabbadgeslist_viewable_by_authenticated_user"></a>

This feature was introduced in GitLab 10.6.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_viewable_by_authenticated_user_response = (
    gitlab.badges.list_viewable_by_authenticated_user(
        id="id_example",
        page=1,
        per_page=20,
        name="string_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID or URL-encoded path of the project owned by the authenticated user.

##### page: `int`<a id="page-int"></a>

Current page number

##### per_page: `int`<a id="per_page-int"></a>

Number of items per page

##### name: `str`<a id="name-str"></a>

Name for the badge

#### 🔄 Return<a id="🔄-return"></a>

[`BadgesListViewableByAuthenticatedUserResponse`](./git_lab_python_sdk/pydantic/badges_list_viewable_by_authenticated_user_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/projects/{id}/badges` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.badges.preview_badge_from_group`<a id="gitlabbadgespreview_badge_from_group"></a>

This feature was introduced in GitLab 10.6.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
preview_badge_from_group_response = gitlab.badges.preview_badge_from_group(
    id="id_example",
    link_url="link_url_example",
    image_url="image_url_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID or URL-encoded path of the group owned by the authenticated user.

##### link_url: `str`<a id="link_url-str"></a>

URL of the badge link

##### image_url: `str`<a id="image_url-str"></a>

URL of the badge image

#### 🔄 Return<a id="🔄-return"></a>

[`APIEntitiesBasicBadgeDetails`](./git_lab_python_sdk/pydantic/api_entities_basic_badge_details.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/groups/{id}/badges/render` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.badges.remove_from_group`<a id="gitlabbadgesremove_from_group"></a>

This feature was introduced in GitLab 10.6.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
gitlab.badges.remove_from_group(
    id="id_example",
    badge_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID or URL-encoded path of the group owned by the authenticated user.

##### badge_id: `int`<a id="badge_id-int"></a>

The badge ID

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/groups/{id}/badges/{badge_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.badges.remove_from_project`<a id="gitlabbadgesremove_from_project"></a>

This feature was introduced in GitLab 10.6.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
gitlab.badges.remove_from_project(
    id="id_example",
    badge_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID or URL-encoded path of the project owned by the authenticated user.

##### badge_id: `int`<a id="badge_id-int"></a>

The badge ID

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/projects/{id}/badges/{badge_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.badges.render_preview_from_project`<a id="gitlabbadgesrender_preview_from_project"></a>

This feature was introduced in GitLab 10.6.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
render_preview_from_project_response = gitlab.badges.render_preview_from_project(
    id="id_example",
    link_url="link_url_example",
    image_url="image_url_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID or URL-encoded path of the project owned by the authenticated user.

##### link_url: `str`<a id="link_url-str"></a>

URL of the badge link

##### image_url: `str`<a id="image_url-str"></a>

URL of the badge image

#### 🔄 Return<a id="🔄-return"></a>

[`APIEntitiesBasicBadgeDetails`](./git_lab_python_sdk/pydantic/api_entities_basic_badge_details.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/projects/{id}/badges/render` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.badges.update_group_badge`<a id="gitlabbadgesupdate_group_badge"></a>

This feature was introduced in GitLab 10.6.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_group_badge_response = gitlab.badges.update_group_badge(
    body=None,
    id="id_example",
    badge_id=1,
    link_url="string_example",
    image_url="string_example",
    name="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID or URL-encoded path of the group owned by the authenticated user.

##### badge_id: `int`<a id="badge_id-int"></a>

##### link_url: `str`<a id="link_url-str"></a>

URL of the badge link

##### image_url: `str`<a id="image_url-str"></a>

URL of the badge image

##### name: `str`<a id="name-str"></a>

Name for the badge

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BadgesUpdateGroupBadgeRequest`](./git_lab_python_sdk/type/badges_update_group_badge_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`APIEntitiesBadge`](./git_lab_python_sdk/pydantic/api_entities_badge.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/groups/{id}/badges/{badge_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.badges.update_project_badge`<a id="gitlabbadgesupdate_project_badge"></a>

This feature was introduced in GitLab 10.6.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_project_badge_response = gitlab.badges.update_project_badge(
    body=None,
    id="id_example",
    badge_id=1,
    link_url="string_example",
    image_url="string_example",
    name="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID or URL-encoded path of the project owned by the authenticated user.

##### badge_id: `int`<a id="badge_id-int"></a>

##### link_url: `str`<a id="link_url-str"></a>

URL of the badge link

##### image_url: `str`<a id="image_url-str"></a>

URL of the badge image

##### name: `str`<a id="name-str"></a>

Name for the badge

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BadgesUpdateProjectBadgeRequest`](./git_lab_python_sdk/type/badges_update_project_badge_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`APIEntitiesBadge`](./git_lab_python_sdk/pydantic/api_entities_badge.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/projects/{id}/badges/{badge_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.batched_background_migrations.get_migration`<a id="gitlabbatched_background_migrationsget_migration"></a>

Retrieve a batched background migration

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_migration_response = gitlab.batched_background_migrations.get_migration(
    id=1,
    database="main",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

The batched background migration id

##### database: `str`<a id="database-str"></a>

The name of the database

#### 🔄 Return<a id="🔄-return"></a>

[`APIEntitiesBatchedBackgroundMigration`](./git_lab_python_sdk/pydantic/api_entities_batched_background_migration.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/admin/batched_background_migrations/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.batched_background_migrations.list`<a id="gitlabbatched_background_migrationslist"></a>

Get the list of batched background migrations

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = gitlab.batched_background_migrations.list(
    database="main",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### database: `str`<a id="database-str"></a>

The name of the database, the default `main`

#### 🔄 Return<a id="🔄-return"></a>

[`BatchedbackgroundmigrationsListResponse`](./git_lab_python_sdk/pydantic/batchedbackgroundmigrations_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/admin/batched_background_migrations` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.batched_background_migrations.pause_migration`<a id="gitlabbatched_background_migrationspause_migration"></a>

Pause a batched background migration

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
pause_migration_response = gitlab.batched_background_migrations.pause_migration(
    body=None,
    id=1,
    database="main",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

The batched background migration id

##### database: `str`<a id="database-str"></a>

The name of the database

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BatchedbackgroundmigrationsPauseMigrationRequest`](./git_lab_python_sdk/type/batchedbackgroundmigrations_pause_migration_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`APIEntitiesBatchedBackgroundMigration`](./git_lab_python_sdk/pydantic/api_entities_batched_background_migration.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/admin/batched_background_migrations/{id}/pause` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.batched_background_migrations.resume_migration`<a id="gitlabbatched_background_migrationsresume_migration"></a>

Resume a batched background migration

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
resume_migration_response = gitlab.batched_background_migrations.resume_migration(
    body=None,
    id=1,
    database="main",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

The batched background migration id

##### database: `str`<a id="database-str"></a>

The name of the database

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BatchedbackgroundmigrationsResumeMigrationRequest`](./git_lab_python_sdk/type/batchedbackgroundmigrations_resume_migration_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`APIEntitiesBatchedBackgroundMigration`](./git_lab_python_sdk/pydantic/api_entities_batched_background_migration.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/admin/batched_background_migrations/{id}/resume` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.branches.check_if_exists`<a id="gitlabbranchescheck_if_exists"></a>

Check if a branch exists

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
gitlab.branches.check_if_exists(
    id="id_example",
    branch="branch_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID or URL-encoded path of the project

##### branch: `str`<a id="branch-str"></a>

The name of the branch

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/projects/{id}/repository/branches/{branch}` `head`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.branches.create_branch`<a id="gitlabbranchescreate_branch"></a>

Create branch

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_branch_response = gitlab.branches.create_branch(
    id="id_example",
    branch="branch_example",
    ref="ref_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID or URL-encoded path of the project

##### branch: `str`<a id="branch-str"></a>

The name of the branch

##### ref: `str`<a id="ref-str"></a>

Create branch from commit sha or existing branch

#### 🔄 Return<a id="🔄-return"></a>

[`APIEntitiesBranch`](./git_lab_python_sdk/pydantic/api_entities_branch.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/projects/{id}/repository/branches` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.branches.delete_branch`<a id="gitlabbranchesdelete_branch"></a>

Delete a branch

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
gitlab.branches.delete_branch(
    id="id_example",
    branch="branch_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID or URL-encoded path of the project

##### branch: `str`<a id="branch-str"></a>

The name of the branch

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/projects/{id}/repository/branches/{branch}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.branches.delete_merged`<a id="gitlabbranchesdelete_merged"></a>

Delete all merged branches

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
gitlab.branches.delete_merged(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID or URL-encoded path of the project

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/projects/{id}/repository/merged_branches` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.branches.get_all`<a id="gitlabbranchesget_all"></a>

Get a project repository branches

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = gitlab.branches.get_all(
    id="id_example",
    page=1,
    per_page=20,
    search="string_example",
    regex="string_example",
    sort="name_asc",
    page_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID or URL-encoded path of the project

##### page: `int`<a id="page-int"></a>

Current page number

##### per_page: `int`<a id="per_page-int"></a>

Number of items per page

##### search: `str`<a id="search-str"></a>

Return list of branches matching the search criteria

##### regex: `str`<a id="regex-str"></a>

Return list of branches matching the regex

##### sort: `str`<a id="sort-str"></a>

Return list of branches sorted by the given field

##### page_token: `str`<a id="page_token-str"></a>

Name of branch to start the pagination from

#### 🔄 Return<a id="🔄-return"></a>

[`BranchesGetAllResponse`](./git_lab_python_sdk/pydantic/branches_get_all_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/projects/{id}/repository/branches` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.branches.get_single_branch`<a id="gitlabbranchesget_single_branch"></a>

Get a single repository branch

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_single_branch_response = gitlab.branches.get_single_branch(
    id="id_example",
    branch=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID or URL-encoded path of the project

##### branch: `int`<a id="branch-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`APIEntitiesBranch`](./git_lab_python_sdk/pydantic/api_entities_branch.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/projects/{id}/repository/branches/{branch}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.branches.protect_branch`<a id="gitlabbranchesprotect_branch"></a>

Protect a single branch

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
protect_branch_response = gitlab.branches.protect_branch(
    body=None,
    id="id_example",
    branch="branch_example",
    developers_can_push=True,
    developers_can_merge=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID or URL-encoded path of the project

##### branch: `str`<a id="branch-str"></a>

The name of the branch

##### developers_can_push: `bool`<a id="developers_can_push-bool"></a>

Flag if developers can push to that branch

##### developers_can_merge: `bool`<a id="developers_can_merge-bool"></a>

Flag if developers can merge to that branch

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BranchesProtectBranchRequest`](./git_lab_python_sdk/type/branches_protect_branch_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`APIEntitiesBranch`](./git_lab_python_sdk/pydantic/api_entities_branch.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/projects/{id}/repository/branches/{branch}/protect` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.branches.unprotect_branch`<a id="gitlabbranchesunprotect_branch"></a>

Unprotect a single branch

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
unprotect_branch_response = gitlab.branches.unprotect_branch(
    id="id_example",
    branch="branch_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID or URL-encoded path of the project

##### branch: `str`<a id="branch-str"></a>

The name of the branch

#### 🔄 Return<a id="🔄-return"></a>

[`APIEntitiesBranch`](./git_lab_python_sdk/pydantic/api_entities_branch.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/projects/{id}/repository/branches/{branch}/unprotect` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.broadcast_messages.create_message`<a id="gitlabbroadcast_messagescreate_message"></a>

This feature was introduced in GitLab 8.12.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_message_response = gitlab.broadcast_messages.create_message(
    body=None,
    message="string_example",
    starts_at="1970-01-01T00:00:00.00Z",
    ends_at="1970-01-01T00:00:00.00Z",
    color="string_example",
    font="string_example",
    target_access_levels=[1],
    target_path="string_example",
    broadcast_type="banner",
    dismissable=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### message: `str`<a id="message-str"></a>

Message to display

##### starts_at: `datetime`<a id="starts_at-datetime"></a>

Starting time

##### ends_at: `datetime`<a id="ends_at-datetime"></a>

Ending time

##### color: `str`<a id="color-str"></a>

Background color

##### font: `str`<a id="font-str"></a>

Foreground color

##### target_access_levels: List[`int`]<a id="target_access_levels-listint"></a>

Target user roles

##### target_path: `str`<a id="target_path-str"></a>

Target path

##### broadcast_type: `str`<a id="broadcast_type-str"></a>

Broadcast type. Defaults to banner

##### dismissable: `bool`<a id="dismissable-bool"></a>

Is dismissable

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BroadcastmessagesCreateMessageRequest`](./git_lab_python_sdk/type/broadcastmessages_create_message_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`APIEntitiesBroadcastMessage`](./git_lab_python_sdk/pydantic/api_entities_broadcast_message.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/broadcast_messages` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.broadcast_messages.delete_message`<a id="gitlabbroadcast_messagesdelete_message"></a>

This feature was introduced in GitLab 8.12.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_message_response = gitlab.broadcast_messages.delete_message(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

Broadcast message ID

#### 🔄 Return<a id="🔄-return"></a>

[`APIEntitiesBroadcastMessage`](./git_lab_python_sdk/pydantic/api_entities_broadcast_message.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/broadcast_messages/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.broadcast_messages.get_specific_message`<a id="gitlabbroadcast_messagesget_specific_message"></a>

This feature was introduced in GitLab 8.12.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_specific_message_response = gitlab.broadcast_messages.get_specific_message(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

Broadcast message ID

#### 🔄 Return<a id="🔄-return"></a>

[`APIEntitiesBroadcastMessage`](./git_lab_python_sdk/pydantic/api_entities_broadcast_message.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/broadcast_messages/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.broadcast_messages.list_all`<a id="gitlabbroadcast_messageslist_all"></a>

This feature was introduced in GitLab 8.12.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_response = gitlab.broadcast_messages.list_all(
    page=1,
    per_page=20,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page: `int`<a id="page-int"></a>

Current page number

##### per_page: `int`<a id="per_page-int"></a>

Number of items per page

#### 🔄 Return<a id="🔄-return"></a>

[`APIEntitiesBroadcastMessage`](./git_lab_python_sdk/pydantic/api_entities_broadcast_message.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/broadcast_messages` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.broadcast_messages.update_message`<a id="gitlabbroadcast_messagesupdate_message"></a>

This feature was introduced in GitLab 8.12.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_message_response = gitlab.broadcast_messages.update_message(
    body=None,
    id=1,
    message="string_example",
    starts_at="1970-01-01T00:00:00.00Z",
    ends_at="1970-01-01T00:00:00.00Z",
    color="string_example",
    font="string_example",
    target_access_levels=[1],
    target_path="string_example",
    broadcast_type="banner",
    dismissable=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

Broadcast message ID

##### message: `str`<a id="message-str"></a>

Message to display

##### starts_at: `datetime`<a id="starts_at-datetime"></a>

Starting time

##### ends_at: `datetime`<a id="ends_at-datetime"></a>

Ending time

##### color: `str`<a id="color-str"></a>

Background color

##### font: `str`<a id="font-str"></a>

Foreground color

##### target_access_levels: List[`int`]<a id="target_access_levels-listint"></a>

Target user roles

##### target_path: `str`<a id="target_path-str"></a>

Target path

##### broadcast_type: `str`<a id="broadcast_type-str"></a>

Broadcast Type

##### dismissable: `bool`<a id="dismissable-bool"></a>

Is dismissable

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BroadcastmessagesUpdateMessageRequest`](./git_lab_python_sdk/type/broadcastmessages_update_message_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`APIEntitiesBroadcastMessage`](./git_lab_python_sdk/pydantic/api_entities_broadcast_message.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/broadcast_messages/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.bulk_imports.get_entity_details`<a id="gitlabbulk_importsget_entity_details"></a>

This feature was introduced in GitLab 14.1.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_entity_details_response = gitlab.bulk_imports.get_entity_details(
    import_id=1,
    entity_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### import_id: `int`<a id="import_id-int"></a>

The ID of user's GitLab Migration

##### entity_id: `int`<a id="entity_id-int"></a>

The ID of GitLab Migration entity

#### 🔄 Return<a id="🔄-return"></a>

[`APIEntitiesBulkImports`](./git_lab_python_sdk/pydantic/api_entities_bulk_imports.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/bulk_imports/{import_id}/entities/{entity_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.bulk_imports.get_migration_details`<a id="gitlabbulk_importsget_migration_details"></a>

This feature was introduced in GitLab 14.1.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_migration_details_response = gitlab.bulk_imports.get_migration_details(
    import_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### import_id: `int`<a id="import_id-int"></a>

The ID of user's GitLab Migration

#### 🔄 Return<a id="🔄-return"></a>

[`APIEntitiesBulkImport`](./git_lab_python_sdk/pydantic/api_entities_bulk_import.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/bulk_imports/{import_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.bulk_imports.list_entities`<a id="gitlabbulk_importslist_entities"></a>

This feature was introduced in GitLab 14.1.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_entities_response = gitlab.bulk_imports.list_entities(
    import_id=1,
    status="created",
    page=1,
    per_page=20,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### import_id: `int`<a id="import_id-int"></a>

The ID of user's GitLab Migration

##### status: `str`<a id="status-str"></a>

Return import entities with specified status

##### page: `int`<a id="page-int"></a>

Current page number

##### per_page: `int`<a id="per_page-int"></a>

Number of items per page

#### 🔄 Return<a id="🔄-return"></a>

[`BulkimportsListEntitiesResponse`](./git_lab_python_sdk/pydantic/bulkimports_list_entities_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/bulk_imports/{import_id}/entities` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.bulk_imports.list_entities_0`<a id="gitlabbulk_importslist_entities_0"></a>

This feature was introduced in GitLab 14.1.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_entities_0_response = gitlab.bulk_imports.list_entities_0(
    page=1,
    per_page=20,
    sort="desc",
    status="created",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page: `int`<a id="page-int"></a>

Current page number

##### per_page: `int`<a id="per_page-int"></a>

Number of items per page

##### sort: `str`<a id="sort-str"></a>

Return GitLab Migrations sorted in created by `asc` or `desc` order.

##### status: `str`<a id="status-str"></a>

Return all GitLab Migrations' entities with specified status

#### 🔄 Return<a id="🔄-return"></a>

[`BulkimportsListEntities200Response`](./git_lab_python_sdk/pydantic/bulkimports_list_entities200_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/bulk_imports/entities` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.bulk_imports.list_migrations`<a id="gitlabbulk_importslist_migrations"></a>

This feature was introduced in GitLab 14.1.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_migrations_response = gitlab.bulk_imports.list_migrations(
    page=1,
    per_page=20,
    sort="desc",
    status="created",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page: `int`<a id="page-int"></a>

Current page number

##### per_page: `int`<a id="per_page-int"></a>

Number of items per page

##### sort: `str`<a id="sort-str"></a>

Return GitLab Migrations sorted in created by `asc` or `desc` order.

##### status: `str`<a id="status-str"></a>

Return GitLab Migrations with specified status

#### 🔄 Return<a id="🔄-return"></a>

[`BulkimportsListMigrationsResponse`](./git_lab_python_sdk/pydantic/bulkimports_list_migrations_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/bulk_imports` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.bulk_imports.start_new_migration`<a id="gitlabbulk_importsstart_new_migration"></a>

This feature was introduced in GitLab 14.2.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
start_new_migration_response = gitlab.bulk_imports.start_new_migration(
    body=None,
    configuration_url="string_example",
    configuration_access_token="string_example",
    entities_source_type=["string_example"],
    entities_source_full_path=["string_example"],
    entities_destination_namespace=["string_example"],
    entities_destination_slug=["string_example"],
    entities_destination_name=["string_example"],
    entities_migrate_projects=[True],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### configuration_url: `str`<a id="configuration_url-str"></a>

Source GitLab instance URL

##### configuration_access_token: `str`<a id="configuration_access_token-str"></a>

Access token to the source GitLab instance

##### entities_source_type: List[`str`]<a id="entities_source_type-liststr"></a>

Source entity type

##### entities_source_full_path: List[`str`]<a id="entities_source_full_path-liststr"></a>

Relative path of the source entity to import

##### entities_destination_namespace: List[`str`]<a id="entities_destination_namespace-liststr"></a>

Destination namespace for the entity

##### entities_destination_slug: List[`str`]<a id="entities_destination_slug-liststr"></a>

Destination slug for the entity

##### entities_destination_name: List[`str`]<a id="entities_destination_name-liststr"></a>

Deprecated: Use :destination_slug instead. Destination slug for the entity

##### entities_migrate_projects: List[`bool`]<a id="entities_migrate_projects-listbool"></a>

Indicates group migration should include nested projects

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BulkimportsStartNewMigrationRequest`](./git_lab_python_sdk/type/bulkimports_start_new_migration_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`APIEntitiesBulkImport`](./git_lab_python_sdk/pydantic/api_entities_bulk_import.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/bulk_imports` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.ci_variables.create_new_instance_variable`<a id="gitlabci_variablescreate_new_instance_variable"></a>

Create a new instance-level variable

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_instance_variable_response = (
    gitlab.ci_variables.create_new_instance_variable(
        body=None,
        key="string_example",
        value="string_example",
        protected=True,
        masked=True,
        raw=True,
        variable_type="env_var",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### key: `str`<a id="key-str"></a>

The key of the variable. Max 255 characters

##### value: `str`<a id="value-str"></a>

The value of a variable

##### protected: `bool`<a id="protected-bool"></a>

Whether the variable is protected

##### masked: `bool`<a id="masked-bool"></a>

Whether the variable is masked

##### raw: `bool`<a id="raw-bool"></a>

Whether the variable will be expanded

##### variable_type: `str`<a id="variable_type-str"></a>

The type of a variable. Available types are: env_var (default) and file

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CivariablesCreateNewInstanceVariableRequest`](./git_lab_python_sdk/type/civariables_create_new_instance_variable_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`APIEntitiesCiVariable`](./git_lab_python_sdk/pydantic/api_entities_ci_variable.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/admin/ci/variables` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.ci_variables.delete_instance_variable`<a id="gitlabci_variablesdelete_instance_variable"></a>

Delete an existing instance-level variable

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_instance_variable_response = gitlab.ci_variables.delete_instance_variable(
    key="key_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### key: `str`<a id="key-str"></a>

The key of a variable

#### 🔄 Return<a id="🔄-return"></a>

[`APIEntitiesCiVariable`](./git_lab_python_sdk/pydantic/api_entities_ci_variable.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/admin/ci/variables/{key}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.ci_variables.get_specific_instance_variable`<a id="gitlabci_variablesget_specific_instance_variable"></a>

Get the details of a specific instance-level variable

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_specific_instance_variable_response = (
    gitlab.ci_variables.get_specific_instance_variable(
        key="key_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### key: `str`<a id="key-str"></a>

The key of a variable

#### 🔄 Return<a id="🔄-return"></a>

[`APIEntitiesCiVariable`](./git_lab_python_sdk/pydantic/api_entities_ci_variable.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/admin/ci/variables/{key}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.ci_variables.list_instance_variables`<a id="gitlabci_variableslist_instance_variables"></a>

List all instance-level variables

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_instance_variables_response = gitlab.ci_variables.list_instance_variables(
    page=1,
    per_page=20,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page: `int`<a id="page-int"></a>

Current page number

##### per_page: `int`<a id="per_page-int"></a>

Number of items per page

#### 🔄 Return<a id="🔄-return"></a>

[`APIEntitiesCiVariable`](./git_lab_python_sdk/pydantic/api_entities_ci_variable.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/admin/ci/variables` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.ci_variables.update_instance_variable`<a id="gitlabci_variablesupdate_instance_variable"></a>

Update an instance-level variable

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_instance_variable_response = gitlab.ci_variables.update_instance_variable(
    body=None,
    key="key_example",
    value="string_example",
    protected=True,
    masked=True,
    raw=True,
    variable_type="env_var",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### key: `str`<a id="key-str"></a>

The key of a variable

##### value: `str`<a id="value-str"></a>

The value of a variable

##### protected: `bool`<a id="protected-bool"></a>

Whether the variable is protected

##### masked: `bool`<a id="masked-bool"></a>

Whether the variable is masked

##### raw: `bool`<a id="raw-bool"></a>

Whether the variable will be expanded

##### variable_type: `str`<a id="variable_type-str"></a>

The type of a variable. Available types are: env_var (default) and file

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CivariablesUpdateInstanceVariableRequest`](./git_lab_python_sdk/type/civariables_update_instance_variable_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`APIEntitiesCiVariable`](./git_lab_python_sdk/pydantic/api_entities_ci_variable.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/admin/ci/variables/{key}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.clusters.add_existing_kubernetes_instance_cluster`<a id="gitlabclustersadd_existing_kubernetes_instance_cluster"></a>

This feature was introduced in GitLab 13.2. Adds an existing Kubernetes instance cluster.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_existing_kubernetes_instance_cluster_response = (
    gitlab.clusters.add_existing_kubernetes_instance_cluster(
        body=None,
        name="string_example",
        platform_kubernetes_attributes_api_url="string_example",
        platform_kubernetes_attributes_token="string_example",
        enabled=True,
        environment_scope="*",
        namespace_per_environment=True,
        domain="string_example",
        management_project_id=1,
        managed=True,
        platform_kubernetes_attributes_ca_cert="string_example",
        platform_kubernetes_attributes_namespace="string_example",
        platform_kubernetes_attributes_authorization_type="rbac",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Cluster name

##### platform_kubernetes_attributes_api_url: `str`<a id="platform_kubernetes_attributes_api_url-str"></a>

URL to access the Kubernetes API

##### platform_kubernetes_attributes_token: `str`<a id="platform_kubernetes_attributes_token-str"></a>

Token to authenticate against Kubernetes

##### enabled: `bool`<a id="enabled-bool"></a>

Determines if cluster is active or not, defaults to true

##### environment_scope: `str`<a id="environment_scope-str"></a>

The associated environment to the cluster

##### namespace_per_environment: `bool`<a id="namespace_per_environment-bool"></a>

Deploy each environment to a separate Kubernetes namespace

##### domain: `str`<a id="domain-str"></a>

Cluster base domain

##### management_project_id: `int`<a id="management_project_id-int"></a>

The ID of the management project

##### managed: `bool`<a id="managed-bool"></a>

Determines if GitLab will manage namespaces and service accounts for this cluster, defaults to true

##### platform_kubernetes_attributes_ca_cert: `str`<a id="platform_kubernetes_attributes_ca_cert-str"></a>

TLS certificate (needed if API is using a self-signed TLS certificate)

##### platform_kubernetes_attributes_namespace: `str`<a id="platform_kubernetes_attributes_namespace-str"></a>

Unique namespace related to Project

##### platform_kubernetes_attributes_authorization_type: `str`<a id="platform_kubernetes_attributes_authorization_type-str"></a>

Cluster authorization type, defaults to RBAC

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ClustersAddExistingKubernetesInstanceClusterRequest`](./git_lab_python_sdk/type/clusters_add_existing_kubernetes_instance_cluster_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`APIEntitiesCluster`](./git_lab_python_sdk/pydantic/api_entities_cluster.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/admin/clusters/add` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.clusters.delete_instance_cluster`<a id="gitlabclustersdelete_instance_cluster"></a>

This feature was introduced in GitLab 13.2. Deletes an existing instance cluster. Does not remove existing resources within the connected Kubernetes cluster.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_instance_cluster_response = gitlab.clusters.delete_instance_cluster(
    cluster_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### cluster_id: `int`<a id="cluster_id-int"></a>

The cluster ID

#### 🔄 Return<a id="🔄-return"></a>

[`APIEntitiesCluster`](./git_lab_python_sdk/pydantic/api_entities_cluster.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/admin/clusters/{cluster_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.clusters.get_single_instance_cluster`<a id="gitlabclustersget_single_instance_cluster"></a>

This feature was introduced in GitLab 13.2. Returns a single instance cluster.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_single_instance_cluster_response = gitlab.clusters.get_single_instance_cluster(
    cluster_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### cluster_id: `int`<a id="cluster_id-int"></a>

The cluster ID

#### 🔄 Return<a id="🔄-return"></a>

[`APIEntitiesCluster`](./git_lab_python_sdk/pydantic/api_entities_cluster.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/admin/clusters/{cluster_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.clusters.list_instance_clusters`<a id="gitlabclusterslist_instance_clusters"></a>

This feature was introduced in GitLab 13.2. Returns a list of instance clusters.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_instance_clusters_response = gitlab.clusters.list_instance_clusters()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ClustersListInstanceClustersResponse`](./git_lab_python_sdk/pydantic/clusters_list_instance_clusters_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/admin/clusters` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.clusters.update_instance_cluster`<a id="gitlabclustersupdate_instance_cluster"></a>

This feature was introduced in GitLab 13.2. Updates an existing instance cluster.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_instance_cluster_response = gitlab.clusters.update_instance_cluster(
    body=None,
    cluster_id=1,
    name="string_example",
    enabled=True,
    environment_scope="string_example",
    namespace_per_environment=True,
    domain="string_example",
    management_project_id=1,
    managed=True,
    platform_kubernetes_attributes_api_url="string_example",
    platform_kubernetes_attributes_token="string_example",
    platform_kubernetes_attributes_ca_cert="string_example",
    platform_kubernetes_attributes_namespace="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### cluster_id: `int`<a id="cluster_id-int"></a>

The cluster ID

##### name: `str`<a id="name-str"></a>

Cluster name

##### enabled: `bool`<a id="enabled-bool"></a>

Enable or disable Gitlab's connection to your Kubernetes cluster

##### environment_scope: `str`<a id="environment_scope-str"></a>

The associated environment to the cluster

##### namespace_per_environment: `bool`<a id="namespace_per_environment-bool"></a>

Deploy each environment to a separate Kubernetes namespace

##### domain: `str`<a id="domain-str"></a>

Cluster base domain

##### management_project_id: `int`<a id="management_project_id-int"></a>

The ID of the management project

##### managed: `bool`<a id="managed-bool"></a>

Determines if GitLab will manage namespaces and service accounts for this cluster

##### platform_kubernetes_attributes_api_url: `str`<a id="platform_kubernetes_attributes_api_url-str"></a>

URL to access the Kubernetes API

##### platform_kubernetes_attributes_token: `str`<a id="platform_kubernetes_attributes_token-str"></a>

Token to authenticate against Kubernetes

##### platform_kubernetes_attributes_ca_cert: `str`<a id="platform_kubernetes_attributes_ca_cert-str"></a>

TLS certificate (needed if API is using a self-signed TLS certificate)

##### platform_kubernetes_attributes_namespace: `str`<a id="platform_kubernetes_attributes_namespace-str"></a>

Unique namespace related to Project

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ClustersUpdateInstanceClusterRequest`](./git_lab_python_sdk/type/clusters_update_instance_cluster_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`APIEntitiesCluster`](./git_lab_python_sdk/pydantic/api_entities_cluster.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/admin/clusters/{cluster_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.jobs.get_single_by_id`<a id="gitlabjobsget_single_by_id"></a>

Get a single job by ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_single_by_id_response = gitlab.jobs.get_single_by_id(
    id=1,
    job_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

The ID of the project

##### job_id: `int`<a id="job_id-int"></a>

The ID of the job

#### 🔄 Return<a id="🔄-return"></a>

[`APIEntitiesJob`](./git_lab_python_sdk/pydantic/api_entities_job.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/projects/{id}/jobs/{job_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.jobs.list_for_project`<a id="gitlabjobslist_for_project"></a>

List jobs for a project

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_for_project_response = gitlab.jobs.list_for_project(
    id=1,
    scope=["string_example"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

The ID of the project

##### scope: List[`str`]<a id="scope-liststr"></a>

Return all jobs with the specified statuses

#### 🔄 Return<a id="🔄-return"></a>

[`JobsListForProjectResponse`](./git_lab_python_sdk/pydantic/jobs_list_for_project_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/projects/{id}/jobs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.jobs.run_manual_job`<a id="gitlabjobsrun_manual_job"></a>

Run a manual job

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
gitlab.jobs.run_manual_job(
    id=1,
    job_id=1,
    job_variables_attributes=["string_example"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

The ID of the project

##### job_id: `int`<a id="job_id-int"></a>

The ID of the manual job to run

##### job_variables_attributes: List[`str`]<a id="job_variables_attributes-liststr"></a>

An array containing the custom variables available to the job

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/projects/{id}/jobs/{job_id}/play` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.metadata.get_information`<a id="gitlabmetadataget_information"></a>

This feature was introduced in GitLab 15.2.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_information_response = gitlab.metadata.get_information()
```

#### 🔄 Return<a id="🔄-return"></a>

[`APIEntitiesMetadata`](./git_lab_python_sdk/pydantic/api_entities_metadata.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/metadata` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.metadata.get_version_information`<a id="gitlabmetadataget_version_information"></a>

This feature was introduced in GitLab 8.13 and deprecated in 15.5. We recommend you instead use the Metadata API.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_version_information_response = gitlab.metadata.get_version_information()
```

#### 🔄 Return<a id="🔄-return"></a>

[`APIEntitiesMetadata`](./git_lab_python_sdk/pydantic/api_entities_metadata.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/version` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.migrations.mark_as_executed`<a id="gitlabmigrationsmark_as_executed"></a>

Mark the migration as successfully executed

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
gitlab.migrations.mark_as_executed(
    body=None,
    timestamp=1,
    database="main",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### timestamp: `int`<a id="timestamp-int"></a>

The migration version timestamp

##### database: `str`<a id="database-str"></a>

The name of the database

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MigrationsMarkAsExecutedRequest`](./git_lab_python_sdk/type/migrations_mark_as_executed_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/admin/migrations/{timestamp}/mark` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.plan_limits.get_current_limits`<a id="gitlabplan_limitsget_current_limits"></a>

List the current limits of a plan on the GitLab instance.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_current_limits_response = gitlab.plan_limits.get_current_limits(
    plan_name="default",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### plan_name: `str`<a id="plan_name-str"></a>

Name of the plan to get the limits from. Default: default.

#### 🔄 Return<a id="🔄-return"></a>

[`APIEntitiesPlanLimit`](./git_lab_python_sdk/pydantic/api_entities_plan_limit.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/application/plan_limits` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `gitlab.plan_limits.modify_limits`<a id="gitlabplan_limitsmodify_limits"></a>

Modify the limits of a plan on the GitLab instance.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
modify_limits_response = gitlab.plan_limits.modify_limits(
    body=None,
    plan_name="default",
    ci_pipeline_size=1,
    ci_active_jobs=1,
    ci_project_subscriptions=1,
    ci_pipeline_schedules=1,
    ci_needs_size_limit=1,
    ci_registered_group_runners=1,
    ci_registered_project_runners=1,
    conan_max_file_size=1,
    enforcement_limit=1,
    generic_packages_max_file_size=1,
    helm_max_file_size=1,
    maven_max_file_size=1,
    notification_limit=1,
    npm_max_file_size=1,
    nuget_max_file_size=1,
    pypi_max_file_size=1,
    terraform_module_max_file_size=1,
    storage_size_limit=1,
    pipeline_hierarchy_size=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### plan_name: `str`<a id="plan_name-str"></a>

Name of the plan to update

##### ci_pipeline_size: `int`<a id="ci_pipeline_size-int"></a>

Maximum number of jobs in a single pipeline

##### ci_active_jobs: `int`<a id="ci_active_jobs-int"></a>

Total number of jobs in currently active pipelines

##### ci_project_subscriptions: `int`<a id="ci_project_subscriptions-int"></a>

Maximum number of pipeline subscriptions to and from a project

##### ci_pipeline_schedules: `int`<a id="ci_pipeline_schedules-int"></a>

Maximum number of pipeline schedules

##### ci_needs_size_limit: `int`<a id="ci_needs_size_limit-int"></a>

Maximum number of DAG dependencies that a job can have

##### ci_registered_group_runners: `int`<a id="ci_registered_group_runners-int"></a>

Maximum number of runners registered per group

##### ci_registered_project_runners: `int`<a id="ci_registered_project_runners-int"></a>

Maximum number of runners registered per project

##### conan_max_file_size: `int`<a id="conan_max_file_size-int"></a>

Maximum Conan package file size in bytes

##### enforcement_limit: `int`<a id="enforcement_limit-int"></a>

Maximum storage size for the root namespace enforcement in MiB

##### generic_packages_max_file_size: `int`<a id="generic_packages_max_file_size-int"></a>

Maximum generic package file size in bytes

##### helm_max_file_size: `int`<a id="helm_max_file_size-int"></a>

Maximum Helm chart file size in bytes

##### maven_max_file_size: `int`<a id="maven_max_file_size-int"></a>

Maximum Maven package file size in bytes

##### notification_limit: `int`<a id="notification_limit-int"></a>

Maximum storage size for the root namespace notifications in MiB

##### npm_max_file_size: `int`<a id="npm_max_file_size-int"></a>

Maximum NPM package file size in bytes

##### nuget_max_file_size: `int`<a id="nuget_max_file_size-int"></a>

Maximum NuGet package file size in bytes

##### pypi_max_file_size: `int`<a id="pypi_max_file_size-int"></a>

Maximum PyPI package file size in bytes

##### terraform_module_max_file_size: `int`<a id="terraform_module_max_file_size-int"></a>

Maximum Terraform Module package file size in bytes

##### storage_size_limit: `int`<a id="storage_size_limit-int"></a>

Maximum storage size for the root namespace in MiB

##### pipeline_hierarchy_size: `int`<a id="pipeline_hierarchy_size-int"></a>

Maximum number of downstream pipelines in a pipeline's hierarchy tree

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PlanlimitsModifyLimitsRequest`](./git_lab_python_sdk/type/planlimits_modify_limits_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`APIEntitiesPlanLimit`](./git_lab_python_sdk/pydantic/api_entities_plan_limit.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v4/application/plan_limits` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
