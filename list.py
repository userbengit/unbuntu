# colors = ["red", "green", "blue"]

# print(colors)
# print(colors[0])

# print(len(colors))

# colors.append("yellow")

# print(colors)

# for i in range(4):
# 	print(colors[i])

# print(len(colors))

# print(colors[len(colors)-1])

colors = ["red", "green", "blue", "yellow"]

print(colors)

if "greenaa" in colors: # validation
	colors.remove("greenaa")
else:
	print("not exist")

print(colors)



try:
	colors.remove("greenaa")
except:
	print("not exist")

print(colors)


colors.pop() # remove last element
print(colors)

colors.insert(0, "black")
print(colors)



colors.insert(1, "purple")
print(colors)
print(colors[1])

print(colors.index("redd"))
#find
try:
	print(colors.index("red"))
except:
	print("Not exist")

red_index = []

for i in range(len(colors)): #find index of "red" in list
	if colors[i] == "red":
		red_index.append(i)

print(red_index)

#find number of occurance of "red"


print(colors.count("red"))

print("How many times 'red' occurs: " + str(colors.count("red")))


a = [1,2,10,4,5,0,6]


a.sort()

print(a)


a[0] = "Tran Sinh"



print(a)