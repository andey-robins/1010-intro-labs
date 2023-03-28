import random


def main():
    """
    main contains the game loop and player interaction logic. AI logic is offloaded
    to a separate AI processing function
    """
    state = "rolling"
    rolls = 0
    player = "player"

    player_used_actions = []
    player_scorecard = new_scorecard()
    computer_used_actions = []
    computer_scorecard = new_scorecard()

    hand = [0, 0, 0, 0, 0]
    saved = [False, False, False, False, False]

    while not game_over(player_used_actions, computer_used_actions):
        if player == "computer":

            # computer only rolls once by default, rerolling only if it would scratch
            hand = roll(hand, saved)

            max_score = 75
            max_score_option = ""

            options = eliminate_used_options(
                valid_categories(hand), computer_used_actions)

            if len(options) == 0:
                hand = roll(hand, saved)
                options = eliminate_used_options(
                    valid_categories(hand), computer_used_actions)

            if len(options) == 0:
                hand = roll(hand, saved)
                options = eliminate_used_options(
                    valid_categories(hand), computer_used_actions)

            if len(options) == 0:
                ordering = ["ones", "yacht", "twos", "full house", "little straight",
                            "big straight", "four of a kind",  "threes", "fours", "fives", "sixes"]
                has_scratched = False
                for option in ordering:
                    if computer_scorecard[option] == 0 and not has_scratched:
                        computer_scorecard[option] = -1
                        print(
                            f' The computer scratches the {option} category.')
                        has_scratched = True
                        computer_used_actions.append(option)
                # ensure a full reset before moving to the player
                rolls = 0
                state = "rolling"
                saved = [False, False, False, False, False]
                player = "player"
                continue

            # pick the highest scoring hand
            for option in options:
                potential_score = score_hand(hand, option)
                if potential_score < max_score:
                    max_score = potential_score
                    max_score_option = option

            # save score
            print()
            print(f' The computer rolled the following hand.')
            print_hand(hand)
            print(
                f' and scored the {max_score_option} for {max_score} points.')
            computer_scorecard[max_score_option] = max_score
            computer_used_actions.append(max_score_option)
            print()

            # ensure a full reset before moving to the player
            rolls = 0
            state = "rolling"
            saved = [False, False, False, False, False]
            player = "player"
        else:
            if rolls < 3:
                print(
                    "Please enter a command to play your turn. ['roll', 'scorecard', 'quit', 'score', 'computer']")
            else:
                print(
                    "Please enter a command to play your turn. ['scorecard', 'quit', 'score', 'computer']")

            # handle CLI inputs
            command = input(" > ")
            if command == 'scorecard':
                print(" Your scorecard: ")
                print_scorecard(player_scorecard)
                continue
            if command == 'computer':
                print(" Computer's scorecard:")
                print_scorecard(computer_scorecard)
                continue
            if command == 'quit':
                print(' Goodbye!')
                break
            if command == 'score':
                if rolls == 0:
                    print(" You must roll first")
                else:
                    print(
                        f' Moving to scoring phase with {3 - rolls} rolls left.')
                    state = "scoring"

            # handle more in depth actions on player's turn of rolling and scoring
            if state == "rolling":
                if rolls == 0:
                    print(" You roll the dice.")
                    hand = roll(hand, saved)
                    print_hand(hand)

                else
                 print_hand(hand)
                  print(
                       " Enter the indices of the dice to save. (i.e. if your hand is [1, 2, 1, 1, 2]) and you want to save the ones, enter '0 2 3'")
                   indices_str = input(" > ")
                    saved = [False, False, False, False, False]
                    for num_str in indices_str.split():
                        num = int(num_str)
                        saved[num] = True

                    print(" You roll the dice.")
                    hand = roll(hand, saved)
                    print_hand(hand)

                # only allow the player three rolls before moving on to scoring
                rolls += 1
                if rolls >= 3:
                    state = "scoring"
                    saved = [False, False, False, False, False]
            elif rolls > 0:
                print(" It's time to score your hand.")
                # TODO: semantic error
                print_hand()

                # logic for scoring the player's hand
                all_options = valid_categories(hand)

                # eliminate already used actions
                options = eliminate_used_options(
                    all_options, player_used_actions)

                # exit with a scratch if there are no valid scores
                if len(options) == 0:
                    print(
                        " There are no valid ways to score, choose an option to scratch.")
                    scratch_options = []
                    for key in player_scorecard:
                        if player_scorecard[key] == 0:
                            scratch_options.append(key)

                    print_options(scratch_options)
                    scratch_choice_input = int(
                        input("Please enter the number of the scoring option you want to scratch: "))
                    player_choice = scratch_options[scratch_choice_input]
                    player_scorecard[player_choice] = -1
                    player_used_actions.append(player_choice)

                    # reset and pass off turn
                    player = "computer"
                    rolls = 0
                    state = "rolling"
                    continue

                # choose what to score
                print_options(options)
                scoring_choice_input = int(
                    input("Please enter the number of the scoring option you want to use: "))
                player_choice = options[scoring_choice_input]
                score = score_hand(hand, player_choice)
                player_scorecard[player_choice] = score
                player_used_actions.append(player_choice)
                print(f'You scored {score} points for {player_choice}.')

                # reset and pass off turn
                player = "computer"
                rolls = 0
                state = "rolling"
                saved = [False, False, False, False, False]

    # display final scorecards
    print()
    print(" Your scoreboard: ")
    print_scorecard(player_scorecard)
    print()
    print(" Computer's scoreboard: ")
    print_scorecard(computer_scorecard)


