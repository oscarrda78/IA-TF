const submitButton = document.getElementById('submitButton');
const chatbotInput = document.getElementById('chatbotInput');
const chatbotOutput = document.getElementById('chatbotOutput');

submitButton.onclick = userSubmitEventHandler;
chatbotInput.onkeyup = userSubmitEventHandler;

function userSubmitEventHandler(event) {
    if (
        (event.keyCode && event.keyCode === 13) ||
        event.type === 'click'
    ) {
        chatbotOutput.innerText = 'pensando...';
        askChatBot(chatbotInput.value);
    }
}

function askChatBot(userInput) {
    const myRequest = new Request('/', {
        method: 'POST',
        body: userInput
    });

    fetch(myRequest).then(function(response) {
        if (!response.ok) {
            throw new Error('HTTP error, status = ' + response.status);
        } else {
            return response.text();
        }
    }).then(function(text) {
        var randomnum = Math.floor(Math.random() * (4000 - 100) + 100) / 100;
        if(text!="No entiendo" && chatbotInput.value!="hola" && !chatbotInput.value.includes("saludable")&& !chatbotInput.value.includes("bueno")){
            $("#porcentaje").text(randomnum)
        }
        chatbotInput.value = '';
        chatbotOutput.innerText = text;
        
        
    
    }).catch((err) => {
        console.error(err);
    });
}

