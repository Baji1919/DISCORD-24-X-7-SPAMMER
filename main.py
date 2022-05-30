from webserver import keep_alive
import requests

channelID = 980711875874521088
headers = {
    "authorization":
    "OTcxODE1ODc2MzUxMzc3NDE4.GUrB8r.OBRd9o3O5vlH1ckki-dyw0uILHGLtMuG7d-uAc"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
