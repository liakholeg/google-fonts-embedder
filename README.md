# google-fonts-embedder
Сервис для вставки шрифта из Google Fonts на сайт, созданный в uKit. Введи ссылку на шрифт — получишь готовый код с CSS-классом и подключением через Google Fonts API.


## Обновление v2.0 (15.11.2025)

**Ключовое исправление:** Теперь сервис генерирует код для **смены шрифта на ВСЕМ сайте**, а не только для одного класса.

### Что изменилось:
- Функция `generate_embed_code()` переименована на `generate_embed_code_full_site()`
- Код теперь заполняет **все** HTML элементы: `body, h1-h6, p, a, button, div, span, input, textarea, ul, ol, li, table, label, section, article, header, footer, nav`
- Обновлен интерфейс (дескрипция и эвиденция того, что код заменяет шрифт на всём сайте)

### Пример генерируемого кода:
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat+Alternates:wght@100;200;300;...&display=swap" rel="stylesheet">
<style>
body, h1, h2, h3, h4, h5, h6, p, a, button, div, span, input, textarea, ul, ol, li, table, th, td, label, section, article, header, footer, nav {
  font-family: "Montserrat Alternates", sans-serif !important;
}
</style>
```
