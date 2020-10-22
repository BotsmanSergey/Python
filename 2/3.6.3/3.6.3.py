import requests, json

with open("readfile.txt", 'r') as f:
    for line in f:
        res = json.loads(requests.get("http://numbersapi.com/"+line.strip()+"/math?json=true").text)
        if res["found"] :
            print("Interesting")
        else:print("Boring")