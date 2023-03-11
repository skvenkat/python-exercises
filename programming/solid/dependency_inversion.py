# python-exercises/programming/solid/liskov_substitute.py

from abc import ABC
from typing import final

class AbstractChannel(ABC):

    def get_channel_message(self) -> str:
        pass


class AbstractCommunicator(ABC):

    def get_channel(self) -> AbstractChannel:
        pass

    @final
    def communicate(self, conversation: AbstractConversation, conv_type: str) -> None:
        print(*conversation.do_conversation(conv_type),
            self.get_channel().get_channel_message(),
            sep = '\n'
        )


class SimpleCommunicator(AbstractCommunicator):

    def __init__(self, channel: AbstractChannel) -> None:
        self.channel = channel

    def get_channel(self) -> str:
        return self._channel


class SMSChannel(AbstractChannel):

    def get_channel_message(self) -> str:
        return "(via SMS)"


class SMSCommunicator(AbstractCommunicator):

    def __init__(self):
        self.channel = SMSChannel()

    def get_channel(self) -> AbstractChannel:
        return self.channel

