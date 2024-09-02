# VALIDATE email id

# starting with alphanumericals
# josephhima625@gmail.com
from re import fullmatch

gmail_id="josephhima625@gmail.com"
pattern="\\w[\\w\\._]*@gmail.com"               #for matching the dot \\ is used

matcher=fullmatch(pattern,gmail_id)
print("invalid" if matcher==None else "valid")
