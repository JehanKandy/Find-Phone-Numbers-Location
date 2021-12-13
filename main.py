import  phonenumbers
print("******main.py and p_numbers.py file must be in the same folder ******")
from p_numbers import number

from phonenumbers import geocoder


#find your country code using phone number

ch_number = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_number, "en"))

#find service privader using of your phone number

from phonenumbers import carrier

service_p = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_p, "en"))
