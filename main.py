#  __    __  ____    __    ____       _  _    
# |  |  |  | \   \  /  \  /   /      | || |   
# |  |__|  |  \   \/    \/   / ______| || |_  
# |   __   |   \            / |______|__   _| 
# |  |  |  |    \    /\    /            | |   
# |__|  |__|     \__/  \__/             |_|   
#                                             

# Unique values list
myUniqueList = []

# Rejected values because they are not uniques
myLeftovers = []

# Add value to myUniqueList only if is not already in the list
def AddUniqueValue(value):
	if value not in myUniqueList:
		myUniqueList.append(value)
	else:
		AddRejectedValue(value)

# Add any value to myLeftovers
def AddRejectedValue(value):
	myLeftovers.append(value)


# Add value 1, should be added
AddUniqueValue(1)
print("uniques ", myUniqueList)
print("rejected", myLeftovers)
print()

# Add value "1", should be added
AddUniqueValue("1")
print("uniques", myUniqueList)
print("rejected", myLeftovers)
print()

# Add value False, should be added
AddUniqueValue(False)
print("uniques", myUniqueList)
print("rejected", myLeftovers)
print()

# Add value True, should be not added because True is equal to 1
AddUniqueValue(True)
print("uniques", myUniqueList)
print("rejected", myLeftovers)
print()

# Add value 1, should be rejected and added to myLeftovers
AddUniqueValue(1)
print("uniques", myUniqueList)
print("rejected", myLeftovers)
print()