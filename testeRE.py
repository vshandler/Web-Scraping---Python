import re
p = re.compile('[A-Z][a-z]*: R\$', re.IGNORECASE)
if p:
    print(p)

print(p.match("Shipping: R$123,90").group())



txt = "Shipping: R$123,90"



x = txt.replace("Shipping: R$", "")

print(x)





#'Shipping: R$'28,55
#'R$'105,77'

#Shipping: R$28,55

#R$105,77