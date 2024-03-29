import delicacies.delicacy as dl


class Stolen(dl.Delicacy):
    def __init__(self, name: str, price: float):
        super().__init__(name, 250, price)

    def details(self):
        return f"Stolen {self.name}: {self.portion}g - {self.price:.2f}lv."
