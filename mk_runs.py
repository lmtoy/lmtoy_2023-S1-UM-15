#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs

project="2023-S1-UM-15"

on = {}

# MH: added 123280 from 25 Nov.  Removed 122774 as this was terminated before completing map
on["HB103"] =       [ 122773, 123280,]
#on["HB103"] =       [ 121107, 121108, 122773, 122774, 123280]

on["HB114"] =        [ 123812, 123813,]


on["HB114_13CO"] =  [ 105907, -105908,]

on["HB46"] =        [ 112931, 113062, 113063, 113065,]

on["HB56"] =        [ 122114, 122115,]
#on["HB56"] =        [ 120849, 120850, 120913, 120914, 122114, 122115,]

on["HB60"] =        [ 122324, 122637, 122638,]
#on["HB60"] =        [ 120724, 120725, 121014,
#                     -121946,-121947,      # nov 6 - all bad
#                      122324,              # nov 10
#                      122637, 122638,]     # nov 19

on["HB94"] =        [ 123803, 123804,]




pars1 = {}

#  for 200MHz bandwidth (~500 km/s) need smaller dv,dw, also to avoid birdies when you can
#  add vlsr=0 if you want to see the local CO
pars1["HB103"]      = "dv=6 dw=30 vlsr=-47 restart=1 pix_list=-15  b_order=1 extent=480 otf_cal=1"
pars1["HB114"]      = "dv=6 dw=30 numbands=1 restart=1 pix_list=-13 b_order=1 extent=360 otf_cal=1"
#pars1["HB114_13CO"] = "dv=6 dw=30 numbands=1 restart=1 pix_list=-13 b_order=1 extent=360 otf_cal=1"
pars1["HB46"]       = "dv=6 dw=30 vlsr=-59 restart=1 pix_list=-15  b_order=1 extent=360 otf_cal=1"
pars1["HB56"]       = "dv=6 dw=30 vlsr=-55 restart=1 pix_list=-15  b_order=1 extent=360 otf_cal=1"
pars1["HB60"]       = "dv=6 dw=30 vlsr=-53 restart=1 pix_list=-15  b_order=1 extent=480 otf_cal=1"
pars1["HB94"]       = "dv=6 dw=30 vlsr=-53 restart=1 pix_list=-15  b_order=1 extent=480 otf_cal=1"


pars2 = {}
pars2["HB103"]      = "bank=0 pix_list=-13"
pars2["HB114"]      = "bank=0 pix_list=-13"
#pars2["HB114_13CO"] = ""
pars2["HB46"]       = "bank=0 pix_list=-13"
pars2["HB56"]       = "bank=0 pix_list=-13"
pars2["HB60"]       = "bank=0 pix_list=-13"
pars2["HB94"]       = "bank=0 pix_list=-13"

pars3={}
pars3["HB103"]      = "bank=1 pix_list=-4,13,14,15"
pars3["HB114"]      = "bank=1 pix_list=-4,13,14,15"
#pars3["HB114_13CO"] = ""
pars3["HB46"]       = "bank=1 pix_list=-4,13,14,15"
pars3["HB56"]       = "bank=1 pix_list=-4,13,14,15"
pars3["HB60"]       = "bank=1 pix_list=-4,13,14,15"
pars3["HB94"]       = "bank=1 pix_list=-4,13,14,15"

if __name__ == "__main__":
    runs.mk_runs(project, on, pars1, pars2, pars3, sys.argv)


