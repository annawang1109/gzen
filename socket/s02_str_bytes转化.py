
# byte to str
data_byte = b'abc'
print(str(data_byte,encoding="utf-8"))

# str to byte
data_str = "abc"
print(bytes(data_str, encoding="utf-8"))

def sum(x, y):
    return x+y

def multi(x, y):
    return x*y

data_set = [sum, multi]

print(data_set[0](2,3))