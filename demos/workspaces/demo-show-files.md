## User Story: List Files

As an openEO Platform user, Mia wants to list all files in her user workspace.


There is a variety of ways to list your workspace files.

- Through the openEO API 
- Using the WorkspaceAdapter
- With a 3rd-Party object-storage file explorer

#### 1) openEO API

Disclaimer: We enable this feature soley for internal EODC Workspaces as we want to limit read-operations, especially those exposed through a public API (even despite authentication), on external workspaces.

There is only single step involved, assuming you already have a workspace with some data in it, you can simply make a request to the /workspace/{WORKSPACE_NAME}/files endpoint and get a list of files returned.


```python
import openeo

# Set This variable to your workspace's name.

WORKSPACE_NAME = ""

# Connect to the openEO backend and authenticate with EGI Check-In

connection = openeo.connect("https://openeo.example.eu/openeo/1.2.0")
connection = connection.authenticate_oidc(provider_id="egi")
```


```python
import requests

response = requests.get(
    url="https://openeo.example.eu/openeo/1.2.0/workspaces/WORKSPACE_NAME/files",
    headers={
        "authorization": "Bearer BEARER_TOKEN"
    },
)

print(response.content.decode())
```

## 2) Third Party Applications

This method is less relevant to this tutorial, but you can always use a third-party object-storage browser to view your files or interact with your workspace in general.

Some tools:

- S3 Browser (for S3 systems like Ceph, you can use this for internal EODC Workspace)
- Microsoft Azure Storage Explorer (for Azure Blob Storage)
- ...
