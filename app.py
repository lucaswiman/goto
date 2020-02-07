import contextlib
import sqlite3
import sys

DB_NAME = 'bookmarks.db'

def get_bookmark(bookmark_name: str) -> str:
    with contextlib.closing(sqlite3.connect(DB_NAME)) as conn:
        c = conn.cursor()
        c.execute('SELECT url FROM bookmarks WHERE name=?', (bookmark_name, ))
        url = c.fetchone()
        if url:
            return url[0]
    return url


def set_bookmark(name: str, url: str) -> str:
    prev = get_bookmark(name)
    with contextlib.closing(sqlite3.connect(DB_NAME)) as conn:
        c = conn.cursor()
        if prev:
            print('Updating previous value of {prev} to {url}')
            c.execute('UPDATE bookmarks SET url=? WHERE name=?', url, name)
        else:
            c.execute('INSERT INTO bookmarks(name, url) VALUES (?, ?)', (name, url))
        conn.commit()


def create_schema():
    with contextlib.closing(sqlite3.connect(DB_NAME)) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS bookmarks(
                name TEXT PRIMARY KEY,
                url TEXT
            )
        ''')
        conn.commit()

def display_help():
    print('''\
Usage:
    pipenv run app.py (get|set|add|remove|copy) name (url)?
    pipenv create-schema
''')


if __name__ == '__main__':
    try:
        _, command, *opts = sys.argv
    except ValueError:
        display_help()
    else:
        if command == 'create-schema':
            create_schema()
        elif command == 'get':
            print(get_bookmark(opts[0]))
        elif command in ('set', 'add'):
            set_bookmark(opts[0], opts[1])
        elif command == 'copy':
            raise NotImplementedError()
        elif command == 'remove':
            raise NotImplementedError()
        else:
            display_help()
        

