import requests

URL = 'https://api.freeapi.app/api/v1/public/youtube/playlists'
HEADERS = { 'accept': 'application/json' }

def get_youtube_playlist(url, headers, page, limit):
    params = { 'page': str(page), 'limit': str(limit) }
    res = requests.get(url, headers=headers, params=params).json()
    playlists = res['data']['data']
    playlists_info = []
    for playlist in playlists:
        playlists_info.append({
            'type': playlist['kind'],
            'id': playlist['id'],
            'title': playlist['snippet']['title'],
            'description': playlist['snippet']['description'],
            'published_at': playlist['snippet']['publishedAt'],
            'thumbnail': playlist['snippet']['thumbnails']['standard']['url'],
            'channel_title': playlist['snippet']['channelTitle']
        })
    return playlists_info

def main():
    try:
        playlists_info = get_youtube_playlist(URL, HEADERS, 1, 3)
        index = 1
        for playlist in playlists_info:
            print('-' * 80)
            print(str(index) + ':')
            print(f'\n{playlist['title']}\n\nDescription:\n{playlist['description']}\n\nCreated at {playlist['published_at']} by {playlist['channel_title']}')
            print('-' * 80)
            index += 1
    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    main()
