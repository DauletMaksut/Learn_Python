# '[0-9]+ plus gives as number more than with one digit, if there are no + 10 will be splitted to 1 and 0
import re
text = 'Some 2 numbers to check if i understand task 1 and 232 and 10'
res  = re.findall('[0-9]+', text)
print(res)
res  = re.findall('[num]+', text)
print(res)
text1 = 'me daulet.maksut@nu.edu.kz ssd name daulet maksut daulet.maksut@'
email = re.findall('^me (\S+@\S+)', text1)
print(email)
extend = re.findall('@([^ ]*)', text1)
print(extend)