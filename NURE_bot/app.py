from app import app, db
import os

@app.shell_context_processor
def make_shell_context():
    return {'db': db}

app.secret_key = 'you-will-never-guess'
app.run(debug = True)
app.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))
