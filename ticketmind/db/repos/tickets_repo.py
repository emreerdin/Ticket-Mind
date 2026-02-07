from ticketmind.db import connection
from psycopg2.extras import RealDictCursor


def get_tickets():
    conn = connection.get_db_connection()
    cur = conn.cursor()    
    try:
        cur.execute(
            "SELECT * FROM tickets;"
        )
        results = cur.fetchall()
        return results
    except Exception as e:
        raise e
    finally:
        cur.close()
        connection.release_db_connection(conn)

def get_open_tickets():
    conn = connection.get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    try:
        cur.execute(
            "SELECT * FROM tickets WHERE status = 'open' ORDER BY created_at"
        )
        results = cur.fetchall()
        return results
    except Exception as e:
        raise e
    finally:
        cur.close()
        connection.release_db_connection(conn=conn)