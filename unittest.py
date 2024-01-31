from unittest.mock import MagicMock

mock = MagicMock()
mock[3] = 'fish'
mock.__setitem__.assert_called_with(3, 'fish')
mock.__getitem__.return_value = 'result'

'''exam[le of calling with return value and if I want to see the argument called '''
m = MagicMock(return_value=None)
m(1, 2, a='foo', b='bar')
m()
m.call_args_list
m.call_args_list == [call(1, 2, a='foo', b='bar'), call()]


''' example of udemy'''
import random
from unittest.mock import Mock,patch

class Programmer:
    def __init__(self):
        self.tech_names=[]
    def add_tech(self,tech_name):
        name = tech_name.lower()
        if name not in self.tech_names:
            self.tech_names.append(name)
        return self
    def get_random_tech(self):
        return random.choice (self.tech_names)

programme = Programmer
programme.add_tech('python')
programme.add_tech('sql')

'''now im going to mock the random,choise to retuen python always '''

random.choice = Mock(return_value = 'python')
print(programme.get_random_tech())