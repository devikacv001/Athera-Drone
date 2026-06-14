import cv2
import torch
from PIL import Image
from transformers import CLIPProcessor, CLIPModel

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

print("Loading CLIP...")
model = CLIPModel.from_pretrained(
    "openai/clip-vit-large-patch14"
).to(DEVICE)

processor = CLIPProcessor.from_pretrained(
    "openai/clip-vit-large-patch14"
)

THRESHOLD = 20.0


def detect_product(frame, product_name):

    image = Image.fromarray(
        cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    )

    prompts = [
        f"a photo of {product_name}",
        f"a product called {product_name}",
        f"a package of {product_name}",
        f"a box of {product_name}",
        f"a packet of {product_name}",
    ]

    inputs = processor(
        text=prompts,
        images=image,
        return_tensors="pt",
        padding=True
    ).to(DEVICE)

    with torch.no_grad():
        outputs = model(**inputs)

    logits = outputs.logits_per_image
    score = float(logits.max())

    return score > THRESHOLD, score


def process_image(path, product_name):

    frame = cv2.imread(path)

    if frame is None:
        print("Could not open image")
        return

    detected, score = detect_product(
        frame,
        product_name
    )

    text = (
        "PRODUCT DETECTED"
        if detected
        else
        "NOT DETECTED"
    )

    color = (
        (0, 255, 0)
        if detected
        else
        (0, 0, 255)
    )

    cv2.putText(
        frame,
        text,
        (20, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        color,
        2
    )

    print(text)
    print("Confidence:", round(score, 2))

    cv2.imshow("Result", frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def process_video(path, product_name):

    cap = cv2.VideoCapture(path)

    frame_count = 0
    detected_frames = 0

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        frame_count += 1

        if frame_count % 10 != 0:
            continue

        detected, score = detect_product(
            frame,
            product_name
        )

        if detected:
            detected_frames += 1

        text = (
            "PRODUCT DETECTED"
            if detected
            else
            "NOT DETECTED"
        )

        color = (
            (0,255,0)
            if detected
            else
            (0,0,255)
        )

        cv2.putText(
            frame,
            text,
            (20,50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            color,
            2
        )

        cv2.imshow("Video", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

    print()
    print("Frames checked:", frame_count)
    print("Detected frames:", detected_frames)

    if detected_frames > 0:
        print("FINAL RESULT: PRODUCT DETECTED")
    else:
        print("FINAL RESULT: NOT DETECTED")


def process_webcam(product_name):

    cap = cv2.VideoCapture(0)

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        detected, score = detect_product(
            frame,
            product_name
        )

        text = (
            "PRODUCT DETECTED"
            if detected
            else
            "NOT DETECTED"
        )

        color = (
            (0,255,0)
            if detected
            else
            (0,0,255)
        )

        cv2.putText(
            frame,
            text,
            (20,50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            color,
            2
        )

        cv2.imshow(
            "Product Detector",
            frame
        )

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


def main():

    product_name = input(
        "Enter product name: "
    ).strip()

    mode = input(
        "\n1 = Webcam\n"
        "2 = Image\n"
        "3 = Video\n"
        "Choose: "
    )

    if mode == "1":

        process_webcam(product_name)

    elif mode == "2":

        path = input(
            "Image path: "
        )

        process_image(
            path,
            product_name
        )

    elif mode == "3":

        path = input(
            "Video path: "
        )

        process_video(
            path,
            product_name
        )


if __name__ == "__main__":
    main()