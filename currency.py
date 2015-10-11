s__author__ = 'Hansen'


def convert(amount, home_currency_code, location_currency_code):
    """This function takes an amount of money from
    one currency and converts it to another."""

    if not isinstance(home_currency_code, str) and isinstance(location_currency_code, str) \
            and isinstance(amount, (float, int)):  # Checking that the inputs for the function is in the correct format
        return -1  # if not in the correct format, return -1.

    try:
        import web_utility  # Use the web_utility module.
        url_string = str("https://www.google.com/finance/converter?a=%s&from=%s&to=%s" % (amount,
                         home_currency_code, location_currency_code))
        result = web_utility.load_page(url_string)  # Load the url with specified parameters and return the result URL
    except:  # All errors, return -1.
        return -1
    return float(result[(result.find('<span class=bld>') + 16):(result.find('</span>')-4)])  # Cut the returned URL
    #  so that only the converted amount is returned.


def get_details(country_name):

    if not isinstance(country_name, str):  # Check that the given input is in the str format, otherwise return -1.
        return ""

    try:  # Try and open the file in read only mode.
        with open('currency_details.txt', 'r', encoding="UTF-8") as currency_file:
                content = currency_file.readlines()
    except:  # For all errors, return an empty string.
        return ""

    for line in content:  # Read the content of the file and look for any matches by iterating through each line.
        if country_name.lower() in line.lower():  # Make sure that capitals are not an anomaly.
            currency_file.close()
            return line  # If country found, close the file and return the corresponding line.
    currency_file.close()
    return ""  # If not found, close file and return an empty string.


def write_details(name, code, symbol):  # If needed, open the file and write a new country, code and symbol.

    with open("currency_details.txt", "a", encoding="UTF-8") as currency_file:
        currency_file.write("%s, %s, %s" % (name, code, symbol))
        currency_file.close()
