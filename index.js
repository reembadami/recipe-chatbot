const submitButton = document.getElementById('submitButton');
const chatbotInput = document.getElementById('chatbotInput');
const chatbotOutput = document.getElementById('chatbotOutput');

submitButton.onclick = userSubmitEventHandler;

function userSubmitEventHandler(e, flag=false) {
    let query = {}

    if (flag) {
        query = {
            query: e
        }
    } else {
        e.preventDefault()
        query = {
            query: document.getElementById('myText').value
        }
    }
    fetch('http://127.0.0.1:5000/', {
        method: 'POST',
        body: JSON.stringify(query),
        headers: {
            'Content-type': 'application/json; charset=UTF-8'
        }
    })
    .then(response => response.json())
    .then(json => {
        console.log(json)
        if (flag) {
            chatbotInput.innerText = e;
            chatbotOutput.innerText = json;
        } else {
            chatbotInput.innerText = document.getElementById('myText').value;
            chatbotOutput.innerText = json;
        }
    });
}
