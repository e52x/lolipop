import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
# "MASUK KE CODE PYTHON DULU CUY"  
#CONTOH  NANO LOLIPOP.PY DAN ISI NOMOR TARGET DI Parse"
print(geocoder.description_for_valid_number(phonenumbers.parse("Masukan Nomor Hp Taget"),"en"))
print(carrier.name_for_number(phonenumbers.parse(" Masukan Nomor Hp Taget"),"en"))
