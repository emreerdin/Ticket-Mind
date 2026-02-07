from ticketmind.db.connection import get_db_connection, release_db_connection


def insert_agent_run(agent_name, ticket_id, trace_id, state):
    conn = get_db_connection()
    cur = conn.cursor()

    try:
        cur.execute(
            "INSERT INTO agent_runs (agent_name, input_type, ticket_id, trace_id, current_state) VALUES (%s,%s, %s, %s, %s);",
            (str(agent_name), "TICKET", str(ticket_id), str(trace_id), state.name)
        )
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cur.close()
        release_db_connection(conn=conn)


def update_agent_run(trace_id, state):
    conn = get_db_connection()
    cur = conn.cursor()

    try:
        cur.execute(
            """
            UPDATE agent_runs
            SET current_state = %s
            WHERE trace_id = %s;
            """,
            (state.name, str(trace_id))
        )
        conn.commit()

    except Exception as e:
        conn.rollback()
        raise e

    finally:
        cur.close()
        release_db_connection(conn=conn)
