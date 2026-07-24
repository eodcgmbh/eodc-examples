## Notebooks for the conversion of scientific data into Cloud-Optimized dataformats

Install the necessary environment using the uv package manager: https://docs.astral.sh/uv/#installation

```
uv sync
```

Then execute the individual notebooks to transform the datasets in each notebook in src/.

```
01_geotiff_to_cog.ipynb
02_geotiff_to_zarr.ipynb
03_netCDF_to_zarr.ipynb
04_nat_bufr_to_geoparquet.ipynb
```