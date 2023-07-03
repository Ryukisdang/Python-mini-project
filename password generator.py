from itertools import product
import string


min_len = int(input("enter minimum length of  password: "))
max_len = int(input("enter maximum length of password: "))
counter = 0
character = string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation

file_open = open("wordlist.txt",'w')


for i in range(min_len,max_len+1):
   for j in product(character,repeat=i):
      word = "".join(j)
      file_open.write(word)
      file_open.write('\m')
      counter+=1
print("wordlist of {} passwords created".format(counter))