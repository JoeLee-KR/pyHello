from urllib.parse import urlparse
from yarl import URL

print("pyURL Start::")

url = 'http://user:pass@example.com:8042/over/there?name=ferret#nose'
urllib_url = urlparse(url)
yarl_url = URL(url)

print(yarl_url.scheme) # 'http'
print(urllib_url.scheme) # 'http'

print(yarl_url.user) # 'user'
print(urllib_url.username) # 'user'

print(yarl_url.password) # 'pass'
print(urllib_url.password) # 'pass'

print(yarl_url.host) # 'example.com'
print(urllib_url.hostname) # 'example.com'

print(yarl_url.port) # 8042
print(urllib_url.port) # 8042

print(yarl_url.path) # '/over/there'
print(urllib_url.path) # '/over/there'

print(yarl_url.query_string) # 'name=ferret'
print(urllib_url.query) # 'name=ferret'

print(yarl_url.query) # <MultiDictProxy('name': 'ferret')>
print("urllib is not support MultiDictProxy...!!!")
# urllib에는 없음

print(yarl_url.fragment) # 'nose'
print(urllib_url.fragment) # 'nose'

print("pyURL Stop::")