# ----------------------------------------------------------------------------
#  Name:        grader
#  Purpose: Assignment #2
#
#  Author: Roger McClain
#  Date: 1/22/2017
#  ---------------------------------------------------------------------------
'''
Letter grade calculator that drops the lowest grade if over 4 grades entered

Prompt the user for the point value of their assignments
Print the course average and the corresponding letter grades
'''
grades_list = []  # create grades list
CASES_CONST = 4     # constant for number of grades to accept
def remove_excess(inputs_list):  # function to deal with math

    dropped_grade = 'None'
    if len(inputs_list) >= CASES_CONST:  # see if we need to drop a grade
        dropped_grade = min(inputs_list)  # store dropped grade value
        for i in range(0, 1):  # short loop to remove the min value
            inputs_list.remove(min(inputs_list))
    else:  # not needed but helps separate code
        pass
    total_points = sum(inputs_list)  # total the list
    average_grade = (total_points / (len(inputs_list)))  # calculate average
    output_grade = round(average_grade, 1)
    return [inputs_list, output_grade, dropped_grade]  # return updated values


def letter_grade(point_value):      # figure out what letter grade to print

    letter_grade_calc = point_value
    if (letter_grade_calc >= 90.0):
        return 'A'
    elif (letter_grade_calc >= 80.0) and (letter_grade_calc <= 89.99):
        return 'B'
    elif (letter_grade_calc >= 70.0) and (letter_grade_calc <= 79.99):
        return 'C'
    elif (letter_grade_calc >= 60.0) and (letter_grade_calc <= 69.99):
        return 'D'
    elif (letter_grade_calc < 60.0):
        return 'F'
    else:
        pass

more_input = True                                 # initialize boolean
while more_input:                                 # loop to prompt more inputs
    user_input = input('Please enter a grade and ' +
                       'to stop entering grades and calculate, type "end": ')
    if user_input == 'end':
        more_input = False  # exit the loop if 'end' is entered
    elif float(user_input) < float(0):        # verify grade is not negative
        print('Invalid grade entered')
        continue
    elif float(user_input) > float(100):      # verify grade is less than 100
        print('Invalid grade entered')
        continue
    else:
        number = float(user_input)  # convert input to float
        # add grade to list and converter it to an integer
        grades_list.append(float(number))

results = remove_excess(grades_list)    # call math function on grades_list
# assign output[2] from remove_excess function to a variable
results_excess = results[2]
# call letter_grade function on output[1] from results_excess function
alphabetGrade = letter_grade(results[1])
# print dropped grade line if there is something dropped
if results_excess is not 'None':
    print('The lowest grade dropped: ' + str(results_excess))
print('The course average grade is ' + str(results[1])) # print average
# print letter grade
print('The letter grade for this course is ' + str(alphabetGrade))
print('Based on the following grades: ')        # print used grades
for grade in results[0]:
    print(float(grade))
