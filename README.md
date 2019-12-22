# Proxy parser

#
# Example
```python 
from proxy_parser import Proxy
import asyncio 

async def a():
  a = Proxy()
  await a.open_session()
  p = await a.main()
  print(p)
asyncio.run(a())
# "type " need for getting proxy string
#  change proxy type to "socks4" or "http" if you use not socks5 proxy.
```
## Result :
```
List- template: "socks5://ip:port".
```
#
# **Requirements**
```
Python 3.7+
BeautifulSoup
aiothttp
asyncio
```
