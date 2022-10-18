# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import psutil
import os
from spotify import Spotify

#Alt = mod1
#SUper = mod4
mod = "mod1" #Alt
alt = 'mod4' #Super_L



terminal = guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod],"F6", lazy.spawn('/home/shrrg/.config/audio_volume/0.sh'), desc = 'increase scrren brightness '),
    Key([],"XF86AudioLowerVolume", lazy.spawn('/home/shrrg/.config/audio_volume/dec.sh'), desc = 'increase scrren brightness '),
    Key([], "XF86AudioRaiseVolume", lazy.spawn('/home/shrrg/.config/audio_volume/inc.sh'), desc = 'increase scrren brightness '),
    Key([], "XF86AudioMute", lazy.spawn('/home/shrrg/.config/audio_volume/0.sh'), desc = 'increase scrren brightness '),
    Key([mod],"F3", lazy.spawn('/home/shrrg/.config/brightness/inc.sh'), desc = 'increase scrren brightness '),
    Key([mod], "F2", lazy.spawn('/home/shrrg/.config/brightness/dec.sh'), desc = 'increase scrren brightness '),
    Key([],"XF86MonBrightnessUp", lazy.spawn('/home/shrrg/.config/brightness/inc.sh'), desc = 'increase scrren brightness '),
    Key([], "XF86MonBrightnessDown", lazy.spawn('/home/shrrg/.config/brightness/dec.sh'), desc = 'increase scrren brightness '),

    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "m", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"],"Return",lazy.layout.toggle_split(),desc="Toggle between split and unsplit sides of stack"),
    Key(["control"],  "t", lazy.spawn('konsole'), desc="Launch terminal"),
    Key([mod], "Return", lazy.spawn('kitty'), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "F4", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], 'space', lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "b", lazy.spawn('qutebrowser'), desc="Launch browser"),
    Key([mod,'control'], "b", lazy.spawn('librewolf'), desc="Launch browser"),
    Key([mod], "Down", lazy.to_screen(0)),
    Key([mod], "Up", lazy.to_screen(1)),
    Key([], "Super_L", lazy.spawn('/home/shrrg/.config/rofi/launchers/colorful/launcher.sh'), desc="Launch browser"),
]

groups = [Group(i) for i in "asdfuiop"]

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
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # mod + ctrl = not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            Key([mod, "control"], i.name, lazy.window.togroup(i.name),
                desc="move focused window to group {}".format(i.name)),
        ]
    )
kingaccent_1 = '0d1f58'
layouts = [
    layout.Columns(border_focus="#aaaaaa", border_normal='2a2b2b00', border_width=4, margin =2, border_on_single = False, margin_on_single = 0),
    #layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(border_focus = '#d6a60a', border_normal = '#2a2b2b', border_width = 4),
    # layout.Matrix(),
    #layout.Floating(border_focus = '#cfad3d', border_normal = '#2a2b2b'),
    # layout.MonadTall(border_focus = '#d6a60a', border_normal ='#2a2b2b' , border_width = 4),
    # layout.MonadWide(),
    # layout.RatioTile(),
    #layout.Tile(border_focus = '#d6a60a', border_normal = '#2a2b2b', border_width = 4),
    layout.TreeTab(border_focus = '#d6a60a', border_normal = '#2a2b2b', border_width = 4),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="TabacMono",
    fontsize=12,
    padding=3,
)

widget_defaults = dict(
    font="TabacMono",
    fontsize = 15,
    padding = 2,
    background="#102313"
)
foreground = "#1a7c5b00"
background = "#172d3a00"
foregroundtext = "#911414"
backgroundtext = "#172d3a"
#accent_2 = '#d3ba15'
#accent_2 = '#441010'
accent_2 = '#1933c9'
white = '#ffffff'
black = '#000000'
spotify_color = '#1ED76020'
font = 'TabacMono'

