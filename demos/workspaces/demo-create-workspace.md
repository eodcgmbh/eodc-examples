## User Story: Create EODC Workspace

John wants to create a user workspace at EODC, as he does not have a object-storage solution himself.

It's a very simple task to provision a workspace at EODC, provided that you are already an openEO user.

All you need to do in order to create a workspace from scratch is post to the /workspaces endpoint
in the openEO API with a body consisting of a create intent and the preferred title of your workspace.

like so: 

{   
    'intent':'create',   
    'title':'Example'   
}


```python
import openeo

# Connect to the openEO backend and authenticate with EGI Check-In

connection = openeo.connect("https://openeo.eodc.eu/openeo/1.1.0")
connection = connection.authenticate_oidc(provider_id="egi")
```


```python
import requests

WORKSPACE_NAME = ""

request_body = {
    "intent": "create",
    "title": WORKSPACE_NAME
}

response = requests.post(
    url=f"https://openeo.eodc.eu/openeo/1.1.0/workspaces",
    headers={
        "authorization": f"Bearer {connection.auth.bearer}"
    },
    json=request_body
)
```

The responses content will contain your s3 credentials which you can then use to interact with your newly created workspace.


```python
response.content
```
