from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Загрузка каталога товаров
import itertools

def load_catalog():
    parts = ["products_part1.json", "products_part2.json"]
    all_items = []
    for part in parts:
        with open(part, encoding="utf-8") as f:
            all_items.extend(json.load(f))
    return all_items

catalog = load_catalog()
)

# Поиск по ключевым словам
def search_products(query):
    query = query.lower()
    results = []
    for item in catalog:
        keywords = item.get("keywords", [])
        if (
            query in item["title"].lower()
            or query in item["description"].lower()
            or query in keywords
        ):
            results.append(item)
    return results[:5]

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    if not query:
        return jsonify({"error": "Missing query parameter"}), 400
    results = search_products(query)

    # Форматируем в markdown
    formatted = [
        {
            "markdown": f"**[{item['title']}]({item['url']})** — {item['description']}"
        }
        for item in results
    ]
    return jsonify(formatted)

@app.route('/')
def home():
    return "Wildberries ассистент работает!"

if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
