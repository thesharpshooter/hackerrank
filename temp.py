from collections import Counter
string = "asdadadada"
c = Counter(string)
print c.items()
print frozenset(c.items())
