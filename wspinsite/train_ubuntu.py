
"""
This example shows how to train a chat bot using the
Ubuntu Corpus of conversation dialog.
"""
import logging
from chatterbot import ChatBot
from chatterbot.trainers import UbuntuCorpusTrainer

# Enable info level logging
logging.basicConfig(level=logging.INFO)

chatbot = ChatBot('Ubuntu Bot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3',
    trainer='chatterbot.trainers.CorpusTrainer', 
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace',
        'chatterbot.preprocessors.convert_to_ascii',
        ]
    )

trainer = UbuntuCorpusTrainer(chatbot)
print("Training... This make take a long time.")
# Start by training our bot with the Ubuntu corpus data
trainer.train()

# Now let's get a response to a greeting
#response = chatbot.get_response('How are you doing today?')
#print(response)