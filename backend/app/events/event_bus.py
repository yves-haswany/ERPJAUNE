class EventBus:
    def __init__(self):
        self._handlers = {}

    def register(self, event_name: str, handler):
        self._handlers.setdefault(event_name, []).append(handler)

    async def emit(self, event_name: str, payload: dict):
        handlers = self._handlers.get(event_name, [])
        for handler in handlers:
            await handler(payload)


event_bus = EventBus()
