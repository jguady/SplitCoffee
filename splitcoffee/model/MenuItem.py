import typing


class MenuItem:
    name: str
    price: float

    # def __init__(self, data: dict =None) -> None:
    #     for key, _ in typing.get_type_hints(self).items():
    #         setattr(self, key, data[key])
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"MenuItem(name={self.name}, price={self.price})"

    def __repr__(self):
        return str(self)