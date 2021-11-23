from messages_8_9 import send_messages

text_messages = ["Hello", "How are you?", "Something"]
sent_messages = []

send_messages(text_messages[-1:], sent_messages)

print(f"\nOriginal: {text_messages}")
print(f"Sent: {sent_messages}")
