def module_level_function():
    print("I can be imported")

module_level_variable = "I can be imported too"

def main():
    print("You'll only see me if you run this file as a script")

if __name__ == '__main__':
    main()
    script_only_variable = "I won't be imported"
