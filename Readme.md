# Vote

> Simple Vote, No Login, No Verification

> fake header, ip pool

> get_score.py : request.get() scores for all teams

> vote.py & bad_vote.py : Vote randomly for our team & Vote maliciously for the competitors

## Install on Cloud

1. Create a new folder

```
$ mkdir my_vote
$ cd my_vote
```

2. Initialize the folder with git and a virtualenv

```
$ pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate 
```

3. Install packages

```
$pip install requests
$pip install bs4
$pip install lxml
$pip install fake-useragent
```

## Run

```shell
python get_score.py
python vote.py
```

## nohup run

```shell
nohup python -u vote.py > example.log 2>&1 &
tail -n 5 example.log
ps -ef | grep python
kill -s 9 22484
```
