#basic python

import datetime
today = datetime.date.today()
print("Today date is :", today)
print (' ')

'''Loopoing - control flow in python '''
#WHILE
i = 0
while (i <= 5):
    print ('The value of while loop :', i) 
    if(i == 5):
        break
    else:
        i += 1
#FOR
for i in range(5):
      print ('This is for loop:',i)
      
for j in range(0,10,2):
    print ('for loop skips 2 elem:',j) 
print('---------------------------------------------------------')

''' Multiline comment -
This is LIST examples '''

primes = list()
rmv = list()
alphabets = ['A', 'B', 'C']
print('This is list:', alphabets)
print('This is 1st element :', alphabets[0])

# Check if element exist and append
if 'D' not in alphabets:
    alphabets.append('D')
    print('This is list:', alphabets)
    
nxt = ['E','F','G']
alphabets.extend(nxt)
alphabets.extend(('I','J'))
print('This is list with nxt elem:', alphabets)

abcd = alphabets[0:4]
print('This is list with sliced elem:', abcd)

rmv = alphabets.pop(8)
print('remove with position using popped:', rmv,'. This is new list:', alphabets)

alphabets.remove('I')
print('remove (I) with value, new list:', alphabets)

print('This is empty prime list:', primes)

''' Multiline comment -
This is  TUPLE examples '''
tup = ('red','blue','green')

print ("This is tuple: ", tup)
print ("This is 1st elem in tuple: ", tup[0])
print ("Slicing  tuple: ", tup[1:2], "note the comma")





