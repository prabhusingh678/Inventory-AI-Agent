# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware

# # ✅ FIRST create app
# app = FastAPI()

# # ✅ THEN add middleware
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Example route
# @app.get("/")
# def root():
#     return {"message": "Inventory AI Agent is running 🚀"}

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import psycopg2

app = FastAPI()

# ✅ Enable CORS (important for frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Request schema
class Query(BaseModel):
    question: str

# ✅ Database connection
def get_connection():
    return psycopg2.connect(
        host="db",          # Docker service name
        database="inventory",
        user="postgres",
        password="postgres"
    )

# ✅ MAIN API
@app.post("/ask")
def ask_agent(query: Query):
    question = query.question.lower()

    conn = get_connection()
    cur = conn.cursor()

    try:
        # 🔹 Tool 1: Low stock
        if "low" in question and "stock" in question:
            cur.execute("SELECT name, quantity FROM products WHERE quantity < 10;")
            rows = cur.fetchall()

            if not rows:
                return {"response": "All items are sufficiently stocked ✅"}

            result = "\n".join([f"{name} → {qty}" for name, qty in rows])
            return {"response": f"Low stock items:\n{result}"}

        # 🔹 Tool 2: Total inventory
        elif "total" in question:
            cur.execute("SELECT SUM(quantity) FROM products;")
            total = cur.fetchone()[0]
            return {"response": f"Total inventory count: {total}"}

        # 🔹 Tool 3: List all items
        elif "list" in question or "all items" in question:
            cur.execute("SELECT name, quantity FROM products;")
            rows = cur.fetchall()

            result = "\n".join([f"{name} → {qty}" for name, qty in rows])
            return {"response": f"Inventory List:\n{result}"}

        # 🔹 Default
        else:
            return {"response": "Try asking: low stock, total inventory, or list items 🤖"}

    except Exception as e:
        return {"response": f"Error: {str(e)}"}

    finally:
        cur.close()
        conn.close()

# ✅ Health check
@app.get("/")
def root():
    return {"message": "Inventory AI Agent is running 🚀"}