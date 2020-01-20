friends = ['kevin', 'karen', 'jim', 'oscar', 'toby']
numbers = [4, 5, 6, 7, 8, 9]

print(friends)
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[-1])
print(friends[-2])
print(friends[-3])
print(friends[1:])
print(friends[1:3])
print(friends[:3])
friends[1] = 'mike'
print(friends[1])
# for friend in friends: print(friend)

friends.extend(numbers) # append two array together
friends.append('creed') # append at the end of the list
friends.insert(1, 'kelly')
friends.remove('jim')
print(friends)

# friends.clear()
friends.pop() # remove the last element
print(friends)

print(friends.index('kevin'))
# print(friends.index('none')) # ValueError not in the list

print(friends.count('toby')) # print how many toby

friends = ['kevin', 'karen', 'jim', 'oscar', 'toby']

friends.sort()
print(friends)
print(len(friends))

numbers = [4, 15, 26, 57, 84, 9]

numbers.reverse()
print(numbers)
numbers.sort()
print(numbers)

friends_copy = friends.copy()
print(friends_copy)
