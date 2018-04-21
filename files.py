#Open a file
# "w" is write mode  
fo = open("test.txt", 'w')

#get some info 

print("Name : ", fo.name, "\n")

print("Is Closed: ", fo.closed) 
print("Opening Mode: ", fo.mode)

fo.write("I have started to like python")
fo.write(" and JavaScript.\n")

# close the file 
fo.close() 

print("\nIs Closed: ", fo.closed)

# "a" is for append mode 
fo = open("test.txt", "a")
fo.write("I also like Java, C/C++. ")
fo.close()

#read from file 

fo = open("test.txt", 'r+')
test = fo.read()
print(test)
fo.close()

# create file
# "w+" is creating new file with writing mode   
fo = open("test2.txt", "w+")
fo.write("This is my new file") 
fo.close() 


