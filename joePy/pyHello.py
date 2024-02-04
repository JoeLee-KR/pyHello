#
# need python lib: requests, at venv by conda
#
print("PyHello, ...")
import requests

respo = requests.get("http://naver.com")
print(respo.text)