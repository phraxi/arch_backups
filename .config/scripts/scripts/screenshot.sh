#!/bin/sh
NOW=$(date +%s)
grim -g "$(slurp )" -t jpeg $HOME/screenshots/ScreenShot-$NOW.jpg
feh -. -s $HOME/screenshots/ScreenShot-$NOW.jpg 
