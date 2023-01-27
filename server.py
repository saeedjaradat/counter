from flask import Flask,render_template,session,redirect,request
app=Flask(__name__)
app.secret_key='keep it secret'

@app.route('/')

def count():
    if 'count' not in session:
        session['count'] = 1
    else:
        session['count'] +=1
    return  render_template('index.html', count=session['count'])

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')
@app.route('/destroy_session', methods=['POST'])
def des():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)