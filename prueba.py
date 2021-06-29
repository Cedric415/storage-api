from bottle import Bottle, run

app = Bottle()

@app.route('/')
def greet(name='Stranger'):
    return template('Hello {{name}}, how are you?', name=name)

run(app, host='localhost', port=8080)
