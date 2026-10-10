from flask import Flask , request
from flask import render_template 

app=Flask(__name__)


@app.route('/')
def index():
    return 'index page'

@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {username}                      '

@app.route('/profile/<int:post_id>')
def show_post(post_id):
    return f"post {post_id}"

@app.route('/greeting')
@app.route('/greeting/<name>')
def hello(name=None):
    #telling Flask to open an HTML file and send it to the browser.
    #By default, Flask expects HTML templates inside a folder called templates
    return render_template('greeting.html',name=name)


# when someone visits /formtest , allow both GET , POST requests , since by default flask allow only GET
@app.route('/formtest',methods=['POST','GET'])
def form_test():
    if request.method=='POST':
        #Get the value that the user entered in the form field whose name is "username"
        #%s → placeholder for a string
        #%  → puts the value into the placeholder
        return 'Username : %s' % (request.form['username'])
    else:
        # action tell the browser where i should send the form data
        return ''' <form action="/formtest"  method="post">
        Name: <input name="username"  type="text" /> <br/>
        <input value="send" type="submit" /> 
        </form>'''


if __name__=='__main__':
    app.run(debug=True)