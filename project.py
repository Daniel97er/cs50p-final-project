import re

# !!!No teacher check this program, so please check it befor use it there can be errors!!!

# Cs50p Harvard Python online course final project
# Console program for combinatoric tasks


def main():
    # Main function

    # Get the user desired function
    selection_number = selection()

    # Calculate the desired function and print the solution and maybe advanced solution
    match selection_number:
        # Inclusion_exclusion_procedure
        case 1:
            result_set, cardinality = inclusion_exclusion_procedure()
            print(cardinality)
            if get_advance_solution():
                print(result_set)
        # Permutation with allowed repetition
        case 2:
            element_lists, number_of_permutations = permutation_with_repetition()
            print(number_of_permutations)
            if get_advance_solution():
                print(element_lists)
        # Permutation without repetition
        case 3:
            element_lists, number_of_permutations = permutation_without_repetition()
            print(number_of_permutations)
            if get_advance_solution():
                print(element_lists)
        # Variation with repetition
        case 4:
            element_lists, number_of_variations = variation_with_repetition()
            print(number_of_variations)
            if get_advance_solution():
                print(element_lists)
        # Variation without repetition
        case 5:
            element_lists, number_of_variations = variation_without_repetition()
            print(number_of_variations)
            if get_advance_solution():
                print(element_lists)



def selection():
    """Prompt the user to select a function"""

    user_input_check = False

    # Present the available functions and get user selection
    user_input = input("Please enter the number of the desired function\n"
                     + "1. Inclusion and exclusion function\n"
                     + "2. Permutation with allowed repetition                  Formula: n!\n"
                     + "3. Permutation without allowed repetition               Formula: n!/k!\n"
                     + "4. Variation with all distinguishable elements          Formula: n!/(n-k)!\n"
                     + "5. Variation with not all distinguishable elements      Formula: n^k\n"
                     + "Selected number: ")

    # Check the user selection input if there is not a allowed number entered reprompt the user
    while not user_input_check:
        if selection := re.search(r"^[0-9]$", user_input.strip()) and 5 >= int(user_input.strip()) >= 1:
            # Set check to true if user entered a allowed number
            user_input_check = True
            # Return the selected function number
            return int(user_input.strip())
        else:
            # Reprompt user if there was a false entered input
            user_input = input("Selected number: ")


def get_element_list():
    """Function check the user input and return right format list with user entered elements"""

    # Create list for user entered elements
    input_element_list = []

    # Reprompt user while the entered list is not in the right format
    while True:
        # Get user input elements for the list as a string
            elements_content = input("Elements (Please in the format 1,2,3,a,b or singleton A or 1): ")
            # Check the user entered element string for the right format
            if re.search(r"^[^, ]+,([^, ]+,)*[^, ]+$|^[^, ]+$", elements_content):

                # Filter the list content
                # Check if in the elements string is a comma
                if "," not in elements_content:
                    # Append the the singleton content as a singleton list element
                    input_element_list.append(elements_content)
                else:
                    # Create content_part to build the new elements
                    content_part = ""
                    # Go through element string and check the commas
                    for index in elements_content:
                        # If there is a comma so the content part is at the end and must be add to current list
                        if index == ",":
                            input_element_list.append(content_part)
                            # Create a new content part for the next content after comma
                            content_part = ""
                            continue
                        else:
                            # Concatenate the signs to content_part
                            content_part += index
                    # Append the entire content part to the list
                    input_element_list.append(content_part)

                # Return the new created list with all user entered elements
                return input_element_list


# all_elements maximum calculable value
def get_number_of_selected_elements(all_elements=9999999):
    """Function prompt user to enter the number of selected elements and check it and return it"""

    # Reprompt user while the entered number is not allowed
    while True:
        # Get user input selected numbers
        selected_number = input("Please enter the number of selected elements: ")
        # Check the user entered string for the right format
        if re.search(r"^[0-9]+$", selected_number) and int(all_elements) >= int(selected_number) >= 1:
            # Return input if it is in the right format
            return int(selected_number)


