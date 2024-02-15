from langchain.callbacks.base import BaseCallbackHandler


class HandleChatModelStart(BaseCallbackHandler):
    def on_chat_model_start(self, serialized, messages, **kwargs):
        print(messages)