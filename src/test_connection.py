from database import get_connection

conn = get_connection()
if conn:
    conn.close()