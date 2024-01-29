print("PyHello, ...")
import requests

respo = requests.get("http://naver.com")
print(respo.text)