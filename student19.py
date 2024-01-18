class Student:

    def __init__(self, name: str, house: str):
        self.name = name
        self.house = house

    def __str__(self) -> str:
        return f"{self.name} from {self.house}"

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        if not name:
            raise ValueError("Invalid name")
        self._name = name

    @property
    def house(self) -> str:
        return self.__house

    @house.setter
    def house(self, house: str) -> None:
        valid_houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin", "Quebec"]
        if house not in valid_houses:
            raise ValueError("Invalid house")
        self.__house = house


def get_student() -> Student:
    name:str = ("Name: ")
    house:str = input("House: ")
    student:Student = Student(name, house)
    return student


def main() -> None:
    student = get_student()
    print(student)


if __name__ == "__main__":
    main()
