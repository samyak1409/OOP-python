print('\nhttps://www.w3resource.com/python-exercises/class-exercises/\n')


# 1)
import array
print(array.__dict__, '\n')


# 2)
class Class:
    pass


print(Class.__dict__, '\n')


# 3)
instance = Class()
print(instance.__dict__, '\n')


# 4)
from builtins import abs
print(abs.__doc__)
print(abs(-155), '\n')


# 5)
def student(first_name, last_name):
    return f'First Name: {first_name}\nLast Name: {last_name}\n'


print(student(first_name='Samyak', last_name='Jain'))


# 6)
def student_data(s_id, **kwargs):
    print('S_ID:', s_id)
    if kwargs:
        for k, v in kwargs.items():
            print(f'{k.upper()}:', v)


student_data(s_id=149)
print()
student_data(s_id=143, s_name='Samyak Jain', s_class='Final Year')
