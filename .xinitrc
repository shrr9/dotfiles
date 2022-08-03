#!/bin/sh
#nitrogen --set-zoom-fill ~/Pictures/gruvbox_psy_fox.jpg &
#~/.config/bg_hue/psyfox_hue/psyfox &
tapetenwechsel/set_wallpaper tapetenwechsel/gruvbox_psy_fox_cropped_lowres_hue 2 &
picom --experimental-backends &
#xmodmap ~/.config/swap_esc_caps/swap_esc_caps.sh
setxkbmap -option caps:swapescape
xset r rate 220 40
xset s off
qtile start
