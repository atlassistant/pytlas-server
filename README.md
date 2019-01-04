pytlas-server
===

Pytlas server used to communicate with your assistant!

## Installation

```bash
$ git clone https://github.com/atlassistant/pytlas-server
$ cd pytlas-server
$ pip install -r requirements.txt
$ ./postinstall.sh # To create super user and download needed resources (one time only)
$ ./entrypoint.sh python manage.py runserver # Will run migrations
```