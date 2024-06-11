#Name: Nana Kwasi Owusu
#Date: 17 February, 2024
#Program Description: This is a program that calculates a person's name number and then predicts things about that person based on their name number

#This function takes a number as input. When the number is less than 10, that same number is returned
#but when the number is greater than 9, the individual digits are added until the number is less than 9
def sumDigits(number):
    while number >= 10:
        count = 0
        while number > 0:
            count += number % 10
            number = number // 10
        number=count
    return number

  
#This function has two lists that represents the letters of the alphabets and their corresponding points according to the Cheiro table
#The loop used checks if a letter is in the name typed. The loop then adds the required point using index to the total. Non-alphabets do not add points
def nameNumber(name):
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    points = [1, 2, 3, 4, 5, 8, 3, 5, 1, 1, 2, 3, 4, 5, 7, 8, 1, 2, 3, 4, 6, 6, 6, 5, 1, 7]
    total = 0
    for i in name:
        if i in letters:
            index = letters.index(i)
            total += points[index]
        else:
            total+=0
    return total

#This function predicts a person's behaviour based on their given name number. If a number outside the range 1-9 is given, an invalid input statement is printed
def prediction(number):
    if number == 1:
        print('A person who is successful in personal ambitions.')
    elif number == 2:
        print('A gentle and artistic person.')
    elif number == 3:
        print('A success in their professional career.')
    elif number == 4:
        print('An unlucky person who must put in extra work for success.')
    elif number == 5:
        print('A lucky person who leads an unconventional life. ')
    elif number == 6:
        print('A person who commands the respect of others.')
    elif number == 7:
        print('A person who has a strong inner spirit.')
    elif number == 8:
        print('A person who is misunderstood by others and is not respected for their success.')
    elif number == 9:
        print('A person who is more successful in matters of the material than spiritual.')
    else:
        print('Invalid Input')

#This is the main part of the program. It asks for the user's name and always capitalizes each character
#The number of points their name gives is then placed into the sumDigits Function and added up until an integer in the range 1-9 is produced
#Using their name number, their behavior is predicted using the prediction function 

if __name__ == "__main__":
    print('Welcome to Name Number Generator')
    name = input('Enter Your Name:').upper()
    print(f'Your Name Number is {sumDigits(nameNumber(name))}')
    print('We predict you are:')
    prediction(sumDigits(nameNumber(name)))