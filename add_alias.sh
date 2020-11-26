#! /bin/bash

SCRIPTDIR="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

if [ -d "$SCRIPTDIR/venv/" ]; then
FILEINPUT="\n# MTEC presence tracing\nalias mtec-presence-tracing='$SCRIPTDIR/venv/bin/python $SCRIPTDIR/mtec_presence_tracing.py '\n\n# MTEC presence tracing - setup\nalias mtec-setup='$SCRIPTDIR/venv/bin/python $SCRIPTDIR/setup.py'\n\n# Print stored default user data for MTEC presence tracing form\nalias mtec-info='$SCRIPTDIR/venv/bin/python $SCRIPTDIR/info.py '"
else
FILEINPUT="\n# MTEC presence tracing\nalias mtec-presence-tracing='python3 $SCRIPTDIR/mtec_presence_tracing.py '\n\n# MTEC presence tracing - setup\nalias mtec-setup='python3 $SCRIPTDIR/setup.py'\n\n# Print stored default user data for MTEC presence tracing form\nalias mtec-info='python3 $SCRIPTDIR/info.py '"
fi

if [ -f ~/.bash_aliases ]; then
# if ! grep -q "$FILEINPUT" ~/.bash_aliases ; then
echo  -e $FILEINPUT >> ~/.bash_aliases
echo "Added to ~/.bash_aliases"
# fi
else if [ -f ~/.bashrc ]; then
# if ! grep -q "$FILEINPUT" ~/.bash_aliases ; then
echo -e $FILEINPUT >> ~/.bashrc
echo "Added to ~/.bashrc"
# fi
else
echo ".bashrc and .bash_aliases do not exist."
fi
fi

if [ -f ~/.bashrc ]; then
source ~/.bashrc
fi
