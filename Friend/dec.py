import sys

# Create Variables
int_list = []
reset = ""

# Input for file 1
f1 = str(sys.argv[1])

# Open the File 1
fo_1 = open(f1)
text = fo_1.read()

# Input for file 2
f2 = str(sys.argv[2])
fo_2 = open(f2, "w")

# Decryption process
int_list = [72, 101, 108, 108, 111, 32, 101, 118, 101, 114, 121, 111, 110, 101, 32, 33, 33, 33, 33, 44, 32, 84, 104, 105, 115, 32, 99, 111, 100, 101, 32, 105, 115, 32, 119, 111, 114, 107, 105, 110, 103, 32, 33, 46, 10]
for i in int_list:
	reset = reset + chr(i)

fo_2.write(str(reset))
fo_2.close()
