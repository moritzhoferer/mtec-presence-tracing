#! /bin/bash

SCRIPTDIR="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

if [ -d "$SCRIPTDIR/venv/" ]; then
FILEINPUT="\n# MTEC presence tracing\nalias mtec-presence-tracing='$SCRIPTDIR/venv/bin/python $SCRIPTDIR/mtec_presence_tracing.py '\n\n#MTEC presence tracing - setup\nalias mtec-setup='$SCRIPTDIR/venv/bin/python $SCRIPTDIR/setup.py'\n"
else
FILEINPUT="\n# MTEC presence tracing\nalias mtec-presence-tracing='python3 $SCRIPTDIR/mtec_presence_tracing.py '\n\n#MTEC presence tracing - setup\nalias mtec-setup='python3 $SCRIPTDIR/setup.py'\n"
fi

if [ -f ~/.bash_aliases ]; then
echo  -e $FILEINPUT >> ~/.bash_aliases
echo "Added to ~/.bash_aliases"
else if [ -f ~/.bashrc ]; then
echo -e $FILEINPUT >> ~/.bashrc
echo "Added to ~/.bashrc"
else
echo ".bashrc and .bash_aliases do not exist."
fi
fi
