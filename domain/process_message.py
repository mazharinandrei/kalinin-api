from abc import abstractmethod, ABC


class ReplyService(ABC):
    @abstractmethod
    async def get_reply(self, input_message: str):
        raise NotImplementedError()


class RuleBasedReplyService(ReplyService):
    async def get_reply(self, input_message: str):
        return "хз пока чё сказать на " + input_message
