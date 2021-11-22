import sys
# Input first file name
f1 = str(sys.argv[1])
fo_1 = open(f1)
text = fo_1.read()

# Input the 2nd file name
f2 = str(sys.argv[2])
fo_2 = open(f2, "w")

# Encryption Process
ASCII_values = []
for character in text:
   ASCII_values.append(ord(character))

fo_2.write(str(ASCII_values))
fo_2.close()
