alphabets = []
for  i in range(65,91):
    alphabets = alphabets + list(chr(i)) # list can be concatenated with list datatype not string datatype
for  i in range(97,123):
    alphabets = alphabets + list(chr(i))
print(alphabets)