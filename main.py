# from services.eligibility_service import EligibilityService

# def main():
#     eligible, reason = EligibilityService.is_eligible_to_bet(
#         gambler_id=1,
#         requested_bet_amount=100
#     )

#     print("Eligible:", eligible)
#     print("Reason:", reason)

# if __name__ == "__main__":
#     main()
# from config.database import engine
# from models import Base

# if __name__ == "__main__":
#     Base.metadata.create_all(bind=engine)
#     print("✅ Tables created")

from services.bet_amount_service import BetAmountService

def main():
    amount = BetAmountService.calculate_bet_amount(gambler_id=1)
    print("Calculated bet amount:", amount)

if __name__ == "__main__":
    main()
