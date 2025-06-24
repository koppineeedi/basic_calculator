from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    with open("index.html") as f:
        html = f.read()
    return render_template_string(html)

if __name__ == "__main__":
    app.run(debug=True)
