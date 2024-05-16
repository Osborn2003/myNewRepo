import phonenumbers
from phonenumbers import geocoder
phone_number1 = phonenumbers.parse(input())
phone_number2 = phonenumbers.parse("+2348067511163")
phone_number3 = phonenumbers.parse("+2348157559963")
phone_number4 = phonenumbers.parse("+2349060776841")
phone_number5 = phonenumbers.parse("+2348122966112")

print("\nPhone Numbers Location\n")
print(geocoder.description_for_number(phone_number1, "en"));
print(geocoder.description_for_number(phone_number2, "en"));
print(geocoder.description_for_number(phone_number3, "en"));
print(geocoder.description_for_number(phone_number4, "en"));
print(geocoder.description_for_number(phone_number5, "en"));