from pymongo import MongoClient
from bson import ObjectId

db_url = 'mongodb+srv://youtubemanager:youtubemy@youtube.u7ley.mongodb.net/'
client = MongoClient(db_url, tlsAllowInvalidCertificates = True)
db = client['youtubemanager']
video_collection = db['videos']

def add_video(name, time):
    video_collection.insert_one({'name': name, 'time': time})

def view_videos():
    videos = video_collection.find()
    for vid in videos:
        print(f'ID: {vid['_id']}, NAME: {vid['name']}, TIME: {vid['time']}')

def update_video(id, name, time):
    video_collection.update_one(
        {'_id': ObjectId(id)},
        {'$set': {
            'name': name,
            'time': time
        }}
    )

def delete_video(id):
    video_collection.delete_one({'_id': ObjectId(id)})

def main():
    while True:
        print('1. Add video')
        print('2. View videos')
        print('3. Update video')
        print('4. Delete video')
        print('5. Exit')
        choice = input('Enter your choice: ')
        if choice == '1':
            name = input('Enter video name: ')
            time = input('Enter video time: ')
            add_video(name, time)
        elif choice == '2':
            view_videos()
        elif choice == '3':
            id = input('Enter video id: ')
            name = input('Enter video name: ')
            time = input('Enter video time: ')
            update_video(id, name, time)
        elif choice == '4':
            id = input('Enter video id: ')
            delete_video(id)
        elif choice == '5':
            break
        else:
            print('Invalid choice')

if __name__ == '__main__':
    main()
