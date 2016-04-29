import csv
import pygal

from board import Board


def make_win_chart():
    order_wins = 0
    chaos_wins = 0

    with open("results/results.csv") as result_file:
        reader = csv.reader(result_file, delimiter=",")
        header = next(reader)
        for row in reader:
            if row[0] == "order":
                order_wins += 1
            elif row[0] == "chaos":
                chaos_wins += 1
            else:
                raise KeyError("no match for " + row[0])

    print(order_wins, ":", chaos_wins)

    chart = pygal.Bar()
    chart.y_labels = range(0, 1000, 100)
    chart.add("order", order_wins)
    chart.add("chaos", chaos_wins)
    chart.render_to_file("results/wins.svg")


def make_order_move_count_chart():
    order_wins_move = [0 for _ in range(37)]
    chaos_wins_move = [0 for _ in range(37)]

    with open("results/results.csv") as result_file:
        reader = csv.reader(result_file, delimiter=",")
        header = next(reader)
        for row in reader:
            if row[0] == "order":
                order_wins_move[int(row[1])] += 1
            elif row[0] == "chaos":
                chaos_wins_move[int(row[1])] += 1
            else:
                raise KeyError("no match for " + row[0])

    print(order_wins_move)
    print(chaos_wins_move)

    chart = pygal.Bar()
    chart.add("No. moves to win", order_wins_move)
    chart.render_to_file("results/moves.svg")


def run():
    board = Board()
    for move in range(36):
        pos = board.add_a_random_piece()
        if board.has_move_won(pos):
            return ["order", move]
    return ["chaos", 36]


if __name__ == "__main__":
    with open("results/results.csv", "w") as result_file:
        writer = csv.writer(result_file, delimiter=",")
        writer.writerow(["winner", "moves"])
        for _ in range(1000):
            result = run()
            writer.writerow(result)

    make_win_chart()
    make_order_move_count_chart()
