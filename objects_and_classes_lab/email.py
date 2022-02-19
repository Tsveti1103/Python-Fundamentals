class Email:

    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


command_input = input()
emails = []
while command_input != "Stop":
    command_args = command_input.split()
    s = command_args[0]
    r = command_args[1]
    c = command_args[2]
    email = Email(s, r, c)
    emails.append(email)

    command_input = input()
indexes = list(map(int, input().split(", ")))
for i in range(len(emails)):
    current_email = emails[i]
    if i in indexes:
        current_email.send()
    current_email_info = current_email.get_info()
    print(current_email_info)
