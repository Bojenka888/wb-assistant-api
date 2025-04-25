from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Загрузка каталога товаров
with open('products.json', encoding='utf-8') as f:
    catalog = json.load(f)

# Поиск по ключевым словам
def search_products(query):
    query = query.lower()
    results = []
    for item in catalog:
        if query in item['title'].lower() or query in item['description'].lower():
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