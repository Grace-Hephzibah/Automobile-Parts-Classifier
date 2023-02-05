import splitfolders as sp# or import splitfolders
input_folder = "data"
output = "data-split" #where you want the split datasets saved. one will be created if it does not exist or none is set

sp.ratio(input_folder, output=output, seed=42, ratio=(.7, .2, .1))
