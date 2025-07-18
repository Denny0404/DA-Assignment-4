import mysql.connector

def test_schema():
    conn = mysql.connector.connect(user='root', database='subscribers')
    cursor = conn.cursor()
    cursor.execute("SHOW COLUMNS FROM subscriber;")
    columns = [col[0] for col in cursor.fetchall()]
    assert 'email' in columns
    assert 'subscription_date' in columns
    print("✅ Schema validation passed.")

if __name__ == "__main__":
    test_schema()
