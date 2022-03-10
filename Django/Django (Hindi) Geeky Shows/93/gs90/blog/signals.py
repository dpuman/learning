from django.dispatch import Signal, receiver

# creating Signal
notification = Signal()

# reciever


@receiver(notification)
def custom_signal(sender, **kwargs):
    print('-'*50)
    print('custom_signal')
    print('Sender: ', sender)

    print(f'KWARGS: {kwargs}')
