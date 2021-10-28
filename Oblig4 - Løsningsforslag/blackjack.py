import blackjack_module as bjm


def initialize_round():
    global deck, player_hand, dealer_hand
    print('\n' * 80)  # prints 80 line breaks
    deck = bjm.get_new_shuffled_deck()

    player_hand = []
    dealer_hand = []

    print(f"***********************************")
    print(f"*************BlackJack*************")
    print(f"***********************************")


def take_bets():
    global bet
    valid_bet = False
    while not valid_bet:
        bet = input(f"\nHow many chips do you want to bet (between 1 and {chips})? ")
        try:
            bet = int(bet)
        except ValueError:
            print("\nYou did not enter a valid number")
            continue
        valid_bet = 1 <= bet <= chips

        if not valid_bet:
            print(f"\n{bet} is an invalid amount of chips. You have {chips} chips")
        else:
            print(f"\nYou bet {bet} out of {chips} chips")


def did_player_get_blackjack():
    global chips
    if bjm.calculate_hand_value(player_hand) == 21:  # Did the player get blackjack?
        chips = bjm.end_result(player_hand, dealer_hand, chips=chips, bet=bet, cards_just_dealt=True)
        input()
        return True

    return False


def deal_initial_hands():
    bjm.deal_cards(deck, player_hand, 2)
    bjm.deal_cards(deck, dealer_hand, 2)

    print(f"\nThe cards have been dealt.")
    bjm.print_hand(dealer_hand, bjm.Tcolors.DEALER, True)
    bjm.print_hand(player_hand)


def hit_or_stand_loop():
    should_continue_hit_or_stand = True
    while should_continue_hit_or_stand:
        choice = input("\nWould you like to: \n1 - Hit\n2 - Stand\nAnswer: ")
        print('\n'*80)
        if choice == "1":  # Hit
            should_continue_hit_or_stand = hit()
        elif choice == "2":  # Stand
            stand()
            should_continue_hit_or_stand = False
        else:
            print("\nInvalid choice")


def hit():
    global chips
    print("\nYou chose to hit")
    bjm.deal_card(deck, player_hand)  # Hit the player with a new card

    bjm.print_hand(dealer_hand, bjm.Tcolors.DEALER, True)
    bjm.print_hand(player_hand)

    if bjm.calculate_hand_value(player_hand) > 21:  # The player busted
        chips = bjm.end_result(player_hand, dealer_hand, chips, bet)
        return False

    return True


def stand():
    global chips
    print("\nYou chose to stand")
    bjm.print_hand(player_hand)

    print("\nThe dealer flips their hidden card over")
    bjm.print_hand(dealer_hand, bjm.Tcolors.DEALER)
    input()

    while bjm.calculate_hand_value(dealer_hand) < 17:
        bjm.deal_card(deck, dealer_hand)
        input()

    chips = bjm.end_result(player_hand, dealer_hand, chips, bet)


def continue_or_quit():
    should_continue = input("\nDo you want to continue? (1 - Yes/2 - No)? ")
    if should_continue.lower() != '1':
        print("\nThank you for the game. Welcome back!")
        exit()


def is_player_out_of_chips():
    if chips <= 0:
        print("\nSorry, you're out of chips! *throwsyououtofcasino* (*・_・)ノ⌒*")
        exit()


chips, bet = 5, 0
deck, player_hand, dealer_hand = [], [], []

while True:
    initialize_round()

    take_bets()

    deal_initial_hands()

    if did_player_get_blackjack():
        continue

    hit_or_stand_loop()

    is_player_out_of_chips()

    continue_or_quit()
