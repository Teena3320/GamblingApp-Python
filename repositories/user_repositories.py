from config.database import get_connection


class UserRepository:

    @staticmethod
    def create(username, fullname, email, stake, win_threshold, loss_threshold):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO users (
                username, full_name, email, is_active,
                initial_stake, current_stake,
                win_threshold, loss_threshold, min_required_stake
            )
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """, (
            username, fullname, email, True,
            stake, stake,
            win_threshold , loss_threshold, 10
        ))

        user_id = cursor.lastrowid
        conn.commit()

        cursor.close()
        conn.close()
        return user_id

    @staticmethod
    def get_by_id(user_id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM users WHERE user_id = %s",
            (user_id,)
        )
        user = cursor.fetchone()

        cursor.close()
        conn.close()
        return user

    @staticmethod
    def get_by_username(username):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM users WHERE username = %s",
            (username,)
        )
        user = cursor.fetchone()

        cursor.close()
        conn.close()
        return user

    @staticmethod
    def update_stake(user_id, new_stake):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE users SET current_stake = %s WHERE user_id = %s",
            (new_stake, user_id)
        )

        conn.commit()
        cursor.close()
        conn.close()