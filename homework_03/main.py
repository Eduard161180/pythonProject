
def p(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


for d in range(1, 100):
    if p(d):
        print(d, end=' ')


t = 'Миру Мир!'
str_t = set(t)
res = ''
for x in str_t:
    if t.count(x) == 1:
        res += x
print(res)