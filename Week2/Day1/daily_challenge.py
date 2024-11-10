#Daily Challenge

class Farm:
    def __init__(self, farm_name):
        self.farm_name = farm_name
        self.animal = []

    def add_animal(self,*args):
        for arg in args:
            self.animal.append(arg)
        print(self.animal)

    def get_info(self):
        output = f'{self.farm_name} farm'
        print(output)
        return output

macdonald = Farm('Macdonald')
macdonald.add_animal('cow')

