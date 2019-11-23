from csv import DictWriter
import os

# ------ Number of Data Which User Want to Import ----
num = input('How Many Peoples Data You Gonna Import Today: \n')


for a in range(int(num)):
    print("""
    Complete Your Info Please> \n""")

# ------ Get Inputs fill from the user ------

    name = input('Your Name: \n')
    age = input('Your Age:\n')
    phone = input('Your Phone Number: \n')
    gender = input('Enter (M) for Male and (F) for female: \n')

# ------- placing some conditions looking for best results------
    if gender.upper() == 'M':
        gender = 'MALE'
    else:
        pass
    if gender.upper() == 'F':
        gender = 'FEMALE'

# ------- Creating <CSV FILE> and managing fieldnames -----
    with open('Data.csv', 'a', newline='') as info:
        dictwriter = DictWriter(info, fieldnames=['name', 'age', 'phone', 'gender'])
        if os.stat('Data.csv').st_size == 0:
            dictwriter.writeheader()
        dictwriter.writerow({
            'name':name,
            'age':age,
            'phone':phone,
            'gender':gender
        })
# ------ thanking the user for completing the model-----
    print("-"*40)
    print(f'''Thanks {name} For Finish This Object Fully''')
    print("-"*40)
