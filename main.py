class MyClass:
    def __init__(self, p_1):
        self.p_1 = p_1


my_1 = MyClass(78)
my_2 = my_1
del my_1
print(my_2.p_1)
