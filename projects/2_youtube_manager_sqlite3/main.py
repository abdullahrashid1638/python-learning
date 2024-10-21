import sqlite3 as db

con =  db.connect('youtube.db')

cursor = con.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
''')

def view_videos():
    cursor.execute('SELECT * FROM videos')
    for row in cursor.fetchall():
        print(row)

def add_video(name, time):
    cursor.execute('INSERT INTO videos (name, time) VALUES (?, ?)', (name, time))
    con.commit()

def update_video(id, name, time):
    cursor.execute('UPDATE videos SET name = ?, time = ? WHERE id = ?', (name, time, id))
    con.commit()

def delete_video(id):
    cursor.execute('DELETE FROM videos WHERE id = ?', (id,))
    con.commit()

def main():
    while True:
        print('\n   Youtube Manager Menu')
        print('1. View all videos')
        print('2. Add a video')
        print('3. Update a video')
        print('4. Delete a video')
        print('5. Exit')
        choice = input('Enter your choice: ')

        match choice:
            case '1':
                view_videos()
            case '2':
                name = input('Enter video name: ')
                time = input('Enter video time: ')
                add_video(name, time)
            case '3':
                id = input('Enter video id: ')
                name = input('Enter video name: ')
                time = input('Enter video time: ')
                update_video(id, name, time)
            case '4':
                id = input('Enter video id: ')
                delete_video(id)
            case '5':
                break
            case _:
                print('Invalid choice')

    con.close()

if __name__ == '__main__':
    main()
