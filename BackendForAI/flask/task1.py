from flask import Flask,request

app=Flask(__name__)


@app.route('/login',methods=['POST','GET'])
def loging():
    if request.method=='POST':
        return f"Logged in as {(request.form['username'])}"
    else:
        return '''<form action='./login' method='POST' >
        <input type='text' name='username' > <br/>  <br/> 
        <input value='Login' type='submit' >'''
    
@app.route('/logout')
def logout():
    return f'You are not logged in'


if __name__=='__main__':
    app.run(debug=True)