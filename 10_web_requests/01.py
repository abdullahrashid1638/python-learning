import requests

def fetch_random_user():
    res = requests.get('https://api.freeapi.app/api/v1/public/randomusers/user/random')
    data = res.json()

    if data['success'] and 'data' in data:
        user = data['data']
        username = user['login']['username']
        country = user['location']['country']
        return username, country
    else:
        raise Exception('Failed to fetch user data')

def main():
    try:
        username, country = fetch_random_user()
        print(f"Username: {username}, Country: {country}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == '__main__':
    main()
