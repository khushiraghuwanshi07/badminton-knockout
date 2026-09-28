# BADMINTON KNOCKOUT FIXTURE
# For N players with BYE

players = []

n = int(input("Enter number of players: "))

for i in range(n):
    name = input("Enter player name: ")
    players.append(name)

# Find next power of 2
total = 1
while total < n:
    total = total * 2

# Calculate BYEs
byes = total - n

print("\n================================")
print("       BADMINTON FIXTURE")
print("================================")

print("Total Players :", n)
print("Total BYEs     :", byes)

# Add BYE to make number of players a power of 2
for i in range(byes):
    players.append("BYE")

round_no = 1
current_players = players

while len(current_players) > 1:

    print("\n---------- ROUND", round_no, "----------")

    next_round = []
    match_no = 1

    for i in range(0, len(current_players), 2):

        p1 = current_players[i]
        p2 = current_players[i + 1]

        if p1 == "BYE":
            print("Match", match_no, ":", p2, "gets BYE")
            next_round.append(p2)

        elif p2 == "BYE":
            print("Match", match_no, ":", p1, "gets BYE")
            next_round.append(p1)

        else:
            print("Match", match_no, ":", p1, "vs", p2)

            # Winner is entered by user
            winner = input("Enter winner: ")
            next_round.append(winner)

        match_no += 1

    current_players = next_round
    round_no += 1

print("\n================================")
print("       TOURNAMENT WINNER")
print("================================")
print(current_players[0])