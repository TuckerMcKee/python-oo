"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self,start):
        self.start = start
    
    def generate(self):
        """prints current serial number then increments it by one"""
        print(self.start)
        self.start += 1

    def reset(self):
        """resests serial number back to 100"""
        self.start = 100




