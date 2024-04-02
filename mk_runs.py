#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs

project="2023-S1-UM-15"

on = {}

on["HB114_13CO"] =  [ 105907, -105908 ]


on["HB46"] =        [ 112931, 113062, 113063, 113065,]


pars1 = {}

#  for 200MHz bandwidth (~500 km/s) need smaller dv,dw, also to avoid birdies when you can
#  add vlsr=0 if you want to see the local CO
pars1["HB114_13CO"] = "dv=10 dw=30 numbands=1 restart=1 pix_list=-13 b_order=1 extent=360"

pars1["HB46"]       = "dv=10 dw=30 numbands=1 restart=1 pix_list=-13 b_order=1 extent=360"


pars2 = {}
pars2["HB114_13CO"] = ""
pars2["HB46"] = ""


if __name__ == "__main__":
    runs.mk_runs(project, on, pars1, pars2, sys.argv)


