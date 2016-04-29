import csv


def run():
    board = Board()
    for move in range(36):
        pos = board.add_a_random_piece()
        if board.has_move_won(pos):
            return ["order", move]
    return ["chaos", 36]


if __name__ == "__main__":
    with open("results.csv", "w") as result_file:
        writer = csv.writer(result_file, delimiter=",")
        writer.writerow(["winner", "moves"])
        for _ in range(1000):
            result = run()
            writer.writerow(result)
