# CONDITIONALS

x = 7

# BASIC If 
if x < 6: 
    print("This is true")

#If Else 

if x < 6: 
    print("This is true 1 ")
else:
    print('This is false')

#Elif
color = 'red'
if color == 'red':
    print('Color is red')
elif color == 'blue':
    print("Color is blue")
else:
    print("Color is not red of blue")

# Nested if
if color == 'red':
    if x < 10:
        print("Color is red and x is less then 10")

# Lofical Operators 
if color == 'red' and x <10:
    print("Color is red and x is less then 10")
