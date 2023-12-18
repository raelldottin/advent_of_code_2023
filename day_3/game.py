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

    def is_symbol_except_dot_or_digit(self, variable):
        return  variable != '.' and not variable.isdigit()

    def solve(self):
        for line_index, line in enumerate(self.data):
            future_index = 0
            for character_index, character in enumerate(line):
                if future_index > 0 and character_index <= future_index:
                    continue
                number = []
                if character.isdigit():
                    number.append(character)
                    print(f"{character=}")
                    while (character_index + 1) < len(line):
                        character_index = character_index + 1
                        if line[character_index].isdigit():
                            number.append(line[character_index])
                            future_index = character_index
                        else:
                            break
                    print(f"Line {line_index + 1}: {number=}")
                    continue
                if (character_index - 1) >= 0 and ((character_index - 1) < len(line)):
                    if (self.data[line_index][character_index - 1] != ".") and (not self.data[line_index][character_index - 1].isdigit()):
                        print(f"Match on line {line_index} and character {character_index - 1}: {self.data[line_index][character_index - 1]} {self.data[line_index][character_index]}")
                        continue
                if (character_index + 1) >= 0 and ((character_index + 1) < len(line)):
                    if (self.data[line_index][character_index + 1] != ".") and (not self.data[line_index][character_index + 1].isdigit()):
                        print(f"Match on line {line_index} and character {character_index + 1}: {self.data[line_index][character_index + 1]} {self.data[line_index][character_index]}")
                        continue
                #if (line[line_index][character_index] != ".") and (not line[character_index].isdigit()):
                #    print(f"Match on line {character_index}: {line[character_index]}")
                #if line_index - 1 >= 0 and line_index - 1 < len(self.data):
                #    if (character_index - 1) >= 0 and character_index - 1 < len(line):
                #        if (line[character_index - 1] != ".") and (not line[character_index - 1].isdigit()):
                #            print(f"Match on line {character_index - 1}: {line[character_index - 1]}")
                #    if (character_index + 1) >= 0 and character_index + 1 < len(line):
                #        if (line[character_index + 1] != ".") and (not line[character_index + 1].isdigit()):
                #            print(f"Match on line {character_index + 1}: {line[character_index + 1]}")
def main() -> None:
    answer = Solution()
    answer.solve()


if __name__ == "__main__":
    main()
