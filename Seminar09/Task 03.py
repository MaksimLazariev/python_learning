"""
Задача 2.

Реализовать метакласс, позволяющий создавать всегда один и тот же объект класса

"""


class DocMeta(type):
    def __init__(self, *args, **kwargs):
        self.__a = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__a is None:
            print("а не создан, создаем")
            self.__a = super().__call__(*args, **kwargs)
        else:
            print("a создан, копируем")
        return self.__a


class MyClass(metaclass=DocMeta):
    pass


obj_1 = MyClass()
obj_2 = MyClass()
obj_3 = MyClass()
obj_4 = MyClass()

print(obj_1 is obj_4)
