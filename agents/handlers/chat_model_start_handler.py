from langchain.callbacks.base import BaseCallbackHandler
from pyboxen import boxen

def boxen_print(*args, **kwargs):
    print(boxen(*args, **kwargs))

class HandleChatModelStart(BaseCallbackHandler):
    def on_chat_model_start(self, serialized, messages, **kwargs):
        for message in messages[0]:
            if message.type == "system": 
                boxen_print(message.content, title=message.type, color='Green')
            elif message.type == "ai" and "function_call" in message.additional_kwargs: 
                call = message.additional_kwargs['function_call']
                boxen_print(
                    f"Running tool {call["name"]} with args {call["arguments"]}", 
                    title="Function Call", 
                    color='cyan'
                    )
            elif message.type == "ai": 
                boxen_print(message.content, title=message.type, color='red')
            elif message.type == "human": 
                boxen_print(message.content, title=message.type, color='blue')
            else:
                boxen_print(message.content, title=message.type)
