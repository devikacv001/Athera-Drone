STORE_TYPES = {

    # Grocery / Supermarket
    "milk": "supermarket",
    "bread": "supermarket",
    "cucumber": "supermarket",
    "carrot": "supermarket",
    "brinjal": "supermarket",
    "rice": "supermarket",
    "egg": "supermarket",
    "eggs": "supermarket",
    "banana": "supermarket",
    "apple": "supermarket",
    "tomato": "supermarket",
    "potato": "supermarket",
    "onion": "supermarket",
    "sugar": "supermarket",
    "salt": "supermarket",

    # Pharmacy
    "paracetamol": "pharmacy",
    "paracetamol tablet": "pharmacy",
    "paracetamol tablets": "pharmacy",
    "crocin": "pharmacy",
    "crocin strip": "pharmacy",
    "dolo": "pharmacy",
    "dolo 650": "pharmacy",
    "tablet": "pharmacy",
    "tablets": "pharmacy",
    "medicine": "pharmacy",

    # Stationery
    "pen": "stationery",
    "pencil": "stationery",
    "notebook": "stationery",
    "book": "stationery",

    # Electronics
    "charger": "electronics",
    "earphones": "electronics",
    "headphones": "electronics",
    "usb cable": "electronics"
}


def find_best_shop(items):

    categories = []

    for item in items.keys():

        item_lower = item.lower().strip()

        # Handle Whisper spelling mistakes
        if (
            "tablet" in item_lower
            or "dolo" in item_lower
            or "crocin" in item_lower
            or "paracetamol" in item_lower
            or "parasitamol" in item_lower
            or "medicine" in item_lower
        ):
            categories.append("pharmacy")
            continue

        category = STORE_TYPES.get(
            item_lower,
            "supermarket"
        )

        categories.append(category)

    if not categories:

        return {
            "shop_type": "supermarket"
        }

    most_common = max(
        set(categories),
        key=categories.count
    )

    return {
        "shop_type": most_common
    }