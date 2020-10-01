# Personal-Password-Manager

Consider starring the repo? :star:

A password manager that encodes your passwords based on your unique key and allows you to store it on a remote host.

## Installation Steps
1. `pip install -r requirements.txt`
2. Generate your encryption key using `python encryption.py`
3. Create a config.json file with the following config
```
Adding the host,username and password of your MySql DB
{
  "host":"",
  "user":"",
  "password":""
}
```
4. Use the endpoints from `helper.py` to perform the CRUD functions.
