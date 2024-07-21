import requests; # type: ignore

response = requests.get("http://api.open-notify.org/astros.json")
json = response.json();
print(json);

for person in json['people']: 
  print(person)