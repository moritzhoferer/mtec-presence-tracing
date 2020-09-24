# MTEC Presence Tracking

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

## Requirements

You need the following programs and packages:

* [Python 3](https://www.python.org/download/releases/3.0/)
* [Selenium](https://selenium-python.readthedocs.io/)
* Geckodriver for Firefox or Chrome

## Set up alias on Linux or Mac

Add these lines to the `~/.bashrc` or `~/.bash_aliases` file:

``` {bash}
# MTEC presence tracing
alias mtec-presence-tracing='python3 $SCRIPTDIR/main.py '
```

by executing `add_alias.sh`.
