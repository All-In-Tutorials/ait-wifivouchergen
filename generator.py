import os
import itertools
import string

def generate_combinations(option):
    if option == "1":
        return ["".join(combo) for combo in itertools.product(string.ascii_uppercase, repeat=4)]
    elif option == "2":
        return [str(num) + "".join(combo) for num, combo in itertools.product(range(10), itertools.product(string.ascii_uppercase, repeat=3))]
    elif option == "3":
        return [uc1 + str(num) + uc2 + uc3 for uc1, num, uc2, uc3 in itertools.product(string.ascii_uppercase, range(10), string.ascii_uppercase, string.ascii_uppercase)]
    elif option == "4":
        return [uc1 + uc2 + str(num) + uc3 for uc1, uc2, num, uc3 in itertools.product(string.ascii_uppercase, string.ascii_uppercase, range(10), string.ascii_uppercase)]
    elif option == "5":
        return [uc1 + uc2 + uc3 + str(num) for uc1, uc2, uc3, num in itertools.product(string.ascii_uppercase, string.ascii_uppercase, string.ascii_uppercase, range(10))]
    elif option == "6":
        return [str(num1) + str(num2) + uc1 + uc2 for num1, num2, uc1, uc2 in itertools.product(range(10), range(10), string.ascii_uppercase, string.ascii_uppercase)]
    elif option == "7":
        return [str(num1) + str(num2) + str(num3) + uc1 for num1, num2, num3, uc1 in itertools.product(range(10), range(10), range(10), string.ascii_uppercase)]
    elif option == "8":
        return [str(num1) + str(num2) + str(num3) + str(num4) for num1, num2, num3, num4 in itertools.product(range(10), range(10), range(10), range(10))]
    elif option == "9":
        return [uc1 + uc2 + str(num1) + str(num2) for uc1, uc2, num1, num2 in itertools.product(string.ascii_uppercase, string.ascii_uppercase, range(10), range(10))]
    elif option == "10":
        return [uc1 + str(num1) + str(num2) + str(num3) for uc1, num1, num2, num3 in itertools.product(string.ascii_uppercase, range(10), range(10), range(10))]
    elif option == "11":
        return [uc1 + str(num1) +  uc2 + str(num2) for uc1, num1, uc2, num2 in itertools.product(string.ascii_uppercase, range(10), string.ascii_uppercase, range(10))]
    elif option == "12":
        return [uc1 + str(num1) + str(num2) + uc2 for uc1, num1, num2, uc2 in itertools.product(string.ascii_uppercase, range(10), range(10), string.ascii_uppercase)]
    elif option == "13":
        return [str(num1) + uc1 + str(num2) + uc2 for num1, uc1, num2, uc2 in itertools.product(range(10), string.ascii_uppercase, range(10), string.ascii_uppercase)]
    elif option == "14":
        return [str(num1) + uc1 + uc2 + str(num2) for num1, uc1, uc2, num2 in itertools.product(range(10), string.ascii_uppercase, string.ascii_uppercase, range(10))]
    else:
        return []

def save_to_file(file_path, data):
    with open(file_path, "w") as f:
        f.write("\n".join(item.strip() for item in data if item.strip()))

def create_dictionary(option):
    base_dir = "Dictionary"
    os.makedirs(base_dir, exist_ok=True)

    # Create prefix.txt inside Dictionary directory
    prefix_file = os.path.join(base_dir, "prefix.txt")
    if not os.path.exists(prefix_file):
        with open(prefix_file, "w") as f:
            f.write("")
    
    dir_names = {
        "1": "UC-UC-UC-UC",
        "2": "Num-UC-UC-UC",
        "3": "UC-Num-UC-UC",
        "4": "UC-UC-Num-UC",
        "5": "UC-UC-UC-Num",
        "6": "Num-Num-UC-UC",
        "7": "Num-Num-Num-UC",
        "8": "Num-Num-Num-Num",
        "9": "UC-UC-Num-Num",
        "10": "UC-Num-Num-Num",
        "11": "UC-Num-UC-Num",
        "12": "UC-Num-Num-UC",
        "13": "Num-UC-Num-UC",
        "14": "Num-UC-UC-Num",
    }

    if option == "15":
        print("Generating all dictionaries...")
        for key in dir_names.keys():
            create_dictionary(key)
        print("All dictionaries have been generated successfully!")
        return

    if option not in dir_names:
        print("Invalid option. Please enter a number between 1 and 15.")
        return
    
    target_dir = os.path.join(base_dir, dir_names[option])
    os.makedirs(target_dir, exist_ok=True)
    
    username_file = os.path.join(target_dir, "username.txt")
    password_file = os.path.join(target_dir, "password.txt")
    
    # Generate all possible combinations based on option
    combinations = generate_combinations(option)
    
    # Write data to files line by line
    save_to_file(username_file, combinations)
    save_to_file(password_file, combinations)
    
    print(f"Setup completed. Directory '{target_dir}' and files created with all username and password combinations.")

def main():
    print("Select dictionary to create:")
    print("1 - Uppercase Letters (AAAA)")
    print("2 - Number, Uppercase, Uppercase, Uppercase (1AAA)")
    print("3 - Uppercase, Number, Uppercase, Uppercase (A1AA)")
    print("4 - Uppercase, Uppercase, Number, Uppercase (AA1A)")
    print("5 - Uppercase, Uppercase, Uppercase, Number (AAA1)")
    print("6 - Number, Number, Uppercase, Uppercase (11AA)")
    print("7 - Number, Number, Number, Uppercase (111A)")
    print("8 - Number, Number, Number, Number (1111)")
    print("9 - Uppercase, Uppercase, Number, Number (AA11)")
    print("10 - Uppercase, Number, Number, Number (A111)")
    print("11 - Uppercase, Number, Uppercase, Number (A1A1)")
    print("12 - Uppercase, Number, Number, Uppercase (A11A)")
    print("13 - Number, Uppercase, Number, Uppercase (1A1A)")
    print("14 - Number, Uppercase, Uppercase, Number (1AA1)")
    print("15 - All of the above (Generate all dictionaries)")
    option = input("Enter your choice: ").strip()
    
    if option not in {"1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"}:
        print("Invalid choice. Please enter a number between 1 and 15.")
        return
    
    create_dictionary(option)

if __name__ == "__main__":
    main()
