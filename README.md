pytlas-server
===

Pytlas server used to communicate with your assistant made with the Django framework.

🚧 WORK IN PROGRESS. At the moment, I use Django admin to be able to edit user settings, it will change in the future to have a real management system to handle your assistant needs.

## Installing and running

```bash
$ git clone https://github.com/atlassistant/pytlas-server
$ cd pytlas-server
$ pip install -r requirements.txt
$ ./postinstall.sh # To create super user and download needed resources (one time only)
$ ./entrypoint.sh python manage.py runserver # Will run migrations
```

## WebSocket protocol

In order to communicate in real time with your assistant, I made a tiny protocol easy to understand. All messages follow the same main body structure:

```json
{
  "type": "<message type>",
  "contextual": "properties"
}
```

All messages received will follow the same payload as the one [sent by pytlas client](https://pytlas.readthedocs.io/en/latest/core_components/client.html).

### Connection

Open a websocket connection with your assistant on this URL: `<site_url>/ws/assistant/`.

### Authentication

If your first message is not this one, the socket will be closed immediately.

You must start by retrieving an access token using a POST on `<site_url>/api/token` with the following JSON body:

```json
{
  "username": "<username>",
  "password": "<password>"
}
```

When you got the access token, you'll just have to send a WS message with this payload:

```json
{
  "type": "authenticate",
  "token": "<your access token>"
}
```

### Receiving ready

You will receive this message when your agent is ready to communicate with you.

```json
{
  "type": "ready",
  "language": "<your profile language such as fr_FR>"
}
```

### Sending message to your agent

Sending a message to be parsed by your agent is as simple as emitting this message:

```json
{
  "type": "message",
  "message": "<your message>"
}
```

### Receiving answer

When a skill is giving back informations to you.

```json
{
  "type": "answer",
  "data": {
    "text": "<the textual answer>",
    "cards": [
      {
        "header": "<card title>",
        "subhead": "<optional card subheader>",
        "text": "<card main content>",
        "media": "<optional media link>",
        "header_link": "<optional card link>"
      }
    ],
    "other": "metadata"
  }
}
```

### Receiving ask

When a skill wants you to give it more information.

```json
{
  "type": "ask",
  "data": {
    "text": "<the question>",
    "slot": "<slot requiring inputs>",
    "choices": ["<optional array of string representings limited available choices>"],
    "other": "metadata"
  }
}
```

### Receiving thinking

When a work is under progress.

```json
{
  "type": "thinking",
}
```

### Receiving done

When a skill has done its work.

```json
{
  "type": "done",
  "require_input": <boolean>,
}
```

### Receiving context switching

Upon context switching, you will receive this message:

```json
{
  "type": "context",
  "name": "<context name>"
}
```