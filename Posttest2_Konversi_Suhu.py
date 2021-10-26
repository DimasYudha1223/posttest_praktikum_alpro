#Program Menghitung Konversi Suhu Fahrenheit,Reamur,Kelvin ke Celcius
#Rumus yang digunakan sebagai berikut:
#Reamur Ke Celcius = (5/4)*Reamur
#Fahrenheit Ke Celcius = (F-32)*5/9
#Kelvin Ke Celcius = K-273.15

########################################################################################

#Reamur Ke Celcius
print("==========>>>Konversi Suhu Reamur<<<==========")
suhu_reamur = float(input("Silakan Input Suhu Reamur : "))
reamur_ke_celcius = (5/4)*suhu_reamur 
print ("Hasil Nilai Konversi Reamur >>>> : ",reamur_ke_celcius, "°C")

########################################################################################

#Fahrenheit Ke Celcius
print("==========>>>Konversi Suhu Fahrenheit<<<==========")
suhu_fahrenheit = float(input("Silakan Input Suhu Reamur : "))
fahrenheit_ke_celcius = (suhu_fahrenheit-32)*5/9
print ("Hasil Nilai Konversi Fahrenheit >>>> : ",fahrenheit_ke_celcius, "°C")
 
#########################################################################################

#Kelvin Ke Celcius
print("==========>>>Konversi Suhu Kelvin<<<==========")
suhu_kelvin = float(input("Silakan Input Suhu Kelvin : "))
kelvin_ke_celcius = suhu_kelvin-273.15
print ("Hasil Nilai Konversi Kelvin >>>> : ",kelvin_ke_celcius, "°C")
 
