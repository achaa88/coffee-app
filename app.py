import database

MENUS_PROMPT = """"\n-- Coffee Bean App --
Please choose one of these options:

1 - Add a new bean.
2 - See all beans.
3 - Find a new bean by name.
4 - See which preparation method is best for a bean.
5 - Exit.

Your Selection:"""

def menu():
    connection = database.connect()
    database.create_tables(connection)

    while (user_input := input(MENUS_PROMPT)) != "5":
        print(user_input)
        if user_input == "1":
            name = input("enter bean name: ")
            method = input("enter how you have prepared it: ")
            rating = int(input("enter your rating score (0-100): "))

            database.add_bean(connection, name, method, rating)
        elif user_input == "2":
            beans = database.get_all_beans(connection)

            for bean in beans:
                print(f"{bean[1]} ({bean[2]}) - {bean[3]}/100")
        elif user_input == "3":
            name = input("enter bean name to find: ")
            beans = database.get_beans_by_name(connection, name)

            for bean in beans:
                print(f"{bean[1]} ({bean[2]}) - {bean[3]}/100")
        elif user_input == "4":
            name = input("enter bean name to find: ")
            best_method = database.get_best_preparation_for_bean(connection, name)

            print(f"The best preparation method for {name} is: {best_method[2]}")
        else:
            print("Invalid choice, try again")

menu()