from django.dispatch import Signal, receiver

# Creating signal
notification = Signal(["request", "user"])

# receiver function
@receiver(notification)
def showNotification(sender, **kwargs):
    print("------------------")
    print("sender:", sender)
    print(f'{kwargs}')
    print("Notification")