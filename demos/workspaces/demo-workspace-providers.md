## Workspace Providers

Workspace Providers are the name of the different underlying object-storage types that are supported by any given backend.

To access a list of supported workspace providers, just call the /workspace_providers endpoint. The information in this
list also contains the formatting of parameters used when registering a workspace of the given type.



```python
import json
import requests

response = requests.get(
    url=f"https://openeo.eodc.eu/openeo/1.1.0/workspace_providers",
)


print(json.dumps(json.loads(response.content.decode()), indent=4, sort_keys=True))
```
