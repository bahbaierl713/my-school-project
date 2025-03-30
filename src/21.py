class RandomClass:
    def add_numbers(self, *args):
        result = 0
        for num in args:
            if isinstance(num, int) or isinstance(num, float):
                result += num
            else:
                raise ValueError("All arguments must be numbers")
        return result

random_object = RandomClass()
print(random_object.add_numbers(1, 2.5, "hello", [4, 6]))
