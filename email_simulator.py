
import datetime


# Represents an individual email sent between two users
class Email:
    def __init__(self, sender, receiver, subject, body):
        # Store the sender, receiver, subject, and email body
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body

        # Record the date and time when the email is created
        self.timestamp = datetime.datetime.now()

        # Set the email's initial status to unread
        self.read = False

    # Changes the email's status to read
    def mark_as_read(self):
        self.read = True

    # Displays the complete contents of an email
    def display_full_email(self):
        # Mark the email as read when it is opened
        self.mark_as_read()

        print('\n--- Email ---')
        print(f'From: {self.sender.name}')
        print(f'To: {self.receiver.name}')
        print(f'Subject: {self.subject}')
        print(f"Received: {self.timestamp.strftime('%Y-%m-%d %H:%M')}")
        print(f'Body: {self.body}')
        print('------------\n')

    # Returns a short summary of the email
    # This is used when displaying the inbox email list
    def __str__(self):
        # Determine whether the email has been read
        status = 'Read' if self.read else 'Unread'

        return f"[{status}] From: {self.sender.name} | Subject: {self.subject} | Time: {self.timestamp.strftime('%Y-%m-%d %H:%M')}"


# Represents a user who can send, receive, and manage emails
class User:
    def __init__(self, name):
        # Store the user's name
        self.name = name

        # Create an inbox for the user
        self.inbox = Inbox()

    # Creates and sends an email to another user
    def send_email(self, receiver, subject, body):
        # Create a new email using the sender, receiver, subject, and body
        email = Email(sender=self, receiver=receiver, subject=subject, body=body)

        # Deliver the email to the receiver's inbox
        receiver.inbox.receive_email(email)

        print(f'Email sent from {self.name} to {receiver.name}!\n')

    # Displays all emails stored in the user's inbox
    def check_inbox(self):
        print(f"\n{self.name}'s Inbox:")
        self.inbox.list_emails()

    # Opens and reads an email using its position in the inbox
    def read_email(self, index):
        self.inbox.read_email(index)

    # Deletes an email using its position in the inbox
    def delete_email(self, index):
        self.inbox.delete_email(index)


# Represents an inbox that stores and manages received emails
class Inbox:
    def __init__(self):
        # Create an empty list to store received emails
        self.emails = []

    # Adds a newly received email to the inbox
    def receive_email(self, email):
        self.emails.append(email)

    # Displays a numbered list of all emails in the inbox
    def list_emails(self):
        # Check whether the inbox contains any emails
        if not self.emails:
            print('Your inbox is empty.\n')
            return

        print('\nYour Emails:')

        # Display each email with a number starting from 1
        for i, email in enumerate(self.emails, start=1):
            print(f'{i}. {email}')

    # Opens an email selected by the user
    def read_email(self, index):
        # Check whether the inbox is empty
        if not self.emails:
            print('Inbox is empty.\n')
            return

        # Convert the user's number into a list index
        # This is necessary because Python lists start at index 0
        actual_index = index - 1

        # Check that the selected email number is valid
        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return

        # Display the selected email in full
        self.emails[actual_index].display_full_email()

    # Deletes an email selected by the user
    def delete_email(self, index):
        # Check whether the inbox is empty
        if not self.emails:
            print('Inbox is empty.\n')
            return

        # Convert the user's number into a list index
        actual_index = index - 1

        # Check that the selected email number is valid
        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return

        # Remove the selected email from the inbox
        del self.emails[actual_index]

        print('Email deleted.\n')


# Main function that demonstrates how the email system works
def main():
    # Create two user accounts
    tory = User('Tory')
    ramy = User('Ramy')

    # Send an email from Tory to Ramy
    tory.send_email(ramy, 'Hello', 'Hi Ramy, just saying hello!')

    # Send a reply from Ramy to Tory
    ramy.send_email(tory, 'Re: Hello', 'Hi Tory, hope you are fine.')

    # Display Ramy's inbox
    ramy.check_inbox()

    # Open and read the first email in Ramy's inbox
    ramy.read_email(1)

    # Delete the first email from Ramy's inbox
    ramy.delete_email(1)

    # Display Ramy's inbox again to confirm the email was deleted
    ramy.check_inbox()


# Ensures the main function runs only when this file is executed directly
if __name__ == '__main__':
    main()
