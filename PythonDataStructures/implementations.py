from node import Node






"""Exercise 1A (Tuple)"""
months_T = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

pi_Day = months_T[4]

print(pi_Day)



"""Exercise 1B (Set)"""
fruits_Veggies = {'Strawberries', 'Apple', 'Peas', 'Broccoli', 'Orange'}
fruits_Veggies.update(['Watermelon', 'Banana', 'Green Beans', 'Carrots'])

print(fruits_Veggies)


"""Exercise 1C (Dictionary)"""
user = {
    "firstname": "Jared",
    "lastname": "Martin",
    "email": "Jared@aol.com",
    "phone number": "1234567891"
}

print('My first name is {data[firstname]} and my last name is {data[lastname]}, my phone number is {data[phone number]} and my email is {data[email]}'.format(data = user))


"""Exercise 2, first part, Dictionaries stored in a list"""
family1 = {
    "firstname": "Casandra",
    "lastname": "Martin",
    "relation": "Fiance"
}

family2 = {
    "firstname": "Benjamin",
    "lastname": "McMahon",
    "relation": "Step son"
}

family3 = {
    "firstname": "Juliana",
    "lastname": "McMahon",
    "relation": "Step daughter"
}

family4 = {
    "firstname": "Taylor",
    "lastname": "Martin",
    "relation": "Daughter"
}

family5 = {
    "firstname": "Torrence",
    "lastname": "Martin",
    "relation": "Daughter"
}

family6 = {
    "firstname": "Teagan",
    "lastname": "Martin",
    "relation": "Daughter"
}


family_List = [family1, family2, family3, family4, family5, family6]





