red_truth = 12
green_truth = 13
blue_truth = 14

game = 0
total = 0
with open("input.txt", "r") as fp:
    for row in fp:
        game += 1
        valid_game = True
        round_str = row.split(": ")[1]
        rounds = round_str.split("; ")
        for rnd in rounds:
            red = 0
            green = 0
            blue = 0
            plays = rnd.split(", ")
            for play in plays:
                if "red" in play:
                    red = int(play.split(" ")[0])
                elif "green" in play:
                    green = int(play.split(" ")[0])
                elif "blue" in play:
                    blue = int(play.split(" ")[0])
            if red > red_truth or green > green_truth or blue > blue_truth:
                valid_game = False
                break
        if valid_game:
            total += game
print(total)