def get_advance_solution():
    """Ask the user if it is desired to print the all elements"""

    # Print the question and check the answer format
    while True:
        answer = input("Print all solution elements?\n"
                     + "Please enter yes or no: ")
        # Return the answer or reprompt user if there was a not allowed answer
        if answer.strip().lower() == "yes":
            return True
        elif answer.strip().lower() == "no":
            return False


def inclusion_exclusion_procedure():
    """Function return distinguishable elements from the user entered sets and the number of this elements"""

    sets_list = []

    # Get the number of sets
    while True:
        sets_number = input("Number of sets to enter: ")
        # Check user input
        if re.search(r"^[0-9]+$", sets_number):
            # Break while loop when user enter a allowed number
            break

    # Create list with user entered number of sets
    print("Please enter numbers in the format 1,a,2,3 or singleton for every set")
    for number in range(int(sets_number)):
        # Prompt user entered right format content for every set
        input_list = get_element_list()

        # Append the entire current list as a set to the sets list
        sets_list.append(set(input_list))


    # Create a set with all elements which are in after the inclusion exclusion procedure
    new_set = set()

    # Put in all the elements to the new set
    for index in sets_list:
        for digit in index:
            new_set.add(digit)

    # Return the new set and number of the elements
    return new_set, len(new_set)


def permutation_with_repetition():
    """Function return lists with all permutations and the number of lists"""

    # Get the user entered elements
    element_list = get_element_list()

    # Function to build recursively the permutation lists
    def permutation_func(element_list):
        # Check if there is only one element in the list
        if len(element_list) <= 1:
            # Return the singleton as a list element
            return [element_list]
        else:
            # Recursively go through element_list and create the remainder lists to concatenate with the respectively first element of the current list
            return [
                [element_list[index]] + remainder for index in range(len(element_list)) for remainder in permutation_func(element_list[:index] + element_list[index + 1:])
            ]
    # Get the permutation lists with the recursively function
    permutation_lists = permutation_func(element_list)

    # Return the permutation lists and the number of the permutations
    return permutation_lists, len(permutation_lists)


def permutation_without_repetition():
    """Function return lists with all distinguishable permutations and the number of lists"""

    # Get a list with all permutations
    permutation_list = permutation_with_repetition()[0]


    # Sort out the distinguishable lists with elements
    end_list = []

    for index in permutation_list:
        if index not in end_list:
            end_list.append(index)

    # Return end_list with all distinguishable permutation lists of elements and the number of the all permutations
    return end_list, len(end_list)


def variation_with_repetition():
    """Function return list with all variations and the number of the lists"""

    # Get a list with all permutations
    permutation_list = permutation_with_repetition()

    temp_list = []
    end_list = []

    # Get the variation number from user
    variations = get_number_of_selected_elements(len(permutation_list[0]))

    # Get a list with all variations
    for index in permutation_list[0]:
        temp_list = []
        for j in index[:variations]:
            temp_list.append(j)
        end_list.append(temp_list)

    # Sort out the distinguishable elements
    result_list = []

    for index in end_list:
        if index not in result_list:
            result_list.append(index)

    # Return list with variations and the number of the variations
    return result_list, len(result_list)


def variation_without_repetition():
    """Function return list with all distinguishable variations and the number of the list"""

    # Get the user entered elements
    element_list = get_element_list()
    # Get the number of user entered element
    num_elements = len(element_list)
    # Get the variation number of the user
    num_places = get_number_of_selected_elements()

    result_list = []
    end_list = []

    # Loop to create all n^k variations
    for i in range(pow(len(element_list), num_places)):

        # Index variable
        value = i
        # List with indexes
        indexes = []

        # Create indexes list for indexing
        while value:
            indexes.append(value % num_elements)
            value = value // num_elements

        # Go through the respectively part of elements
        for _ in range(len(indexes), num_places):
            # Append the part to the result_list
            result_list.append(element_list[num_elements - 1])

        # Loop to build the right variations
        for index in range(len(indexes) - 1, -1, -1):
            # Append the slice part to result_list
            result_list.append(element_list[num_elements - 1 - indexes[ index ]])

        # Append result_list to end_list every num_places
        end_list.append(result_list)
        # Create new result_list for the next loop iteration
        result_list = []

    # Return list with all variations and the number of all variations
    return end_list, len(end_list)



if __name__ == "__main__":
    # Run main function
    main()
