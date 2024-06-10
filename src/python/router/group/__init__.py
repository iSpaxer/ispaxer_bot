from src.python.filter.ChatTypeFilter import ChatTypeFilter
from src.python.router.group.admin_group_router import admin_group_router
from src.python.router.group.callback_group_router import callback_group_router

group_routers = [
    admin_group_router, callback_group_router
]

for router in group_routers:
    router.message.filter(ChatTypeFilter(["group", "supergroup"]))

