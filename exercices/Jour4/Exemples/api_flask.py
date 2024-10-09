from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)


# Fonction pour initialiser la base de données SQLite
def init_db():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT
        )
    """
    )
    conn.commit()
    conn.close()


# Route pour récupérer tous les items (Read)
@app.route("/items", methods=["GET"])
def get_items():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items")
    items = cursor.fetchall()
    conn.close()
    return jsonify(items)


# Route pour créer un nouvel item (Create)
@app.route("/items", methods=["POST"])
def create_item():
    new_item = request.json
    name = new_item.get("name")
    description = new_item.get("description")

    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO items (name, description) VALUES (?, ?)", (name, description)
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "Item created successfully!"}), 201


# Route pour récupérer un item par ID (Read)
@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items WHERE id = ?", (item_id,))
    item = cursor.fetchone()
    conn.close()

    if item:
        return jsonify(item)
    else:
        return jsonify({"error": "Item not found"}), 404


# Route pour mettre à jour un item (Update)
@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    updated_item = request.json
    name = updated_item.get("name")
    description = updated_item.get("description")

    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE items SET name = ?, description = ? WHERE id = ?",
        (name, description, item_id),
    )
    conn.commit()
    conn.close()

    return jsonify({"message": "Item updated successfully!"})


# Route pour supprimer un item (Delete)
@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM items WHERE id = ?", (item_id,))
    conn.commit()
    conn.close()

    return jsonify({"message": "Item deleted successfully!"})


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
