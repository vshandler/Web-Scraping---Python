import re
p = re.compile('^(.*?)([\d\.,]+)(.*)$', re.IGNORECASE)
if p:
    print(p)

print(p.match("Shipping: R$123,90").group(2))
print(p.match("R$123,90").group(2))

print('Replece')
txt = "Shipping: R$r123,90d"
x = txt.replace("Shipping: R$", "")
print(x)

#'Shipping: R$'28,55
#'R$'105,77'

#Shipping: R$28,55

#R$105,77