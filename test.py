# list
a = [1, 1, 2, 3]

# set
b = {1, 1, 2, 3}

# tuple
c = (1, 1, 2, 3)

# dictionary
d = {"A": "a", "B": "b"}

data = " a : {}\n b : {}\n c : {}\n d : {}"
print(data.format(a, b, c, d["A"]))
print()
for key, value in d.items():
    print(f"key : {key}, value : {value}")
