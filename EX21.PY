# Keyword Argument

def phoneNo(country_code, area, first, last):
    return f"{country_code}-{area}-{first}-{last}"

phoneNumber = phoneNo(country_code="+91", area="", first="94913", last="87249")
print(phoneNumber)