# Attack 6
## Reverse engineering
We can now read the file in `/home/ingridnilsen/level3_secrets.txt`:
This gives us this info: 
```
Url: https://state-secrets.internal.regjeringen.uiaikt.no/download
Username: ingridnilsen
Password: 3xtr3m3ly s3cur3
```
We can then access that website with those credentials and download the file that shows up.
We can then use this command: `strings reverse-engineering-bin | less` to 
We manually look through the strings and spot these lines:
`statsminister` and `erna` which we can assume is the username and password.
We can then use these credentials to login and reveal the state secrets. 