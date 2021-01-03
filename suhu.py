# Judul
print("Konversi Suhu")
print("------------------------------------------")
# Petunjuk pemakaian
print("Cara pemakaian:")
def petunjukCase(urutan, sebelum, sesudah):
    print("Angka " + urutan + " untuk mengubah " + sebelum + " ke " + sesudah)

petunjukCase("1", "Celcius", "Fahrenheit")
petunjukCase("2", "Fahrenheit", "Celcius")


print("------------------------------------------")
# Bikin input untuk memilih case
inputCase = input("Ingin merubah apa? ")

# Statement if untuk memilih case
if int(inputCase) == 1:
    print("Anda akan merubah suhu dari Celcius ke Fahrenheit")
    inputCelcius = input("Masukkan suhu yang akan diubah: ")
    print("Anda akan mengubah suhu " + inputCelcius + " celcius menhjadi fahrenheit")
    fahrenheit = 9/5 * float(inputCelcius) + 32
    print("Jadi, suhu dalam satuan fahrenheit adalah " + str(fahrenheit) + " derajat celcius")
    
elif int(inputCase) == 2:
    print("Anda akan merubah suhu dari Fahrenheit ke Celcius ")
    inputFahrenheit = input("Masukkan suhu yang akan diubah: ")
    print("Anda akan mengubah suhu " + inputFahrenheit + " fahrenheit menjadi celcius")
    celcius = 5/9 * (float(inputFahrenheit) - 32)
    print("Jadi, suhu dalam satuan celcius adalah " + str(celcius) + " derajat celcius")
    
else:
    print("Masukkan angka dengan benar")


    



