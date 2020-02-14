# This is how you can run this script:
# pvpython Test_Simple.py

import paraview.simple as pv

pv.Sphere()

pv.Show()

pv.SaveScreenshot("Simple.png")
print("Rendering done. You should find an image file named `Simple.png` that shows a sphere.")
