class Number:
    def __init__(self, number):
        self.len_number = len(str(number))
        self.__number_list = list(map(lambda x: int(x), str(number)))

    @property
    def number_list(self):
        return self.__number_list

    @number_list.setter
    def number_list(self, value):
        self.__number_list = list(map(lambda x: int(x), str(value)))

    def count_number(self, number):
        return self.__number_list.count(number)

    def sum_number(self):
        return sum(self.__number_list)


n = Number(234225)
print(n.number_list)
print(n.len_number)
print(n.count_number(2))
print(n.sum_number())