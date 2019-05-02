from flask  import Flask
app = Flask(__name__)

#: route untuk index
@app.route('/')
def hello():
    return 'Hello Bosku!!!'

#: route menambahkan url biasa
@app.route('/setting')
def setting():
    return 'Hello Bosku ini di url setting!!!'
    
#: route untuk url tambahan + parameter
@app.route('/profile/<username>')
def show_profile(username):
    #: tanda %s untuk tipe data string
    return 'Hello %s' % username + '!!!'
    
#: route untuk url tambahan + tipe data parameter
@app.route('/show_id/<int:blog_id>')
def show_blog(blog_id):
    #: tanda %d untuk tipe data angka
    return 'Hello ID anda =   %d' % blog_id