from flask import Flask , request
from flask import render_template 

app=Flask(__name__)

################################
@app.route('/')
def helloworld():
    return 'hello world'
################################
@app.route('/<name>')
def hello_name(name=None):
    return f'hello {name}'
################################
@app.route('/user/<username>')
def hello_user(username):
    return f'hello user :{username}'
#################################
@app.route('/post/<int:number>')
def number(number):
    return 'number %d ' %number
#################################
@app.route('/<name>')
def index(name=None):
    return render_template('hello.html',name=name)
#################################
@app.route('/formtest',methods=['POST','GET'])
def formtest():
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
    app.run(debug=True,port=5002)