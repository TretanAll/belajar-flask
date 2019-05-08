from flask  import Flask, render_template
app = Flask(__name__)

#: route untuk index
@app.route('/')
def hello():
    #:memanggil templates yang sudah dibuat
    return render_template('index.html')

    
#: route untuk url tambahan + parameter
@app.route('/profile/<username>')
def show_profile(username):
    #: tanda %s untuk tipe data string
    return 'Hello %s' % username + '!!!'