from config.database import get_connection


class BettingSessionRepository:

    @staticmethod
    def create_session(gambler_id, strategy, start_stake, status="RUNNING"):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO betting_sessions (gambler_id, strategy, start_stake, status) VALUES (%s,%s,%s,%s)",
            (gambler_id, strategy, start_stake, status)
        )

        session_id = cursor.lastrowid
        conn.commit()
        cursor.close()
        conn.close()
        return session_id

    @staticmethod
    def finish_session(session_id, end_stake, total_bets, status="COMPLETED"):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE betting_sessions SET end_stake=%s, total_bets=%s, status=%s, ended_at=NOW() WHERE session_id=%s",
            (end_stake, total_bets, status, session_id)
        )

        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def get_by_gambler_id(gambler_id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM betting_sessions WHERE gambler_id = %s ORDER BY started_at DESC",
            (gambler_id,)
        )
        sessions = cursor.fetchall()

        cursor.close()
        conn.close()
        return sessions

    @staticmethod
    def get_by_id(session_id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM betting_sessions WHERE session_id = %s",
            (session_id,)
        )
        session = cursor.fetchone()

        cursor.close()
        conn.close()
        return session