from channels import Group
import json
from .models import Post

# Connected to websocket.connect
def ws_add(message):
    # Accept the connection
    message.reply_channel.send({"accept": True})
    # Add to the chat group
    Group("blogger").add(message.reply_channel)


# Connected to websocket.receive
def ws_message(message):
    data = json.loads(message.content['text'])
    if data['state'] == 'new':
        post = Post.add_post(str(data['user']), data['body'])
        Group("blogger").send({
            "text": " %s~%s~%s~%s" % (data['user'], data['body'], post.id, 'new'),
        })
    elif data['state'] == 'edit' and data['body']:
        print(data)
        post = Post.edit_post(data['id'], data['body'])
        Group("blogger").send({
            "text": " %s~%s~%s~%s" % (data['user'], data['body'], data['id'], 'edit'),
        })
    else:
        post = Post.delete_post(data['id'])
        print(data)
        Group("blogger").send({
        "text": " %s~%s~%s~%s" % (data['user'], 'empty', data['id'], 'delete'),
        })

# Connected to websocket.disconnect
def ws_disconnect(message):
    Group("blogger").discard(message.reply_channel)
