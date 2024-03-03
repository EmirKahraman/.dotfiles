#!/usr/bin/env bash 

#
#    █████╗ ██╗   ██╗████████╗ ██████╗ ███████╗████████╗ █████╗ ██████╗ ████████╗███████╗██╗  ██╗
#   ██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██║  ██║
#   ███████║██║   ██║   ██║   ██║   ██║███████╗   ██║   ███████║██████╔╝   ██║   ███████╗███████║
#   ██╔══██║██║   ██║   ██║   ██║   ██║╚════██║   ██║   ██╔══██║██╔══██╗   ██║   ╚════██║██╔══██║
#   ██║  ██║╚██████╔╝   ██║   ╚██████╔╝███████║   ██║   ██║  ██║██║  ██║   ██║██╗███████║██║  ██║
#   ╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝╚═╝╚══════╝╚═╝  ╚═╝
#
#   Emir Kahraman (2024)                                             ~/.config/qtile/autostart.sh
#   an autostart script for Qtile


### AUTOSTART PROGRAMS ###
picom --daemon &                # controls transperancy
#/usr/bin/emacs --daemon &      # if you want to use emacs again uncomment
sleep 1

### UNCOMMENT ONLY ONE OF THE FOLLOWING TWO OPTIONS! ###
# 1. Uncomment to restore last saved wallpaper
# xargs xwallpaper --stretch < ~/.cache/wall &
# 2. Uncomment to set wallpaper with nitrogen
nitrogen --restore &

# Touchpad Settings
xinput set-prop 11 344 1
xinput set-prop 11 317 1

xinput set-prop 12 346 1
xinput set-prop 12 317 1


# Set Keyboard
setxkbmap tr

#Done