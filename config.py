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

mod = "mod4"
terminal = guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
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
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn('kitty'), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key(["control"], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "b", lazy.spawn('qutebrowser'), desc="Launch browser"),
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
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(border_focus="#d6a60a", border_normal="2a2b2b", border_width=4),
    #layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(border_focus = '#d6a60a', border_normal = '#2a2b2b', border_width = 4),
    # layout.Matrix(),
     layout.MonadTall(border_focus = '#d6a60a', border_normal = '#2a2b2b', border_width = 4),
    # layout.MonadWide(),
    # layout.RatioTile(),
    #layout.Tile(border_focus = '#d6a60a', border_normal = '#2a2b2b', border_width = 4),
    # layout.TreeTab(border_focus = '#d6a60a', border_normal = '#2a2b2b', border_width = 4),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)

widget_defaults = dict(
    font="SourceCodeProBold",
    fontsize = 10,
    padding = 2,
    background="#102313"
)
foreground = "#d6a60a"
background = "#2a2b2b"

extension_defaults = widget_defaults.copy()
screens = [
    Screen(
        bottom=bar.Bar(
#                [            
#                widget.CurrentLayout(),
#                widget.GroupBox(),
#                widget.Prompt(),
#                widget.WindowName(),
#                widget.Chord(
##                    chords_colors={
#                        "launch": ("#ff0000", "#ffffff"),
##                    },
#                    name_transform=lambda name: name.upper(),
#                ),
#                widget.Systray(),
#                widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
#                widget.QuickExit(),
#            ],
#
#
            [
            
            widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = foreground,
                       background = background   
                       ),

            widget.Sep(
                       linewidth = 0,
                       padding = 5,
                       foreground = foreground,
                       background = background   
                       ),

              widget.GroupBox(
                       font = "SourceCodePro",
                       fontsize = 12,
                       margin_y = 3,
                       margin_x = 0,
                       padding_y = 5,
                       padding_x = 3,
                       borderwidth = 3,
                       inactive = "#725b0d",
                       active = '#d6a60a',
                       rounded = False,
                       this_current_screen_border = "#d6a60a",
                       highlight_color = "#d6a60a",
                       highlight_method = "block",
                       foreground = '#2a2b2b',
                       background = background
                       ),
             widget.TextBox(
                       text = '|',
                       font = "Source Code Pro",
                       background = background,
                       foreground = "#d6a60a",
                       padding = 2,
                       fontsize = 14
                       ),



             widget.WindowName(
                       foreground = foreground,
                       background = background,
                       padding = 0
                       ),


             widget.TextBox(
                       text = '',
                       font = "SourceCodePro",
                       background = background,
                       foreground = foreground,
                       padding = -13,
                       fontsize = 37
                       ),

             widget.Net(
                       interface = "enp1s0",
                       format = 'Net: {down} ↓↑ {up}',
                       foreground = background,
                       background = foreground,
                       padding = 5,
                       fontsze = 12
                       ),

             widget.TextBox(
                       text = '',
                       font = "SourceCodePro",
                       background = foreground,
                       foreground = background,
                       padding = -13,
                       fontsize = 37
                       ),

             widget.ThermalSensor(
                       fontsize = 12,
                       foreground = foreground,
                       background = background,
                       threshold = 90,
                       fmt = 'Temp: {}',
                       padding = 5
                       ),

             widget.TextBox(
                       text = '',
                       font = "SourceCodePro",
                       background = background,
                       foreground = foreground,
                       padding = -13,
                       fontsize = 37
                       ),

             widget.Clock(format="%m %d %a %H:%M", 
                     fontsize = 12,
                     foreground=background, 
                     background = foreground),

             widget.QuickExit(foreground = background,
                     background = foreground,
                     default_text = 'Ψ'
                     ),

             ], 
             24,
            #border_width=[3, 3, 3, 3],  # Draw top and bottom borders
            #border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
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
follow_mouse_focus = True
bring_front_click = False
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
wmname = "Qtile"
