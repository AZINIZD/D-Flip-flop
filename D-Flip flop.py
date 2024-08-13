class DFlipFlop:
    def __init__(self):
        self.D = 0  # Input D
        self.Q = 0  # Output Q

    def clock_edge(self):
        """Simulate the rising edge of the clock."""
        self.Q = self.D  # Q takes the value of D

# Example usage
if __name__ == "__main__":
    dff = DFlipFlop()

    # Set input D
    dff.D = 1
    dff.clock_edge()  # Simulate clock edge
    print("Output Q after clock edge:", dff.Q)  # Output: 1

    # Change input D
    dff.D = 0
    dff.clock_edge()  # Simulate clock edge
    print("Output Q after clock edge:", dff.Q)  # Output: 0