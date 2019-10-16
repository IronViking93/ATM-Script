import sys

#account balance 
account_balance = float(500.25)

#the printbalance function displays the users current account balance.
def printbalance():
  return 'Your current balance:\n {}'.format(account_balance)

#the deposit function with ask the user how much they want to add to the account and will
#display the amount theu deposited and the new balance.
def deposit():
  deposit_amount = float(input('How much would you like to deposit today?\n'))
  return 'Deposit was ${}, current balance is ${}'.format("%.2f"%deposit_amount, account_balance+deposit_amount)

# the withdrawal function asks the user how much they are wanting to take out of their account 
# and will display the balance after the withdrawal.
# if the withdrawal amount if more than the balance, it will indicate the requested amount is
# greater than the current balance.
def withdrawal():
  withdrawal_amount = float(input('How much would you like to withdraw today?\n'))
  if withdrawal_amount > account_balance:
    return '${} is greater than your account balance of ${}'.format('%.2f'%withdrawal_amount, account_balance)
  else:  
    return 'Withdrawal amount was ${}, current balance is ${}'.format('%.2f'%withdrawal_amount, account_balance-withdrawal_amount)

# the quit function returns the statement to indicate the user has quit the
# banking session
def quit():
  if userchoice == 'Q':
    return 'Thank you for banking with us.'

#asks the user what they would like to do.
userchoice = input("What would you like to do?\n (B)alance, (D)eposit, (W)ithdrawl, or (Q)uit?\n")
#depending on the user input, the if/elif/else statements will call the functions
#associated to the user input.
if userchoice == 'B':
  print(printbalance())
elif userchoice == 'D':
  print(deposit())
elif userchoice == 'W':
  print(withdrawal())
else:
  print(quit())



