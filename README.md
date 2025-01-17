# 2023-S1-UM-15

this project aims to observe a molecular cloud in the outer galactic disk at 200MHz
and thus very high resolution (0.0625 km/s)

## HB46

Simple cloud at the expected vlsr=-59

## HB56

The source is not at the expected vlsr=-55 but more at -49

## HB60

The source of interest has vlsr=-47, another strong source is around vlsr=-30, which is also present
at the OFF position, hence results in negative signal.   For the puprose of the pipeline, vlsr=-40 was
choosen, with a wider dv=15.  but a more smart baseline would be better

## HB103

Two lines at __1 (115GHz).


## HB114_13CO

source name is HB114_13CO, but RESTFREQ=115.271 GHz.   vlsr=-47 km/s
numbands=2 but only one restfreq was given. Was this a mistake in observing script?

restfreq=115.271202,115.271204

So the only way to reduce it, is by forcing numbands=1

Only 105907 was observed. There is also 105908 but this seems a short (failed?) obsnum of only 180 sec.

This is one of the rare 200 MHz (8k channels) data. There are some birdies in some of
the beams, but with a narrow dv,dw they won't bother us. Otherwise use birdies=

The cloud is pretty narrow and well defined at the default vlsr=-49, or is there a 2nd line?

SLpipeline.sh obsnum=105907 _s=HB114_13CO dv=10 dw=30 numbands=1 restart=1 pix_list=-13 b_order=1 extent=360

Galactic CO can be retrieved this way

SLpipeline.sh obsnum=105907 _s=HB114_13CO dv=10 dw=30 numbands=1 restart=1 pix_list=-13 b_order=1 extent=360 vlsr=0

To see the whole misery of the band, use  vlsr=-93 dv=57 dw=200  - stored in 105907__wide

