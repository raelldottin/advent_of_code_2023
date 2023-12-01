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

    def calibrate(self, s: str) -> int:
        i = 0
        numbers = [str(i) for i in range(1, 9)]
        first_digit = 0
        last_digit = 0
        while i < len(s):
            if s[i : i + 1] in numbers:
                first_digit = s[i : i + 1]
                break
            i = i + 1

        i = len(s)
        while i > 0:
            if s[i - 1 : i] in numbers:
                last_digit = s[i - 1 : i]
                break
            i = i - 1

        value = int(f"{first_digit}{last_digit}")
        print(f"{s=}{value=}")
        return int(f"{first_digit}{last_digit}")


def main():
    solution = Calibration()

    c = 1
    for s in solution.document:
        print(f"Line: {c}")
        solution.values.append(solution.calibrate(s))
        c = c + 1

    print(sum(solution.values))


if __name__ == "__main__":
    main()
