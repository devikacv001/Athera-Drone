let mediaRecorder;
let audioChunks = [];

let userLat = null;
let userLon = null;

// Get Current Location
navigator.geolocation.getCurrentPosition(
    (position) => {
        userLat = position.coords.latitude;
        userLon = position.coords.longitude;

        console.log(
            "Location:",
            userLat,
            userLon
        );
    },
    (error) => {
        console.error(
            "Location Error:",
            error
        );
    }
);

const startBtn =
    document.getElementById("startBtn");

const stopBtn =
    document.getElementById("stopBtn");

// Initial State
startBtn.style.display = "inline-block";
stopBtn.style.display = "none";

// Start Recording
startBtn.onclick = async () => {

    startBtn.style.display = "none";
    stopBtn.style.display = "inline-block";

    document.getElementById("speech").innerText =
        "🎤 Listening...";

    const stream =
        await navigator.mediaDevices.getUserMedia({
            audio: true
        });

    mediaRecorder =
        new MediaRecorder(stream);

    audioChunks = [];

    mediaRecorder.ondataavailable = (event) => {
        audioChunks.push(event.data);
    };

    mediaRecorder.start();
};

// Stop Recording
stopBtn.onclick = async () => {

    if (!mediaRecorder) return;

    mediaRecorder.stop();

    startBtn.style.display = "none";
    stopBtn.style.display = "none";

    document.getElementById("speech").innerText =
        "⏳ Processing...";

    mediaRecorder.onstop = async () => {

        try {

            if (
                userLat === null ||
                userLon === null
            ) {

                document.getElementById("speech")
                    .innerText =
                    "📍 Waiting for location access";

                startBtn.style.display =
                    "inline-block";

                return;
            }

            const audioBlob =
                new Blob(audioChunks);

            const formData =
                new FormData();

            formData.append(
                "audio",
                audioBlob,
                "recording.webm"
            );

            formData.append(
                "lat",
                userLat
            );

            formData.append(
                "lon",
                userLon
            );

            const response =
                await fetch(
                    "http://127.0.0.1:8000/voice",
                    {
                        method: "POST",
                        body: formData
                    }
                );

            console.log(
                "STATUS:",
                response.status
            );

            const data =
                await response.json();

            console.log(
                "BACKEND RESPONSE:"
            );

            console.log(data);

            if (!data) {

                throw new Error(
                    "Backend returned null"
                );
            }

            // Speech
            document.getElementById("speech")
                .innerText =
                data.speech_text || "No speech detected";

            // Requested Items
            const itemsList =
                document.getElementById("itemsList");

            itemsList.innerHTML = "";

            if (data.items) {

                for (const item in data.items) {

                    const li =
                        document.createElement("li");

                    li.innerHTML =
                        `✅ ${item} x${data.items[item]}`;

                    itemsList.appendChild(li);
                }
            }

            // Mission Plan
            const missionList =
                document.getElementById("missionList");

            missionList.innerHTML = "";

            if (data.mission) {

                data.mission.forEach(step => {

                    const li =
                        document.createElement("li");

                    li.innerHTML =
                        `📌 ${step}`;

                    missionList.appendChild(li);
                });
            }

            // Shop Type
            const shopType =
                document.getElementById("shopType");

            if (
                shopType &&
                data.shop_type
            ) {

                shopType.innerHTML =
                    `<b>Category:</b> ${data.shop_type}`;
            }

            // Shops
            const shopList =
                document.getElementById("shopList");

            shopList.innerHTML = "";

            if (
                data.shops &&
                data.shops.length > 0
            ) {

                data.shops.forEach(shop => {

                    const li =
                        document.createElement("li");

                    li.innerHTML = `
                        <b>🏪 ${shop.name}</b>
                        <br>
                        📍 ${shop.distance} meters away
                        <br>
                        <a href="${shop.maps}"
                           target="_blank">
                           Open in Google Maps
                        </a>
                        <hr>
                    `;

                    shopList.appendChild(li);
                });

            } else {

                shopList.innerHTML =
                    "<li>No nearby shops found</li>";
            }

        } catch (error) {

            console.error(
                "FRONTEND ERROR:",
                error
            );

            document.getElementById("speech")
                .innerText =
                "❌ " + error.message;
        }

        // Reset UI
        startBtn.style.display =
            "inline-block";

        stopBtn.style.display =
            "none";
    };
};