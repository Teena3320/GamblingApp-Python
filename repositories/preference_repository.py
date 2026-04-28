from config.database import get_connection


class PreferenceRepository:

    @staticmethod
    def get_by_user_id(user_id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM betting_preferences WHERE gambler_id = %s",
            (user_id,)
        )
        prefs = cursor.fetchone()

        cursor.close()
        conn.close()
        return prefs

    @staticmethod
    def create(user_id, min_bet, max_bet, strategy):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO betting_preferences (
                gambler_id, min_bet, max_bet,
                preferred_strategy, auto_play_enabled, max_bets_per_session
            )
            VALUES (%s,%s,%s,%s,%s,%s)
        """, (
            user_id, min_bet, max_bet,
            strategy, False, 10
        ))

        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def update_strategy(user_id, strategy):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE betting_preferences SET preferred_strategy=%s WHERE gambler_id=%s",
            (strategy, user_id)
        )

        conn.commit()
        cursor.close()
        conn.close()