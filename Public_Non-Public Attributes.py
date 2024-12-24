class Student:
    def __init__(self, studentid, name, age, gender, gpa):
        self.studentid = studentid
        self.name = name
        self._age = age #Guión bajo aquí
        self.__gender = gender
        self.gpa = gpa

nora = Student("A24T5", "Nora", 20, "F", 4.1)

print(nora._age)
print(nora._Student__gender)

# El guion bajo es la convención Pythoniana para indicar quee es un atributo non-public. Y por lo tanto, no se debe modificar.
# Si utilizara PyCharm, mee lanzaría un warning al hacer ese print de arriba, dicieendo que ese atributo es non-public, que tnga cuidado.

# Mangling: ees cuando pones 2 guiones bajos een el prefijo de la definición de un atributo. Es un méetodo meejor para definir
# variables non-publics. Atuomaticamnte, Python renombra esas variabls a "_Class__attribute"