class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method to return the sum of two numbers."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method to return the product of two numbers, also prints the calculation type."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b


# Demonstration
if __name__ == "__main__":
    # Using static method
    sum_result = Calculator.add(10, 5)
    print(f"Sum: {sum_result}")

    # Using class method
    product_result = Calculator.multiply(4, 6)
    print(f"Product: {product_result}")
