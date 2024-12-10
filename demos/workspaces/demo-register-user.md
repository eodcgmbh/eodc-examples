## User Story: Credential Management

This notebook will outline how you can create user credentials, delete them and get them if you forget them.

User credentials refer to a set of s3 credentials used for interacting with your internal EODC workspaces (and ones shared with you).


```python
import openeo

# Connect to the openEO backend and authenticate with EGI Check-In

connection = openeo.connect("https://openeo.eodc.eu/openeo/1.2.0")
connection = connection.authenticate_oidc(provider_id="egi")
```

### Creating

Send a post request to the /workspaces/user endpoint in order to create your credentials, the response will include your new credentials, these will be tied to your account.


```python
import requests

response = requests.post(
    url=f"https://openeo.eodc.eu/openeo/1.1.0/user",
    headers={
        "authorization": f"Bearer {connection.auth.bearer}"
    },
)

response.content.decode()
```

### Removing

Send a delete request to the /workspaces/user endpoint in order to create your credentials, this will invalidate your current set of credentials, you can simply post again in order to receive a new set of credentials in the future.


```python
import requests

response = requests.delete(
    url=f"https://openeo.eodc.eu/openeo/1.1.0/user",
    headers={
        "authorization": f"Bearer {connection.auth.bearer}"
    },
)

response.content.decode()
```

### Getting

If you forgot your credentials you can simply call get on the same /workspaces/user endpoint and the response will include your current credentials.


```python
import requests

response = requests.get(
    url=f"https://openeo.eodc.eu/openeo/1.1.0/user",
    headers={
        "authorization": f"Bearer {connection.auth.bearer}"
    },
)

response.content.decode()
```
