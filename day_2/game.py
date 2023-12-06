class Input:
    def __init__(self):
        self.data = []
        with open("input", "r") as input:
            for line in input:
                self.data.append(line.strip())
        print(f"Loaded {len(self.data)} lines from input data")


class Game(Input):
    def __init__(self):
        super().__init__()

    def santize_data(self, data):
        record = {}
        for game in data:
            id, game = game.split(": ")
            id = int(id.split(" ")[1])
            record[id] = []
            game = game.split("; ")
            game = [s.split(", ") for s in game]

            for cubes_revealed in game:
                cubes = {}
                for set_of_cubes in cubes_revealed:
                    value, key = set_of_cubes.split(" ")
                    cubes[key] = int(value)

                record[id].append(cubes)

        return record

    def solution_part1(self, data, spec):
        sum = 0

        for id, record in data.items():
            flag = False

            for cubes_revealed in record:
                for key in spec:
                    if key in cubes_revealed:
                        if cubes_revealed[key] > spec[key]:
                            flag = True
                            break
            if flag:
                continue
            sum = sum + id
        return sum

    def solution_part2(self, data, spec):
        sum = {"total": 0}

        # Iterate through the game records
        for id, record in data.items():
            sum["power"] = 1
            # Create empty lists for the dice colors
            for color in spec:
                sum[color] = 0
            # get each set of cubes
            for cubes_revealed in record:
                # checking if each color exists in a set of cubes
                for color in spec:
                    if color in cubes_revealed:
                        # save the color to the list if it 

                        if sum[color] == 0:
                            sum[color] = cubes_revealed[color]
                        if cubes_revealed[color] > sum[color]:
                            sum[color] = cubes_revealed[color]

            for color in spec:
                if sum[color]:
                    sum["power"] = sum["power"] * sum[color] 

            sum["total"] = sum["total"] + sum["power"]

        return sum["total"]


def main():
    solution = Game()
    sum = solution.solution_part1(
        (solution.santize_data(solution.data)), {"red": 12, "green": 13, "blue": 14}
    )
    print(f"Part 1 sum of the IDs of possible games: {sum}")

    sum = solution.solution_part2(
        (solution.santize_data(solution.data)), {"red", "green", "blue"}
    )
    print(f"Part 2 sum of the IDs of possible games: {sum}")


if __name__ == "__main__":
    main()
