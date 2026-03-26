from app.database import get_db

def check_stock(query):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM products WHERE quantity < 5")
    return cursor.fetchall()

def update_inventory(query):
    return "Inventory updated successfully"

def generate_report():
    return "Report generated"