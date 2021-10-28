import random
import card_printer as cp


class Tcolors:
    PLAYER = '\033[96mplayer\033[0m'
    DEALER = '\033[92mdealer\033[0m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def print_win_string(quote):
    print(f"\n{Tcolors.OKBLUE}{quote}{Tcolors.ENDC}")


def print_lose_string(quote):
    print(f"\n{Tcolors.FAIL}{quote}{Tcolors.ENDC}")


full_deck = {"Two of clubs": 2, "Three of clubs": 3, "Four of clubs": 4, "Five of clubs": 5, "Six of clubs": 6,
             "Seven of clubs": 7, "Eight of clubs": 8, "Nine of clubs": 9, "Ten of clubs": 10,
             "Jack of clubs": 10, "Queen of clubs": 10, "King of clubs": 10, "Ace of clubs": 11,
             "Two of diamonds": 2, "Three of diamonds": 3, "Four of diamonds": 4, "Five of diamonds": 5,
             "Six of diamonds": 6, "Seven of diamonds": 7, "Eight of diamonds": 8, "Nine of diamonds": 9,
             "Ten of diamonds": 10, "Jack of diamonds": 10, "Queen of diamonds": 10, "King of diamonds": 10,
             "Ace of diamonds": 11,
             "Two of hearts": 2, "Three of hearts": 3, "Four of hearts": 4, "Five of hearts": 5, "Six of hearts": 6,
             "Seven of hearts": 7, "Eight of hearts": 8, "Nine of hearts": 9, "Ten of hearts": 10,
             "Jack of hearts": 10, "Queen of hearts": 10, "King of hearts": 10, "Ace of hearts": 11,
             "Two of spades": 2, "Three of spades": 3, "Four of spades": 4, "Five of spades": 5, "Six of spades": 6,
             "Seven of spades": 7, "Eight of spades": 8, "Nine of spades": 9, "Ten of spades": 10,
             "Jack of spades": 10, "Queen of spades": 10, "King of spades": 10, "Ace of spades": 11,
             }


def get_new_shuffled_deck():
    deck = list(full_deck.keys())
    random.shuffle(deck)
    return deck


def get_card_value(card):
    return full_deck[card]


def calculate_hand_value(hand):
    hand_value = 0
    number_of_aces = 0

    for card in hand:
        hand_value += get_card_value(card)
        if "Ace" in card:
            number_of_aces += 1

    while number_of_aces and hand_value > 21:
        hand_value -= 10
        number_of_aces -= 1

    return hand_value


def deal_cards(deck, hand, number_of_cards):
    for i in range(number_of_cards):
        hand.append(deck.pop())


def deal_card(deck, hand):
    card = deck.pop()
    hand.append(card)
    print(f"Drawn card:")
    print(cp.ascii_version_of_card(hand[-1:]))


def end_result(player_hand, dealer_hand, chips=0, bet=0, cards_just_dealt=False):
    print('\n' * 80)
    print(f"**********************")
    print(f"****END SUMMARY:******")
    print(f"**********************")
    print_hand(dealer_hand, Tcolors.DEALER)
    print_hand(player_hand)
    return print_result_and_update_chips(calculate_hand_value(player_hand), calculate_hand_value(dealer_hand), chips,
                                         bet, cards_just_dealt)


def print_result_and_update_chips(player_hand_value, dealer_hand_value, chips=0, bet=0, cards_just_dealt=False):
    chip_string = "You {} {} chips and now have {} chips".format({}, {}, {})

    if player_hand_value == 21 and cards_just_dealt:
        chips += bet*2
        print_win_string(chip_string.format("won", bet*2, chips))
        print_win_string("You got blackjack! Congratulations, you win!")
    elif player_hand_value > 21:
        chips -= bet
        print_lose_string(chip_string.format("lost", bet, chips))
        print_lose_string("You busted! :( You lose!")
    elif dealer_hand_value > 21:
        chips += bet
        print_win_string(chip_string.format("won", bet, chips))
        print_win_string("Dealer busted! You win!")
    elif dealer_hand_value < player_hand_value:
        chips += bet
        print_win_string(chip_string.format("won", bet, chips))
        print_win_string("You have the better hand. You win!")
    elif player_hand_value < dealer_hand_value:
        chips -= bet
        print_lose_string(chip_string.format("lost", bet, chips))
        print_lose_string("The dealer has the better hand. You lose!")
    elif player_hand_value == dealer_hand_value:
        print(f"\nYou bet {bet} chips, but didn't lose any. You have {chips} chips left.")
        print(f"\nYour hand is the same as the dealer's. Noone wins!")

    return chips


def print_hand(hand, whos_hand=Tcolors.PLAYER, hide_first_card=False):
    hand_value = calculate_hand_value(hand)

    if hide_first_card:
        hand_value = get_card_value(hand[-1])
        # whos_hand += " visible"

    print(f"\nThe {whos_hand} hand has a value of {hand_value}:")

    if hide_first_card:
        print(cp.ascii_version_of_hidden_card(hand))
    else:
        print(cp.ascii_version_of_card(hand))
