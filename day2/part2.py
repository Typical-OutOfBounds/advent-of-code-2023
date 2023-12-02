game = 0
total = 0
with open("input.txt", "r") as fp:
    for row in fp:
        game += 1
        valid_game = True
        round_str = row.split(": ")[1]
        rounds = round_str.split("; ")
        red_max = 0
        green_max = 0
        blue_max = 0
        for rnd in rounds:
            plays = rnd.split(", ")
            for play in plays:
                if "red" in play:
                    red = int(play.split(" ")[0])
                    if red > red_max:
                        red_max = red
                elif "green" in play:
                    green = int(play.split(" ")[0])
                    if green > green_max:
                        green_max = green
                elif "blue" in play:
                    blue = int(play.split(" ")[0])
                    if blue > blue_max:
                        blue_max = blue
        power = red_max * green_max * blue_max
        total += power
print(total)