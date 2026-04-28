from config.database import get_connection


class StakeTransactionRepository:

    @staticmethod
    def create(gambler_id, transaction_type, amount, balance_before, balance_after, reference_id=None, description=None):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO stake_transactions (gambler_id, transaction_type, amount, balance_before, balance_after, reference_id, description) VALUES (%s,%s,%s,%s,%s,%s,%s)",
            (gambler_id, transaction_type, amount, balance_before, balance_after, reference_id, description)
        )

        transaction_id = cursor.lastrowid
        conn.commit()
        cursor.close()
        conn.close()
        return transaction_id

    @staticmethod
    def get_by_gambler_id(gambler_id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM stake_transactions WHERE gambler_id = %s ORDER BY transaction_id DESC",
            (gambler_id,)
        )
        transactions = cursor.fetchall()

        cursor.close()
        conn.close()
        return transactions

    @staticmethod
    def get_by_id(transaction_id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM stake_transactions WHERE transaction_id = %s",
            (transaction_id,)
        )
        transaction = cursor.fetchone()

        cursor.close()
        conn.close()
        return transaction