function submitForm() {
    const userInput = document.getElementById('userInput').value;
    fetch('process_form.php', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({userInput: userInput})
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('displayArea').innerText = data.userInput;
    })
    .catch(error => console.error('Error:', error));
}
