
def c():
    """
    Buat program untuk memeriksa apakah sebuah angka merupakan bilangan Armstrong.
    Bilangan Armstrong adalah angka yang sama dengan jumlah pangkat 𝑛-nya, di mana 𝑛 adalah jumlah digit angka tersebut.

    MASUKAN
    n = 153

    KELUARAN
    153 adalah bilangan Armstrong
    """
    
    n = input("Masukkan angka yang ingin dicheck:")
    hasil_check = checkArmstrong(n)
    n = int(n)
    if hasil_check == n:
        print("angka adalah armstrong")
    else:
        print("bukan armstrong")


def checkArmstrong(n):
    n_in_str = str(n)
    n_digit= len(n_in_str)

    sum_pow = sum(int(digit)**n_digit for digit in n_in_str)
    return sum_pow


