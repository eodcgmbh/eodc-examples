## User Story: Save openEO result to Workspace

Mia is a data scientist, she wants to have access to the user workspace solution to store user results produced with the openEO Platform service offering.

In order to save results from openEO jobs to workspaces, make sure that either your external workspace is registered with the openEO backend (see External Workspace Registration Notebook) or you have provisioned a local workspace.

Then all you need to do, is add the export_to_workspace process after your save_result process in the process graph

arguments: {"workspace": WORKSPACE_NAME}


```python
import openeo

# Set This variable to your workspace's name.

WORKSPACE_NAME = ""

# Connect to the openEO backend and authenticate with EGI Check-In

connection = openeo.connect("https://openeo.eodc.eu/openeo/1.1.0")
connection = connection.authenticate_oidc(provider_id="egi")
```

## Using the openeo python library

To export data to a workspace using the openeo library, you can simply


```python
import openeo

# Set This variable to your workspace's name.

WORKSPACE_NAME = ""

# Connect to the openEO backend and authenticate with EGI Check-In

connection = openeo.connect("https://openeo.eodc.eu/openeo/1.1.0")
connection = connection.authenticate_oidc(provider_id="egi")
```


```python
collection = connection.load_collection(
    collection_id="boa_sentinel_2",
    spatial_extent={
        "west": 16.156771491786476,
        "east": 16.59018048465475,
        "south": 48.08419286799747,
        "north": 48.34670064966687,
    },
    temporal_extent=["2019-01-01T00:00:00Z", "2019-01-31T00:00:00Z"],
    bands=["B02"],
)

result = collection.save_result().process(
    "export_workspace", arguments={"workspace": WORKSPACE_NAME}
)
```

Run this to start the job.


```python
job = result.create_job()

job.start()
```

Run this to check the status of your job.


```python
job
```

After the job has run through you can check the exported files in your workspace!
