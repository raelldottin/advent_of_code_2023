class Solution:
    def __init__(self):
        self.data = []
        with open("input", "r") as file:
            self.data = [line.strip() for line in file]
        print(f"Loaded {len(self.data)} lines from input data")

    def is_adjacent(self, line, index, delta):
        new_index = index + delta
        if 0 <= new_index < len(line):
            char = line[new_index]
            return char != '.' and not char.isdigit()
        return False

    def adjacency(self, line_index, char_index):
        line = self.data[line_index]
        # Check adjacent characters on the same, previous, and next lines
        for i in range(-1, 2):
            if line_index + i >= 0 and line_index + i < len(self.data):
                for delta in (-1, 0, 1):
                    if self.is_adjacent(self.data[line_index + i], char_index, delta):
                        return True
        return False

    def solve(self):
        total_sum = 0
        for line_index, line in enumerate(self.data):
            number = []
            for char_index, char in enumerate(line):
                if char.isdigit():
                    number.append(char)
                    if (char_index == len(line) - 1 or not line[char_index + 1].isdigit()) and \
                       self.adjacency(line_index, char_index):
                        total_sum += int(''.join(number))
                        number = []

        print(f"Sum: {total_sum}")

def main():
    solution = Solution()
    solution.solve()

if __name__ == "__main__":
    main()
