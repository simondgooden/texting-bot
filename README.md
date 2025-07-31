Setup:
Upload the following to data/ ```~/Library/Messages/chat.db```

Create a `.env.local` file in the root of the project. Add the following variables:

```
OPENAI_API_KEY=your_openai_key

ANTHROPIC_API_KEY=your_anthropic_key #optional for
```


Running:
Set Up:
1 Start local DB for personal privacy: To run use ```brew services start mongodb/brew/mongodb-community```
- To stop use ```brew services stop mongodb/brew/mongodb-community```

2 create local env and install dependencies: ```python -m venv venv``` 
-```source venv/bin/activate```
- ```pip install -r requirements.txt``

3 install the external imessage-importer: ```cargo install imessage-exporter```
- This is needed to translate your text messages from binary to readable text

4 Import messages: ```python text-data-ingestion/get_data.py --default```
- Run the following for list of all library commands ```python text-data-ingestion/get_data.py```
