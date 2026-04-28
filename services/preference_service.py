from repositories.preference_repository import PreferenceRepository


class PreferenceService:

    @staticmethod
    def create_default(user_id):
        PreferenceRepository.create(
            user_id=user_id,
            min_bet=10,
            max_bet=200,
            strategy="FIXED"
        )

    @staticmethod
    def change_strategy(user_id, strategy):
        PreferenceRepository.update_strategy(user_id, strategy)

    @staticmethod
    def get_preferences(user_id):
        return PreferenceRepository.get_by_user_id(user_id)