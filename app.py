from flask import Flask, render_template
import os

app = Flask(__name__, template_folder="templates")

# Add these configuration settings
app.config['SERVER_NAME'] = 'localhost:5000'  # Or your actual domain
app.config['APPLICATION_ROOT'] = '/'         # Root path of your app
app.config['PREFERRED_URL_SCHEME'] = 'http'  # Or 'https' if using SSL


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

def save_static_html():
    output_dir = "static_site"
    os.makedirs(output_dir, exist_ok=True)  # Create directory if it doesn't exist
    
    with app.app_context():
        routes = [
            ('/', 'index.html'),
            ('/about', 'about.html'),
            ('/project', 'project.html'),
            ('/conductor', 'conductor.html'),  # Fixed typo
            ('/member', 'member.html'),
            ('/media', 'media.html'),
            ('/concert', 'concert.html'),
            ('/publication', 'publication.html'),
            ('/support', 'support.html'),
            ('/contact', 'contact.html')
        ]
        
        for route, filename in routes:
            try:
                html_content = render_template(filename)
                output_path = os.path.join(output_dir, filename)
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                with open(output_path, "w", encoding='utf-8') as f:
                    f.write(html_content)
                print(f"Generated static file: {output_path}")
            except Exception as e:
                print(f"Error generating {filename}: {str(e)}")

if __name__ == '__main__':
    # Run this manually or via command line when needed
    save_static_html()
    # app.run(debug=True)  # Uncomment to run the development server

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555, debug=True)