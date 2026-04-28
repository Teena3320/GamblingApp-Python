from config.database import get_connection


class BetRepository:

    @staticmethod
    def create(user_id, amount):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO bets (user_id, amount, status) VALUES (%s,%s,'OPEN')",
            (user_id, amount)
        )

        bet_id = cursor.lastrowid
        conn.commit()

        cursor.close()
        conn.close()
        return bet_id

    @staticmethod
    def get_by_id(bet_id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM bets WHERE bet_id = %s",
            (bet_id,)
        )
        bet = cursor.fetchone()

        cursor.close()
        conn.close()
        return bet

    @staticmethod
    def get_by_user_id(user_id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM bets WHERE user_id = %s ORDER BY bet_id DESC",
            (user_id,)
        )
        bets = cursor.fetchall()

        cursor.close()
        conn.close()
        return bets

    @staticmethod
    def update_status(bet_id, status, payout):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE bets SET status=%s, payout=%s WHERE bet_id=%s",
            (status, payout, bet_id)
        )

        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def delete(bet_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM bets WHERE bet_id = %s",
            (bet_id,)
        )

        conn.commit()
        cursor.close()
        conn.close()