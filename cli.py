from decimal import Decimal

from services.user_service import UserService
from services.preference_service import PreferenceService
from services.session_runner import SessionRunner
from services.bet_service import BetService
from services.bet_settlement_service import BetSettlementService
from services.bet_amount_service import BetAmountService
from services.eligibility_service import EligibilityService

from config.database import initialize_database
from domain.outcome_service import OutcomeService
from repositories.user_repositories import UserRepository


def register():
    username = input("Enter username: ")
    fullname = input("Enter full name: ")
    email = input("Enter email: ")
    stake = Decimal(input("Initial stake: "))
    win_threshold = Decimal(input("Win threshold: "))
    loss_threshold = Decimal(input("Loss threshold: "))

    user_id = UserService.register(username, fullname, email, stake, win_threshold, loss_threshold)
    PreferenceService.create_default(user_id)

    print("User registered successfully")
    return user_id


def login():
    username = input("Enter username: ")
    user_id = UserService.login(username)

    if not user_id:
        print("User not found")
        return None

    print("Login successful")
    return user_id


def choose_strategy(user_id):
    print("\nChoose strategy:")
    print("1. FIXED")
    print("2. PERCENTAGE")
    print("3. MARTINGALE")
    print("4. REVERSE_MARTINGALE")
    print("5. FIBONACCI")
    print("6. D'ALEMBERT")

    choice = input("Selection: ")

    mapping = {
        "1": "FIXED",
        "2": "PERCENTAGE",
        "3": "MARTINGALE",
        "4": "REVERSE_MARTINGALE",
        "5": "FIBONACCI",
        "6": "D_ALEMBERT"
    }

    strategy = mapping.get(choice)

    if not strategy:
        print("Invalid choice")
        return

    PreferenceService.change_strategy(user_id, strategy)
    print("Strategy updated")


def prompt_manual_bet(user_id):
    user = UserRepository.get_by_id(user_id)
    prefs = PreferenceService.get_preferences(user_id)

    current_stake = Decimal(str(user["current_stake"]))
    min_bet = Decimal(str(prefs["min_bet"]))
    max_bet = Decimal(str(prefs["max_bet"]))
    strategy = prefs["preferred_strategy"]

    print(f"Current balance: {current_stake}")
    print(f"Minimum bet: {min_bet}")
    print(f"Maximum bet: {max_bet}")

    if strategy == "PERCENTAGE":
        print("Enter bet percentage instead of a fixed amount.")
        prompt = "Bet percentage (1-100): "
    else:
        prompt = "Bet amount: "

    while True:
        raw_value = input(prompt)
        try:
            amount = BetAmountService.validate_manual_bet(user_id, raw_value)
            return amount
        except Exception as exc:
            print(f"Invalid bet: {exc}")
            continue


def play_manual(user_id):
    amount = prompt_manual_bet(user_id)

    eligible, reason = EligibilityService.is_eligible_to_bet(user_id, requested_bet_amount=amount)
    if not eligible:
        print(f"Cannot bet: {reason}")
        return False

    bet_id = BetService.place_bet(user_id, amount)

    outcome = OutcomeService.determine_outcome(0.5)
    BetSettlementService.resolve_bet(bet_id, outcome.value)

    user = UserRepository.get_by_id(user_id)

    print(f"Bet: {amount} → {outcome.value}")
    print(f"Balance: {user['current_stake']}")

    return True


def pretty_print_auto_session(result):
    print("\n=== Auto Session Results ===")
    print(f"Status: {result.get('status', 'UNKNOWN')}")

    if result.get('status') == 'STOPPED':
        print(f"Reason: {result.get('reason', 'No reason provided')}")

    results = result.get('results', [])
    total = len(results)
    wins = sum(1 for r in results if r.get('result') == 'WIN')
    losses = total - wins

    print(f"Rounds executed: {total}")
    print(f"Wins: {wins}")
    print(f"Losses: {losses}")

    if results:
        print("\nRound details:")
        for index, row in enumerate(results, start=1):
            bet = Decimal(str(row.get('bet', 0)))
            result_text = row.get('result', 'UNKNOWN')
            print(f" {index:>2}. Bet: {bet:.2f} → {result_text}")


def start_cli():
    initialize_database()

    print("\n=== Gambling CLI ===")
    print("1. Register")
    print("2. Login")

    option = input("Choose option: ")

    if option == "1":
        user_id = register()
    elif option == "2":
        user_id = login()
        if not user_id:
            return
    else:
        return

    choose_strategy(user_id)

    while True:
        print("\n1. Play manual bet")
        print("2. Run auto session")
        print("3. Exit")

        action = input("Select: ")

        if action == "1":
            if not play_manual(user_id):
                break

        elif action == "2":
            rounds_input = input("Enter number of auto-play rounds: ")
            try:
                rounds = int(rounds_input)
                if rounds <= 0:
                    raise ValueError()
            except ValueError:
                print("Invalid round count. Using 10 rounds.")
                rounds = 10

            result = SessionRunner.run(user_id, rounds=rounds)
            pretty_print_auto_session(result)

        elif action == "3":
            print("Goodbye")
            break

        else:
            print("Invalid option")
