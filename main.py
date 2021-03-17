import random

# Make a Python program that prints your name.
print('romell')

# Make a program that displays the lyrics of a song.
print('I stay out too late \n Got nothing in my brain \n That\'s what people say \n That\'s what people say')

# Make a program that displays several numbers.
def print_random_nums(n):
  for number in range(n):
    print(random.randint(-100, 100))

print_random_nums(5)

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
print_random_nums(3)

# Create a program that generates 100 random numbers and find the frequency of each number.
def gen_num_list(n):
  random_num_list = []
  for num in range(n):
    random_num_list.append(random.randint(-101, 101))
  return random_num_list

def random_occurence_count(input_list):
  count_totals = dict()
  for num in input_list:
    count_totals[num] = count_totals.setdefault(num, 0) + 1
  return count_totals

def print_dictionary_contents(input_dict):
  for key, val in input_dict.items():
    print('{0} : {1}'.format(key, val))

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

# Make a program that lists the countries in the set
def print_list(list_input):
  for elem in list_input:
    print(elem)

clist = ['Canada','USA','Mexico','Australia']
print_list(clist)

# Create a loop that counts from 0 to 100
def count_up(start, exclusive_limit):
  arr = []
  for i in range(start, exclusive_limit):
    arr.append(i)
  return arr

print_list(count_up(0, 101))

# Make a multiplication table using a loop
for i in range(1, 11):
  for j in range(1, 11):
    res = i * j
    print('{0} x {1} = {2}'.format(i, j, res))

# Output the numbers 1 to 10 backwards using a loop
def reverse_list(list_input):
  list_output = []
  if len(list_input) > 1:
    index = len(list_input) - 1
  else:
    index = -1
  while index >= 0:
    list_output.append(list_input[index])
    index -= 1
  return list_output

print_list(reverse_list(count_up(1, 11)))

# Create a loop that counts all even numbers to 10
def gen_odd_or_even(start, exclusive_limit, remainder = 0):
  list_output = []
  for num in range(start, exclusive_limit):
    if num % 2 == remainder:
      list_output.append(num)
  return list_output

print_list(gen_odd_or_even(0, 11))

# Create a loop that sums the numbers from 100 to 200
def sum_list(list_input):
  res = 0
  for num in list_input:
    res += num
  return [res]

print_list(sum_list(count_up(100, 201)))

# Make a program that lists the countries in the set below using a while loop.
def while_list_iter(list_input, rev = False):
  if len(list_input) > 0 and rev is False:
    start = 0
    end = len(list_input) - 1
    incrementor = 1
  else:
    start = len(list_input) - 1
    end = 0
    incrementor = -1
  while start != end:
    print(list_input[start])
    start += incrementor

while_list_iter(clist)

# What‟s the difference between a while loop and a for loop?
# incrementor is not initialized automatically in while LookupError

# Can you sum numbers in a while loop?
# yes

# Can a for loop be used inside a while loop?
# yes

# Make a function that sums the list mylist = [1,2,3,4,5]
sum_list(count_up(1, 6))

# Can functions be called inside a function?
# yes

# Can a function call itself? (hint: recursion)
# yes

# Can variables defined in a function be used in another function? (hint: scope)
# yes by using the keyword 'global'

# Make a program that displays the states in the U.S.
states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
print_list(states)

# Display all states starting with the letter M
m_states = lambda x : x[0].lower() == 'm'

def apply_to_list(input_list, condition):
  list_output = []
  for elem in input_list:
    if condition(elem):
      list_output.append(elem)
  return list_output

print_list(apply_to_list(states, m_states))

# Given the list y = [6,4,2] add the items 12, 8 and 4.
y = [6,4,2]
def add_to_list(list_input, *items):
  list_output = list_input
  for item in items:
    list_output.append(item)
  return list_output

print(add_to_list(y, 12, 8, 4))

# Change the 2nd item of the list to 3.
y[1] = 3
print(y)

# Given a list with pairs, sort on the first element
x = [ (3,6),(4,7),(5,9),(8,4),(3,1)]
first_elem = lambda x : x[0]

def sort_by_elem(list_input, condition):
  return sorted(list_input, key = condition)

print(sort_by_elem(x, first_elem))

# Now sort on the second element
second_elem = lambda x : x[1]
print(sort_by_elem(x, second_elem))

# Create a list of one thousand numbers
list_1000 = gen_num_list(1000)
print(list_1000)

# Get the largest and smallest number from that list
def find_in_list(list_input, condition = 'largest'):
  sorted_list = sorted(list_input)
  if condition == 'largest':
    return sorted_list[-1]
  else:
    return sorted_list[0]

print('the largest number in list is {0}'.format(find_in_list(list_1000)))
print('the smallest number in list is {0}'.format(find_in_list(list_1000, 'smallest')))

# Create two lists, an even and odd one.
print(gen_odd_or_even(0, 25))
print(gen_odd_or_even(0, 25, 1))

# Make a mapping from countries to country short codes
countries = {
  'Afghanistan' : 'AF',
  'Brazil' : 'BR',
  'China' : 'CN',
  'France' : 'FR',
  'Great Britain' : 'GB',
  'Germany' : 'DE',
  'Mexico' : 'MX',
  'Philippines' : 'PH',
  'United States of America' : 'US'
}

# Print each item (key and value)
print_dictionary_contents(countries)