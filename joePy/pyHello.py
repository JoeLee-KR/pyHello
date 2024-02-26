#
# need python lib: requests, at venv by conda
#
print("PyHello, ...")
import requests

respo = requests.get("http://google.com")
print(respo.text)
print("EOF")