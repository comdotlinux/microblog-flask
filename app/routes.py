from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'guru'}
    return '''
    <html>
        <head>
            <title>Home page - microblog</title>
        </head>
        <body>
            <h1>Hello, ''' + user['username'] + '''</h1>
        </body>
    </html>
    '''
