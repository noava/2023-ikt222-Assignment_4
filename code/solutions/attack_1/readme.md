# Attack 1
### Password Length
The script determines the correct password length by iterating for each length it sends and checks the response time. 
When the response time is longer than the previous it knows that the length is correct.
### Password Guessing
Then it tries to guess the password one character at a time. 
For each of the `17` characters found from the password length function. 
It joins all the characters that are correct into the password 