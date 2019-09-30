import requests
'''
r = requests.get("http://www.google.com")

r.encoding = 'utf-8'
s = r.text
print(s)
'''

def getText(url):
    try:
        r = requests.get(url, timeout = 500)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "Erroroccur!"


if __name__ == "__main__":
    url = "http://www.bilibili.com"
    print(getText(url))