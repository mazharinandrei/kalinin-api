from abc import ABC, abstractmethod


class ReplyService(ABC):
    @abstractmethod
    async def get_reply(self, input_message: str):
        raise NotImplementedError
