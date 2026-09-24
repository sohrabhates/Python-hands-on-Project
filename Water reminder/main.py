import time
from plyer import notification
while True:
    notification.notify(
        title="Water Reminder",
        message="Please sip some water!"
    )
    time.sleep(60)