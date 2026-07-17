print("stinkycrunchguy was here")
def greet(name: str) -> str:
    """
    Returns a greeting message for the given name.

    :param name: The name to greet
    :return: A greeting string
    """
    return f"Hello, {name}!"

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    print(greet(user_name))
    print("Welcome to DevAsc")