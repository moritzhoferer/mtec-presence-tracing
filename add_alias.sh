#! /bin/bash

SCRIPTPATH="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

if [ -f ~/.bash_aliases ]; then
echo "# MTEC presence tracing
alias mtec-presence-tracing='python3 $SCRIPTPATH/mtec_presence_tracing.py '
" >> ~/.bash_aliases
echo "Added to ~/.bash_aliases"
else if [ -f ~/.bashrc ]; then
echo "# MTEC presence tracing
alias mtec-presence-tracing='python3 $SCRIPTPATH/mtec_presence_tracing.py '
" >> ~/.bashrc
echo "Added to ~/.bashrc"
else
echo ".bashrc and .bash_aliases do not exist."
fi
fi