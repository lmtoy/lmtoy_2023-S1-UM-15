#! /usr/bin/env python
#
#   script generator for project="2021-S1-US-3"
#
#   lmtinfo.py grep US-3 Science Map | awk '{print $2}' | sort


import os
import sys

# in prep of the new lmtoy module
try:
    lmtoy = os.environ['LMTOY']
    sys.path.append(lmtoy)
    from lmtoy import runs
except:
    print("No LMTOY with runs.py")
    sys.exit(0)

project="2023-S1-UM-15"

on = {}

on["HB114_13CO"] =  [ 105907, ]

pars1 = {}

#  for 200MHz bandwidth (~500 km/s) need smaller dv,dw
pars1["HB114_13CO"] = "dv=50 dw=100 numbands=1" 

pars2 = {}

pars2["HB114_13CO"] = ""

if __name__ == "__main__":
    runs.mk_runs(project, on, pars1, pars2)

