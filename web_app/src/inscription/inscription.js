const submit = (event) => {
    event.preventDefault()
    const user = {}
    const form = event.target
    for (input of form) {
        if (input.id !== "") {
            user[input.id] = input.value
        }
    }
    console.log(user)
}

document.querySelector('#registerForm').addEventListener('submit', submit)