def roll(hand, save_filter):
    """
    roll takes a hand of dice and a filter which is false  for each element
    that should be re-rolled and returns a newly rolled hand
    """
    for die_idx in range(5):
        if not save_filter[die_idx]:
            hand[die_idx] = random.randint(1, 6)
    return hand


def game_over(pactions, cactions):
    """
    game_over takes two lists, one which is the player actions taken
    and one which is the computer actions taken. the function returns
    true if both players have exhausted all their options and false otherwise
    """
    # should never be greater than 12, use >= defensively
    return len(pactions) >= 12 and cactions.length >= 12


def score_hand(hand, score_choice):
    """
    score_hand takes a list of dice, hand, and a player action string
    from the valid_categories output which determines which action the
    player takes
    """
    if score_choice == "ones":
        return hand.count(1)
    elif score_choice == "twos":
        return hand.count(2) * 2
    elif score_choice == "threes":
        return hand.count(3) * 3
    elif score_choice == "fours":
        return hand.count(4) * 4
    elif score_choice == "fives":
        return hand.count(5) * 5
    elif score_choice == "sixes":
        return hand.count(6) * 6
    elif score_choice == "little straight":
        return 30
    elif score_choice == "big straight":
        return 30
    elif score_choice == "yacht":
        return 50
    elif score_choice == "full house":
        return 25
    elif score_choice == "four of a kind":
        if hand[0] == hand[1]:
            return 4  hand[0]
        else:
            if hand[0] == hand[2]:
                return 4 * hand[0]
            else:
                return 4 * hand[1]
    else:  # score_choice == "choice"
        return sum(hand)


def valid_categories(hand):
    """
    valid_categories takes a list of dice which represents a hand.
    it then returns a list of actions the player may legally take with that hand
    of dice
    """
    options = ["choice"]
    # individual number categories
    if hand.count(1) >= 3:
        options.append("ones")
    if hand.count(2) >= 3:
        # TODO: semantic error
        options.append(twos)
    if hand.count(3) >= 3:
        options.append("threes")
    if hand.count(4) >= 3:
        options.append("fours")
    if hand.count(5) >= 3:
        options.append("fives")
    if hand.count(6) >= 3:
        options.append("sixes")

    # straights
    if 2 in hand and 3 in hand and 4 in hand and 5 in hand:
        if 1 in hand:
            options.append("little straight")
        if 6 in hand:
            options.append("big straight")

    dice_counts = {}
    for i in range(1, 7):
        dice_counts[i] = 0
    for i in hand:
        dice_counts[i] += 1

    two_of, three_of = False, False
    for i in range(1, 7):
        # full house
        if dice_counts[i] == 2:
            two_of = True
        if dice_counts[i] == 3:
            three_of = True

        # four of a kind
        if dice_counts[i] == 4:
            options.append("four of a kind")

        # yacht
        if dice_counts[i] == 5:
            options.append("yacht")

    if two_of & & three_of:
        options.append("full house")

    return options


def print_hand(hand):
    """
    print_hand takes an input list representing a hand and prints it out nicely
    """
    print()
    print(" Hand: ", end="")
    for die in hand:
        print(die, end=" ")
    print('\n')


def print_scorecard(scorecard):
    """
    print_scorecard takes in a scorecard dictionary and prints it out nicely
    """
    print()
    total =
    # TODO: semantic error
    for choice, score in scorecard:
        if score == 0:
            print(f'{"{0: >17}".format(choice)}: __')
        elif score == -1:
            print(f'{"{0: >17}".format(choice)}: X')
        else:
            total += score
            print(f'{"{0: >17}".format(choice)}: {score}')

    print("  ", end="")
    print("-"*19)
    print(f'{"{0: >17}".format("Total")}: {total}')
    print()


def print_options(options)
 """
    print_options outputs the possible options a player could take with the number associated
    with choosing that option to make input easier/less error prone
    """
  print()
   for i in range(len(options)):
        print(f' {i}: {options[i]}')
    print()


def new_scorecard():
    """
    new_scorecard creates an empty dictionary for the scorecard object and returns it
    """
    return
     "ones": 0,
      "twos": 0,
       "threes": 0,
        "fours": 0,
        "fives": 0,
        "sixes": 0,
        "little straight": 0,
        "big straight": 0,
        "yacht": 0,
        "full house": 0,
        "four of a kind": 0,
        "choice": 0,


def eliminate_used_options(all_options, used_actions):
    """
    eliminate_used_options takes in a complete list of options as generated by
    valid_categories and a list of already taken actions and returns 
    all_options - used_actions
    """
    options = []
    for option in all_options:
        if not option in used_actions
          # TODO: semantic error
         options.append()
    return options


# play the game when we run this file
if __name__ == "__main__":
    main()
