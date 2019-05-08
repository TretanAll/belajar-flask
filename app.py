from flask  import Flask, render_template, request
app = Flask(__name__)

#: route untuk index
@app.route('/')
def hello():
    #:memanggil templates yang sudah dibuat
    return render_template('index.html')

    
#: route untuk url tambahan + parameter
@app.route('/profile/<username>')
def show_profile(username):
    #: memanggil profil.html dengan parameter username
    return render_template('profil.html', username=username) #: key = value

@app.route('/login', methods=['GET','POST'])
def show_login():
    if request.method == 'POST':
        return 'Email kamu adalah '+ request.form['email']
    return render_template('login.html')