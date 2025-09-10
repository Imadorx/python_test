from flask import Flask, render_template, request  ,redirect , url_for
import psycopg2
from psycopg2.extras import RealDictCursor
import models

app = Flask(__name__)


@app.route("/")
def index():
    posts = models.get_all_posts()
    return render_template('index.html', posts=posts)

@app.route("/add-post", methods=["POST"])
def add_post():
    title = request.form['title']
    content = request.form['p_content']
    models.add_post(title, content)
    return redirect(url_for('index'))

@app.route("/update-post/<int:post_id>", methods=["GET", "POST"])
def update_post(post_id):
    if request.method == "POST":
        title = request.form['title']
        content = request.form['p_content']
        models.update_post(post_id, title, content)
        return redirect(url_for('index'))
    else:
        post = models.get_post(post_id)
        return render_template('update_post.html', post=post)

@app.route("/delete-post/<int:post_id>", methods=["POST"])
def delete_post(post_id):
    models.delete_post(post_id)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True, port=9000)


