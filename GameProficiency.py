def calculate_rank():
    while True:
        wins_value = int(input("Enter the number of wins: "))
        games_played_value = int(input("Enter the number of games played: "))
        
        # wins_value must not exceed games_played_value
        if games_played_value >= wins_value:
            break
        else:
            print("Invalid input. The number of games played must not be less than the number of wins. Please try again.")

    #membership functions for wins
    low_wins_membership = max(0, min((10 - wins_value) / 10, 1))
    medium_wins_membership = max(0, min((wins_value - 10) / 20, 1))
    high_wins_membership = max(0, min((wins_value - 30) / 30, 1))

    #membership functions for games played
    low_games_membership = max(0, min((10 - games_played_value) / 10, 1))
    medium_games_membership = max(0, min((games_played_value - 10) / 30, 1))
    high_games_membership = max(0, min((games_played_value - 40) / 30, 1))

    #fuzzy logic rules
    rule1 = min(low_wins_membership, low_games_membership)
    rule2 = min(medium_wins_membership, low_games_membership)
    rule3 = min(high_wins_membership, low_games_membership)
    rule4 = min(low_wins_membership, medium_games_membership)
    rule5 = min(medium_wins_membership, medium_games_membership)
    rule6 = min(high_wins_membership, medium_games_membership)
    rule7 = min(low_wins_membership, high_games_membership)
    rule8 = min(medium_wins_membership, high_games_membership)
    rule9 = min(high_wins_membership, high_games_membership)

    #centroid defuzzification
    numerator = (
        rule1 * 5 + rule2 * 20 + rule3 * 40 +
        rule4 * 20 + rule5 * 50 + rule6 * 70 +
        rule7 * 40 + rule8 * 70 + rule9 * 90
    )
    denominator = rule1 + rule2 + rule3 + rule4 + rule5 + rule6 + rule7 + rule8 + rule9

    if denominator != 0:
        fuzzy_result = numerator / denominator
    else:
        fuzzy_result = 0

    # linguistic label
    if fuzzy_result <= 15:
        result = 'a Happy Noob'
    elif fuzzy_result <= 35:
        result = 'a Determined Rookie'
    elif fuzzy_result <= 60:
        result = 'a Hungry Veteran'
    elif fuzzy_result <= 80:
        result = 'an Evil Warlord'
    elif fuzzy_result <= 90:
        result = 'a BurnOut' 
    elif fuzzy_result <= 100:
        result = 'in Gamer Utopia'
    else:
        result = 'Unknown'

    #value of rules
    # print(f"rule1: {rule1}")
    # print(f"rule2: {rule2}")
    # print(f"rule3: {rule3}")
    # print(f"rule4: {rule4}")
    # print(f"rule5: {rule5}")
    # print(f"rule6: {rule6}")
    # print(f"rule7: {rule7}")
    # print(f"rule8: {rule8}")
    # print(f"rule9: {rule9}")
    # print(f"numerator: {numerator}")
    # print(f"denominator: {denominator}")
    # print(f"---------------------------")
    
    
    #crisp output
    formatted_result = "{:.2f}".format(fuzzy_result)
    print(f"Player's Game Proficiency: {formatted_result}")
    print(f"You are {result}!!")

while True:
    print()
    print("===== Fuzzy Rank Calculator Menu =====")
    print("1. Calculate Rank")
    print("2. Exit")

    choice = input("Enter your choice (1-2): ")

    if choice == '1':
        calculate_rank()
    elif choice == '2':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1 or 2.")
