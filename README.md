# wspinbot
Mon agent conversationnel fait dans le cadre de mon cours d'exploration en intelligence artificelle a GG
1. `git clone https://github.com/CommittedSpin/wspinbot.git`
2. `cd wspinbot`
3. `python -m venv .`
4. `source ./bin/activate`
5. `pip install django chatterbot chatterbot_corpus`
6. `cd ./wspinsite`
7. `python train.py`
8. `python manage.py migrate`
9. `python manage.py runserver`
