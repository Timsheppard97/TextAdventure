#Basic function to delete the user input right after they input it
def delete_user_input():
    print("\033[1A" + "\033[K")

def while_case_input():
    delete_user_input()
    print("Please enter 1 of the provided options.")

def option1_input():
    raw_option1 = input("*Look around* *Sleep* \n")
    option1 = raw_option1.lower()