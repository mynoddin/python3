#STRING FUNCTIONS 

myStr = "Hello World!"
myStr2 = "loveyou"
myStr3 = "love you"

# Capitalize
print(myStr.capitalize())

#Swap case 
print(myStr.swapcase())

#Get length 
print(len(myStr))

#Replace 
print(myStr.replace("World", "Everyone"))

#
sub = "l"
print(myStr.count(sub))

#Starts_with
print(myStr.startswith('H'))

print(myStr.startswith('el'))

#ends_with
print(myStr.endswith('!'))

print(myStr.endswith("World"))

print(myStr.endswith("World!"))

#Split to list 
print(myStr.split())

#find  - print the first occurance index
print(myStr.find('World'))

print(myStr.find('e'))
#if nothing found will print -1
 
print(myStr.find('f'))

#its also case sensitive
print(myStr.find('w'))

#index - if not found will show error 
print(myStr.index('H'))

#isAlpanumeric 
print(myStr.isalnum())
print(myStr2.isalnum())

print(myStr3.isalnum())

#Is all alphabetic 
print(myStr2.isalpha())

#is all numeric 
print(myStr.isnumeric())

myNum = "234234234"
print(myNum.isnumeric())