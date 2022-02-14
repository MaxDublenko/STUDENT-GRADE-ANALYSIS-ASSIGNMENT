import random
array = []
for i in range(50):
    array.append(random.randint(0,100))

while True:
    print('1. Display All Grades')
    print('2. Randomize Grades')
    print('3. Stats')
    print('4. Count Honours')
    print('5. Exit')
    answer = int(input('Pick a number: '))
    if answer == 1:
        for i in range(50):
            print(array[i])
    elif answer == 2:
        array = []
        for i in range(50):
            array.append(random.randint(0,100))
    elif answer == 3:
        sortedArray = array.sort()
        print(f'Highest grade is {sortedArray[-1]}')
        print(f'Lowest grade is {sortedArrat[0]}')
        number = 0
        for i in range(50):
            number = number + int(array[i])
        average = number / 50
        print(f'Average grade is {average}')
    elif answer == 4:
        numofHonours = 0
        for i in range(50):
            if int(array[i]) > 79:
                numofHonours = numofHonours + 1
        print(numofHonours)
    elif answer == 5:
        exit()
