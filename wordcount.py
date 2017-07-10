filename = "test.txt"
the_file = open(filename)

the_dict = {}

for line in the_file:
    line = line.rstrip()
    words = line.split(' ')
    
    for word in words:
        the_dict[word] = the_dict.get(word, 0) + 1
        
#print the_dict

for each, count in the_dict.items():
    print "{} {}".format(each, count)



