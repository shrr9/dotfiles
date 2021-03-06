if status is-interactive
    # Commands to run in interactive sessions can go here
pfetch
set fish_greeting
status is-login; and pyenv init --path | source
status is-interactive; and pyenv init - | source
alias :q='exit'
alias texinit='cp ~/.config/init.tex ./init.tex && nvim init.tex'
alias syncgpu="rsync -a -v --exclude=model pijahn@gpu04.itp.uni-heidelberg.de:/remote/gpu06/pijahn/toy_integrator/output/ ~/Uni/BA/out/"
alias synciflow="rsync -a -v pijahn@gpu04.itp.uni-heidelberg.de:/remote/gpu06/pijahn/i-flow ~/Uni/BA/iflowoutput/"
alias syncuni="rsync -a -v shrrg@192.168.0.209:~/Uni ~/"
alias lastinstalled="cat /var/log/pacman.log | grep installed"
alias whichcstate="cat /sys/module/intel_idle/parameters/max_cstate"
alias whichgpu="glxinfo|egrep \"OpenGL vendor|OpenGL renderer\""
alias setnvidia="optimus-manager --switch nvidia --no-confirm"
alias watchtime="watch -n1 \"date '+%D%n%T'|figlet -k -f slant\""
alias !!="history[1]"
alias ls='ls -lha --color=auto'
alias vim='nvim'
alias vifm='vifm . ~/Uni'
alias gpu='ssh pijahn@gpu02.itp.uni-heidelberg.de'
alias cpu='ssh pijahn@pi103.itp.uni-heidelberg.de'
alias gpu4='ssh pijahn@gpu04.itp.uni-heidelberg.de'
alias gpx='ssh -X pijahn@gpu02.itp.uni-heidelberg.de'
alias ec='./.swap_esc_caps_script.sh'
#alias please='eval doas $history[1]'
export EDITOR=nvim
#export LHAPDF_DATA_PATH=~/.pdfsets/
set theme_color_scheme gruvbox
fish_vi_key_bindings
export LC_ALL="en_US.UTF-8"
export LC_CTYPE="en_US.UTF-8"
end

