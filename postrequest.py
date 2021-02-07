import requests
url='http://localhost:5005/webhooks/rest/webhook'
myobj={
	"message":"Hi",
	"sender":"Bibhuti",
}
x=requests.post(url, json=myobj)
print(x.json())