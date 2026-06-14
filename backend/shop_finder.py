import requests
from geopy.distance import geodesic


def get_city(lat, lon):

    url = (
        f"https://nominatim.openstreetmap.org/reverse"
        f"?lat={lat}"
        f"&lon={lon}"
        f"&format=json"
    )

    response = requests.get(
        url,
        headers={
            "User-Agent": "shopping-drone"
        }
    )

    data = response.json()

    address = data.get(
        "address",
        {}
    )

    return (
        address.get("city")
        or address.get("town")
        or address.get("village")
        or ""
    )


def find_nearby_shops(lat, lon, category):

    city = get_city(lat, lon)

    print("CITY:", city)

    search_query = f"{category} {city}"

    url = (
        f"https://nominatim.openstreetmap.org/search"
        f"?q={search_query}"
        f"&format=json"
        f"&limit=20"
    )

    response = requests.get(
        url,
        headers={
            "User-Agent": "shopping-drone"
        }
    )

    data = response.json()

    shops = []

    user_location = (lat, lon)

    for place in data:

        try:

            shop_lat = float(place["lat"])
            shop_lon = float(place["lon"])

            distance = geodesic(
                user_location,
                (shop_lat, shop_lon)
            ).meters

            shops.append({
                "name": place["display_name"],
                "distance": round(distance),
                "maps":
                f"https://www.google.com/maps?q={shop_lat},{shop_lon}"
            })

        except:
            pass

    shops.sort(
        key=lambda x: x["distance"]
    )

    return shops[:5]