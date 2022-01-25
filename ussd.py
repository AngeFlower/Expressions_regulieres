import re
def ussd(code):
	return re.match("^[*][0-9]+(#)",code)
#print(ussd("*800#"))

def transfer(code):
	return re.match("^[*][0-9]+(#)+[0-9]+[*]",code)
#print(transfer("*800#1*"))
def transfer_rev(code):
	return re.match("^[*][0-9]+(#)+[0-9]+[*]+[0-9]+[*]",code)
#print(transfer_rev("*800#1*1*"))

def transfer_rev(numero):
	return re.match("^6[1,2,8,9]([ ]?[0-9]{3}){2}$",numero)
#print(transfer_rev("61004331"))

def transfer_rev(montant):
	return re.match("[0-9]+",montant)
#print(transfer_rev("10000"))

def transfer_rev(PIN):
	return re.match("[0-9]+",PIN)
#print(transfer_rev("1999"))