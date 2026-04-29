from cli import start_cli
from config.database import initialize_database

def main():
    initialize_database()
    start_cli()

if __name__ == "__main__":
    main()