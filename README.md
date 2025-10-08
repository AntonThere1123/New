Основная структура сайта
Это интернет-магазин на Flask с такими разделами:

🏠 Главная страница (/)
python
@app.route('/')
def index():
    shop = productDB()  # Берет товары из базы данных
    return render_template('Main.html', shop=shop)
Показывает все товары из базы данных на главной странице

Использует функцию productDB() для получения списка товаров

📰 Раздел "Новости"
/News - главная страница новостей

/News/Promo - страница с акциями

/News/Announcements - страница с анонсами

🛍️ Раздел "Товары"
/Products - каталог товаров

/Products/Accessories - страница аксессуаров

👤 Личный кабинет (/MyOffice)
python
@app.route('/MyOffice', methods=['GET', 'POST'])
def my_office():
    if request.method == 'POST':
        username = request.form['username']  # Получает логин из формы
        password = request.form['password']  # Получает пароль из формы
        message = f'Добро пожаловать, {username}'
Есть вход через логин/пароль

Показывает приветствие после входа

📝 Регистрация (/register)
python
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return redirect(url_for('my_office'))  # Перенаправляет в кабинет
Регистрирует новых пользователей

После регистрации автоматически переводит в личный кабинет

📊 Работа с данными
python
def productDB():
    listDB = cursor.execute('SELECT * FROM product ')  # Берет все товары
    return listDB.fetchall()
Использует SQLite базу данных my_database.db

Хранит информацию о товарах в таблице product

🔗 Дополнительные страницы
/About_us - "О нас"

/Contacts - "Контакты"

/acc_user/<username> - персональная страница пользователя

Технические особенности:

Использует шаблоны HTML (render_template)

Поддержка GET/POST запросов

Режим отладки включен (debug=True)

 Внешний вид главной страницы
📱 Навигационное меню
html
<li class="navigation"><a href="/MyOffice">Личный кабинет</a></li>
<li class="navigation"><a href="/Products">Товары</a></li>
<li class="navigation"><a href="/News">Новинки</a></li>
5 основных разделов в верхнем меню

Все ссылки ведут на соответствующие страницы Flask

Стильное черное меню без подчеркиваний

🖼️ Дизайн и оформление
css
body {
    background-image: url('static/F1.png');
    background-repeat: repeat;
}
Узорчатый фон из изображения F1.png

Логотип сайта в левом верхнем углу (Key.png)

Центрированное приветствие "ДОБРО ПОЖАЛОВАТЬ НА ЭТОТ САЙТ"

🛍️ Система товаров
html
<div class="product-grid">
    <div class="product-card">
        <img src="static/Key.png" alt="T-Shirt Sample Image">
        <h3 class="product-title">Футболка Premium</h3>
        <span class="price">Цена: ₽1500</span>
        <button class="buy-btn">Купить</button>
    </div>
</div>
Особенности карточек товаров:

6 карточек с футболками разных категорий

Анимация при наведении - карточка увеличивается (transform: scale(1.05))

Кнопка "Купить" с золотым фоном

Цены от 700 до 1500 рублей

🎯 Интерактивные элементы
css
.product-card:hover {
    transform: scale(1.05);
}
Плавные анимации при взаимодействии

Эффекты наведения на карточки товаров

Кнопки меняют цвет при наведении (с золотого на оранжевый)

🔄 Связь с Flask
python
# В коде Flask:
def index():
    shop = productDB()  # Данные из БД
    return render_template('Main.html', shop=shop)
Страница получает реальные данные о товарах из базы данных

Но в текущем HTML товары захардкожены - нужно подключить переменную shop

Что можно улучшить:

Заменить статические товары на данные из shop

Добавить изображения для всех товаров

Сделать кнопку "Купить" функциональной
