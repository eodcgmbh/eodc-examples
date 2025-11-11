## Example Environment for all Notebooks
### Note: Not all Dependencies are needed for every Notebook

mamba env create -f environment.yml

mamba activate eodc-examples

mamba install -c conda-forge libgdal=3.11.4 gdal=3.11.4

pip install eodc==2025.10.2
