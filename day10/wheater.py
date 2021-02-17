import requests as req

search=input("location: ")

url="http://api.weatherapi.com/v1/current.json"
api_key="b38131ccc91d48399c3200307211702"

response = req.get(url,params={
    "key":api_key,
    "q":search,
    "lang":"en"
})

res=response.json()

loc=f"{res['location']['region']}/{res['location']['country']}"
temp=res['current']['temp_c']
cond=res['current']['condition']["text"]

print(f"temperature in {loc} is {temp}. {cond}")
