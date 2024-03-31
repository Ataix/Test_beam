from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


User = get_user_model()


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def send_notification(self, event):
        await self.send(text_data=event['message'])


@receiver(post_save, sender=User)
def send_notification_on_create_or_update(sender, instance, created, **kwargs):
    if created:
        message = f'New {sender.__name__} created: {instance}'
    else:
        message = f'{sender.__name__} updated: {instance}'
    async_to_sync(NotificationConsumer.send_notification)({
        'type': 'send_notification',
        'message': message
    })


@receiver(post_delete, sender=User)
def send_notification_on_delete(sender, instance, **kwargs):
    message = f'{sender.__name__} deleted: {instance}'
    async_to_sync(NotificationConsumer.send_notification)({
        'type': 'send_notification',
        'message': message
    })
