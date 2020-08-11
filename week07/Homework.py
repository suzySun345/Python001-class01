from abc import ABCMeta,abstractmethod
class Animal(metaclass=ABCMeta):

    def __init__(self, a_type, shape, nature):
        self.a_type = a_type
        self.shape = shape
        self.nature = nature

    @property
    def is_feral(self):
        shape_dic = {'大':3,'小':1,'中等':2}
        shape_int = shape_dic[self.shape]
        print(shape_int)
        if self.a_type == '食肉' and  shape_int >= 2 and self.nature == '凶猛':
            return True
        else:
            return False


class Cat(Animal):
    sound = 'miao'
    def __init__(self, name, a_type, shape, nature):
        self.name = name
        super().__init__(a_type, shape, nature)
        
    @property
    def is_pet(self):
        if self.nature == '温顺':
            return True
        else:
            return False


class Zoo:
    animal_type = []
    def __init__(self, name ):
        self.name = name
    
    def __getattr__(self):
        pass
    
    def add_animal(self, name):
        print(type(name).__name__)
        if not type(name).__name__ in Zoo.animal_type:
            Zoo.animal_type.append(type(name).__name__)
            
        else:
            print("已经有该动物类型")

if __name__ == '__main__':

    z = Zoo('时间动物园')

    cat1 = Cat('Nini', '食肉', '小', '温顺')
    cat2 = Cat('Nini', '食肉', '小', '温顺')

    z.add_animal(cat1)
    z.add_animal(cat2)
    print(cat1.is_feral)
    print(cat1.is_pet)
