#
#    ██████╗ ██████╗ ███╗   ██╗███████╗██╗ ██████╗    ██████╗ ██╗   ██╗
#   ██╔════╝██╔═══██╗████╗  ██║██╔════╝██║██╔════╝    ██╔══██╗╚██╗ ██╔╝
#   ██║     ██║   ██║██╔██╗ ██║█████╗  ██║██║  ███╗   ██████╔╝ ╚████╔╝ 
#   ██║     ██║   ██║██║╚██╗██║██╔══╝  ██║██║   ██║   ██╔═══╝   ╚██╔╝  
#   ╚██████╗╚██████╔╝██║ ╚████║██║     ██║╚██████╔╝██╗██║        ██║   
#    ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝     ╚═╝ ╚═════╝ ╚═╝╚═╝        ╚═╝   
#
#   Emir Kahraman (2024)                      ~/.config/qtile/config.py
#   Qtile config

# Icons: https://fontawesome.com/search?o=r&m=free
# Qtile: https://docs.qtile.org/en/stable/manual/config/index.html#configuration-variables
# Extra: https://qtile-extras.readthedocs.io/en/stable/index.html

import os
import re
import socket
import subprocess
import psutil
import json
from libqtile import hook
from libqtile import qtile
from typing import List  
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown, KeyChord
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.widget import Spacer, Backlight
from libqtile.widget.image import Image
from libqtile.dgroups import simple_key_binder
from pathlib import Path
from libqtile.log_utils import logger

from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration
from qtile_extras.widget.decorations import RectDecoration
from qtile_extras.widget.decorations import PowerLineDecoration



# Set Defaults
# --------------------------------------------------------

mod = "mod4"                # SUPER KEY
myTerm = "kitty"            # Default terminal
myBrowser = "opera"         # Default browser

home = str(Path.home())     # Get home path


# Keybindings
# --------------------------------------------------------

# A function for hide/show all the windows in a group
@lazy.function
def minimize_all(qtile):
    for win in qtile.current_group.windows:
        if hasattr(win, "toggle_minimize"):
            win.toggle_minimize()

keys = [

    ## Switch between windows
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window around"),
    
    ## Move windows
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),

    ## Resize windows
    # Works in 'bsp' and 'columns' layout.
    Key([mod, "control"], "left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "up", lazy.layout.grow_up(), desc="Grow window up"),
    
    # Works in 'monadtall' layout.
    #Key([mod, "control"], "down", lazy.layout.shrink(), desc="Grow window to the left"),
    #Key([mod, "control"], "up", lazy.layout.grow(), desc="Grow window to the right"),
    
    ## Other layout keybinds
    Key([mod, "shift"], "space", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "m", lazy.layout.maximize(), desc='Toggle between min and max sizes'),
    Key([mod], "t", lazy.window.toggle_floating(), desc='toggle floating'),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc='toggle fullscreen'),
    Key([mod, "shift"], "m", minimize_all(), desc="Toggle hide/show all windows on current group"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),

    ## System
    Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),

    #Key([mod, "shift"], "q", lazy.spawn("dm-logout -r"), desc="Logout menu"),
    #Key([mod, "control"], "q", lazy.spawn(home + "/dotfiles/qtile/scripts/powermenu.sh"), desc="Open Powermenu"),

    ## Apps
    Key([mod], "Return", lazy.spawn(myTerm), desc="Launch terminal"),
    Key([mod, "shift"], "Return", lazy.spawn("rofi -show drun"), desc="Launch Rofi"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "b", lazy.spawn(myBrowser), desc="Launch Browser"),
    Key([mod], "c", lazy.spawn("code"), desc="Launch Visual Studio Code"),   

    ## Fn keys
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +5%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 5%-")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer set Master 10%- unmute")),
    Key([], "XF86AudioMute", lazy.spawn("amixer set Master toggle")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer set Master 10%+ unmute")),    
    
    #Key([mod], "Print", lazy.spawn(home + "/dotfiles/qtile/scripts/screenshot.sh")),  
]

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]


# Groups
# --------------------------------------------------------

