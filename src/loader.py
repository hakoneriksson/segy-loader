from segysak.segy import segy_converter
from segysak import open_seisnc
from pathlib import Path

segy_file = Path("data/volve10r12-full-twt-sub3d.sgy")
print("SEG-Y exists:", segy_file.exists())

nc_file = segy_file.with_suffix(".nc")
if not nc_file.exists():
    # Convert the SEG-Y file to a netCDF file
    segy_converter(segy_file, nc_file)

seisnc = open_seisnc(nc_file)

print(seisnc)
