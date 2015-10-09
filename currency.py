__author__ = 'Hansen'


def convert(amount, home_currency_code, location_currency_code):

    if not isinstance(home_currency_code, str) and isinstance(location_currency_code, str) \
            and isinstance(amount, (float, int)):
        return int(-1)

    try:
        import web_utility
        url_string = str("https://www.google.com/finance/converter?a=%s&from=%s&to=%s" % (amount,
                         home_currency_code, location_currency_code))
        result = web_utility.load_page(url_string)
    except:  # All exceptions
        return int(-1)
    converted_amount = float(result[(result.find('<span class=bld>') + 16):(result.find('</span>')-4)])
    return converted_amount


def get_details(country_name):

    if not isinstance(country_name, str):
        return ""

    try:
        in_file = open('currency_details.txt', 'r', encoding="UTF-8")
    except:  # All exceptions.
        return ""

    content = in_file.readlines()
    for line in content:
        if country_name.lower() in line.lower():
            return line
    in_file.close()
    return ""


print(convert("100", "AUD", "JPY"))
print(get_details("Japan"))

"""

def write_details(name, code, symbol):

    outfile = open("currency_details.txt", "w", encoding="UTF-8")
    infile = open("currency_details.txt", "r", encoding="UTF-8")
    content = infile.readline()
    for line in content:
        print('r')
        if line > name:
            outfile.write('%s,%s,%s' % (name, code, symbol))
            return print('r')
    outfile.close()

def file_length():
    in_file = open("currency_details.txt", "r", encoding="UTF-8")
    total = 0
    for line in in_file:
        number = int(line)
        total += number
    print(total)
    in_file.close()

"""
