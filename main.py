# 16
def tekshir(son):
    if son % 2 == 0 and son % 3 == 0:
        return "Mos "
    else:
        return "Mos emas"


res = tekshir(6)
print(tekshir)

# 17
def tekshir(matn):
    for belgi in matn:
        if belgi.isdigit():
            return "Raqam bor"
    return "Raqam yoq"



print(tekshir("salom"))
print(tekshir("dunyo1"))

# 19
def tekshirish(parol):
    if parol.isalpha():
     return "Faqat harf"

    return "Boshqa belgilar bor"

text = "sfgeydgugefu3545"
res = tekshirish('retey')
print(res)


# 20
def qabul(ism):
    if ism.lower():
        return "Ism notogri qilingan"

    return "To‘g‘ri yozilgan"

text = "regwerUYGEYDG"
res = qabul('Ali')
print(res)
