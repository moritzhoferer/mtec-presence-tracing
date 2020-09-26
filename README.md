# MTEC Presence Tracing

This tool serves the pure purpose to fill the MTEC presence tracing form faster.

## How to use

Execute in terminal with:

``` {bash}
./mtec_presence_tracing.py hhmm hhmm
```

where the first time is the arrival and the second the departure time. The date is automatically for today.

In a Python GUI you navigate to the respective directory and execute

``` {python}
run mtec_presence_tracing.py hhmm hhmm
```

If you want to change your data, you can run the `setup.py` script or manipulate the `user_data.csv` file manually.

## Set up aliases on Linux or Mac

To make life easier, you can also define aliases. Add these lines to the `~/.bashrc` or `~/.bash_aliases` file:

``` {bash}
# MTEC presence tracing
alias mtec-presence-tracing='python3 $SCRIPTDIR/mtec_presence_tracing.py '

#MTEC presence tracing - setup
alias mtec-setup='python3 $SCRIPTDIR/setup.py'
```

or execute `add_alias.sh`. Afterwards, you run `source ~/.bashrc`.

## Requirements

You need the following programs and packages:

* [Python 3](https://www.python.org/download/releases/3.0/)
* [Selenium](https://selenium-python.readthedocs.io/): `python3 -m pip install selenium`
* [Firefox](https://www.mozilla.org/en-US/firefox/all/#product-desktop-release): `sudo apt update && sudo apt install firefox`
* [Geckodriver for Firefox](https://github.com/mozilla/geckodriver): `sudo apt install firefox-geckodriver`

Command line commands are for Debian, Ubuntu, and related Linux distributions using Advanced Package Tool.
