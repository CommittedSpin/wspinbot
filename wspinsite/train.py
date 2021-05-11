from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
chatbot = ChatBot('Chatterbot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///chatterbot.corpus.sqlite',
    #trainer='chatterbot.trainers.CorpusTrainer', 
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace',
        'chatterbot.preprocessors.convert_to_ascii',
        ]
    )

trainer = ChatterBotCorpusTrainer(chatbot)
# Training on the english and french corpuses
trainer.train(
    'chatterbot.corpus.english',
    'chatterbot.corpus.french'
)
