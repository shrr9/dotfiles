#!/bin/bash
/home/shrrg/tapetenwechsel/set_wallpaper /home/shrrg/tapetenwechsel/psy_fox 1.7 &
picom --experimental-backends &
setxkbmap -option caps:swapescape
setxkbmap -layout us &
xset r rate 220 40 &
doas chmod 777 /sys/class/backlight/intel_backlight/brightness
qtile start
