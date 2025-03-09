def cek_angka(a, b, c):
    if a != b and b != c and a != c:
        if a + b == c or a + c == b or b + c == a:
            return True
    return False

print(cek_angka(3, 5, 8))  # True
print(cek_angka(2, 2, 4))  # False
print(cek_angka(1, 2, 4))  # False
