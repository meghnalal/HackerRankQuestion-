roman= {"I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "XL": 40,
        "L": 50,
        "XC": 90,
        "C": 100,
        "CD": 400,
        "D": 500,
        "CM": 900,
        "M": 1000}

s = 1040
res = ''

for key in reversed(roman.keys()):
            result = s // roman[key]
            res += key * result
            s -= roman[key] * result


print(res)

''' maybe better solution'''
roman = [("M", 1000),
         ("CM", 900),
         ("D", 500),
         ("CD", 400),
         ("C", 100),
         ("XC", 90),
         ("L", 50),
         ("XL", 40),
         ("X", 10),
         ("IX", 9),
         ("V", 5),
         ("IV", 4),
         ("I", 1)]

s = 1040
res = ''

for symbol, value in roman:
    quotient = s // value
    res += symbol * quotient
    s -= value * quotient

print(res)  # Output: 'MXL'

'''try using not hash table'''


