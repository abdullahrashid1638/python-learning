import json

def list_all_videos(videos):    
    print('\n')
    print('*' * 70)
    for index, video in enumerate(videos, start = 1):
        print(f'{ index }, { video['name'] } Duration: { video['time'] }')
    print('\n')
    print('*' * 50)

def add_video(videos):
    name = input('Enter video name: ')
    time = input('Enter video time: ')
    videos.append({
        'name': name,
        'time': time
    })
    save(videos)

def update_details(videos):
    list_all_videos(videos)
    index = int(input('Enter the video number to update: '))

    if 1 <= index <= len(videos):
        name = input('Enter new video name: ')
        time = input('Enter new video time: ')

        videos[index - 1] = { 'name': name, 'time': time }        
        save(videos)
    else:
        print('Invalid index selected!')

def delete_video(videos):
    list_all_videos(videos)
    index = int(input('Enter the video number to delete: '))

    if 1 <= index <= len(videos):
        del videos[index - 1]
        save(videos)
    else:
        print('Invalid index selected!')

def load_data():
    try:
        with open(videos_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save(videos):
    with open(videos_file, 'w') as file:
        json.dump(videos, file)

def main():
    videos = load_data()

    while True:
        print('\n YouTube Manager | Choose an option from below')
        print('1. List all YouTube videos')
        print('2. Add a YouTube video')
        print('3. Update a YouTube video details')
        print('4. Delete a YouTube video')
        print('5. Exit the program')
        choice = input('Enter your choice: ')

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_details(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print('Invalid choice')

if __name__ == '__main__':
    main()
