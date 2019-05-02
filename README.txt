1. Untuk Menginstall Flask di
    pip install flask
2. Untuk Menjalankan flask di windows
    set FLASK_APP=app.py
    set FLASK_ENV=development // untuk mengaktifkan environment
    flask run

    Atau bisa jua
    python -m flask run

    Atau agar bisa leboh mudah melihat perubahan tanpa restart server di linux
    FLASK_APP=app.py FLASK_DEBUG=1 python -m flask run