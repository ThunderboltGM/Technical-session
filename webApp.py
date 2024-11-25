from Flask import flask
import render_templates,url_for

def home():
    return render_templates('/home')

app = flask()
if __name__ == "__main__":
    app.run(debug=True)