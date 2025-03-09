def cek_digit_belakang(a, b, c):
    if (a % 10 == b % 10) or (a % 10 == c % 10) or (b % 10 == c % 10):
        return True
    return False

try:
    a, b, c = map(int, input("Masukkan tiga angka: ").split())
    print(cek_digit_belakang(a, b, c))
except ValueError:
    print("Input harus berupa tiga angka yang dipisahkan dengan spasi.")
