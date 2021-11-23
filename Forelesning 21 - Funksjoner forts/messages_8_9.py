def show_messages(messages):
    print("\nPrinting all messages:")
    for message in messages:
        print(message)


def send_messages(messages, sent_messages):
    print("\nSending messages:")
    while messages:  # len(messages) > 0:
        current_message = messages.pop(0)
        print(current_message)
        sent_messages.append(current_message)


if __name__ == '__main__':
    text_messages = ["When should we meet?", '21:00 at Carols', "Hello?"]
    text_messages.append("Wazzup?")

    show_messages(text_messages)

    # print("Inside main 8.9")


# print("HELLO FROM 8.9")