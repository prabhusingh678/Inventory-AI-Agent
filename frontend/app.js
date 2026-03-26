const API_URL = "http://localhost:8000/ask"; // ✅ Correct for browser

async function askAgent() {
    const input = document.getElementById("question");
    const chat = document.getElementById("chat");

    const question = input.value.trim();
    if (!question) return;

    // ✅ Show user message
    chat.innerHTML += `<div class="message user">${question}</div>`;
    input.value = "";

    // ✅ Show loading message
    const loadingId = "loading-" + Date.now();
    chat.innerHTML += `<div class="message ai" id="${loadingId}">Typing...</div>`;
    chat.scrollTop = chat.scrollHeight;

    try {
        const res = await fetch(API_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ question })
        });

        // ✅ Handle HTTP errors
        if (!res.ok) {
            throw new Error("Server error: " + res.status);
        }

        const data = await res.json();

        // ✅ Replace loading with response
        document.getElementById(loadingId).innerText =
            data.response || JSON.stringify(data);

    } catch (err) {
        console.error(err);

        // ❌ Show error in UI
        document.getElementById(loadingId).innerText =
            "❌ Error: Unable to connect to backend";
    }

    chat.scrollTop = chat.scrollHeight;
}

// ✅ Press ENTER to send
document.getElementById("question").addEventListener("keypress", function (e) {
    if (e.key === "Enter") {
        askAgent();
    }
});