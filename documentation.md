# How to Publish STAC Data at EODC

## Overview

This guide explains how customers can publish their data in the EODC-hosted STAC API [endpoint](https://proxy.dev.services.eodc.eu/collections)

The typical workflow consists of preparing STAC metadata, authenticating to the API, and creating STAC **Collections** and **Items**.

# 1. Prerequisites

Before publishing STAC data at EODC, make sure you have:

### Access credentials

You need valid **EODC user credentials** to authenticate against the STAC API.

### STAC metadata

Your dataset must be described using valid **STAC metadata**:

* **Collection** – describes a dataset
* **Items** – describe individual scenes or data entries
* **Assets** – links to the actual data files

Example structure:

```
dataset/
 ├── collection.json
 └── items/
      ├── item_001.json
      ├── item_002.json
      └── ...
```

### Required metadata fields

Some metadata fields are required by the STAC catalouge.
In particular, the **access field** defines who can see the data.

Example: visible to all users in an organisation

```json
{
  "access": {
    "visibility": "organisation",
    "allowed_users": [],
    "allowed_organisations": ["eodc"]
  }
}
```

Example: visible only to a specific users

```json
{
  "access": {
    "visibility": "user",
    "allowed_users": ["john.smith@eodc.eu","jane.smith@eodc.eu"],
    "allowed_organisations": []
  }
}
```

If the `access` field is missing or configured incorrectly, the data may not be visible in the catalogue.


# 2. Workflow for publishing STAC data

The typical workflow for publishing data at EODC is:

1. Authenticate to the STAC API
2. Prepare STAC metadata
3. Create a **Collection**
4. Create **Items**
5. Update metadata if necessary
6. Verify that the data appears in the catalogue


# 3. Example Tutorial

A complete hands-on example for publishing STAC metadata at EODC is available as a Jupyter notebook.

The notebook demonstrates the full workflow:

1. Authenticate to the STAC API
2. Load sample STAC metadata
3. Create a Collection
4. Create Items
5. Update an Item
6. Delete STAC entities

You can find the tutorial here:

**[tutorial.ipynb](./tutorial.ipynb)**

Open the notebook and run the cells step by step to interact with the STAC API.


# 4. Common mistakes

### Missing access metadata

If the `access` field is missing, the dataset may not be visible to other users.

### Invalid STAC structure

Make sure the metadata follows the **STAC specification**.

Helpful tool:

```
stac-validator
```

### Incorrect asset links

Assets must point to valid and accessible data files.


# 5. Troubleshooting

### Item creation fails

Check:

* Collection exists
* Item IDs are unique
* metadata structure is valid JSON


### Data not visible in the catalogue

Possible reasons:

* incorrect `access` settings
* wrong organisation name
* missing permissions

### Validation errors

Run a STAC validator before ingestion:

```
stac-validator collection.json
```


# 6. Support

If you encounter problems publishing STAC data at EODC, please contact:

**EODC Support**
[support@eodc.eu](mailto:support@eodc.eu)
