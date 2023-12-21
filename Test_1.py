import requests

url = "https://s3.amazonaws.com/open-to-cors/assignment.json"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    if "products" in data and isinstance(data["products"], dict):
        product_data = data["products"]

        product_list = [{"id": key, **value} for key, value in product_data.items()]

        sorted_data = sorted(product_list, key=lambda x: int(x['popularity']), reverse=True)

        for product in sorted_data:
            print(f"ID: {product['id']}")
            print(f"Title: {product['title']}")
            print(f"Price: {product['price']}")
            print(f"Popularity: {product['popularity']}")
            print("-------------")
    else:
        print("The structure of the JSON data is not as expected.")
else:
    print(f"Failed to download JSON file. Status code: {response.status_code}")
