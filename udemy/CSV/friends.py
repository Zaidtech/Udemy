# ask the user for a list of 3 friends
# For each friend we'll tell the user weather they are nearby
# for each nearby friends we'll save their name to ' nearby_friends.txt'
friend = []
friends = input("Enter your friends name ").split(" ")
print(friends)
people = open('people.txt', 'r')
people_nearby = [line.strip(" ") for line in people.readlines()]  # list of line 1 ,2,3,4...
print(people_nearby)
people.close()
friends_set = set(friends)
people_nearby_set = set(people_nearby)

friends_set_nearby = friends_set.intersection(people_nearby_set)
nearby_friend_file = open('nearby_friends.txt', 'w')

for friend in friends_set_nearby:
    print(f'{friend} is nearby!')
    nearby_friend_file.write(f'{friend} \n')

nearby_friend_file.close()
