import blackjack_module as bjm

chips = 5
while True:
    print("\n" * 80)
    # Initialize deck and hands
    deck = bjm.get_new_shuffled_deck()
    player_hand, dealer_hand = [], []

    valid_bet = False
    while not valid_bet:
        bet = input(f"You have {chips} chips how many do you wan to bet? \nBetween 1 and {chips}: ")
        try:
            bet = int(bet)
        except ValueError:
            print("\nYou did not enter a valid number")
            continue

        valid_bet = 1 <= bet <= chips

        if valid_bet:
            print(f"\nYou bet {bet} chips")
        else:
            print(f"\n{bet} is an invalid amount of chips. You have {chips} chips.")

    # Deal cards to player and dealer
    bjm.deal_cards(deck, player_hand, 2)
    bjm.deal_cards(deck, dealer_hand, 2)

    print("\nThe cards have been dealt.")

    # Print player and dealer hand (first dealer card hidden)
    bjm.print_hand(player_hand)
    bjm.print_hand(dealer_hand, bjm.Tcolors.DEALER, True)

    # Check if player got blackjack
    if bjm.calculate_hand_value(player_hand) == 21:
        print("BlackJack! You win!")
        chips += bet*2
        print(f"You won {bet*2} chips and now have {chips}")
        input()
        continue

    should_continue_hit_or_stand = True
    while should_continue_hit_or_stand:
        # Ask what the player want to do! Hit or stand?
        choice = input("Would you like to:\n1 - Hit\n2 - Stand\nAnswer: ")
        print("\n" * 80)

        if choice == "1":  # Hit
            print("\nYou chose hit.")
            bjm.deal_cards(deck, player_hand, 1)
            bjm.print_hand(player_hand)
            bjm.print_hand(dealer_hand, bjm.Tcolors.DEALER, True)
            if bjm.calculate_hand_value(player_hand) > 21:  # Check if player busted
                print("Oh no! You busted! :(")
                chips -= bet
                print(f"You lost {bet} chips and now have {chips}")
                should_continue_hit_or_stand = False
        elif choice == "2":  # Stand
            print("\nYou chose stand.")
            bjm.print_hand(player_hand)
            print("\nThe dealer reveals his hidden card")
            bjm.print_hand(dealer_hand, bjm.Tcolors.DEALER)
            bjm.print_hand(dealer_hand, bjm.Tcolors.DEALER)

            while bjm.calculate_hand_value(dealer_hand) < 17:
                bjm.deal_cards(deck, dealer_hand, 1)
                print(f"\nThe dealer got: {dealer_hand[-1]}")
                input()

            bjm.print_hand(dealer_hand, bjm.Tcolors.DEALER)
            bjm.print_hand(player_hand)

            chips = bjm.print_result_and_calculate_chips(bjm.calculate_hand_value(player_hand),
                                                 bjm.calculate_hand_value(dealer_hand),
                                                 chips, bet)
            should_continue_hit_or_stand = False
        else:
            print("\nInvalid choice")

    if chips == 0:
        print("\nSorry, you're out of chips! *throwsyououtofcasino* (*・_・)ノ⌒*")
        exit()

    should_continue = input("\nDo you want to continue? (1 - Yes /2 - No): ")
    if should_continue != "1":
        exit()