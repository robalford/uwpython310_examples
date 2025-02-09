import if_name_equals_main

def main():
    if_name_equals_main.module_level_function()
    print(if_name_equals_main.module_level_variable)
    # print(if_name_equals_main.script_only_variable)  # This will raise AttributeError


if __name__ == '__main__':
    main()
