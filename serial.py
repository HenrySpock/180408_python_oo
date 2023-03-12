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
    def __init__(self, start=0):
        """Initialize the generator with a starting number."""
        self.start = start
        self.next_serial = start + 1
        self.current_number = start

    def generate(self):
        """Return the next serial number."""
        result = self.next_serial
        self.next_serial += 1
        self.current_number += 1
        return result
    
    def current_number(self):
        """Return the current serial number."""
        return self.current_number

    def reset(self):
        """Reset the generator to the initial state."""
        self.next_serial = self.start

    def __repr__(self):
        """Return string representation of the SerialGenerator instance."""
        return f"<SerialGenerator Starting Number = {self.start}, Current Number = {self.current_number}, Next Number = {self.next_serial}>"
