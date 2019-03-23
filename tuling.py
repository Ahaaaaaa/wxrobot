import json
from requests import post


def tuling(text):
    res = post(
        url='http://openapi.tuling123.com/openapi/api/v2',
        headers={'Content-Type': 'application/json'},
        data=json.dumps({
            "reqType": 0,
            "perception": {
                "inputText": {
                    "text": text
                }
            },
            "userInfo": {
                "apiKey": "55e07df9a0164cd79bd314cb12a4863b",
                "userId": "8be3b7b8f343ddc7"
            }
        })
    )
    result = res.json()["results"]
    if len(result) == 1:
        return result[0]["values"]["text"]
    else:
        return result[len(result) - 1]["values"]["text"] + result[len(result) - 2]["values"]["url"]
