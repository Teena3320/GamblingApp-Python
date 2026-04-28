from services.gambler_report_service import GamblerReportService

report = GamblerReportService.generate_report(gambler_id=1)
print("UC5 Report:")
print(report.summary())