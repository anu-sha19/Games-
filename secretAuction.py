import os
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

def highest_bidder(bid):
   max = 0
   for key in bids:
      if bids[key]>max:
         name= key
         max=bids[key]
   print(f"Congratulations {name}.The winner is {name} with a bid of ${max}")

print(f"{logo} Welcome to the Secret Auction Program!!!")
current_bidders = True
bids={}
while current_bidders:
   name = input("What is your name?")
   bid = int(input("How much would you like to bid?"))
   bids[name]=bid
   more_bidders= input('Type "yes" if there are more bidders, "no" if there are none.').lower()
   if more_bidders == "yes":
      os.system("cls")
      print(logo)
   else:
      current_bidders = False
      highest_bidder(bids)

  
   





