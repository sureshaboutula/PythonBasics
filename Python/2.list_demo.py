values = [1, 2, 4.5, 3+2j, True, "Test"]

print(values)
print(values[0])
print(values[-1])
print(values[1:5])
print(values[1:5:2])
print(values[1::2])

values.append(25)
print(values)

values.insert(3, 10)
print(values)

values[-2] = "Suresh"
print(values)

del values[0]
print(values)