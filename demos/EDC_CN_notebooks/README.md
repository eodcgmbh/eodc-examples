## Notebooks for converting scientific data into cloud-optimized formats

Install the necessary environment using the `uv` package manager: https://docs.astral.sh/uv/#installation

Then go inside this repo and install all dependencies with

```
uv sync
```

You can find the individual notebooks to transform the datasets under "src".

```
01_geotiff_to_cog.ipynb
02_geotiff_to_zarr.ipynb
03_netcdf_to_zarr.ipynb
04_nat_bufr_to_geoparquet.ipynb
```