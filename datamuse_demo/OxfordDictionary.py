import requests

response = requests.get("https://joughtred-oxford-english-dictionary-v1.p.rapidapi.com/senses/",
  headers={
    "X-RapidAPI-Host": "joughtred-oxford-english-dictionary-v1.p.rapidapi.com",
    "X-RapidAPI-Key": "efbbc2b37emsh9b6e1977057aa9dp10e37ejsn4a629c79092b"
  }
)
print(response)