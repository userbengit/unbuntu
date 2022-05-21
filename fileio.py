# file = open("data.txt", "w")


# file.write("Tran The Sinh \n")
# file.write("aa")
file = open("data.txt", "r")

data = file.read()

print(data)
file.close()


file = open("data.txt", "a")
file.write("c\n")
file.close()


with open("data.txt", "w") as file:
	file.write("Hello world")