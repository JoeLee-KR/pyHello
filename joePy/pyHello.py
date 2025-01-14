#
# need python lib: requests, at venv by conda
#
import requests
print("PyHello, ...")


respo = requests.get("http://google.com")
print(respo.text)
print( "EOF")