extension_defaults = widget_defaults.copy()
screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.Image(
                    filename = '~/.config/qtile/icons/Arch_button.png',
                    background = black,
                    margin = 2, 
                    mouse_callbacks = {'Button1':lazy.spawn('/home/shrrg/.config/rofi/launchers/colorful/launcher.sh')}
                    ),


                widget.TextBox(
                        text = '◣', 
                        font = font, 
                        fontsize = 88, 
                        padding = -13, 
                        background = accent_2, 
                        foreground = black),

                widget.GroupBox(
                         font = font,
                         fontsize = 14,
                         margin_y = 3,
                         margin_x = 0,
                         padding_y = 5,
                         padding_x = 3,
                         borderwidth = 3,
                         inactive = "#323232",
                         active = white,
                         rounded = False,
                         this_current_screen_border = black,
                         highlight_color = foregroundtext,
                         highlight_method = "block",
                         foreground = '#2a2b2b',
                         background = accent_2, 
                         ),

                widget.TextBox(
                        text = '◣', 
                        font = font, 
                        fontsize = 88, 
                        padding = -13, 
                        foreground = accent_2, 
                        background = background),

                widget.Prompt(foreground = '#ffffff',#foregroundtext, 
                              background = background, 
                              font = font),

                widget.WindowName(
                          foreground = '#ffffff',
                          background = background,
                          padding = 0, 
                          font = font,
                          fontsize = 12,
                          for_current_screen = True,
                          max_chars = 40
                          ),

                widget.TextBox(
                          text = '◢',
                          #text = 'T',
                          font = font,
                          background = background,
                          foreground = spotify_color,
                          padding = -13,
                          fontsize = 88
                          ),
                Spotify(
                        format = '{track} {icon} ',
                        background = spotify_color, 
                        foreground = '#777777',
                        pause_icon = '◀', 
                        play_icon = '||', 
                        ),

               widget.Image(
                   filename = '~/.config/qtile/icons/spotify.png',
                   background = spotify_color,
                   margin = 2, 
                   ),


                widget.TextBox(
                          text = '◢',
                          font = font,
                          foreground = accent_2,
                          background = spotify_color,
                          padding = -13,
                          fontsize = 88
                          ),


                widget.WidgetBox(widgets = [

                    widget.Battery(
                            foreground = white,
                            background = accent_2,
                            font = font,
                            fontsize = 15,
                            charge_char = '+',
                            discharge_char = '-',
                            format = '{char}{percent:2.0%}',
                            update_interval = 5
                            ),

                       widget.Image(
                           filename = '~/.config/qtile/icons/battery.png',
                           background = accent_2,
                           margin = 2, 
                           ),


                     widget.TextBox(
                               text = '◢',
                               font = font,
                               background = accent_2,
                               foreground = black,
                               padding = -13,
                               fontsize = 88
                               ),
                     widget.Wlan(
                               background = black,
                               foreground = white,
                               padding = 5,
                               fontsize = 15,
                               mouse_callbacks = {'Button1':lazy.spawn('kitty -e nmtui')},
                               interface = "wlo1",
                               format = '{percent:2.0%}'
                               ),
                     widget.Net(
                               interface = "wlo1",
                               format = '{down}',
                               background = black,
                               prefix = 'k',
                               foreground = white,
                               padding = 5,
                               fontsize = 15,
                               mouse_callbacks = {'Button1':lazy.spawn('kitty -e nmtui')},
                               ),

                       widget.Image(
                           filename = '~/.config/qtile/icons/net.png',
                           background = black,
                           margin = 2, 
                           mouse_callbacks = {'Button1':lazy.spawn('kitty -e nmtui')}
                           ),

                      widget.TextBox(
                                text = '◢',
                                font = font,
                                background = black,
                                foreground = accent_2,
                                padding = -13,
                                fontsize = 88
                                ),

                      widget.CPU(
                              foreground = white,
                              background = accent_2,
                              format = '{load_percent}%',
                              update_interval = 0.4, 
                              mouse_callbacks = {'Button1':lazy.spawn('kitty -e htop')},
                              max_chars = 12
                      ),


                       widget.CPUGraph(
                                  type = 'box',
                                  border_width = 0,
                                  fill_color = white,
                                  frequency = 0.1,
                                  graph_color = white,
                                  background = accent_2, 
                                  mouse_callbacks = {'Button1':lazy.spawn('kitty -e htop')},
                                  foreground = accent_2, 
                       ),

                       widget.Image(
                           filename = '~/.config/qtile/icons/cpu.png',
                           background = accent_2,
                           margin = 2, 
                           mouse_callbacks = {'Button1':lazy.spawn('kitty -e htop')}
                           ),

                       widget.TextBox(
                                 text = '◤',
                                 font = "SourceCodePro",
                                 background = black,
                                 foreground = accent_2,
                                 padding = -13,
                                 fontsize = 88
                                 ),

                       widget.Volume(foreground = white, 
                               update_interval = 0.10,
                               background = black, 
                               font = font, 
                               fontsize = 15,
                               mouse_callbacks = {'Button1':lazy.spawn('kitty -e alsamixer')},
                               ),

                       widget.Image(
                           filename = '~/.config/qtile/icons/audio.png',
                           background = black,
                           margin = 2, 
                           mouse_callbacks = {'Button1':lazy.spawn('kitty -e alsamixer')}
                           ),
                
                       widget.TextBox(
                                 text = '◤',
                                 font = "SourceCodePro",
                                 background = accent_2,
                                 foreground = black,
                                 padding = -13,
                                 fontsize = 88
                                 ),
                    ], 
                    background = accent_2,
                    text_closed = '<-',
                    text_open = '->',
                    close_button_location = 'right',
                    font = 'TabacMono',
                    ),
                    widget.TextBox(
                              text = '◢',
                              font = "SourceCodePro",
                              background = accent_2,
                              foreground = black,
                              padding = -13,
                              fontsize = 88
                              ),
                    widget.Clock(format="%a %d/%m; %H:%M:%S", 
                            fontsize = 15,
                            foreground=white, 
                            background = black,
                            mouse_callbacks = {'Button1':lazy.spawn('kitty -e /home/shrrg/.config/qtile/scripts/show_cal')},
                            font = font),



             ], 
             26,
             background = '#00000000',
        ),
    ),
]
# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = False
bring_front_click = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = False

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None


wmname = "Qtile"
