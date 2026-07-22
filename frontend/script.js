function fill(item){

    document.getElementById("query").value=item.innerText;

}

async function predictWeather(){

    const query=document.getElementById("query").value;

    if(query===""){

        alert("Enter a question");

        return;

    }

    document.getElementById("loading").style.display="block";

    document.getElementById("result").innerHTML="";

    const API = "https://weather-agent-68sn.onrender.com";

    try {
    const response = await fetch(
        `${API}/chat?query=${encodeURIComponent(query)}`
    );

    const data = await response.json();

    document.getElementById("loading").style.display = "none";

    if (!data.success) {
        document.getElementById("result").innerHTML =
            `<div class="card">${data.error}</div>`;
        return;
    }

    let emoji = "🌤";

    if (data.prediction.temperature < 15)
        emoji = "❄";
    else if (data.prediction.temperature > 30)
        emoji = "🔥";

    document.getElementById("result").innerHTML = `
        <div class="card">
            <div class="temp">${emoji} ${data.prediction.temperature}°C</div>
            <h2>${data.prediction.city}</h2>
            <p><b>Date:</b> ${data.prediction.date}</p>
            <p class="answer">${data.answer}</p>
        </div>
    `;
}
catch (err) {
    document.getElementById("loading").style.display = "none";
    document.getElementById("result").innerHTML =
        `<div class="card">⚠️ Unable to connect to the server.</div>`;
    console.error(err);
}
}