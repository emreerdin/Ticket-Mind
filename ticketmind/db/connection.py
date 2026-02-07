import os
from psycopg2.pool import SimpleConnectionPool
from psycopg2.extras import RealDictCursor
from psycopg2.extensions import connection as PGConnection
from dotenv import load_dotenv



load_dotenv()

DATABASE_DSN = (
    f"host={os.getenv('HOST')} "
    f"dbname={os.getenv('DB_NAME')} "
    f"user={os.getenv('DB_USERNAME')} "
    f"password={os.getenv('DB_PASSWORD')} "
    f"port=5433"
)

pool = SimpleConnectionPool(
    minconn=1,
    maxconn=5,
    dsn=DATABASE_DSN
)

def get_db_connection() -> PGConnection:
    """
    Pool'dan bir connection alır.
    """
    return pool.getconn()

def release_db_connection(conn: PGConnection):
    pool.putconn(conn=conn)