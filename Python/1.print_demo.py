print("Hello World!")

# Comment

# Variables ->
a = 3
print(a)
print(type(a))
str = "Hello World!"
print(str)
print(type(str))

b, c, d = 5, 7.2, "Great"
print(b, c, d)

#print("Value is "+b) #TypeError: can only concatenate str (not "int") to str
print("Value is ", b)

print("{} {}".format("Value is ", b))
print(type(b), type(c), type(d))
