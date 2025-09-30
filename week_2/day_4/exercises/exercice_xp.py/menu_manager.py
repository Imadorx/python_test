import psycopg2
from menu_item import get_connection

class MenuManager:

    @classmethod
    def get_by_name(cls, name):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM Menu_Items WHERE item_name = %s", (name,))
        row = cur.fetchone()
        cur.close()
        conn.close()
        if row:
            return {"id": row[0], "name": row[1], "price": row[2]}
        return None

    @classmethod
    def all_items(cls):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM Menu_Items")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return [{"id": r[0], "name": r[1], "price": r[2]} for r in rows]
