# ex 8.9

messages = ['hey there', 'howdy', 'hola']
sent_messages = []
def show_messages(incoming_list):
    for message in messages:
        print(message)
        
# ex 8.9
def send_messages(incoming_list, sent_list):
    while incoming_list:
        current_msg = incoming_list.pop()
        print(f"{current_msg}")
        sent_list.append(current_msg)
        

send_messages(messages[:], sent_messages)
# ex 8.11
print(messages, sent_messages)