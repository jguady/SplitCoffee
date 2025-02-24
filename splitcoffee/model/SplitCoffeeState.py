

class SplitCoffeeState:
    person_name: str
    debt: float
    time_last_paid: int

    def __init__(self, person_name, debt= 0.0, time_last_paid = 0):
        self.person_name = person_name
        self.debt = debt
        self.time_last_paid = time_last_paid

    def __str__(self):
        return f"SplitCoffeeState(person_name={self.person_name}, debt={self.debt:.2f}, time_last_paid={self.time_last_paid})"

    def __repr__(self):
        return str(self)