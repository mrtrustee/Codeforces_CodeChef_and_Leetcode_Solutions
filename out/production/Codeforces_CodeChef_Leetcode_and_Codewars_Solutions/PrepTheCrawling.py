import requests
url = "http://www.prepthecrawling.com"
r = requests.get(url)
print(r.status_code)
print(r.reason)
print(r.headers)
print(r.request)
print(r.request.headers)

def calc(a, b,c):
    urly = 'http://www.prepthecrawling.com'
    params = {"a": a, "b": b, "c": c}
    d = requests.get(urly, params=params)
    return r.text

print(calc(4,6,"*"))
print(calc(4,6, "/"))
