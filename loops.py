# loops 
people = ['John', 'Sara', 'Tim', 'Bob']

#For loops 

for person in people:
    print('Current Person: ', person)

# Iterate by seq index: 
for i in range(len(people)): 
    print('Current people : ', people[i])

# for printing sequence only
for i in range(0, 10):
    print(i)

#While loop

count  = 0
while count  <= 10:
    print("Count: ", count)
    if count == 5:
        break
    count = count + 1

'This program instructs to use loops in python3'