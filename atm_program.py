import random
import datetime
from customer import Customer

atm = Customer(id)

while True:
    print('Pin = 1234')
    id = int(input('Masukkan pin anda: '))
    trial = 0

    while (id != int(atm.checkPin()) and trial < 3):
        id = int(input('Pin anda salah. Silakan Masukkan lagi: '))
        trial += 1

        if trial == 3:
            print('Error. silakan ambil kartu dan coba lagi..')
            exit()

    while True:
        print('\nSelamat datang di ATM Coba Coba..')
        print(' 1 - Cek Saldo \n 2 - Debet \n 3 - Simpan \n 4 - Ganti Pin \n 5 - Keluar ')

        selectmenu = int(input('\nSilakan pilih menu: '))

        if selectmenu == 1:
            print('\nSaldo anda sekarang: Rp. ',
            str(atm.checkBalance()) + '\n')
            print('* - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - *')

        elif selectmenu == 2:
            nominal = float(input('Masukkan nominal saldo: '))
            verify_withdraw = input('Konfirmasi: Anda akan melakukan debat dengan nominal berikut ? y/n ' + str(nominal) + ' ')

            if verify_withdraw == 'y':
                print('Saldo awal anda adalah: Rp. ' + str(atm.checkBalance()) + '')
            else:
                break
                
            if nominal < atm.checkBalance():
                atm.withdrawBalance(nominal)
                print('Transaksi debet berhasil!')
                print('Saldo sisa sekarang: Rp. ' + str(atm.checkBalance()) + '\n')
                print('* - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - *')

            else:
                print('Maaf. saldo anda tidak cukup untuk melakukan debet!')
                print('Silakan lakukan penambahan nominal saldo\n')
                print('* - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - *')

        elif selectmenu == 3:
            nominal = float(input('Masukkan nominal saldo: '))
            verify_withdraw = input('Konfirmasi: Anda akan melakukan debat dengan nominal berikut ? y/n ' + str(nominal) + ' ')

            if verify_withdraw == 'y':
                atm.depositBalance(nominal)
                print('Saldo anda sekarang adalah: Rp.' + str(atm.checkBalance()) + '\n')
                print('* - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - *')

            else:
                break

        elif selectmenu == 4:
            verify_pin = int(input('Masukkan pin Anda: '))

            while verify_pin != int(atm.checkPin()):
                print('Pin Anda salah, silakan masukkan pin: ')

            updated_pin = int(input('Silakan masukkan pin baru: '))
            print('pin anda berhasil diganti!')

            verify_newpin = int(input('Coba masukkan pin baru: '))

            if verify_newpin == updated_pin:
                print('Pin baru Anda sukses!\n')
                print('* - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - *')

            else:
                print('Maaf, pin Anda salah!\n')
                print('* - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - *')

        elif selectmenu == 5:
            print("Resi tercetak otomatis saat anda keluar. \nHarap simpan tanda terima ini sebagai bukti transaksi anda.")
            print("\tNo. Record: ", random.randint(100000, 1000000))
            print("\tTanggal : ", datetime.datetime.now())
            print("\tSaldo akhir : ", atm.checkBalance())
            print("Terima kasih telah menggunakan ATM Coba - coba!")
            exit()

        else:
            print('Error. Maaf, menu tidak tersedia\n')
            print('* - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - *')

