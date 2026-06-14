from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
import whisper
import tempfile

from extractor import extract_items
from mission_planner import graph
from shop_planner import find_best_shop
from shop_finder import find_nearby_shops

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

print("Loading Whisper model...")
model = whisper.load_model("small")
print("Whisper model loaded!")


@app.post("/voice")
async def process_voice(
    audio: UploadFile,
    lat: float = Form(...),
    lon: float = Form(...)
):

    print("Voice request received")

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".webm"
    ) as temp:

        temp.write(await audio.read())
        temp_path = temp.name

    print("Audio saved:", temp_path)

    result = model.transcribe(temp_path)

    text = result["text"]

    print("Recognized text:", text)

    items = extract_items(text)

    print("\n======================")
    print("ITEMS:", items)
    print("======================")

    mission = graph.invoke(
        {
            "items": items
        }
    )

    shop_plan = find_best_shop(items)

    print("\n======================")
    print("SHOP PLAN:", shop_plan)
    print("======================")

    live_shops = find_nearby_shops(
        lat,
        lon,
        shop_plan["shop_type"]
    )

    print("\n======================")
    print("LIVE SHOPS:", live_shops)
    print("======================")

    response_data = {
        "speech_text": text,
        "items": items,
        "mission": mission["plan"],
        "shop_type": shop_plan["shop_type"],
        "shops": live_shops
    }

    return response_data