# 2-Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# Предикату можно заменить на понятие "бит".
# Должна получиться таблица истинности.

print("{:10} {:10} {:10} {:10}".format("x", "y", "z", "result"))
print("_______________________________________")
print()
for x in range(2):
    for y in range(2):
            for z in range(2):
                if (not (x or y or z) == (not x and not y and not z)) == 1:
                    print("{:10} {:10} {:10} {:10}".format(str(bool(x)), str(bool(y)), str(bool(z)), 'True'))
                else:
                    print("{:10} {:10} {:10} {:10}".format(str(bool(x)), str(bool(y)), str(bool(z)), 'False'))


