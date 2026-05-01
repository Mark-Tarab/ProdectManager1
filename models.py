class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

class Note:
    def __init__(self, id, title, content, color, is_pinned, user_id):
        self.id = id
        self.title = title
        self.content = content
        self.color = color
        self.is_pinned = is_pinned
        self.user_id = user_id