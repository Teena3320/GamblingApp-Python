from decimal import Decimal

from config.database import engine, SessionLocal
from models import Base
from models.user import User
from models.betting_preferences import BettingPreferences

from services.bet_service import BetService
from services.bet_settlement_service import BetSettlementService
from services.bet_amount_service import BetAmountService
from services.eligibility_service import EligibilityService
from services.betting_session_service import BettingSessionService

from domain.outcome_service import OutcomeService

def enable_autoplay(gambler_id):
    db = SessionLocal()
    prefs = db.query(BettingPreferences).filter(
        BettingPreferences.gambler_id == gambler_id
    ).first()

    prefs.auto_play_enabled = True
    db.commit()
    db.close()

    print(" Autoplay enabled")

def register_user():
    db = SessionLocal()

    username = input("Enter username: ")
    email = input("Enter email: ")
    stake = Decimal(input("Initial stake: "))

    user = User(
        username=username,
        email=email,
        initial_stake=stake,
        current_stake=stake,
        win_threshold=stake * 2,
        loss_threshold=stake / 2,
        min_required_stake=Decimal("10"),
        is_active=True,
    )

    db.add(user)
    db.commit()
    db.refresh(user)
    gambler_id = user.user_id

    prefs = BettingPreferences(
        gambler_id=gambler_id,
        min_bet=Decimal("10"),
        max_bet=Decimal("200"),
        preferred_strategy="FIXED",
        auto_play_enabled=False,
        max_bets_per_session=10,
    )

    db.add(prefs)
    db.commit()
    db.close()

    print(" User registered and activated")
    return gambler_id


def login_user():
    db = SessionLocal()
    username = input("Enter username: ")

    user = db.query(User).filter(User.username == username).first()
    if not user:
        db.close()
        print(" User not found")
        return None

    user.is_active = True
    gambler_id = user.user_id

    db.commit()
    db.close()
    print(" Logged in")
    return gambler_id


def choose_strategy(gambler_id):
    db = SessionLocal()

    prefs = db.query(BettingPreferences).filter(
        BettingPreferences.gambler_id == gambler_id
    ).first()

    if not prefs:
        print(" Betting preferences not found")
        db.close()
        return

    print("\nChoose strategy:")
    print("1. FIXED")
    print("2. PERCENTAGE")
    print("3. MARTINGALE")

    choice = input("Selection: ")

    if choice == "1":
        prefs.preferred_strategy = "FIXED"
    elif choice == "2":
        prefs.preferred_strategy = "PERCENTAGE"
    elif choice == "3":
        prefs.preferred_strategy = "MARTINGALE"
    else:
        print("Invalid choice")

    db.commit()
    db.close()


def play_manual_round(gambler_id):
    eligible, reason = EligibilityService.is_eligible_to_bet(gambler_id)
    if not eligible:
        print(f"Cannot bet: {reason}")
        return False

    bet_amount = BetAmountService.calculate_bet_amount(gambler_id)

    db = SessionLocal()
    user = db.query(User).filter(User.user_id == gambler_id).first()
    db.close()

    bet_id = BetService.place_bet(user.username, bet_amount)

    outcome = OutcomeService.determine_outcome(win_probability=0.5)
    BetSettlementService.resolve_bet(bet_id, outcome.value)

    db = SessionLocal()
    user = db.query(User).filter(User.user_id == gambler_id).first()
    db.close()

    print(f" Bet {bet_amount} → {outcome.value}")
    print(f" Current balance: {user.current_stake}")

    return True


def main():
    Base.metadata.create_all(bind=engine)

    print("\n Welcome to Gambling CLI ")
    print("1. Register")
    print("2. Login")

    option = input("Choose option: ")

    if option == "1":
        gambler_id = register_user()
    elif option == "2":
        gambler_id = login_user()
        if not gambler_id:
            return
    else:
        return

    choose_strategy(gambler_id)

    while True:
        print("\n1. Play bet")
        print("2. Start auto session")
        print("3. Exit")

        action = input("Select: ")

        if action == "1":
            if not play_manual_round(gambler_id):
                break
        elif action == "2":
            enable_autoplay(gambler_id)
            result = BettingSessionService.run_session(gambler_id)
            print("Session result:", result)
        elif action == "3":
            print(" Goodbye")
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
