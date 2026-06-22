# Drysat workshop @ _eodc_

## Install environment and setup project

First, you need to install `uv` on your OS: https://docs.astral.sh/uv/getting-started/installation/. After pulling the repository, navigate to:
```bash
cd demos/drysat-workshop
```
Then you can install the project with: 
```bash
uv sync
```

## Workshop

We prepared two Jupyter Notebooks:

- `gfm.ipynb`: Explains how to use STAC, how to use the GFM STAC catalogue hosted at _eodc_, and how to load, visualise and export data.
- `era5.ipynb`: Explains how to access object storages, how to pull non-cloud-native data, and how to load cloud-native data like Zarr. The technical aspects are introduced in the context of the CLMS Soil Water Index (SWI) product available as netCDF files and ERA5 available as Zarr. 

To run the notebooks you only need to select the Python binary in the virtual environment created by `uv` as a kernel.


> [!NOTE]  
> Note that you need credentials for the second notebook to run. Ask the workshop admins to provide you the respective credentials and place them in an ".env" file at same level as the notebook.