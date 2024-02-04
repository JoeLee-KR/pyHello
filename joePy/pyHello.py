#
<<<<<<< HEAD
#  need pre-install requests library at venv, conda-env ...
#
print("PyHello, ...")

=======
# need python lib: requests, at venv by conda
#
print("PyHello, ...")
>>>>>>> 404c1a4dba56575ff61492072518955c7e240769
import requests

respo = requests.get("http://naver.com")
print(respo.text)