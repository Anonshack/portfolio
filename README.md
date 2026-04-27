# 🚀 Kudratbek Kazakjonov — Django Portfolio

Django asosidagi portfolio veb-sayti — ro'yxatdan o'tish, login, fikr qoldirish va 3 tilli interfeys (UZ/EN/RU).

---

## 📁 Loyiha strukturasi

```
portfolio/
├── portfolio_project/       # Django settings, urls, wsgi
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── portfolio_app/           # Asosiy ilova
│   ├── models.py            # Review modeli
│   ├── views.py             # Home, register, login, logout, add_review
│   ├── forms.py             # RegisterForm, LoginForm, ReviewForm
│   ├── urls.py
│   ├── admin.py
│   ├── templates/portfolio_app/
│   │   ├── index.html       # Asosiy sahifa
│   │   ├── login.html
│   │   └── register.html
│   └── static/portfolio_app/
│       └── img/
│           └── me.jpeg      # ← O'z rasmingizni shu yerga qo'ying!
├── locale/
│   ├── uz/LC_MESSAGES/django.po  # O'zbek tarjimalar
│   ├── ru/LC_MESSAGES/django.po  # Rus tarjimalar
│   └── en/LC_MESSAGES/django.po  # Ingliz (passthrough)
├── requirements.txt
├── Procfile                 # Railway/Heroku uchun
├── railway.json
├── nixpacks.toml
├── manage.py
└── .env.example
```

---

## 💻 Lokal ishga tushirish

### 1. Virtual environment yarating
```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
# yoki
venv\Scripts\activate           # Windows
```

### 2. Dependencies o'rnating
```bash
pip install -r requirements.txt
```

### 3. .env fayl yarating
```bash
cp .env .env
# .env faylini oching va SECRET_KEY ni o'zgartiring
```

### 4. O'z rasmingizni qo'ying
```
portfolio_app/static/portfolio_app/img/me.jpeg
```

### 5. Migrate va superuser
```bash
python manage.py migrate
python manage.py createsuperuser
```

### 6. Tarjimalarni compile qiling
```bash
python manage.py compilemessages
```

### 7. Static fayllarni yig'ing
```bash
python manage.py collectstatic
```

### 8. Ishga tushiring
```bash
python manage.py runserver
```

**http://localhost:8000** da oching! 🎉

---

## 🚂 Railway'ga Deploy qilish

### 1. GitHub'ga yuklang
```bash
git init
git add .
git commit -m "Initial portfolio"
git branch -M main
git remote add origin https://github.com/USERNAME/portfolio.git
git push -u origin main
```

### 2. Railway.app'da yangi loyiha
1. [railway.app](https://railway.app) ga kiring
2. **New Project** → **Deploy from GitHub repo**
3. Repositoriyangizni tanlang

### 3. PostgreSQL qo'shing
1. Railway'da **+ Add Service** → **Database** → **PostgreSQL**
2. DATABASE_URL avtomatik o'rnatiladi

### 4. Environment Variables qo'shing
Railway dashboard → **Variables** bo'limiga:

| Variable | Value |
|----------|-------|
| `SECRET_KEY` | `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"` |
| `DEBUG` | `False` |

### 5. Deploy!
Railway avtomatik deploy qiladi. Domain: `https://your-project.railway.app` 🎉

### 6. Superuser yaratish (Railway shell orqali)
```bash
# Railway dashboard → your service → Shell
python manage.py createsuperuser
```

**Admin panel:** `https://your-domain.railway.app/admin/`

---

## ✨ Funksiyalar

| Funksiya | Tavsif |
|---------|--------|
| 🌐 **3 til** | UZ / EN / RU — sahifa yangilanmasdan |
| 🔐 **Register/Login** | Django auth tizimi |
| ⭐ **Fikrlar** | Login qilgan userlar fikr qoldirishlari mumkin |
| 🌙 **Dark/Light** | Mavzu almashtirish |
| 📱 **Responsive** | Mobil qurilmalar uchun moslashgan |
| 📧 **EmailJS** | Aloqa formasi (EmailJS orqali) |
| 🛡️ **Admin** | Django admin panelida fikrlarni boshqarish |

---

## ⚙️ Sozlamalar

**Rasm qo'shish:**
```
portfolio_app/static/portfolio_app/img/me.jpeg
```

**EmailJS sozlash** (index.html ichida):
```javascript
const EMAILJS_PUBLIC_KEY  = 'YOUR_KEY';
const EMAILJS_SERVICE_ID  = 'YOUR_SERVICE_ID';
const EMAILJS_TEMPLATE_ID = 'YOUR_TEMPLATE_ID';
```

**Yangi tarjima qo'shish:**
```bash
python manage.py makemessages -l uz
# .po faylni tahrirlang
python manage.py compilemessages
```

---

## 🛠️ Texnologiyalar

- **Django 4.2** — Backend framework
- **WhiteNoise** — Static file serving
- **PostgreSQL** — Production database (Railway)
- **SQLite** — Development database
- **Gunicorn** — WSGI server
- **Railway** — Cloud hosting

---

Made️ by Kudratbek Kazakjonov
