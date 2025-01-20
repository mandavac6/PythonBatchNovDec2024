"""
Purpose: Importance of Self

    Self is the placeholder for the instance created from that class.
    NOTE: self is not keyword in python. But, PEP 8 recommends to use the same.
"""


class Car:
    Company_name = "FORD"  # class variable

    def __init__(self, name):
        print("\nNew Car instance is created")
        self.name = name  

    def display_name(self):
        return self.name


if __name__ == "__main__":
    ford_mustang = Car("ford mustang")  
    print(ford_mustang.display_name())
    print(vars(ford_mustang))

    ford_ecosport = Car("ford ecosport")
    print(ford_ecosport.display_name())
    print(vars(ford_ecosport))