groups = [
    Group("1", layout='columns', spawn='kitty'),
    Group("2", layout='tile'),
    Group("3", layout='tile'),
    Group("4", layout='tile'),
    Group("5", layout='columns'),
    Group("6", layout='columns'),
    Group("7", layout='columns'),
    Group("8", layout='columns'),
    Group("9", layout='columns'),
]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=False),
                desc="Move focused window to group {}".format(i.name),
            ),
        ]
    )



# Pywal Colors - Preconfigured Colors
# --------------------------------------------------------

colors = os.path.expanduser('~/.cache/wal/colors.json')
colordict = json.load(open(colors))
Color0=(colordict['colors']['color0'])
Color1=(colordict['colors']['color1'])
Color2=(colordict['colors']['color2'])
Color3=(colordict['colors']['color3'])
Color4=(colordict['colors']['color4'])
Color5=(colordict['colors']['color5'])
Color6=(colordict['colors']['color6'])
Color7=(colordict['colors']['color7'])
Color8=(colordict['colors']['color8'])
Color9=(colordict['colors']['color9'])
Color10=(colordict['colors']['color10'])
Color11=(colordict['colors']['color11'])
Color12=(colordict['colors']['color12'])
Color13=(colordict['colors']['color13'])
Color14=(colordict['colors']['color14'])
Color15=(colordict['colors']['color15'])


# Set Layout Defaults
# --------------------------------------------------------

layout_theme = {
    "border_width": 2,
    "margin": 3,
    "border_focus": Color6,
    "border_normal": Color1,
    "single_border_width": 3                
}


# Layouts
# --------------------------------------------------------

layouts = [
    layout.Tile(
        shift_windows=True,
        border_width = 0,
        margin = 2,
        ratio = 0.3,
        ),
    layout.Max(
        border_width = 0,
        margin = 2,
        ),
    layout.Columns(
        border_width = 1,
        margin = 3,
        border_focus = Color6,
        border_normal = Color1,
        single_border_width = 3
    ),

    #layout.Bsp(**layout_theme),
    #layout.Floating(**layout_theme)
    #layout.RatioTile(**layout_theme),
    #layout.VerticalTile(**layout_theme),
    #layout.Matrix(**layout_theme),
    #layout.MonadTall(**layout_theme),
    #layout.MonadWide(**layout_theme),
    #layout.Stack(**layout_theme, num_stacks=2),
    #layout.TreeTab(
    #     font = "Ubuntu Bold",
    #     fontsize = 11,
    #     border_width = 0,
    #     bg_color = colors[0],
    #     active_bg = colors[8],
    #     active_fg = colors[2],
    #     inactive_bg = colors[1],
    #     inactive_fg = colors[0],
    #     padding_left = 8,
    #     padding_x = 8,
    #     padding_y = 6,
    #     sections = ["ONE", "TWO", "THREE"],
    #     section_fontsize = 10,
    #     section_fg = colors[7],
    #     section_top = 15,
    #     section_bottom = 15,
    #     level_shift = 8,
    #     vspace = 3,
    #     panel_width = 240
    #     ),
    #layout.Zoomy(**layout_theme),
]


# Set Widget Defaults
# --------------------------------------------------------

widget_defaults = dict(
    font="Ubuntu Bold",
    fontsize = 12,
    padding = 0,
)

extension_defaults = widget_defaults.copy()


# Decorations
# https://qtile-extras.readthedocs.io/en/stable/manual/how_to/decorations.html
# --------------------------------------------------------

decor_left = {
    "decorations": [
        PowerLineDecoration(
            # path="arrow_left"
            # path="rounded_left"
            # path="forward_slash"
            # path="back_slash"
        ),
        RectDecoration(
            colour = Color0,
        )
    ],
}

decor_right = {
    "decorations": [
        PowerLineDecoration(
            # path="arrow_right"
            # path="rounded_right"
            # path="forward_slash"
            # path="back_slash"
        )
    ],
}


# Widgets
# --------------------------------------------------------

