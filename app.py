from flask import Flask
app = Flask(__name__)

@app.route('/voice_text')
def get_voice_text():
        return 'Hello, World!'

if __main__ =="__main__":
    app.run(debug=True)
