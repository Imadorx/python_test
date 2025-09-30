import psycopg2 ;
def get_connection():
    return psycopg2.connect(
        dbname="restaurant",
        user="postgres",     
        password="20020429",  
        host="localhost",
        port="5432"
    )

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def save(self):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO Menu_Items (item_name, item_price) VALUES (%s, %s)",
                    (self.name, self.price))
        conn.commit()
        cur.close()
        conn.close()
        print(f"{self.name} was added successfully!")

    def delete(self):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM Menu_Items WHERE item_name = %s", (self.name,))
        if cur.rowcount > 0:
            print(f"{self.name} was deleted successfully!")
        else:
            print(f"Error: {self.name} not found.")
        conn.commit()
        cur.close()
        conn.close()

    def update(self, new_name, new_price):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("UPDATE Menu_Items SET item_name=%s, item_price=%s WHERE item_name=%s",
                    (new_name, new_price, self.name))
        if cur.rowcount > 0:
            print(f"{self.name} updated to {new_name} ({new_price}) successfully!")
            self.name, self.price = new_name, new_price
        else:
            print(f"Error: {self.name} not found.")
        conn.commit()
        cur.close()
        conn.close()
