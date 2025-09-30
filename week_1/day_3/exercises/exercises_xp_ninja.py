class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []   
        self.messages = []       

   
    def call(self, other_phone):
        record = f"{self.phone_number} called {other_phone.phone_number}"
        print(record)
        self.call_history.append(record)

    def show_call_history(self):
        print("Call History:")
        for call in self.call_history:
            print(call)

   
    def send_message(self, other_phone, content):
        message = {
            "to": other_phone.phone_number,
            "from": self.phone_number,
            "content": content
        }
        self.messages.append(message)
        other_phone.messages.append(message)  
        print(f"Message sent from {self.phone_number} to {other_phone.phone_number}")

    def show_outgoing_messages(self):
        print(f"Outgoing messages from {self.phone_number}:")
        for msg in self.messages:
            if msg["from"] == self.phone_number:
                print(msg)

    def show_incoming_messages(self):
        print(f"Incoming messages for {self.phone_number}:")
        for msg in self.messages:
            if msg["to"] == self.phone_number:
                print(msg)

    def show_messages_from(self, number):
        print(f"Messages for {self.phone_number} from {number}:")
        for msg in self.messages:
            if msg["from"] == number and msg["to"] == self.phone_number:
                print(msg)

if __name__ == "__main__":
    phone1 = Phone("123-456")
    phone2 = Phone("789-000")
    phone3 = Phone("555-333")


    phone1.call(phone2)
    phone1.call(phone3)
    phone1.show_call_history()


    phone1.send_message(phone2, "Hey, how are you?")
    phone2.send_message(phone1, "I’m good, thanks!")
    phone3.send_message(phone1, "Call me back please!")

    print("\n--- Outgoing / Incoming / Filtered ---")
    phone1.show_outgoing_messages()
    phone1.show_incoming_messages()
    phone1.show_messages_from("555-333")

