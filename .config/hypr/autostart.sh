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
#   an autostart script for Hyprland


### AUTOSTART PROGRAMS ###
waybar
#picom --daemon &                # controls transperancy
#/usr/bin/emacs --daemon &       # if you want to use emacs again uncomment
sleep 1

### UNCOMMENT ONLY ONE OF THE FOLLOWING THREE OPTIONS! ###
# 1. Uncomment to restore last saved wallpaper
#xargs xwallpaper --stretch < ~/.cache/wall &
# 2. Uncomment to set a random wallpaper on login
# find /usr/share/backgrounds/dtos-backgrounds/ -type f | shuf -n 1 | xargs xwallpaper --stretch &
# 3. Uncomment to set wallpaper with nitrogen
nitrogen --restore &

# Touchpad Settings
xinput set-prop 12 346 1
xinput set-prop 12 317 1

# Set Keyboard
setxkbmap tr

#Done