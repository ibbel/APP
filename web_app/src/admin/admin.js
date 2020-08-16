const users = [
    { id: 1, login: 'IbBel', email: 'IbBel@gmail.com', },
    { id: 2, login: 'ChrisRed', email: 'CR@gmail.com', },
    { id: 3, login: 'LSK', email: 'LSK@gmail.com', },
    { id: 4, login: 'JoDoe', email: 'jd@mail.fr', },
]

const deleteUser = event => {
    console.log(event.target.id)
}

const renderUsers = () => {
    const list = document.querySelector('#userList')
    for (user of users) {
        const li = document.createElement('li')
        const data = document.createTextNode(`Login : ${user.login}  Email: ${user.email}`)
        const button = document.createElement('button')
        button.setAttribute("id", user.id.toString())
        button.addEventListener('click', deleteUser)
        button.innerHTML = "Supprimer"
        li.appendChild(data)
        li.appendChild(button)
        list.appendChild(li)
    }
}

const getUsers = () => {
    const options = {
        method: 'GET',
        headers: {
            'Access-Control-Allow-Origin': '*'
        }
    }
    fetch('http://127.0.0.1:5000/api/users', options)
    .then(resp => resp.json())
    .then(json => console.log(json))
}

renderUsers()

getUsers()