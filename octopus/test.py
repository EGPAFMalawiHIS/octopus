import requests

data = {
    "type": "send-sms",
    "task_num": 1,
    "tasks": [
        {
            "tid": 1,
            "to": "+265998006237",
            "sms": "This is a test",
        }
    ],
}

try:
    r = requests.post(
        "http://192.168.100.202/goip_post_sms.html?version=1.0&username=root&password=root",
        json=data,
        headers={"Content-type": "application/json;charset=utf-8"},
    )

    print("sent successfully", r.json())

except Exception as e:
    print(e)
