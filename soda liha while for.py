import random

s = []

for i in range(10):
    s.append(random.randint(100,200))

st = 0
sum_soda = 0 
sum_liha = 0


while st < len(s):
    if s[st] % 2 == 0:
        sum_soda += s[st]
    st += 1

for i in s:
    if not i % 2 == 0:
        sum_liha += i


print(s, sum_soda, sum_liha)


