const users = [
    { lastname: 'Bellahcene', firstname: 'Ibrahim', birth: "19/01/1995", },
    { lastname: 'Redfield', firstname: 'Chris', birth: "01/01/1973", },
    { lastname: 'S.Kennedy', firstname: 'Leon', birth: "15/05/1977", },
    { lastname: 'Doe', firstname: 'John', birth: "99/99/9999", },
  ]
  
  const searchUser = () => {
    const user = document.querySelector("#searchInput").value
    console.log('user : ', user)
  }
  
  const renderUsers = () => {
    const table = document.querySelector('#userTable')
    for (user of users) {
        const tr = table.insertRow()
        for (key in user) {
            let cell = tr.insertCell()
            cell.innerHTML = user[key]
        }
    }
  
  }
  
  document.querySelector("#searchButton").addEventListener('click', searchUser)
  renderUsers()