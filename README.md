<h1 align="center"> Personal-Password-Manager </h1> <br>

<!-- Add banner Image here -->

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Features](#features)
- [Contribution](#contribution)

## Introduction


![GitHub last commit](https://img.shields.io/github/last-commit/sansyrox/Personal-Password-Manager)  ![GitHub issues](https://img.shields.io/github/issues/sansyrox/Personal-Password-Manager)


A password manager that encodes your passwords based on your unique key and allows you to store it on a remote host.

## Installation

1. Install required dependencies using:

```sh
$ pip install -r requirements.txt
```

2. Generate your encryption key using:

```sh
$ python encryption.py`
```

3. Create a config.json file with hostname, username and password of your MySql DB

Example: Config.json
```
Add the host, username and password of your MySql DB
{
  "host": "www.example.com",
  "user": "DBadmin",
  "password": "DBpassword"
}
```

4. Use the endpoints from `helper.py` to perform the CRUD functions.

## Features

1. Personal-Password-Manager is based on python and thus is platform independent.
2. Personal-Password-Manager uses Fernet to generate encryption keys

## Contribution

Check [CONTRIBUTING.md](https://github.com/sansyrox/Personal-Password-Manager/blob/main/CONTRIBUTING.md) for the information regarding contribution.