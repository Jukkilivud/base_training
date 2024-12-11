from typing import List, Optional


class Sample:
    def __init__(self, sepal_length: float, sepal_width: float, petal_length: float, petal_width: float, species: Optional[str] = None,) -> None:
        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self. petal_width = petal_width
        self.species = species
        self.classification: Optional[str] = None

    def __repr__(self) -> str:
        if self.species is None:
            known_unknown = 'UnknownSample'
        else:
            known_unknown = 'KnownSample'
        if self.classification is None:
            classification = ''
        else:
            classification = f", {self.classification}"
        return (f"{known_unknown}(" f"sepal_length={self.sepal_length}, " f"sepal_width={self.sepal_width}, " f"petal_length={self.petal_width}, " f"petal_width={self.petal_width}," f"species={self.species!r}" f"{classification}"  f")")


# Наследование
class Contact:
    all_contacts: List["Contact"] = []

    def __init__(self, name: str, email: str) -> None:
        self.email = email
        Contact.all_contacts.append(self)

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}(" f"{self.name!r}, {self.email!r}" f")")


# Ромбовидное наследование
class BaseClass:
    num_base_calls = 0

    def call_me(self) -> None:
        print("Calling method on BaseClass")
        self.num_base_calls += 1


class LeftSubclass(BaseClass):
    num_left_calls = 0

    def call_me(self) -> None:
        BaseClass.call_me(self)
        print("Calling method on LeftSubclass")
        self.num_left_calls += 1


class RightSubclass(BaseClass):
    num_right_calls = 0

    def call_me(self) -> None:
        BaseClass.call_me(self)
        print("Calling method on RightSubclass")
        self.num_right_calls += 1


class Subclass(LeftSubclass, RightSubclass):
    num_sub_calls = 0

    def call_me(self) -> None:
        LeftSubclass.call_me(self)
        RightSubclass.call_me(self)
        print("Calling method on Subclass")
        self.num_sub_calls += 1


s = Subclass()
s.call_me()
