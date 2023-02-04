# Combinatoric-task-solver

## Description

  This is my final project for the Harvard python online
  course Cs50p. My final project is a Python console program
  which solves combinatoric tasks. The program is user
  friendly and react on user input errors.

  !!! No teacher has check the program, so please check
  before you use it there can be errors!!!


## List of all Combinatoric-task-solver functions

  1. Inclusion and exclusion function
  2. Permutation with allowed repitition
     Formula: n!
  3. Permutation without allowed repition
     Formula: n!/k!
  4. Variation with all different elements
     Formula: n!/(n-k)!
  5. Variation with not all different elements
     Formula: n^k

  The function names in combinatorics can sometimes be
  misleading, I ask you to pay attention to the respective
  formulas in order to select the right function.


## requirements.txt

  Textfile with all libraries.
  1. Library re.


## project.py

  The project.py file is the whole main program with main
  function and all other functions. Below is the description
  of the functions.

  ## main()

    In the main function, the user is first directed to the
    selection function so that he can select a function that
    solves his combinatorial task. Then the selected function
    is executed and the result is displayed on the console.

  ## selection()

    In this function, the user is asked to select one of the
    seven combinatorics solvers. The function is user-friendly
    and prompts the user to re-enter the number if the user
    enter a not allowed input. The function return a number
    between one and seven inclusive which stands for the
    choosen combinatoric task solver function.

  ## get_element_list()

    This function check the user input and return right
    format list with user entered elements. First the user
    must entered elements in the right format 1,A,a etc. or
    as a singleton A or 1. Elements longer than one character
    are tolerated. If the user entered everything correctly,
    a list of user enteredelements is returned.

  ## get_number_of_selected_elements()

    Function prompts the user to enter an integer in the
    context of all_elements. The function then checks the
    input and prompts the user to re-enter a number if the
    input was incorrect. If the input was in the correct
    format i.e. 1 or 5 or 2 then the value is returned.

  ## get_advance_solution()

    This function ask the user if print the whole solution
    elements. If the user not enter yes or no repeat the
    entry. This function is to avoid very big outputs of
    solution elements in the console.

  ## inclusion_exclusion_procedure()

    With this function, the user can first determine the
    total number of sets to be entered as a pure integer with
    no other characters. If an incorrect entry is made, the
    entry is repeated. Then the user is prompted to fill in
    the respective sets in the format 1,A,a etc. or as a
    singleton A or 1. After the calculations, the function
    returns the solution set according to the
    inclusion-exclusion principle, simplified here as a set
    without duplicate entries. The function also returns the
    cardinality, i.e. the number of elements.

  ## permutation_with_repetition()

    This function prompts the user to enter a few elements
    in the format 1,2,3,a,b or as a singleton 1 or 2. After
    that, the lists with the respective permutations are
    built with an additional recursive function. The first
    element is always taken and then concatenated with the
    rest of the list by recursion until the termination
    condition is met.After completion of the recursive
    permutation creation, the permutation list and its
    length, i.e. the number of possible permutations, is
    returned.

  ## permutation_without_repetition()

    This function use the permutation_without_repetition()
    to create a list with all permutation lists. Then the
    function sort the permutation lists which looks equal
    out of the list. Finally, it outputs a list with all
    the distinguishable permutations and the number of lists.

  ## variation_with_repetition()

    This function use the permutation_without_repetition() to
    get all the permutations. Next, the user is prompted to
    select a variation number within the length of the total
    elements. Subsequently, the variations are formed and not
    different ones sorted out. At the end, the function
    returns the list of variations and the number of
    variations.

  ## variation_without_repetition()

    This function first asks the user to enter the elements
    and then to enter how large the respective variations
    should be. After that, the function builds a list with
    the respective variations and calculates the number and
    returns it.


## test_project.py

  Python file with some function tests.
