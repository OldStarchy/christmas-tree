def tryParse(num):
    try:
        return True, int(num)
    except:
        return False, 0


# initialize
size = None


# prompt user for input  / INPUT
while (size == None):
    suc, num = tryParse(input('enter size: '))
    if (suc):
        size = num


# run / process data     / OUTPUT
output = ''
for i in range(size): # loop over each line
    line = ''

    for j in range((size - (i + 1))):
        line = line + ' '
    
    for j in range(i + 1): # loop over each star in the line
        line = line + '* '
        
    for j in range((size - (i + 1))):
        line = line + ' '
        
    output = output + line + '\n'

print(output)
