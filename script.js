function sendMessage() {

    let input = document.getElementById("input").value

    if (input.trim() === "") return

    let box = document.getElementById("messages")

    // user bubble
    box.innerHTML += `
        <div class="msg user">
            ${input}
        </div>
    `
    fetch("/chat", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            message: input
        })

    })
    .then(res => res.json())

    .then(data => {

        box.innerHTML += `
            <div class="msg bot">
                ${data.reply}
            </div>
        `
        box.scrollTop = box.scrollHeight
    })
    document.getElementById("input").value = ""

}
