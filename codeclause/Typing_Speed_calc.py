import time

def calculate_speed(text_input, elapsed_time):
    words_typed = len(text_input.split())
    minutes_elapsed = elapsed_time / 60
    speed = words_typed / minutes_elapsed
    return speed

def calculate_accuracy(user_input, text_to_type):
    correct_characters = sum(1 for i, j in zip(user_input, text_to_type) if i == j)
    total_characters = max(len(user_input), len(text_to_type))
    accuracy_percentage = (correct_characters / total_characters) * 100
    return accuracy_percentage

def main():
    print("Welcome to the Typing Speed and Accuracy Calculator!")
    prompt = "Type the following text as fast and accurately as you can:\n"
    text_to_type = """The Mississippi River is the second-longest river and chief river of the second-largest drainage system on the North American continent, second only to the Hudson Bay drainage system. 
    From its traditional source of Lake Itasca in northern Minnesota, it flows generally south for 2,340 miles (3,766 km) to the Mississippi River Delta in the Gulf of Mexico. 
    With its many tributaries, the Mississippi's watershed drains all or parts of 32 U.S. states and two Canadian provinces between the Rocky and Appalachian mountains. 
    The main stem is entirely within the United States; the total drainage basin is 1,151,000 sq mi (2,980,000 km2), of which only about one percent is in Canada. 
    The Mississippi ranks as the fourteenth-largest river by discharge in the world. 
    The river either borders or passes through the states of Minnesota, Wisconsin, Iowa, Illinois, Missouri, Kentucky, Tennessee, Arkansas, Mississippi, and Louisiana."""
    print(prompt)
    print(text_to_type)
    
    input("Press Enter when you're ready to start typing.")
    
    start_time = time.time()
    user_input = input("Type the text here: ")
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    typing_speed = calculate_speed(user_input, elapsed_time)
    accuracy = calculate_accuracy(user_input, text_to_type)
    
    print(f"\nTime taken: {elapsed_time:.2f} seconds")
    print(f"Typing speed: {typing_speed:.2f} words per minute")
    print(f"Accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    main()
