# CONDITIONALS
age = 19
isBirthday = True

if age >= 21:
    print('you can drink')
    if isBirthday:
        print('free drink!')
elif age >= 18:
    print('you can enter - no drinks')
else: 
    print('go home')

# TERNARY OPERATORS
#something we want to do => if condition is met => else do something else
msg = ('go vote') if (age >= 18) else 'go play'

# BOOLEAN OPERATIONS
#and, or, not work the same as $$ || !
x = 102
x == 103 or x > 100 #True

age = 66
if age < 10 or age >= 65:
    print('YOUR TICKET IS 5$')
else:
    print('YOUR TICKET IS 10$')

    # falsy: 0, 0.0, False, None => equivalent to null in js, [] => empty list, {} => empty dictionary, set() => empty set
    #truthy: everything else

#LOOPING
##while loops
num = 0
while num <= 100:
    if num == 50:
        break #use to break out of a loop
    print(num)
    num += 10
print('all done')
    #no ++ or --
##simple guessing game
target = 37
guess = None
guess = input("enter your guess: \n") #a way to get input from terminal
while guess != target:
    guess = input('guess again: \n')
    if guess == 'q' or guess == 'quit':
        break
    guess = int(guess) #parses from string to integer
print('You found it!')
##for loops => works like js for...of loop
for snack in ['Peanut', 'Twizzler', 'Mars Bar']:
    print('I ate a', snack)
for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    print(char)
##range => a way to generate numbers
for n in range(10):
    print(n) #prints n 10 times (0-9)
list(range(10)) #creates list with items 0-9; creating a range on its own will not automatically print those values
##can also pass in a start, stop and interval
list(range(1,10,2)) #[1,3,5,7,9]
list(range(10,0,-1)) #[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# FUNCTIONS
def greet(person):
    return f'Hello there, {person}'
greet('rane') #execute func => if a value is not explicitly returned, func will return None
def divide(a,b):
    if type(a) is int and type(b) is int:
        return a/b
    return 'a & b must be integers' #we don't have to explicitly type else much like in js
##function arguments => providing too many or too few yields an error
def three_things(a,b,c):
    print('hi')
    #args are REQUIRED so! three_things(1,2,3) => works perfectly fine || three_things(1) => ERROR || three_things(1,2,3,4) => ERROR
#can pass in args by name
def send_email(to_email, from_email, subject, body):
    email = f"""
        to: {to_email}
        from: {from_email}
        subject: {subject}
        -------------------------------------
        body: {body}
    """
    return email

#send_email(subject="hi", to_email="ranepours@gmail.com" from_email="mrwrong@gmail.com" body="Hey girl, I'm here to waste your time and string you along. I hope you're ready because I sure am. xx") => idk why this is erroring but we'll cross that bridge when we get there
#default values
def power(num,power=1):
    return num ** power #if no value is passed, power defaults to one - ALSO defaulted args cannot go before non-defaulted ones

# HODGEPODGE
## in terminal => dir(): shows methods/attributes of object that's passed in
## help(): show me help on how to use passed in object 
# """can use triple quotes for comments as well which will be shown when we call help() on some object - useful when working on teams => THIS IS CALLED A DOCSTRING""" => these are normally at the begining of a gile
# CMD+/ TO BLOCK COMMENT!!!! CAN HIGHLIGHT THEN PRESS THOSE KEYS N BOOM ITS ALL COMMENTED OUT => I FINALLY LEARNED HOW TO DO IT BLESS UPPPPPP