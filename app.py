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

def generate_embed_code_full_site(font_name):
    """Генирирует embed-код для замены шрифта на ВСЁМ сайте (не только для одного класса)"""
    if not font_name:
        return None
    
    font_param = font_name.replace(' ', '+')
    google_fonts_link = f'https://fonts.googleapis.com/css2?family={font_param}:wght@100;200;300;400;500;600;700;800;900&display=swap'
    
    # Код для замены шрифта на всем сайте
    embed_code = f'''<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{google_fonts_link}" rel="stylesheet">
<style>
body, h1, h2, h3, h4, h5, h6, p, a, button, div, span, input, textarea, ul, ol, li, table, th, td, label, section, article, header, footer, nav {{
  font-family: "{font_name}", sans-serif !important;
}}
</style>'''
    
    return {
        'font_name': font_name,
        'google_link': google_fonts_link,
        'embed_code': embed_code,
        'description': 'Код для замены шрифта на ВСЁМ сайте'
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
    
    result = generate_embed_code_full_site(font_name)
    return jsonify(result), 200

if __name__ == '__main__':
    app.run(debug=True)
