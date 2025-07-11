import sqlite3
from flask import g

def init_db(app):
    app.teardown_appcontext(close_db)
    with app.app_context():
        db = get_db()
        db.execute('''
            CREATE TABLE IF NOT EXISTS credentials (
                id INTEGER PRIMARY KEY,
                platform TEXT NOT NULL,
                access_token TEXT NOT NULL
            )
        ''')
        db.commit()

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect('social.db')
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()
