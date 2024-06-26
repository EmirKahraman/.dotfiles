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

#   XKeys: https://github.com/qtile/qtile/blob/master/libqtile/backend/x11/xkeysyms.py


### AUTOSTART PROGRAMS ###
picom --daemon &                # controls transperancy
#/usr/bin/emacs --daemon &      # if you want to use emacs again uncomment
sleep 1

### UNCOMMENT ONLY ONE OF THE FOLLOWING THREE OPTIONS! ###
# 1. Uncomment to restore last saved wallpaper
# xargs xwallpaper --stretch < ~/.cache/wall &
# 2. Uncomment to set wallpaper with nitrogen
nitrogen --restore &
# 3. Uncomment to set wallpaper with pywal
# wal -i $HOME/Wallpapers/active/       # does not work


# Touchpad Settings
xinput set-prop "UNIW0001:00 093A:0274 Touchpad" "libinput Tapping Enabled" 1
xinput set-prop "UNIW0001:00 093A:0274 Touchpad" "libinput Natural Scrolling Enabled" 1

# Set Keyboard
setxkbmap tr

#Done