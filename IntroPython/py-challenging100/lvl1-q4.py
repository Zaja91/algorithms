# Question: Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number. Suppose the following input is supplied to the program: 34,67,55,33,12,98 Then, the output should be: ['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98')

var = input("Please enter a list of numbers divided by ',' : ")
l = var.split(',')
t = tuple(var.split(','))
print("This is a list :", l)
print("This is the same as tuple:", tuple(var.split(',')))