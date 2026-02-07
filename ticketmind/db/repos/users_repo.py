from ticketmind.db.connection import get_db_connection, release_db_connection
from psycopg2.extras import RealDictCursor

def ticket_user_check(user_id):
    conn = get_db_connection()
    cur = conn.cursor()

    try:
        cur.execute(
            "SELECT * FROM users WHERE user_id = %s",
            (user_id,)
        )
        return True
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cur.close()
        release_db_connection(conn=conn)

def get_user(user_id):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    try:
        cur.execute(
            "SELECT * FROM users WHERE user_id = %s",
            (user_id,)
        )
        user = cur.fetchone()
        return user
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cur.close()
        release_db_connection(conn=conn)