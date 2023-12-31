class Generator:
    def binary_generate(self, size: int) -> list[list[int]]:
        """
        Binary generator
        """
        if size <= 0:
            raise ValueError("Size must be greater than zero")

        result = []
        row = [0] * size

        index = 0
        while index >= 0:
            index = size - 1
            result.append(row.copy())
            # descrease index if number of rows is equal to 1
            while index >= 0 and row[index] == 1:
                index -= 1

            if index >= 0:
                row[index] = 1
                for i in range(index + 1, size):
                    row[i] = 0
        return result

    def combination(self, n: int, k: int) -> list[list[int]]:
        """
        Combination generator number
        """
        if n <= 0 and k <= 0 and k > n:
            raise ValueError(
                "n and k must be greater than zero. k must be less than n."
            )

        result = []
        row = list(range(1, k + 1))

        index = 0
        while index >= 0:
            index = k - 1
            result.append(row.copy())

            while index >= 0 and row[index] >= (n - k + index + 1):
                index -= 1

            if index >= 0:
                row[index] += 1
                for i in range(index + 1, k):
                    row[i] = row[i - 1] + 1

        return result

    def permutation(self, n: int) -> list[list[int]]:
        """
        Permutation
        """
        if n <= 0:
            raise ValueError("n must be > 0")

        result: list[list[int]] = []
        row = list(range(1, n + 1))

        return result


gen = Generator()
# print(gen.binary_generate(3))

print(gen.combination(5, 5))
