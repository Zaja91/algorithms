# Passed by reference
def change(value):
    value = 2
    return value

val = 1
val2 = change(val)

print(val2)
print(val) #1