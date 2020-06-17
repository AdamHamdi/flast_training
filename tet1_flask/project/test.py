from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)
@app.route('/')
def hello():
  return render_template('hello.html')
@app.route('/login')
def loging_in():
  return render_template('login.html')


@app.route('/welcome/<user>')
def show_profile(user):
   return render_template('welcome.html',name = user )
@app.route('/welcome/<user>/<int:score>')
def show_score(score,user):
   return render_template('hello.html',name=user,marks = score )


@app.route('/posts/<int:post_id>')
def show_post(post_id):
   return 'Post %s' %post_id 

@app.route('/admin')
def hello_admin():
   return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return'Hello %s as guest'% guest
@app.route('/user/<name>')
def hello_user(name):
  if(name=='admin'):
     return redirect(url_for('hello_admin')) 
  else:
     return redirect(url_for('hello_guest',guest=name)) 
   
@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name
 
@app.route('/login',methods=['POST','GET'])
def login():
   if request.method=='POST':
      username=request.form['username']
      password=request.form['password']
      return redirect(url_for('success',name=username))  
   else:   
      username=request.args.get['username']
      password=request.args.get['password']
      return redirect(url_for('success',name=username))
##############################  
@app.route('/result')
def result():
   dict={'physic':50,'chemistry':60,'maths':70}
   return render_template('result.html',result=dict)
@app.route('/student')
def student():
   return render_template('student.html')


@app.route('/result',methods=['POST','GET'])
def student_subject():
   if request.method=='POST':
      result=request.form
      return render_template('result.html',result=result)   
###############cookies#################
@app.route('/index')
def index():
   return render_template('index3.html')

@app.route('/getcookie')
def getcookies():
  <str name>=request.cookies.get('userID')
   return '<h1>welcome'+name+'</h1>'

@app.route('/setcookie',methods=['POST','GET'])
def setcookie():
   if request.method=='POST':
      user=request.form['nm']
      resp=make_response(render_template('readcookies.html'))
      resp.set_cookie('userID',user)
      return resp
   return render_template('index3.html')

   
if __name__ == "__main__":
    app.run(debug=True)
    