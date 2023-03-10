from flask import Flask, render_template, session, redirect

app = Flask(__name__)    
app.secret_key = 'speak friend and enter'
# Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    if session.get('count'):
        print('key exists!')
        session['count'] += 1
    else:
        print("key 'count' does NOT exist")
        session['count'] = 1
    return render_template('index.html', count = session['count'])

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

# @app.route('/')

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)