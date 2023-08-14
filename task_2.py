# Задача 2. Запис у журнал при створенні класу


class Meta(type):
    def __new__(cls, *args, **kwargs):
        print("Class 'MyClass' has been created")
        return super().__new__(cls, *args, **kwargs)


class MyClass(metaclass=Meta):
    pass
