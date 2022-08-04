from website import create_app
from flask import render_template



app = create_app()

  

@app.route('/forget_password')
def forget_password():
    return render_template('forget_password.html')
app.run(host ="0.0.0.0",port = "8080" ,debug = True)