""" Overloading a Circuit Breaker """

class CircuitBreaker:
    def __init__(self, max_amps):
        self.capacity = max_amps  # max capacity in amps
        self.load = 0             # present load in amps

    def connect(self, amps):
        self.load += amps
