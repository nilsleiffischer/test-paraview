# This is how you can run this script:
# mpiexec -n NUM_PROCS pvbatch Test_Parallel.py

import paraview.simple as pv
import paraview.servermanager as pvserver

num_partitions = pvserver.ActiveConnection.GetNumberOfDataPartitions()
print("Rendering {} data partitions".format(num_partitions))

sphere = pv.Sphere()
pids = pv.ProcessIdScalars()

rep = pv.Show()
lut = pv.GetLookupTableForArray(
    "ProcessId", 1,
    RGBPoints=[0.0, 0.23, 0.3, 0.754, num_partitions, 0.706, 0.016, 0.15],
    ColorSpace='Diverging')
rep.LookupTable = lut
rep.ColorArrayName = 'ProcessId'

pv.Render()
pv.WriteImage('Parallel.png')
print("Rendering done. You should find an image file named `Parallel.png` that shows a sphere. The sphere should be divided into wedges that are color-coded by processor.")
