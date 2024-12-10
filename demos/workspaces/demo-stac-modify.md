## STAC Modify Process

The stac_modify process allows you to modify the created stac resources of the save_result processes. So you can edit any properties of the stac objects.

The modification of the resource functions according to the [RFC 7386: JSON Merge Patch](https://www.rfc-editor.org/rfc/rfc7386.html) specification.

in this demo we will be changing the ID of the STAC collection as an example.


```python
import openeo

# Connect to the openEO backend and authenticate with EGI Check-In

connection = openeo.connect("https://openeo.eodc.eu/openeo/1.1.0")
connection = connection.authenticate_oidc(provider_id="egi")
```

## Changes

In order to change the collection id of the saved stac resource, we have to call the stac_modify process after save_result.

The stac_modify process has 2 arguments: "data", which takes in the stac resource that gets returned by save_result and "changes", which takes in the changes we want to apply to the stac resource as a dictionary.

The changes are then applied according to the [RFC 7386: JSON Merge Patch](https://www.rfc-editor.org/rfc/rfc7386.html) specification.

In our case we will have to pass the following argument as "changes", with "newid" being the new id we assign for this collection.


```python
CHANGES = {"id": "newid"}

WORKSPACE_NAME = "test2"
```


```python
from openeo.rest.datacube import THIS

cube = connection.load_collection(collection_id="boa_sentinel_2", spatial_extent={
          "west": 16.156771491786476,
          "east": 16.59018048465475,
          "south": 48.08419286799747,
          "north": 48.34670064966687
        }, temporal_extent=[
          "2019-01-01T00:00:00Z",
          "2019-01-31T00:00:00Z"
        ],
        bands=[
          "B02"
        ])

result = cube.save_result()\
  .process("stac_modify", arguments={"changes" : CHANGES}, data=THIS)\
  .process("export_workspace", arguments={"workspace": WORKSPACE_NAME, "merge": None}, data=THIS)

```

Optionally you can print the process graph here.


```python
result.print_json()
```

Run this to start the job


```python
job = result.create_job()

job.start()
```

Run this to check on your jobs status.


```python
job
```

## Check new ID

Now you can check the STAC collection from your workspace using the workspace adapter to see the new ID.


```python
from eodc.workspace import CephAdapter, EODC_CEPH_URL

# Set these variables to your own.

S3_ENDPOINT = EODC_CEPH_URL
S3_ACCESS_KEY = ""
S3_SECRET_KEY = ""

adapter: CephAdapter = CephAdapter(S3_ENDPOINT, S3_ACCESS_KEY, S3_SECRET_KEY)

collections = adapter.list_stac_collections(WORKSPACE_NAME)

collections
```
