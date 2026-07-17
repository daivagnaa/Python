import time
from plyer import notification

# Install plyer package
try:
    import plyer
except ImportError:
    import pip
    pip.main(['install', 'plyer'])

while True:
    notification.notify(
        title="Hydration Reminder",
        message="Sip some water",
        timeout=5  # seconds
    )
    time.sleep(1800)  # Remind every 30 minutes