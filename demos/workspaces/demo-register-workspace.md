## User Story: Registering a Workspace

John is a PhD student with user collection data stored in a container on Azure blob storage service. 

Instead of creating a internal EODC workspace, you can register your own workspace and use it in much the same way.

All you need to do is post to the "/workspaces" endpoint with a  and submit your credentials.


```python
import openeo

# Connect to the openEO backend and authenticate with EGI Check-In

connection = openeo.connect("https://openeo.eodc.eu/openeo/1.1.0")
connection = connection.authenticate_oidc(provider_id="egi")
```

You can fill out the following variables so they fit with the workspace that you are trying to register.

IMPORTANT NOTE: Make sure the workspace name corresponds to your underlying bucket/container


```python
# If your workspace is a s3 compatible object storage fill out these variables

WORKSPACE_NAME = ""

S3_ENDPOINT = ""
S3_ACCESS_KEY = ""
S3_SECRET_KEY = ""

ext_ws = {
    "intent": "register",
    "storage_type": "ceph",
    "credentials": {
        "url": S3_ENDPOINT,
        "access_key": S3_ACCESS_KEY,
        "secret_key": S3_SECRET_KEY, 
    },

}
```


```python
# If your workspace is azure blob storage, fill out the connection string

WORKSPACE_NAME = ""

AZURE_CONNECTION_STRING = ""

ext_ws = {
    "intent": "register",
    "storage_type": "azure",
    "credentials": {
        "connection_string": AZURE_CONNECTION_STRING, 
    },
}
```

After filling out these request bodies, you can send a request to the given endpoint and your workspace will be registered in our backend.


```python
import requests

response = requests.post(
    url=f"https://openeo.eodc.eu/openeo/1.1.0/workspace/{WORKSPACE_NAME}/register",
    json=ext_ws,
    headers={
        "authorization": f"Bearer {connection.auth.bearer}"
    },
)

response.content
```

If the response is positive, we have successfully registered our workspace under our user and can now use it as we would any other workspace, by passing the workspace name in our process graphs.
