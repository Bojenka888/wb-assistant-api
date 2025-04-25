from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

# Загрузка товаров
with open('products.json', encoding='utf-8') as f:
    catalog = json.load(f)

# Поиск по ключевым словам
def search_products(query):
    query = query.lower()
    results = []
    for item in catalog:
        title = item.get("title", "")
        description = item.get("description", "")
        url = item.get("url", "")
        if query in title.lower() or query in description.lower():
            # Формат Markdown с кликабельной ссылкой
            formatted_item = f"**[{title}]({url})** — {description}"
            results.append(formatted_item)
    return results[:4]  # максимум 4 товара

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    if not query:
        return jsonify({"error": "Missing query parameter"}), 400
    results = search_products(query)
    return jsonify(results)

@app.route('/')
def home():
    return "Wildberries ассистент работает!"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
