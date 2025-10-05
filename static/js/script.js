const chatMessages = document.querySelector(".chat-messages");
const inputField = document.querySelector(".chat-input input");
const sendButton = document.querySelector(".chat-input button");

async function sendMessage() {
    const userMessage = inputField.value.trim();
    if(!userMessage) return;

    const userDiv = document.createElement("div");
    userDiv.classList.add("message", "user");
    userDiv.textContent = userMessage;
    chatMessages.appendChild(userDiv);

    inputField.value = "";

    chatMessages.scrollTop = chatMessages.scrollHeight;

    try{
        const response = await fetch("/get_response",{
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({message: userMessage})
        });

        const data = await response.json();

        const botDiv = document.createElement("div");
        botDiv.classList.add("message", "bot");
        botDiv.textContent = data.reply;
        chatMessages.appendChild(botDiv);

        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
    catch (error) {
        console.error("Error: ", error);
    }
}

sendButton.addEventListener("click", sendMessage);

inputField.addEventListener("keypress", function(event){
    if (event.key === "Enter"){
        sendMessage();
    }
});