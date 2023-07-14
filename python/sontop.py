import random

n = int(input("n="))
x = []
for i in range(1, n + 1):
    x.append(i)

compyuter = random.choice(x)
a = 0

while True:
    a += 1
    y = int(input("y="))
    
    if y == compyuter:
        print("Siz kompyuter uylagan soni topdingiz!")
        break
    else:
        print("Qayta urinib kuring.")
        
    compyuter = random.choice(x)

print(f"Siz {a} ta urinishda topdingiz.")
