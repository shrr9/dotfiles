#!/bin/sh
nitrogen --set-zoom-fill ~/Pictures/mimose.jpg &
picom --experimental-backends &
xmodmap ~/.config/swap_esc_caps/swap_esc_caps.sh
xset r rate 220 40
xset s off  
qtile start
