import re 
def Lumitel(telephone):
	return re.match("^6[1,2,7,8,9]([ ]?[0-9]{3}){2}",telephone)


def Leo(telephone):
	return re.match("^7[1,2,9]([ ]?[0-9]{3}){2}$",telephone)
#print(Leo("79724174"))

def Smart(telephone):
	return re.match("^75([ ]?[0-9]{3}){2}$",telephone)
#print(Smart("75897654"))

def Onamob(telephone):
	return re.match("^77([ ]?[0-9]{3}){2}$",telephone)
#print(Onamob("77685432"))

def Email(nom):
	return re.match("^([\w])+(@)+(gmail.)+([a-z]+)",nom)
print (Email("ange257@gmail.bi"))