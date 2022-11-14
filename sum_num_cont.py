#!/usr/bin/env python3

# Created by: Marcus Wehbi
# Created on: Nov 10 2022
# This program asks the user how many numbers they would like
# to add. It then uses a while loop to calculate and display
# the sum of the numbers they inputted.
# This program uses a continue statement.


def main():
    # initialize counter, the sum of the numbers, and the string to display sum
    loop_counter = 0
    sum = 0
    answer = ""

    while True:
        # get how many numbers the user wants to input
        # Get it as a string
        user_num_a_string = input("How many numbers would you like to add?: ")
        print("")

        try:
            # converts the first user input to an integer
            user_num_a_int = int(user_num_a_string)

            # Make sure they inputted a valid integer
            if user_num_a_int >= 0:
                # calculate the sum of the entered numbers
                while loop_counter < user_num_a_int:
                    # keep getting numbers as long as...
                    # the counter is less than the first input
                    # gets input from user for the actual numbers to add
                    user_num_b_string = input("Enter a whole number: ")

                    try:
                        # converts entered number from string to integer
                        user_num_b_int = int(user_num_b_string)
                        # joins the strings

                        if user_num_b_int < 0:
                            print(
                                "{} is negative, therefore it cannot be added".format(
                                    user_num_b_int
                                )
                            )
                            print("")
                            # go back to the top of the loop
                            continue

                        # add the number to the sum when it is valid
                        print("{} added to the sum.".format(user_num_b_int))
                        print("")
                        # add input to the sum
                        sum = sum + user_num_b_int
                        # increment the counter
                        loop_counter = loop_counter + 1
                        # add to the final sum output
                        answer += str(user_num_b_int) + " + "
                    except Exception:
                        # if they did not enter a valid integer, tell them
                        print("{} is not a number.".format(user_num_b_string))
                        print("")
                        # go back to the top of the loop
                        continue
                if loop_counter == user_num_a_int:
                    # Once you have reached the amount of numbers they wanted...
                    # to input, display the final sum
                    print("{}0 = {} ".format(answer, sum))
                    print("The sum is {}.".format(sum))
                    # Exit the loop
                    break
            else:
                # Tell the user to enter a whole number
                print("Please enter a whole number!")
                print("")
        except Exception:
            # Tell the user to enter a valid number
            print("{} is not a number.".format(user_num_a_string))
            print("")


if __name__ == "__main__":
    main()
