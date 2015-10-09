__author__ = 'Hansen'

import time


class Details:
    def __init__(self):
        self.locations = []

    def add_date(self, country_name, start_date, end_date):
        import re
        pattern_match = re.compile('^[0-9]{4}\/[0-9]{2}\/[0-9]{2}$')
        if not pattern_match.match(end_date) and pattern_match.match(start_date) and isinstance(country_name, str):
            raise FormatError('The date to be added is not in correct format! Try YYYY/MM/DD')

        start_date = time.strptime(start_date, "%Y/%m/%d")
        end_date = time.strptime(end_date, "%Y/%m/%d")

        if end_date <= start_date:
            raise FormatError("The 'end date' is before the 'start date!'")
        
        for location in self.locations:
            if (location['Date started'] == start_date) or (location['Date ended'] == end_date):
                raise FormatError('Entered Date is already in use!')

        self.locations.append({
            'Country': country_name,
            'Date started': time.strftime("%Y/%m/%d", start_date),
            'Date ended': time.strftime("%Y/%m/%d", end_date)
        })

    def current_country(self, date):
        try:
            format_date_input = time.strptime(date, "%Y/%m/%d")
        except:
            raise FormatError('Input date is not in correct format! Try: YYYY/MM/DD')

        for item in self.locations:
            format_date_start = time.strptime((item.get('Date started')), "%Y/%m/%d")
            format_date_end = time.strptime((item.get('Date ended')), "%Y/%m/%d")

            if format_date_start <= format_date_input <= format_date_end:
                return item['Country']
        raise FormatError('No country at that date!')

    def is_empty(self):
        return len(self.locations) == 0


class Country:
    def __init__(self, name, currency_code, currency_symbol):
        self.name = name
        self.currency_code = currency_code
        self.currency_symbol = currency_symbol

    def __str__(self: object):
        return self.name + " " + self.currency_code + " " + self.currency_symbol

    def format_amount(self: object, amount: float):
        if not amount >= 0:
            raise FormatError('Amount must be a positive integer!')
        try:
            float(amount)
        except:
            raise FormatError('Amount must be a positive integer!')
        return self.currency_symbol + str(("%.2f" % round(amount)))


class Error(Exception):
    pass


class FormatError(Error):
    def __init__(self: object, value: str) -> None:
        self.value = value


test_country = Country("Australia", "AUD", "$")
print(test_country)
print("Formatted amount test: " + test_country.format_amount(100))

test_details = Details()
test_details.add_date("Australia", "2015/10/01", "2015/10/03")
test_details.add_date("Belarus", "2015/10/05", "2015/10/08")
print("Current Country: " + test_details.current_country("2015/10/02"))
print("Locations is empty: " + str(test_details.is_empty()))
