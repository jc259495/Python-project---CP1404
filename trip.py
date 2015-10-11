__author__ = 'Hansen'

import time
import re


class Details:
    def __init__(self):  # Initialise the list 'locations'.
        self.locations = []

    def add_date(self, country_name, start_date, end_date):
        # Check that the input is the right type and in the correct format, if not, raise FormatError.
        pattern_match = re.compile('^[0-9]{4}\/[0-9]{2}\/[0-9]{2}$')
        if not pattern_match.match(end_date) and pattern_match.match(start_date) and isinstance(country_name, str):
            raise FormatError('The date to be added is not in correct format! Try YYYY/MM/DD')
        #  Change the input dates to pythons built it 'time'. This way we can easily compare dates with logic.
        start_date = time.strptime(start_date, "%Y/%m/%d")
        end_date = time.strptime(end_date, "%Y/%m/%d")

        if end_date <= start_date:  # Check if end date is before start date, if so, raise a FormatError.
            raise FormatError("The 'end date' is before the 'start date!'")
        
        for location in self.locations:  # Check if the dates are already in use, if so, raise FormatError.
            if (location['Date started'] == start_date) or (location['Date ended'] == end_date):
                raise FormatError('Entered Date is already in use!')

        # Append the desired trip dates onto the locations list.
        self.locations.append({
            'Country': country_name,
            'Date started': time.strftime("%Y/%m/%d", start_date),
            'Date ended': time.strftime("%Y/%m/%d", end_date)
        })

    def current_country(self, date):
        pattern_match = re.compile('^[0-9]{4}\/[0-9]{2}\/[0-9]{2}$')
        if not pattern_match.match(date):  # Check that the input is in the correct format, if not, raise FormatError.
            raise FormatError('Input date is not in correct format! Try: YYYY/MM/DD')
        # Change all string dates to pythons built in date for comparability.
        format_date_input = time.strptime(date, "%Y/%m/%d")

        for line in self.locations:
            format_date_start = time.strptime((line.get('Date started')), "%Y/%m/%d")
            format_date_end = time.strptime((line.get('Date ended')), "%Y/%m/%d")
            # If the input date is found in between the start and end date, return the corresponding country
            # otherwise, raise FormatError.
            if format_date_start <= format_date_input <= format_date_end:
                return line['Country']
        raise FormatError('No country at that date!')

    def is_empty(self):  # If the length of the list 'locations' is empty, return True.
        return len(self.locations) == 0


class Country:
    def __init__(self, name, currency_code, currency_symbol):  # Initialise the variables.
        self.name = name
        self.currency_code = currency_code
        self.currency_symbol = currency_symbol

    def __str__(self: object):  # Called to to compute the "informal" string representation of an object.
        return self.name + " " + self.currency_code + " " + self.currency_symbol

    def format_amount(self: object, amount: float):
        # Check that the input is a positive integer, if not, raise FormatError
        if not amount >= 0:
            raise FormatError('Amount must be a positive integer!')
        try:
            float(amount)
        except:
            raise FormatError('Amount must be a positive integer!')
        # Send the positive integer rounded to two decimal places and its currency symbol.
        return self.currency_symbol + str(("%.2f" % round(amount)))


class Error(Exception):  # When an error is raised from the exception of the 'Try' logic, pass this class.
    pass


class FormatError(Error):  # When FormatError is raised display the attached string to the user.
    def __init__(self: object, value: str) -> None:
        self.value = value
