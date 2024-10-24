const fetchRandomUser = async () => {
    const res = await fetch('https://api.freeapi.app/api/v1/public/randomusers/user/random')
    const data = await res.json()

    if (data.success && data.data) {
        const user = data.data
        const username = user.login.username
        const country = user.location.country
        return [username, country]
    } else {
        throw new Error('Failed to fetch user')
    }
}

let username, country

fetchRandomUser()
    .then(res => {
        [username, country] = res
        console.log(`Username: ${username}, Country: ${country}`)
    })
