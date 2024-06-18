from src.python.router.payment.command_payment_router import command_payment_router
from src.python.router.payment.callback_payment_router import callback_payment_router

from src.python.filter.ChatTypeFilter import ChatTypeFilter

payment_routers = [
    command_payment_router, callback_payment_router
]

for router in payment_routers:
    router.message.filter(ChatTypeFilter(["private"]))
