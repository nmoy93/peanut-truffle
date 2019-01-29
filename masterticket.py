ticket_price = 10
tickets_remaining = 100

print("Welcome! There are {} tickets to the concert remaining.".format(tickets_remaining))

name = raw_input("Before we get started, what is your name?  ")

num_tickets = raw_input("How many tickets will you be purchasing, {}?  ".format(name))
num_tickets = int(num_tickets)

amount_due = ticket_price * num_tickets
print("That will be ${}.".format(amount_due))

proceed = raw_input("Do you want to proceed with your purchase? (Select Y/N)")
if proceed == "y" or "Y":
    print("CHA CHING - SOLD!")

    # decrement tickets remaining by the number of tickets purchased
    tickets_remaining -= num_tickets
    print("There are {} tickets remaining.".format(tickets_remaining))
else:
    print("Thanks anyways {}!".format(name))
# //TODO: Send to github
