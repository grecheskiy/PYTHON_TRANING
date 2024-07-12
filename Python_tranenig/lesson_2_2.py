text = """Два кота, два друга, шли как-то по тропинке в лесу. Шли два кота, шли, пока не ушли с тропинки и не дошли
до деревни. Два кота решили не идти дальше и остаться жить в деревне 3 3 3 3 3"""
import re

d = dict()
s1 = re.sub(r"\d+", "", text, flags=re.UNICODE)
print(s1)
words = re.findall(r'\b\w+\b', s1.lower())
for word in words:
    if word in d:
        d[word] = d[word] + 1
    else:
        d[word] = 1

mark = sorted((value, key) for (key, value) in d.items())
sortdict = dict([(k, v) for v, k in mark])

list2 = []
for k in sortdict:
    half = (k, d[k])
    list2.append(half)
a = list(reversed(list2))
print(a)

