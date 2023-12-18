class Input:
    def __init__(self):
        self.data = []
        with open("input", "r") as input:
            for line in input:
                self.data.append(line.strip())
        print(f"Loaded {len(self.data)} lines from input data")


class Solution(Input):
    def __init__(self):
        super().__init__()

    def is_adjacent(self, data, line_index, char_index, delta):
        """
        Check if the character at a specific position is not '.' and not a digit.
        """
        new_index = char_index + delta
        if 0 <= new_index < len(data[line_index]):
            char = data[line_index][new_index]
            return char != "." and not char.isdigit()
        return False

    def adjacency(self, data, line_index, character_index) -> bool:
        # Check left and right on the current line
        if self.is_adjacent(data, line_index, character_index, -1) or \
           self.is_adjacent(data, line_index, character_index, 1):
            return True

        # Check the previous line
        if line_index > 0:
            for delta in (-1, 0, 1):
                if self.is_adjacent(data, line_index - 1, character_index, delta):
                    return True

        # Check the next line
        if line_index < len(data) - 1:
            for delta in (-1, 0, 1):
                if self.is_adjacent(data, line_index + 1, character_index, delta):
                    return True

        return False


    def solve(self):
        sum = 0
        for line_index, line in enumerate(self.data):
            future_index = 0
            number = []
            match = False
            for character_index, character in enumerate(line):
                if match and not line[character_index].isdigit():
                    print(f"Line {line_index + 1}: {character=} {number=} {match=}")
                    sum = sum + int(''.join(number))
                    number = []
                    match = False
                if line[character_index].isdigit():
                    prev_match = match
                    match = self.adjacency(self.data, line_index, character_index)
                    if not match and prev_match:
                        match = prev_match
                    number.append(line[character_index])
                    future_index = character_index
                    character_index = character_index + 1

        print(f"Sum: {sum}")

def main() -> None:
    answer = Solution()
    answer.solve()


if __name__ == "__main__":
    main()
