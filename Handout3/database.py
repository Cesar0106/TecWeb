import sqlite3
from dataclasses import dataclass

@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''


class Database:
    def __init__(self, banco):
        self.conn = sqlite3.connect(banco+".db")
        self.criatabela = ("CREATE TABLE IF NOT EXISTS note ( id INTEGER PRIMARY KEY,  title TEXT ,content TEXT NOT NULL);")
        self.conn.execute(self.criatabela)

    def add(self,note):
        addnote = (f"INSERT INTO note (title, content)  VALUES ('{note.title}', '{note.content}');")
        self.conn.execute(addnote)
        self.conn.commit()

    def get_all(self):
        cursor = self.conn.execute("SELECT id, title, content FROM note;")
        notelist = []
        for linha in cursor:
            id = linha[0]
            title = linha[1]
            content = linha[2]
            notelist.append(Note(id = id, title = title, content= content))
        return notelist

    def update(self, entry):
        updatenote = (f"UPDATE note SET title='{entry.title}', content = '{entry.content}' WHERE id = {entry.id};")
        self.conn.execute(updatenote)
        self.conn.commit()

    def delete(self, note_id):
        deletenote = (f"DELETE FROM note WHERE id = {note_id};")
        self.conn.execute(deletenote)
        self.conn.commit()