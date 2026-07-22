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

    const response=await fetch(

        "http://127.0.0.1:8000/chat?query="+encodeURIComponent(query)

    );

    const data=await response.json();

    document.getElementById("loading").style.display="none";

    if(!data.success){

        document.getElementById("result").innerHTML=

        `<div class="card">

            ${data.error}

        </div>`;

        return;

    }

    let emoji="🌤";

    if(data.prediction.temperature<15)

        emoji="❄";

    else if(data.prediction.temperature>30)

        emoji="🔥";

    document.getElementById("result").innerHTML=

    `
    <div class="card">

        <div class="temp">

            ${emoji} ${data.prediction.temperature}°C

        </div>

        <h2>${data.prediction.city}</h2>

        <p><b>Date:</b> ${data.prediction.date}</p>

        <p class="answer">

            ${data.answer}

        </p>

    </div>
    `;
}