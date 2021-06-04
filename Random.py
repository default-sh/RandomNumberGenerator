import time


class Random:
    def __init__(self, seed=None):
        if seed is None:
            self.seed = int(time.time() * (10 ** 7))
        else:
            try:
                self.seed = int(seed)
            except ValueError:
                raise ValueError("Please use a valid integer for the seed.")
        self.next_seed = 0

    def __generate_percentage(self):
        a = 134775813
        c = 1
        m = 2 ** 32

        if self.next_seed == 0:
            next_seed = (self.seed * a + c) % m
        else:
            next_seed = (self.next_seed * a + c) % m
        self.next_seed = next_seed
        random_percent = float(next_seed // m)
        return random_percent

    def choice(self, index: list):
        random_index = round((self.__generate_percentage() * (len(index) - 1)))
        return index[random_index]

    def randomint(self, minimum: int, maximum: int):
        index = [x for x in range(minimum, maximum + 1)]  # Generates a list of integers from the min to max.
        return self.choice(index)

    def randombytes(self, amount: int):
        if amount < 0:
            raise ValueError("Cannot use negative integers as input for byte amount.")

        else:
            frame = b''
            if amount < 0:
                raise ValueError("Cannot use negative integers as input for byte amount.")
            for _ in range(0, amount):
                frame += bytes([self.randomint(0, 255)])
            return frame
