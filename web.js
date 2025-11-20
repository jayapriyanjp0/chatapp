let socket=new WebSocket("ws://localhost:8080")
socket.onopen(function(e){

    displayMessage('connect websocket server')

})
socket.onmessage(function(e){
    displayMessage('connect',e.data)
})
// Function to display messages on the screen
function displayMessage(message, sender) {
    const messageContainer = document.getElementById("messages");
    const messageElement = document.createElement("div");
    messageElement.classList.add("message");
    messageElement.classList.add(
        sender === "client" ? "client-message" : "server-message"
    );
    messageElement.textContent = message;

    // Wrap the message in a container to handle alignment
    const messageWrapper = document.createElement("div");
    messageWrapper.classList.add("message-wrapper");
    messageWrapper.appendChild(messageElement);

    messageContainer.appendChild(messageWrapper);
    messageContainer.scrollTop = messageContainer.scrollHeight;
}

function message(){
    let message=document.getElementById("messageInput").value;
    if (message.trim !==''){
        socket.send(message);
        displayMessage(message,'client');
        document.getElementById('messageInput').value=='';

    }
}