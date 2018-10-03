#This program asks user for name, age, and displays it
#afterwards with their name, age, and what age they
#will be next year.
#

def main():

    #get user name
    name = input('What is your name?')
    #get user age
    age = int(input('What is your age?'))
    #calculate user age next year
    new_age = age + 1
    #display user name and new age
    print('Your name is ', name, 'and you will be ', new_age,' next year.')

#call main function
main()
