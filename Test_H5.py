# Before running this script, set the path below to a location where you have `h5py` installed.
# Installation instructions:
# 1. Create a virtual environment with ParaView's Python:
#    ```
#    path/to/paraview/install/python3 -m venv ./env
#    ```
# 2. Install `h5py` in the environment **using ParaView's HDF5**:
#    ```
#    . ./env/bin/activate
#    HDF5_DIR=path/to/paraview/install/ pip install --no-binary=h5py h5py
#    ```
#    Note that the `HDF5_DIR` should have `include` and `lib` directories with ParaView's HDF5.
# 3. Set the path below to `path/to/env/lib/python3.7/site-packages`
extra_packages_path = '/data/home/nfischer/test-paraview/env/lib/python3.7/site-packages'
# Then, this is how you can run this script:
# pvpython Test_H5.py

import paraview.simple as pv

import sys
sys.path.append(extra_packages_path)

import h5py

pv.Sphere()

pv.Show()

pv.SaveScreenshot("H5.png")
print("Rendering done. You should find an image file named `H5.png` that shows a sphere.")
