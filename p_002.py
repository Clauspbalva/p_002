"""
p_002.py | Claus Pagano | Last update: 2022-9-4

Algorithms and Data Structures practice with Python

"""


# ---------------------------------------------------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------------------------------------------------

import time
from datetime import datetime


# ---------------------------------------------------------------------------------------------------------------------
# GLOBAL CONSTANTS & VARIABLES
# ---------------------------------------------------------------------------------------------------------------------

DAY_SECONDS = 24 * 60 * 60
YEAR_DAYS = 365
LEAP_YEAR_DAYS = 366
YEAR_SECONDS = YEAR_DAYS * DAY_SECONDS
LEAP_YEAR_SECONDS = LEAP_YEAR_DAYS * DAY_SECONDS
FIRST_YEAR = 1970
FIRST_MONTH = 1
LAST_MONTH = 12


# --------------------------------------------------------------------------------------------------
# FUNCTIONS DEFINITION
# --------------------------------------------------------------------------------------------------

def date_from_epoch(time_epoch):
    """Returns a string representation of the epoch time

        Args:
            time_epoch (float): UNIX epoch of a given time

        Returns:
            str: string representation of the epoch time with format 'YYYY-MM-DD'
    """

    # Year calculation
    days = int(time_epoch / DAY_SECONDS)
    year = FIRST_YEAR
    years_seconds = 0
    find = True
    while find:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            years_seconds += LEAP_YEAR_SECONDS
            year_days = LEAP_YEAR_DAYS
            leap_year = True
        else:
            years_seconds += YEAR_SECONDS
            year_days = YEAR_DAYS
            leap_year = False
        if time_epoch <= years_seconds:
            find = False
        else:
            year += 1
            days -= year_days

    # Month and day calculation
    month = FIRST_MONTH
    months_days = 0
    day = days
    find = True
    while find:
        if month in [1, 3, 5, 7, 8, 10, 12]:
            month_days = 31
        elif month in [4, 6, 9, 11]:
            month_days = 30
        elif leap_year:
            month_days = 29
        else:
            month_days = 28
        months_days += month_days
        if days <= months_days:
            find = False
        else:
            month += 1
            day -= month_days

    # For debugging
    # return {'epoch': int(time_epoch), 'year': year, 'month': month, 'day': day}

    return str(year) + '-' + ('0' + str(month) if month < 10 else str(month)) + '-' + str(day + 1)


# --------------------------------------------------------------------------------------------------
# MAIN PROCEDURE
# --------------------------------------------------------------------------------------------------

def main():

    # Test
    print(date_from_epoch(time.time()))
    # print(date_from_epoch(time.mktime(datetime.date(datetime.now()).timetuple())))


if __name__ == "__main__":
    main()