#
# ~/.bash_profile
#

[[ -f ~/.bashrc ]] && . ~/.bashrc

if [[ "$(tty)" = "/dev/tty1" ]]; then
    exec Hyprland
fi

if [[ "$(tty)" = "/dev/tty2" ]]; then
    exec startx
fi
