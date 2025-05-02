from flask import Flask, render_template, request
import requests
import certifi
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    quote = None
    if request.method == 'POST':
        quote = get_quote()
    return render_template('index.html', quote=quote)

def get_quote():
    url = "https://api.quotable.io/random"
    try:
        response = requests.get(url, verify=False)
        response.raise_for_status()  # Проверяем на ошибки HTTP
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching quote: {e}")
        return {"content": "Не удалось загрузить цитату. Попробуйте еще раз.", "author": "Ошибка"}

if __name__ == '__main__':
    app.run(debug=True)