## User Story: Load Data

Loading your user-collections is a simple process, in order to ensure this notebook works, make sure to already have results of a job saved
in your workspace so we can load it here.
If you don't you can check out the save result demo notebook first.


```python
import openeo

# Connect to the openEO backend and authenticate with EGI Check-In

connection = openeo.connect("https://openeo.eodc.eu/openeo/1.1.0")
connection = connection.authenticate_oidc(provider_id="egi")
```

In order to load a user collection, we have to first find out the collection id, we can do this by listing the stac collections within the workspace using
the list_stac_collections(WORKSPACE_NAME) function. This function returns us a list of tuples consisting of the collection_id and the path to the stac collection json.


```python
from eodc.workspace import CephAdapter, EODC_CEPH_URL

# Set these variables to your own.

WORKSPACE_NAME = ""

S3_ENDPOINT = EODC_CEPH_URL
S3_ACCESS_KEY = ""
S3_SECRET_KEY = ""

adapter: CephAdapter = CephAdapter(S3_ENDPOINT, S3_ACCESS_KEY, S3_SECRET_KEY)

collections = adapter.list_stac_collections(WORKSPACE_NAME)

collections
```

Now you can set your url manually or get it via the list_stac_collections return value.


```python
# URL = ""

collection_id = collections[0][0]

collection = collections[0][-1]

URL = collection.links[1].absolute_href

URL
```

You can also check the available STAC items of your given collection beforehand by using the get_stac_items function of the workspace adapter.


```python
items = adapter.get_stac_items(workspace_name=WORKSPACE_NAME, collection_id=collection_id)

items
```

We are also defaulting to the same spatial_extent and the same temporal_extent as in the save result notebook, feel free to change these to fit your use case.

If you want to check the full extent of your user collection you can use the following code:


```python
print(adapter.get_collection(WORKSPACE_NAME, collection_id).extent.spatial.bboxes) # This prints the maximum bounding box around all items in the STAC collection
print(adapter.get_collection(WORKSPACE_NAME, collection_id).extent.temporal.intervals) # This prints the maximum temporal extent of all items in the STAC collection
```

Now we can start a job with the corresponding url in the load_stac node.

This will load results from a previous job which we can then further transform and use as we like.


```python
collection = connection.load_stac(
    url=URL,
    spatial_extent={
        "west": 16.156771491786476,
        "east": 16.59018048465475,
        "south": 48.08419286799747,
        "north": 48.34670064966687,
    },
    temporal_extent=["2019-01-01T00:00:00Z", "2019-01-31T00:00:00Z"]
)

result = collection.save_result(format="netCDF")
```

Run this to start the job.


```python
job = result.create_job()

job.start()
```

Run this to check the status of your job.


```python
job # Execute this to check on your jobs progress
```

Once the job has run through you can check the results!
