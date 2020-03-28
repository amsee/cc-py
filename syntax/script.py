# exercise 1


# python 2
print "This is how you print in python 2."

# python 3
print("This is how you print in python 3.")

# concatenating strings
print "Hello " + "there" + " funny bunny."


# exercise 2


january_to_june_rainfall = 1.93 + 0.71 + 3.53 + 3.41 + 3.69 + 4.50
annual_rainfall = january_to_june_rainfall

july_rainfall = 1.05
annual_rainfall += july_rainfall

august_rainfall = 4.91
annual_rainfall += august_rainfall

september_rainfall = 5.16
annual_rainfall += september_rainfall

october_rainfall = 7.20
annual_rainful += october_rainfall

november_rainfall = 5.06
annual_rainfall += november_rainfall

december_rainfall = 4.06
annual_rainfall += december_rainfall

cucumbers = 2
price_per_cucumber = 3.25
total_cost = cucumbers * price_per_cucumber
# output total cost
print(total_cost) # returns a float


# exercise 3


cucumbers = 100
num_people = 6

whole_cucumbers_per_person = cucumbers / num_people
print(whole_cucumbers_per_person)

float_cucumbers_per_person = float(cucumbers)/num_people
print(float_cucumbers_per_person)


# exercise 4


# a multi-line string
haiku = """The old pond,
A frog jumps in:
Plop!"""

# booleans
age_is_100 = True;
name_is_amy = False;


# exercise 5


float_1 = 0.25
float_2 = 40.0
product = float_1 * float_2
# concatenate float and string
big_string = "The product was " + str(product)


# review


#Create variable called skill_completed and set it equal to the string "Python Syntax"
skill_completed = "Python Syntax"

#Create a variable called exercises_completed and set it equal to 13. Create another variable called points_per_exercise and set it equal to 5
exercises_completed = 13
#The amount of points for each exercise may change, because points don't exist yet
points_per_exercise = 5

#Create a variable called point_total and set it equal to 100.
point_total = 100

#Update point_total to be what it was before plus the result of multiplying exercises_completed and points_per_exercise.
point_total += exercises_completed * points_per_exercise

#Print a string to the console that says:
print "I got " + str(point_total) + " points!"