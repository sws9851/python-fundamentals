import datetime


class Email:
    def __init__(self, sender: "User", receiver: "User", subject: str, body: str) -> None:
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.timestamp = datetime.datetime.now()
        self.read = False

    def mark_as_read(self) -> None:
        self.read = True

    def display_full_email(self) -> None:
        """Print the email in full. Opening it also marks it as read."""
        self.mark_as_read()
        print("\n--- Email ---")
        print(f"From: {self.sender.name}")
        print(f"To: {self.receiver.name}")
        print(f"Subject: {self.subject}")
        print(f"Received: {self.timestamp.strftime('%Y-%m-%d %H:%M')}")
        print(f"Body: {self.body}")
        print("------------\n")

    def __str__(self) -> str:
        status = "Read" if self.read else "Unread"
        return f"[{status}] From: {self.sender.name} | Subject: {self.subject} | Time: {self.timestamp.strftime('%Y-%m-%d %H:%M')}"


class Inbox:
    def __init__(self) -> None:
        self.emails: list[Email] = []

    def receive_email(self, email: Email) -> None:
        self.emails.append(email)

    def list_emails(self) -> None:
        if not self.emails:
            print("Your inbox is empty.\n")
            return
        print("\nYour Emails:")
        for i, email in enumerate(self.emails, start=1):
            print(f"{i}. {email}")

    def _is_valid(self, index: int) -> bool:
        """Check a 1-based index, printing the reason if it fails."""
        if not self.emails:
            print("Inbox is empty.\n")
            return False
        if not 1 <= index <= len(self.emails):
            print("Invalid email number.\n")
            return False
        return True

    def read_email(self, index: int) -> None:
        if not self._is_valid(index):
            return
        self.emails[index - 1].display_full_email()

    def delete_email(self, index: int) -> None:
        if not self._is_valid(index):
            return
        del self.emails[index - 1]
        print("Email deleted.\n")


class User:
    def __init__(self, name: str) -> None:
        self.name = name
        self.inbox = Inbox()

    def send_email(self, receiver: "User", subject: str, body: str) -> None:
        email = Email(sender=self, receiver=receiver, subject=subject, body=body)
        receiver.inbox.receive_email(email)
        print(f"Email sent from {self.name} to {receiver.name}!\n")

    def check_inbox(self) -> None:
        print(f"\n{self.name}'s Inbox:")
        self.inbox.list_emails()

    def read_email(self, index: int) -> None:
        self.inbox.read_email(index)

    def delete_email(self, index: int) -> None:
        self.inbox.delete_email(index)


def main() -> None:
    tory = User("Tory")
    ramy = User("Ramy")

    tory.send_email(ramy, "Hello", "Hi Ramy, just saying hello!")
    ramy.send_email(tory, "Re: Hello", "Hi Tory, hope you are fine.")

    ramy.check_inbox()
    ramy.read_email(1)
    ramy.delete_email(1)
    ramy.check_inbox()


if __name__ == "__main__":
    main()
