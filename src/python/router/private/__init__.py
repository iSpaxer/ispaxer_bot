from .callback_router import callback_router
from .command_router import router as command_router
from .fsm_router import fsm_router
from .user_data_router import user_data_router
from ...filter.ChatTypeFilter import ChatTypeFilter

private_routers = [
    callback_router, command_router, fsm_router, user_data_router
]
for router in private_routers:
    router.message.filter(ChatTypeFilter(["private"]))  # todo
