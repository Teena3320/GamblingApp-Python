from config.database import get_connection


class AlertRepository:

    @staticmethod
    def create(gambler_id, alert_type, message):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO alerts (gambler_id, alert_type, message) VALUES (%s,%s,%s)",
            (gambler_id, alert_type, message)
        )

        alert_id = cursor.lastrowid
        conn.commit()
        cursor.close()
        conn.close()
        return alert_id

    @staticmethod
    def get_by_gambler_id(gambler_id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM alerts WHERE gambler_id = %s ORDER BY created_at DESC",
            (gambler_id,)
        )
        alerts = cursor.fetchall()

        cursor.close()
        conn.close()
        return alerts

    @staticmethod
    def get_by_id(alert_id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM alerts WHERE alert_id = %s",
            (alert_id,)
        )
        alert = cursor.fetchone()

        cursor.close()
        conn.close()
        return alert

    @staticmethod
    def delete(alert_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM alerts WHERE alert_id = %s",
            (alert_id,)
        )
        conn.commit()

        cursor.close()
        conn.close()