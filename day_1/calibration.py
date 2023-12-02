class Input:
    def __init__(self):
        self.document = []
        with open("input", "r") as input:
            for line in input:
                self.document.append(line.strip())
        print(f"Loaded {len(self.document)} lines into the calibration document")


class Calibration(Input):
    def __init__(self):
        super().__init__()
        self.values = []

    def convert(self, s: str) -> str:
        # print(f"{s=}")
        if s == "one":
            s = "1"
        elif s == "two":
            s = "2"
        elif s == "three":
            s = "3"
        elif s == "four":
            s = "4"
        elif s == "five":
            s = "5"
        elif s == "six":
            s = "6"
        elif s == "seven":
            s = "7"
        elif s == "eight":
            s = "8"
        elif s == "nine":
            s = "9"
        # print(f"{s=}")

        return s

    def calibrate(self, s: str) -> int:
        numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        numbers.extend(
            ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
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
        match_index = i + 1
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

        # I don't know if missing values is considered 0.
        # value = (
        #    int(f"{first_digit}{last_digit}")
        #    if last_digit != "0"
        #    else int(f"{first_digit}")
        # )
        value = int(f"{first_digit}{last_digit}")
        print(f"String: {s}")
        print(f"Calibration value: {value}")
        return value


def main():
    solution = Calibration()

    c = 1
    for s in solution.document:
        print(f"Line Number: {c}")
        solution.values.append(solution.calibrate(s))
        c = c + 1

    print(f"Sum of all calibration values is {sum(solution.values)}")


if __name__ == "__main__":
    main()
