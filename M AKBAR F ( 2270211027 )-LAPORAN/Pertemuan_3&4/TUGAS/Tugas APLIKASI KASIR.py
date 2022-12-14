print("=============== PROGRAM KASIR LUX STORE ===============")

print(" SELAMAT DATANG DI LUX STORE")
print(" TOP UP GAME BY LUX")
print(" BUKA 24 JAM")
print(" BEST SERVICE & BEST PRICE")
print(" PROSES CEPAT SEPERTI KILAT")
print("======================================")

import time

tanggal = time.strftime (" %d-%m-%y - %H:%M:%S ")
print(tanggal)
print(type(tanggal))

Nama_pembeli=str(input("Masukkan nama Pembeli: "))
Nickname=str(input("Masukan Nickname: "))
user_ID=str(input("Masukan user ID: "))
alamat=str(input("Masukan Alamat anda: "))
NO_telepon=str(input("Masukan nomor telepon anda: "))

def pilihDiamonds():
   global totaldiamonds
   global bonus
   global diamonds
   print ("\n================= Pilih Item =================")
   print("1. 299 diamonds + 15 bonus- Rp 75000")
   print("2. 450 diamonds + 20 bonus- Rp 150000")
   print("3. 1200 diamonds + 50 bonus- Rp 300000")
   print("4. 1600 diamonds + 302 bonus- Rp 380000")
   print("5. 1860 diamonds + 335 bonus- Rp 490000")
   print("6. 3099 diamonds + 589 bonus- Rp 805000")
   print("7. 6509 diamonds + 1218 bonus- Rp 1700000")
   print("8. 7740 diamonds + 1548 bonus- Rp 2050000")
   print("9. 15480 diamonds + 3096 bonus- Rp 4000000")
   print("10. 23220 diamonds + 4644 bonus- Rp 6000000")

   nomor=int(input("Masukan Pilihan: "))
   
   if nomor==1:
       totaldiamonds=75.000
       print (" 314 diamonds = Rp", totaldiamonds)
       diamonds=("314 diamonds")
   elif nomor==2:
       totaldiamonds=150.000
       print (" 470 diamonds = Rp", totaldiamonds)
       diamonds=("470 diamonds")
   elif nomor==3:
       totaldiamonds=300.000
       print (" 1250 diamonds = Rp", totaldiamonds)
       diamonds=("1250 diamonds")
   elif nomor==4:
       totaldiamonds=380.000
       print (" 1902 diamonds = Rp", totaldiamonds)
       diamonds=("1902 diamonds")
   elif nomor==5:
       totaldiamonds=490.000
       print (" 2195 diamonds = Rp", totaldiamonds)
       diamonds=("2195 diamonds")
   elif nomor==6:
       totaldiamonds=805.000
       print (" 3688 diamonds = Rp", totaldiamonds)
       diamonds=("3688 diamonds")
   elif nomor==7:
       totaldiamonds=1700.000
       print (" 2288 diamonds = Rp", totaldiamonds)
       diamonds=("2288 diamonds")
   elif nomor==8:
       totaldiamonds=2050.000
       print (" 9288 diamonds = Rp", totaldiamonds)
       diamonds=("9288 diamonds")
   elif nomor==9:
       totaldiamonds=4000.000
       print (" 18.576 diamonds = Rp", totaldiamonds)
       diamonds=("18.576 diamonds")
   elif nomor==10:
       totaldiamonds=6000.000
       print (" 27.864 diamonds = Rp", totaldiamonds)
       diamonds=("27.864 diamonds")   
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      pilihDiamonds()


def metodepembayaran():
    global metodepembayaran
    print("\n=============== Pilih Metode Pembayaran ===============")
    print("1. Gopay")
    print("2. OVO")
    print("3. DANA")
    print("4. TELKOMSEL")
    print("5. SHOPEE PAY")

    nomor=int(input("masukan pilihan : "))

    if nomor==1:
        metodepembayaran=("Gopay")
        print ("METODE PEMBAYARAN MELALUI GOPAY")
    elif nomor==2:
        metodepembayaran=("OVO")
        print ("METODE PEMBAYARAN MELALUI OVO")
    elif nomor==3:
        metodepembayaran=("DANA")
        print ("METODE PEMBAYARAN MELALUI DANA")
    elif  nomor==4:
        metodepembayaran=("TELKOMSEL")
        print ("METODE PEMBAYARAN MELALUI TELKOMSEL")
    elif  nomor==5:
        metodepembayaran=("SHOPEE PAY")
        print ("METODE PEMBAYARAN MELALUI SHOPEE PAY")
    else : 
        print("pilihan tidak ada, mohon sesuaikan pilihan yang tersedia")
        metodepembayaran()

pilihDiamonds()
totalsemua = totaldiamonds

metodepembayaran()
metode_pembayaran = (" ")

print(" Total harus dibayar : Rp" , totalsemua)
uang=int(input("DI Bayar: Rp "))

print("\n===============================================")
print("========== S T R U K L U X S T O R E ==========")
print("===============================================")

print("tanggal\t\t        :",tanggal)
print("Nama\t\t        :", Nama_pembeli)
print("Nickname\t\t:", Nickname)
print("user ID\t\t        :", user_ID)
print("alamat\t\t        :", alamat)
print("pembayaran\t\t:",metodepembayaran)
print("diamonds\t\t:", diamonds)
print("nomer telepon\t\t:", NO_telepon)
print("Harga\t\t        : Rp", totalsemua)
print("dibayar\t\t        : Rp", uang)
print("===============================================")
print("TERIMA KASIH SUDAH MEMBELI DI LUX STORE")
print("===============================================")