Max = 1000
def URL(string):
    
    string = string.strip()      # remove space
    i = len(string)     # length
    
    count_space = string.count(' ')         # count spaces
    new_length = i + count_space * 2        # new length

    if new_length > Max:            # max length
        return -1

    index = new_length - 1          # point at end
    string = list(string)           # convert into list

    for f in range(i-2, new_length-2):
        string.append('0')

    for j in range(i-1, 0, -1):        
        if string[j] == ' ':
            string[index] = '0'
            string[index - 1] = '2'
            string[index - 2] = '%'
            index = index - 3
        else:
            string[index] = string[j]
            index -= 1
    return ''.join(string)
    
    

string = "Mr John Smith  "
s = URL(string)
print(s)
