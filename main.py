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
def validate_number(potential_number):
  try:
    return int(potential_number)
  except Exception:
    print('that is not a number')
    return False

console_input = validate_number(input('guess a number between 1 and 10: '))
num_list = [1, 3, 4, 7, 9, 3, 7]
if console_input in num_list:
  print('that number is on the list')
else:
  print('not on the list')

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

# Create a program that generates 100 random numbers and find the frequency of each number.
def gen_num_list(n):
  random_num_list = []
  for num in range(n):
    random_num_list.append(random.randint(-50, 50))
  return random_num_list

def random_occurence_count(input_list):
  count_totals = dict()
  for num in input_list:
    count_totals[num] = count_totals.setdefault(num, 0) + 1
  return count_totals

def print_dictionary_contents(input_dict):
  print(input_dict.items())

print_dictionary_contents(random_occurence_count(gen_num_list(100)))

# Make a program that asks a phone number.
# Make a program that asks the users preferred programming language.
digits = input('what is your phone number?')
language_preference = input('what is your favorite programming language?')
print('your favorite programming language is {0} \n your phone number is {1}'.format(language_preference, digits))

# Make a program that asks the number between 1 and 10. If the number is out of range the program should display “invalid number”.
answer = validate_number(input('pick a number between 1 and 10 '))
if answer is False or answer <= 1 or answer >= 10:
  print('invalid number')
else:
  print('good job! you know some numbers')

# Make a program that asks a password.
def password_match():
  password_input = input('create a password: ')
  confirm = input('re-enter you password: ')
  if password_input == confirm:
    print('password successfully created')
  else:
    print('passwords do not match')

password_match()