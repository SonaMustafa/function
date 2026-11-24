def check_password(password):
    errors = []

    if len(password) < 8:
        errors.append("ən azı 8 simvol olmalıdır")

    boyuk_herfler = "ABCÇDEƏFGĞHİJKQLMNOÖPRSŞTUÜVWXYZ"
    kicik_herfler = "abcçdeəfgğhxıijkqlmnoöprsştuüvwxyz"
    reqemler = "0123456789"

    boyuk = 0
    kicik = 0
    reqem = 0
    bosluq = 0

    for i in password:
        if i in boyuk_herfler:
            boyuk = 1
        if i in kicik_herfler:
            kicik = 1
        if i in reqemler:
            reqem = 1
        if i == " ":
            bosluq = 1

    if boyuk == 0:
        errors.append("ən azı 1 böyük hərf olmalıdır")
    if kicik == 0:
        errors.append("ən azı 1 kiçik hərf olmalıdır")
    if reqem == 0:
        errors.append("ən azı 1 rəqəm olmalıdır")
    if bosluq == 1:
        errors.append("boşluq olmamalıdır")

    return errors


cehd = 0
qebul = 0

while cehd < 3:
    sifre = input("Şifrəni daxil edin: ")
    cehd = cehd + 1
    problems = check_password(sifre)

    if len(problems) == 0:
        print("Şifrə qəbul olundu")
        qebul = 1
        break
    else:
        for problem in problems:
            print(problem)

if qebul == 0:
    print("Cəhdlər bitdi")