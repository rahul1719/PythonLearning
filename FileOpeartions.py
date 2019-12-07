import requests

res = requests.get('http://blog.apc.com/post-sitemap.xml')
type(res)
res.status_code == requests.codes.ok
print(len(res.text))

print(res.text[:49635])
