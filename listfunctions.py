
lucky_numbers = [7, 1, 9, 3, 4, 2]
friends = ["Niko", "Matheus", "Mr. Weed", "Hello"]
friends.extend(lucky_numbers)
friends.append("Hello")
friends.insert(1, "Hey")
print(friends)
# you can combine lists with list.extend
# list.append adds single item to the list
# you can insert items into a list with list.insert(index value, item)
friends.remove("Hello")
print(friends)
# list.clear clears the lIst
friends.pop()
# list.pop pops an element off
print(friends.index("Mr. Weed"))
# you can see if there is a specific item in the list
print(friends.count("Hello"))
friends.sort()
print(friends)
lucky_numbers.sort()
print(lucky_numbers)
# list.sort sorts the list alphabetically or numerically in ascending order
lucky_numbers.reverse()
print(lucky_numbers)
friends2 = friends.copy()
print(friends2)






