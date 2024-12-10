## User Story: Workspace Sharing


John creates a user collection by running an openEO process graph. He wants to share this user collection with Nina. Nina wants to visualise John's user collection in a Jupyter Notebook and runs a process graph that uses this as an input collection.

Sharing your workspace is extremely simple, all you have to do is send a post request to the /workspace/{WORKSPACE_NAME}/share/{SHAREE_USER_ID} endpoint with the corresponding workspace name and the user-id of the person you want to share your workspace with (Note: this only works for local EODC workspaces).

This call will allow read access for whoever you share the workspace with, which also means the other person can send load_collection requests using this workspace, but they cannot save results to it.


```python
import openeo

# Connect to the openEO backend and authenticate with EGI Check-In

connection = openeo.connect("https://openeo.eodc.eu/openeo/1.1.0")
connection = connection.authenticate_oidc(provider_id="egi")
```


```python
import requests

WORKSPACE_NAME = ""
SHAREE_USER_ID = ""

response = requests.post(
    url=f"https://openeo.eodc.eu/openeo/1.1.0/workspace/{WORKSPACE_NAME}/share/{SHAREE_USER_ID}",
    headers={
        "authorization": f"Bearer {connection.auth.bearer}"
    },
)

response.content
```

If we get a successful response, we have now shared the workspace and the other person will now have read access and can load your user collections for their own process graphs.

If you want to stop sharing your workspace, you can simply send a delete request to the same endpoint.


```python
import requests

WORKSPACE_NAME = ""
SHAREE_USER_ID = ""

response = requests.delete(
    url=f"https://openeo.eodc.eu/openeo/1.1.0/workspace/{WORKSPACE_NAME}/share/{SHAREE_USER_ID}",
    headers={
        "authorization": f"Bearer {connection.auth.bearer}"
    },
)

response.content
```

A successful response here means the other user will no longer have any access to your workspace.
