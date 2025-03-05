from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/project')
def project():
    return render_template('project.html')

@app.route('/conducter')
def conductor():
    return render_template('conducter.html')

@app.route('/member')
def member():
    return render_template('member.html')

@app.route('/media')
def media():
    return render_template('media.html')

@app.route('/concert')
def concert():
    return render_template('concert.html')

@app.route('/publication')
def publication():
    return render_template('publication.html')

@app.route('/support')
def support():
    return render_template('support.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555, debug=True)