from messages_8_9 import *
#import messages_8_9 as msgs

text_messages = ["When should we meet?", '21:00 at Carols', "Hello?"]
text_messages.append("Wazzup?")

show_messages(text_messages)

sent_messages = []
send_messages(text_messages, sent_messages)

show_messages(text_messages)
show_messages(sent_messages)
