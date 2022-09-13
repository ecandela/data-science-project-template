conda activate venvOsee
conda config --add channels conda-forge
conda env export --from-history > environment.yml
PAUSE