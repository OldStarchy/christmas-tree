def tryParse(num):
    try:
        return True, int(num)
    except:
        return False, 0


size = None


while (size == None):
    suc, num = tryParse(input('enter size: '))
    if (suc):
        size = num


output = ''
for i in range(size):
    line = ''

    for j in range((size - (i + 1))):
        line = line + ' '
    
    for j in range(i + 1):
        line = line + '* '
        
    for j in range((size - (i + 1))):
        line = line + ' '
        
    output = output + line + '\n'

print(output)
