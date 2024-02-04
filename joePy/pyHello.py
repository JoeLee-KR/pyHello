#
#  need pre-install requests library at venv, conda-env ...
#
print("PyHello, ...")

import requests

respo = requests.get("http://naver.com")
print(respo.text)