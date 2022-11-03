# creating virtual environment + installing requirements:
user@host ~/src $ cd daily-tasks
user@host ~/src/daily-tasks $ python -m venv . && source ./Scripts/activate && python -m pip install -r requirements.txt

# executing tasks:
user@host ~/src/daily-tasks $ ./tasks.py

# activating environment:
user@host ~/src/daily-tasks $ source ./Scripts/activate

# deactivating environment:
user@host ~/src/daily-tasks $ deactivate

# storing environment requirements:
user@host ~/src/daily-tasks $ python -m pip freeze > requirements.txt
