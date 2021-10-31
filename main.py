#Fill out config.json and make sure to capitalize first letter in firstName before running

import requests
import json

try:
    config = open('myConfig.json')
except:
    config = open('config.json')

config = json.load(config)
s = requests.session()

formData = {
    "faction": 42,
    "serial": 4980058,
    "email": config["email"],
    "password": config["password"]
}

res = s.post("https://mountdiablodriversed.com/course/content/page/userfront_login", data = formData)
if res.text.find(config["firstName"]) != -1:
    print("Login Success")
else:
    print("Login Fail")
    exit()

seconds = 0
s.get("https://mountdiablodriversed.com/course/content/page/course_lesson/lesson/7.3/su/1")
while True:
    seconds += 5
    res = s.get("https://mountdiablodriversed.com/course/content/page/course_lesson/lesson/7.3/su/5")
    print(f"{res} {seconds}s")