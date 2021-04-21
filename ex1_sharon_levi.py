# =========================General Data==============================
# Name: Sharon Levi
# Exercise: 1
# Language: Python
# Explanation: This program run in a loop and everytime the user
# can choose to run a question from the exercise:
# '1' - question 1
# '2' - question 2
# '3' - question 3
# '4' - question 4
# Everything else - for exit the program.
# The inputs & outputs of every function described in the top of
# each function.
# ========================Functions section==========================
# This function get 2 numbers and count how many digits in the first
# number appears in the second number. then it print the counter.


def question1():
    num1 = list(input("Enter the first number:"))
    num2 = list(input("Enter the second number:"))
    count_digits = 0
    for i in num1:
        for j in num2:
            if i == j:
                count_digits += 1
                break
    print(count_digits)
# -------------------------------------------------------------------
# This function implement a simple stack by a list.
# The user can do the following actions:
# 'i' - for enter a string into  the stack.
# 'e' - for delete a string from the stack.
# 'p' - for print all the values in the stack.
# Another key - for exit.


def question2():
    stack = []  # define empty list called "stack"
    while True:
        option = input("Please enter the wanted action:")
        if option == 'i':
            string = input("Enter a string to insert: ")
            stack.insert(0, string[1:])  # insert the string into the first place in the list
        elif option == 'e':
            if len(stack) != 0:
                stack.pop(0)  # remove the first element if the stack isn't empty
            else:
                break
        elif option == 'p':
            for i in range(len(stack)):
                print(i, stack[i], sep=". ")
        else:
            break
# -------------------------------------------------------------------
# This function get a list of heredity and collect the best of them
# who smaller then 0.1. Then print them.


def question3():
    heredity = [['B2B', 'HLA_A', 'AMHR2', 590, 0.12],
                ['B2B', 'HLA_A', 'AMH', 591, 0.12],
                ['B2B', 'HLA_A', 'AMICA1', 592, 0.12],
                ['B2B', 'HLA_A', 'AMIGO1', 593, 0.12],
                ['B2B', 'HLA_A', 'AMIGO2', 594, 0.12],
                ['B2B', 'HLA_A', 'AMIGO3', 595, 0.12],
                ['B2B', 'HLA_A', 'AMMECR1L', 596, 0.12],
                ['B2B', 'HLA_A', 'AMMECR1', 597, 0.12],
                ['B2B', 'HLA_A', 'AMN1', 598, 0.12],
                ['B2B', 'HLA_A', 'AMN', 599, 0.12],
                ['B2B', 'HLA_A', 'AMOTL1', 600, 0.12],
                ['B2B', 'HLA_A', 'AMOTL2', 601, 0.12],
                ['B2B', 'HLA_A', 'AMOT', 602, 0.12],
                ['B2B', 'HLA_A', 'AMPD1', 603, 0.12],
                ['B2B', 'HLA_A', 'AMPD2', 604, 0.12],
                ['B2B', 'HLA_A', 'AMPD3', 605, 0.12],
                ['B2B', 'HLA_A', 'AMPH', 606, 0.0019],
                ['B2B', 'HLA_A', 'AMTN', 607, 0.12],
                ['B2B', 'HLA_A', 'AMT', 608, 0.12],
                ['B2B', 'HLA_A', 'AMY1A', 609, 0.12],
                ['B2B', 'HLA_A', 'AMY2A', 610, 0.0019],
                ['B2B', 'HLA_A', 'AMY2B', 611, 0.12],
                ['B2B', 'HLA_A', 'AMZ1', 612, 0.12],
                ['B2B', 'HLA_A', 'AMZ2P1', 613, 0.12],
                ['B2B', 'HLA_A', 'AMZ2', 614, 0.12],
                ['B2B', 'HLA_A', 'ANAPC10', 615, 0.12],
                ['B2B', 'HLA_A', 'ANAPC11', 616, 0.12],
                ['B2B', 'HLA_A', 'ANAPC13', 617, 0.12],
                ['B2B', 'HLA_A', 'ANAPC16', 618, 0.12],
                ['B2B', 'HLA_A', 'ANAPC1', 619, 0.12],
                ['B2B', 'HLA_A', 'ANAPC2', 620, 0.0019],
                ['B2B', 'HLA_A', 'ANAPC4', 621, 0.0019],
                ['B2B', 'HLA_A', 'ANAPC5', 622, 0.12],
                ['B2B', 'HLA_A', 'ANAPC7', 623, 0.12],
                ['B2B', 'HLA_A', 'ANGEL1', 624, 0.12],
                ['B2B', 'HLA_A', 'ANGEL2', 625, 0.12],
                ['B2B', 'HLA_A', 'ANGPT1', 626, 0.12],
                ['B2B', 'HLA_A', 'ANGPT2', 627, 0.12],
                ['B2B', 'HLA_A', 'ANGPT4', 628, 0.12],
                ['B2B', 'HLA_A', 'ANGPTL1', 629, 0.12],
                ['B2B', 'HLA_A', 'ANGPTL2', 630, 0.12],
                ['B2B', 'HLA_A', 'ANGPTL3', 631, 0.12],
                ['B2B', 'HLA_A', 'ANGPTL4', 632, 0.12],
                ['B2B', 'HLA_A', 'ANGPTL5', 633, 0.12],
                ['B2B', 'HLA_A', 'ANGPTL6', 634, 0.12],
                ['B2B', 'HLA_A', 'ANGPTL7', 635, 0.12],
                ['B2B', 'HLA_A', 'ANG', 636, 0.12],
                ['B2B', 'HLA_A', 'ANK1', 637, 0.0019],
                ['B2B', 'HLA_A', 'ANK2', 638, 0.0019],
                ['B2B', 'HLA_A', 'ANK3', 639, 0.12],
                ['B2B', 'HLA_A', 'ANKAR', 640, 0.12],
                ['B2B', 'HLA_A', 'ANKDD1A', 641, 0.12],
                ['B2B', 'HLA_A', 'ANKFN1', 642, 0.0019],
                ['B2B', 'HLA_A', 'ANKFY1', 643, 0.12],
                ['B2B', 'HLA_A', 'ANKHD1_EIF4EBP3', 644, 0.12],
                ['B2B', 'HLA_A', 'ANKHD1', 645, 0.12]]
    best_heredity = set()  # define new set list
    for list1 in heredity:
        if list1[len(list1)-1] < 0.1:  # check if its good
            for i in range(3):
                best_heredity.add(list1[i])  # save it to the set list one time
    print(best_heredity)

# -------------------------------------------------------------------
# This function encoding a message by Caesar Cipher method.
# input: encrypted message.
# output: decode of the message.


def question4():
    message = input("Enter a message: ")
    result = ""
    for i in message:
        # Encoding only characters
        if i.isalpha():
            # Encrypt uppercase characters in plain text
            if i.isupper():
                result += chr((ord(i) + 13-65) % 26 + 65)
            # Encrypt lowercase characters in plain text
            else:
                result += chr((ord(i) + 13 - 97) % 26 + 97)
        else:
            result += i
    print(result)


# ===========================Main Loop===============================


while True:
    choice = input("Enter the number of the questions 1-4 or "
                   "one of the other keys for exit:")
    if choice == '1':
        question1()
    elif choice == '2':
        question2()
    elif choice == '3':
        question3()
    elif choice == '4':
        question4()
    else:
        break




