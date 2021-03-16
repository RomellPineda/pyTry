import random

# Make a Python program that prints your name.
print('romell')

# Make a program that displays the lyrics of a song.
print('I stay out too late \n Got nothing in my brain \n That\'s what people say \n That\'s what people say')

# Make a program that displays several numbers.
def gen_random_nums(n):
  for number in range(n):
    print(random.randint(-100, 100))

gen_random_nums(5)

# Make a program that solves and shows the summation of 64 + 32.
def print_sum(a, b):
  res = a + b
  print('the sum of {0} and {1} is {2}'.format(a, b, res))

print_sum(64, 32)

# Make a program that displays your favourite actor/actress.
def fav_actor():
  print('john krasinski')

fav_actor()

# Try to print the word 'lucky' inside s.
s = 'My {0} number is {1}'.format('lucky', 4.13)
print(s)

# Try to print the day, month, year in the form “Today is 2/2/2016”.
s = 'Today is %d/%d/%d' % (3,15,2021)
print(s)

# Try the replace program
s2 = s.replace('2021', '3021')
print(s2)

# Can a string be replaced twice?
s3 = s2.replace('15', '51')
print(s3)

# Does replace only work with words or also phrases?
s4 = s.replace('Today is', 'We live in a twilight world')
print(s4)

# Find out if string find is case sensitive
print(s4.find('Twilight'))
#yes

# What if a query string appears twice in the string?
s5 = 'one two one twoo'
print(s5.find('one'))
#first

# Write a program that asks console input and searches for a query.
console_input = input('pick a number between 1 and 10: ')
num_list = [1, 3, 4, 7, 9]
if console_input in num_list:
  print('that number is on the list')
else:
  print('that number is not on the list')

# Create a list of words and join them, like the example above.
separator = ' '
words = ['no', 'sleep', 'till', 'brooklyn']
phrase = separator.join(words)
print(phrase)

# Can you split a string this string?: World,Earth,America,Canada?
test = 'World,Earth,America,Canada'
res = test.split(',')
print(res)

# Given an article, can you split it based on phrases?
article_split = phrase.split('sleep till')
print(article_split)

# Make a program that prints 3 random numbers.
gen_random_nums(3)

