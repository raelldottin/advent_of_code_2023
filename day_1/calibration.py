class Input:
    def __init__(self):
        self.document = list(open("input", "r"))
        print(f"Loaded {len(self.document)} lines into the calibration document")


class Calibration(Input):
    def __init__(self):
        super().__init__()
        self.values = []

    def convert(self, s: str) -> str:
        # print(f"{s=}")
        table = { "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        }
        

        return table[s]

    def calibrate(self, s: str, part: int = 1) -> int:
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        if part == 2:
            numbers.extend(
                [
                    "zero",
                    "one",
                    "two",
                    "three",
                    "four",
                    "five",
                    "six",
                    "seven",
                    "eight",
                    "nine",
                ]
            )
        first_digit = "0"
        last_digit = "0"

        i = 0
        match = False
        while i < len(s):
            for number in numbers:
                if s[i : i + len(number)] == number:
                    first_digit = s[i : i + len(number)]
                    match = True
                    break

            if match:
                break

            i = i + 1

        match = False
        i = len(s)
        while i > 0:
            for number in numbers:
                if s[i - len(number) : i] == number:
                    last_digit = s[i - len(number) : i]
                    match = True
                    break
            if match:
                break

            i = i - 1

        first_digit = self.convert(first_digit)
        last_digit = self.convert(last_digit)

        value = int(f"{first_digit}{last_digit}")
        # print(f"String: {s}")
        # print(f"Calibration value: {value}")
        return value


def main():
    values = []
    part1 = Calibration()
    c = 1
    for s in part1.document:
        values.append(part1.calibrate(s))
        c = c + 1
    print(f"Sum of all calibration values for part 1 is {sum(values)}")

    values = []
    part2 = Calibration()
    c = 1
    for s in part2.document:
        values.append(part2.calibrate(s, 2))
        c = c + 1
    print(f"Sum of all calibration values for part 2 is {sum(values)}")


if __name__ == "__main__":
    main()
