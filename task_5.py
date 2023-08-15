# Задача 5. Назви класів у CamelCase

class CamelCase(type):

    def __new__(cls, name,  bases, attrs):

        if not name[0].isupper():
            raise TypeError("Class name not in CamelCase")

        return super().__new__(cls, name,  bases, attrs)


class notCamelCase(metaclass=CamelCase):
    pass  # Raises error: 'Class name not in CamelCase'
