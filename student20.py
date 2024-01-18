# Moves get_student into Student class


class Student:
    def __init__(self, nom:str, maison:str):
        self.nom = nom
        self.maison = maison

    def __str__(self):
        return f"{self.nom} de {self.maison}"

    @classmethod
    def get(cls):
        name = input("Nom: ")
        house = input("Maison: ")
        return cls(name, house)

def main():
    student = Student.get()
    print(student)

if __name__ == "__main__":
    main()