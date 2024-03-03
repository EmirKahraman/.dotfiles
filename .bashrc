#
#      ██████╗  █████╗ ███████╗██╗  ██╗██████╗  ██████╗
#      ██╔══██╗██╔══██╗██╔════╝██║  ██║██╔══██╗██╔════╝
#      ██████╔╝███████║███████╗███████║██████╔╝██║     
#      ██╔══██╗██╔══██║╚════██║██╔══██║██╔══██╗██║     
#   ██╗██████╔╝██║  ██║███████║██║  ██║██║  ██║╚██████╗
#   ╚═╝╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝
#
#   Emir Kahraman (2024)                      ~/.bashrc
#      

### Source global definitions                                      #DEFAULT config
if \[ -f /etc/bashrc \]; 
then        
    . /etc/bashrc 
fi

### Color palettes from profile.d                                  #DEFAULT config
for i in /etc/profile.d/*.sh; do
        if [ -r "$i" ]; then
            if [ "$PS1" ]; then
                . "$i"
            else
                . "$i" >/dev/null
            fi
        fi
    done

### COLORS ###


# If not running interactively, don't do anything
[[ $- != *i* ]] && return
[ "$PS1" = "\\s-\\v\\\$ " ] && PS1="[\u@\h \W]\\$ "

### EXPORT ###
export TERM="xterm-256color"                      # getting proper colors
export HISTCONTROL=ignoredups:erasedups           # no duplicate entries
export ALTERNATE_EDITOR=""                        # setting for emacsclient
export EDITOR="code"                              # $EDITOR use Emacs in terminal
export VISUAL="code"                              # $VISUAL use Emacs in GUI mode
export MANPAGER="nvim +Man!"

### SET VI MODE ###
# Comment this line out to enable default emacs-like bindings
set -o vi
bind -m vi-command 'Control-l: clear-screen'
bind -m vi-insert 'Control-l: clear-screen'

### PATH ###
if [ -d "$HOME/.bin" ] ;
  then PATH="$HOME/.bin:$PATH"
fi

if [ -d "$HOME/.local/bin" ] ;
  then PATH="$HOME/.local/bin:$PATH"
fi

if [ -d "$HOME/.emacs.d/bin" ] ;
  then PATH="$HOME/.emacs.d/bin:$PATH"
fi

if [ -d "$HOME/Applications" ] ;
  then PATH="$HOME/Applications:$PATH"
fi

if [ -d "/var/lib/flatpak/exports/bin/" ] ;
  then PATH="/var/lib/flatpak/exports/bin/:$PATH"
fi

if [ -d "$HOME/.config/emacs/bin/" ] ;
  then PATH="$HOME/.config/emacs/bin/:$PATH"
fi

export PATH="${PATH}:${HOME}/.local/bin/"

### SHOPT ###
shopt -s autocd # change to named directory
shopt -s cdspell # autocorrects cd misspellings
shopt -s cmdhist # save multi-line commands in history as single line
shopt -s dotglob
shopt -s histappend # do not overwrite history
shopt -s expand_aliases # expand aliases
shopt -s checkwinsize # checks term size when bash regains control

#ignore upper and lowercase when TAB completion
bind "set completion-ignore-case on"

### ALIASES ###
# navigation
up () {
  local d=""
  local limit="$1"

  # Default to limit of 1
  if [ -z "$limit" ] || [ "$limit" -le 0 ]; then
    limit=1
  fi

  for ((i=1;i<=limit;i++)); do
    d="../$d"
  done

  # perform cd. Show error if cd fails
  if ! cd "$d"; then
    echo "Couldn't go up $limit dirs.";
  fi
}

# Changing "ls"
alias ls='ls -a --color=always --group-directories-first' # my preferred listing
alias la='ls -la --color=always --group-directories-first' # all files and dirs

# Colorize grep output (good for log files)
alias grep='grep --color=auto'
alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'

# adding flags
alias df='df -h'                          # human-readable sizes
alias free='free -m'                      # show sizes in MB

# switch between shells
alias tobash="sudo chsh $USER -s /bin/bash && echo 'Now log out.'"
alias tozsh="sudo chsh $USER -s /bin/zsh && echo 'Now log out.'"
alias tofish="sudo chsh $USER -s /bin/fish && echo 'Now log out.'"

# git
alias gitstat='git status'
alias gitcommit='git commit -m'
alias gitpush='git push origin main'

# wifi 
alias wificonnect_DUDE='nmcli device wifi connect DUDE password' #just being lazy

# termbin
alias tb="nc termbin.com 9999"

### MESSAGES ###
figlet -f 'Georgia11.flf' Welcome

# Done