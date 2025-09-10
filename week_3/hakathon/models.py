import psycopg2
from psycopg2.extras import RealDictCursor

DB_CONFIG = {
    "dbname": "blog",
    "user": "postgres",
    "host": "localhost",
    "port": "5432",
    "password": "20020429"
}

def get_db_connection():
    conn = psycopg2.connect(**DB_CONFIG, cursor_factory=RealDictCursor)
    return conn

def get_all_posts():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM posts ORDER BY p_id DESC")
    posts = cur.fetchall()
    cur.close()
    conn.close()
    return posts

def get_post(post_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM posts WHERE p_id=%s", (post_id,))
    post = cur.fetchone()
    cur.close()
    conn.close()
    return post

def add_post(title, content):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO posts (title, p_content) VALUES (%s, %s)", (title, content))
    conn.commit()
    cur.close()
    conn.close()

def update_post(post_id, title, content):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("UPDATE posts SET title=%s, p_content=%s WHERE p_id=%s", (title, content, post_id))
    conn.commit()
    cur.close()
    conn.close()

def delete_post(post_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM posts WHERE p_id=%s", (post_id,))
    conn.commit()
    cur.close()
    conn.close()



