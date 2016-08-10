from random import randint

from .state import State


class MessageText(State):
    def execute(self, parent_session) -> str:
        text = State.contextualize(parent_session.context, self.properties['text'])  # Add context
        parent_session.send(text)  # Send message
        parent_session.logger.debug('Robot says: ' + text)
        return self.transitions.get('next_state', False)


class MessageRandomText(State):
    def execute(self, parent_session) -> str:
        resp = self.properties['responses']
        i = randint(0, len(resp)-1)
        text = State.contextualize(parent_session.context, resp[i])
        parent_session.send(text)
        parent_session.logger.debug('Robot says: ' + text)
        return self.transitions.get('next_state', False)