from config.database import SessionLocal
from models.alert import Alert
from domain.alerts.alert_type import AlertType

class AlertService:
    """
    UC6: Creates and stores alert notifications.
    """

    @staticmethod
    def send_alert(gambler_id: int, alert_type: AlertType, message: str):
        db = SessionLocal()

        alert = Alert(
            gambler_id=gambler_id,
            alert_type=alert_type.value,
            message=message,
        )

        db.add(alert)
        db.commit()
        db.close()