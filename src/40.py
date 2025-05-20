class SimpleClass:
    def __init__(self):
        self.__private_attribute = "This is a private attribute."

    @staticmethod
    def public_method():
        print("Executing public method.")

    def __private_method(self):
        print("Executing private method.")

class ExampleClass:
    def __init__(self):
        # Assuming ExampleClass has access to SimpleClass's attributes and methods
        self.__shared_attribute = "Shared attribute from SimpleClass."

# Create an instance of the ExampleClass with a reference to SimpleClass
example_instance = ExampleClass()

# Accessing private attributes and public method using example_instance
print(example_instance.public_method())  # Output: Executing public method.
ExampleClass.public_method()  # Output: Executing public method.
