# Задача 4: Контроль створення класу


class NoDunderAttributes(type):

    def __new__(cls, name, bases, attrs):
        for name_attrs in attrs:
            if name_attrs.startswith('__'):
                raise TypeError("Cannot have attribute names starting with '__'")

        return super().__new__(cls, name, bases, attrs)


class MyPrivateClass(metaclass=NoDunderAttributes):
    secret_attribute = 10
