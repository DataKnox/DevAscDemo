

def greet(name: str) -> str:
    """
    Returns a greeting message for the given name.

    :param name: The name to greet
    :return: A greeting string
    """
    return f"Hello, {name}!"

def goodbye(name: str) -> str:
    """
    Returns a goodbye message for the given name.

    :param name: The name to bid farewell
    :return: A goodbye string
    """
    return f"Goodbye, {name}!"

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    print(greet(user_name))
    print("Welcome to DevAsc")
    print(goodbye(user_name))