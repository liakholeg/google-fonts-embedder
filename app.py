from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

def extract_font_from_url(url):
    """Извлекает название шрифта из ссылки Google Fonts"""
    match = re.search(r'specimen/([^/?]+)', url)
    if match:
        font_name = match.group(1).replace('+', ' ')
        return font_name
    return None

def generate_embed_code(font_name):
    """Генерирует embed-код для uKit"""
    if not font_name:
        return None
    
    font_param = font_name.replace(' ', '+')
    google_fonts_link = f'https://fonts.googleapis.com/css2?family={font_param}&display=swap'
    css_class = font_name.lower().replace(' ', '-')
    
    embed_code = f'''<!-- Google Fonts Embed для uKit -->
<link href="{google_fonts_link}" rel="stylesheet">
<style>
  .ukit-font-{css_class} {{
    font-family: '{font_name}', sans-serif;
  }}
</style>

<!-- Как использовать: добавьте класс "ukit-font-{css_class}" к элементам -->
<!-- Пример: <p class="ukit-font-{css_class}">Текст шрифтом {font_name}</p> -->'''
    
    return {
        'font_name': font_name,
        'google_link': google_fonts_link,
        'css_class': css_class,
        'embed_code': embed_code
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/convert', methods=['POST'])
def convert():
    data = request.get_json()
    url = data.get('url', '').strip()
    
    if not url:
        return jsonify({'error': 'URL не указан'}), 400
    
    font_name = extract_font_from_url(url)
    if not font_name:
        return jsonify({'error': 'Не удалось извлечь шрифт из ссылки. Проверьте URL.'}), 400
    
    result = generate_embed_code(font_name)
    return jsonify(result), 200

if __name__ == '__main__':
    app.run(debug=True)
