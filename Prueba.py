# ---------------------------------------------------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------------------------------------------------
import time


# ---------------------------------------------------------------------------------------------------------------------
# GLOBAL CONSTANTS & VARIABLES
# ---------------------------------------------------------------------------------------------------------------------
""""Using months of 30.5 days each. 
    1 year = 366 days"""

days_per_year = 366
seg_per_year = 31622400
seg_per_month = 2635200
seg_per_day = 86400
current_epoch_time = time.time()
years_from_epoch = current_epoch_time / seg_per_year
current_year = int(years_from_epoch + 1970)
months_from_epoch = current_epoch_time / seg_per_month
days_from_epoch = current_epoch_time / seg_per_day

print(current_year)


# --------------------------------------------------------------------------------------------------
# FUNCTIONS DEFINITION
# --------------------------------------------------------------------------------------------------

def date_from_epoch(epoch_time):
    """Returns a string representation of the epoch time

        Args:
            time_epoch (float): UNIX epoch of a given time

        Returns:
            str: string representation of the epoch time with format 'YYYY-MM-DD'
    """

    # TODO: Claus code


    return x



