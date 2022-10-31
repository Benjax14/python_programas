from gettext import find


myStr = "Hello World"

print(type(dir(myStr)))

print(myStr.upper())
print(myStr.lower())
print(myStr.swapcase())
print(myStr.capitalize())

print(myStr.replace('Hello', 'bye'))
print(myStr.count("l"))
print(myStr.startswith("Hola"))
print(myStr.endswith("World"))

print(myStr.split())
print(myStr.find("o"))

print(len(myStr))
print(myStr.index("e"))

print(myStr.isalnum())
print(myStr.isalpha())

print(myStr[4])
print(myStr[-1])

print("Hice un " + myStr)