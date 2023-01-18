from random import randint
# http://a0767593.xsph.ru/payload.php
readed = open("bots.txt", "r").read()
file = open("bots.txt", "w")
file.write(readed)
for i in range(10000):
    file.write(f"http://a{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}.xsph.ru/payload.php\n")