from flask import Flask, request, redirect
import cgi
import os
import jinja2
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def index():
    template = jinja_env.get_template('index.html')
    return template.render(user_error='', pass_error='', ver_error='', email_error='', failed_name='', failed_email='')
    #return form.format(user_error='', pass_error='', ver_error='', email_error='', failed_name='', failed_email='')
@app.route('/', methods=['POST'])
def validate():
    name = request.form['username']
    the_pass = request.form['password']
    ver_pass = request.form['verify']
    the_email = request.form['email']
    user_error =''
    pass_error =''
    ver_error =''
    email_error =''
    if len(name) < 3 or len(name) > 20:
        user_error = "Not a valid username!"
    if " " in name:
        user_error = "Not a valid username!"
    if len(the_pass) < 3 or len(the_pass) > 20:
        pass_error = "Not a valid password!"
    if " " in the_pass:
        pass_error = "Not a valid password!"

    if the_pass != ver_pass:
        ver_error = "Passwords do not match!"
    if len(the_email) > 0:
        if len(the_email) < 3 or len(the_email) > 20:
            email_error ='Not a valid email!'
        elif " " in the_email:
            email_error ='Not a valid email!'
        elif "@" not in the_email and "." not in the_email:
            email_error ='Not a valid email!'




    if not user_error and not pass_error and not ver_error and not email_error:
        return redirect('/welcome?name={0}'.format(name))
    else:
        template = jinja_env.get_template('index.html')
        return template.render(user_error=user_error, pass_error=pass_error, ver_error=ver_error, email_error=email_error, failed_name=name, failed_email=the_email)
        #return form.format(user_error=user_error, pass_error=pass_error, ver_error=ver_error, email_error=email_error, failed_name=name, failed_email=the_email)
@app.route('/welcome')
def hello():
    template = jinja_env.get_template('welcome.html')
    username = request.args.get('name')
    #user = request.form['username']
    #return '<h1> Hello {0}!</h1>'.format(username)
    return template.render(user_name=username)

app.run()