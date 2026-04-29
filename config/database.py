import mysql.connector
from mysql.connector import Error

SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    full_name VARCHAR(255),
    email VARCHAR(255),
    is_active BOOLEAN DEFAULT TRUE,
    initial_stake DECIMAL(15, 4) NOT NULL,
    current_stake DECIMAL(15, 4) NOT NULL,
    win_threshold DECIMAL(15, 4) NOT NULL,
    loss_threshold DECIMAL(15, 4) NOT NULL,
    min_required_stake DECIMAL(15, 4) NOT NULL
);

CREATE TABLE IF NOT EXISTS bets (
    bet_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    amount DECIMAL(15, 2) NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'OPEN',
    payout DECIMAL(15, 2),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE IF NOT EXISTS betting_preferences (
    preference_id INT AUTO_INCREMENT PRIMARY KEY,
    gambler_id INT UNIQUE NOT NULL,
    min_bet DECIMAL(15, 2) NOT NULL,
    max_bet DECIMAL(15, 2) NOT NULL,
    preferred_strategy VARCHAR(50) NOT NULL,
    auto_play_enabled BOOLEAN DEFAULT FALSE,
    max_bets_per_session INT,
    FOREIGN KEY (gambler_id) REFERENCES users(user_id)
);

CREATE TABLE IF NOT EXISTS stake_transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    gambler_id INT NOT NULL,
    transaction_type VARCHAR(30) NOT NULL,
    amount DECIMAL(15, 2) NOT NULL,
    balance_before DECIMAL(15, 2) NOT NULL,
    balance_after DECIMAL(15, 2) NOT NULL,
    reference_id INT,
    description VARCHAR(255),
    FOREIGN KEY (gambler_id) REFERENCES users(user_id)
);

CREATE TABLE IF NOT EXISTS betting_sessions (
    session_id INT AUTO_INCREMENT PRIMARY KEY,
    gambler_id INT NOT NULL,
    strategy VARCHAR(50) NOT NULL,
    start_stake DECIMAL(15, 2) NOT NULL,
    end_stake DECIMAL(15, 2),
    total_bets INT,
    status VARCHAR(30) NOT NULL,
    started_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    ended_at DATETIME,
    FOREIGN KEY (gambler_id) REFERENCES users(user_id)
);

CREATE TABLE IF NOT EXISTS alerts (
    alert_id INT AUTO_INCREMENT PRIMARY KEY,
    gambler_id INT NOT NULL,
    alert_type VARCHAR(50) NOT NULL,
    message VARCHAR(255) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (gambler_id) REFERENCES users(user_id)
);
"""

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        port="3306",
        user="root",
        password="2003",
        database="gambling_db"
    )


def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()

    statements = SCHEMA_SQL.strip().split(";")

    for stmt in statements:
        stmt = stmt.strip()
        if stmt:
            cursor.execute(stmt)
            # print(f"Executed: {stmt[:50]}...")

    conn.commit()
    cursor.close()
    conn.close()