#!/bin/bash

#put swap esc caps into xinitrc
mkdir .config/swap_esc_caps
cp swap_esc_caps.sh ~/.config/swap_esc_caps/swap_esc_caps.sh
cp swap_esc_caps_script.sh ~/.config/swap_esc_caps/swap_esc_caps_script.sh
chmod +x ~.config/swap_esc_caps/swap_esc_caps_script.sh
x =`./~/.config/swap_esc_caps/swap_esc_caps_script.sh ; cat .xinitrc`
echo "$x" > .xinitrc


#nvim config
mkdir ~/.config/nvim
cp init.vim ~/.config/nvim/init.vim
