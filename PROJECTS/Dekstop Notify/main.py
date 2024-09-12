import time

from plyer import notification

if __name__ == "__main__":
    notification.notify(
        title="Drink Water",
        message="LAALALALLALA",
        app_icon="water.ico",
        timeout=0
    )
    time.sleep(1)