widget_list = [
    widget.Prompt(
        font = "Ubuntu Mono",
        fontsize=14
        ),
    widget.GroupBox(
        #foreground = Color7,
        #background = Color0,
        fontsize = 11,
        margin_y = 5,
        margin_x = 5,
        padding_y = 0,
        padding_x = 1,
        borderwidth = 2,
        #active = Color7,
        inactive = Color2,
        rounded = False,
        highlight_color = Color8,
        highlight_method = "line",
        this_current_screen_border = "#00000000",   # active window border
        this_screen_border = Color5,                #
        other_current_screen_border = Color5,       #
        other_screen_border = Color5,               #
        urgent_border = Color6,
        ),
    widget.TextBox(
        text = '|',
        font = "Ubuntu Mono",
        #foreground = Color7,
        padding = 2,
        fontsize = 14
        ),
    widget.CurrentLayoutIcon(
        # custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
        #foreground = Color7,
        padding = 4,
        scale = 0.6
        ),
    widget.CurrentLayout(
        #foreground = Color7,
        padding = 5
        ),
    widget.TextBox(
        text = '|',
        font = "Ubuntu Mono",
        #foreground = Color7,
        padding = 2,
        fontsize = 14
        ),
    widget.WindowName(
        foreground = Color7,
        max_chars = 40
        ),

    #-------------------------------------------
    
    widget.Spacer(length = bar.STRETCH),
    widget.Clock(
        format = "%a, %b %d - %H:%M",
        timezone = ('Turkey')
        ),
    widget.Spacer(length = bar.STRETCH),
    
    #------------------------------------------- 
    
    widget.Net(
        format=('{down:6.2f}{down_suffix:<2}↓↑{up:6.2f}{up_suffix:<2}'),
        foreground = Color7,
        ),
    widget.Spacer(length = 4),
    widget.UPowerWidget(
        foreground = Color7,
        ),
    widget.Spacer(length = 4),
    widget.DF(
        visible_on_warn=False,
        foreground = Color7,
        warn_color = Color6,
        format="Mem: {uf}{m}",
        decorations=[
            BorderDecoration(
                colour = Color5,
                border_width = [0, 0, 2, 0],
                )
            ],
    ),
    widget.Spacer(length = 6),
    widget.Volume(
        foreground = Color7,
        #emoji = True,
        #emoji_list = [],
        fmt = 'Vol: {}',
        decorations=[
            BorderDecoration(
                colour = Color5,
                border_width = [0, 0, 2, 0],
                )
            ],
        ),
    widget.Spacer(length = 6),
    widget.KeyboardLayout(
        configured_keyboards=['tr'],
        foreground = Color7,
        fmt = 'Kbd: {}',
        decorations=[
            BorderDecoration(
                colour = Color5,
                border_width = [0, 0, 2, 0],
                )
            ],
        ),
    #widget.Spacer(length = 4),
    #widget.Systray(padding = 3),
    widget.Spacer(length = 4),
    widget.QuickExit(),
    widget.Spacer(length = 8),
]


# Screens
# --------------------------------------------------------

screens = [
    Screen(
        top=bar.Bar(
            widget_list,
            30,
            padding=20,
            opacity=1,
            margin=2,
            background="#00000000"
        ),
    ),
]


# General Setup
# --------------------------------------------------------

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    border_focus=Color7,
    border_width=2,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),   # gitk
        Match(wm_class="dialog"),         # dialog boxes
        Match(wm_class="download"),       # downloads
        Match(wm_class="error"),          # error msgs
        Match(wm_class="file_progress"),  # file progress boxes
        Match(wm_class='kdenlive'),       # kdenlive
        Match(wm_class="makebranch"),     # gitk
        Match(wm_class="maketag"),        # gitk
        Match(wm_class="notification"),   # notifications
        Match(wm_class='pinentry-gtk-2'), # GPG key password entry
        Match(wm_class="ssh-askpass"),    # ssh-askpass
        Match(wm_class="toolbar"),        # toolbars
        Match(wm_class="Yad"),            # yad boxes
        Match(title="branchdialog"),      # gitk
        Match(title='Confirmation'),      # tastyworks exit box
        Match(title='Qalculate!'),        # qalculate-gtk
        Match(title="pinentry"),          # GPG key password entry
        Match(title="tastycharts"),       # tastytrade pop-out charts
        Match(title="tastytrade"),        # tastytrade pop-out side gutter
        Match(title="tastytrade - Portfolio Report"), # tastytrade pop-out allocation
        Match(wm_class="tasty.javafx.launcher.LauncherFxApp"), # tastytrade settings
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.

wmname = "QTILE"


# Hooks
# --------------------------------------------------------

# HOOK startup
@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

# Done