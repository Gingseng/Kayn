bytes = b"\x18\x86f`\x00\x18x\x18\x18\x18x\xe6\x98"

print (type(bytes))

translating = bytes.decode("utf-8")
print (type(translating))
print (translating)