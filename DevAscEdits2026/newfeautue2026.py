def greet(name: str) -> str:
    """
    Generate a greeting message.
    
    Args:
        name: The name of the person to greet
        
    Returns:
        A personalized greeting string
    """
    return f"Hello, {name}! Welcome to the new feature."


def add_numbers(a: int, b: int) -> int:
    """
    Add two numbers together.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        The sum of a and b
    """
    return a + b


if __name__ == "__main__":
    print(greet("Developer"))
    print(f"2 + 3 = {add_numbers(2, 3)}")