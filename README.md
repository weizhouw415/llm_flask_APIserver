# llm_flask_APIserver

This is a python flask api server for using llm supporting 
1. openai
2. qianfan 

## run
```
python3 app.py
```

## usage
#### curl
```
curl -X POST http://localhost:5000/llm/reply -H "Content-Type: application/json" -d '{"model": "qianfan", "message": "enter your question here", "temperature": 0.9}'
```
#### html
```
visit http://localhost:5000/llm/index
```
## API doc
### 1. /llm/test
- **usage:** test if the server is on 
- **request method:** GET
- **input format:** JSON

### 2. /llm/reply
- **usage:** LLM reply messages
- **request method:** POST
- **input format:** JSON

| params | type | usage | required |
| :-: | :-: | :-: | :-: |
| message | str | input message for LLMs | yes|
| model | str | LLM model to be used (default openai)| no |
| temperature | float | LLM temperature (default 0.9) | no |
| round | int | multi round chat cache size | no |

### 3. /llm/tool
- **usage:** GPT function calling tools
- **request method:** POST
- **input format:** JSON

| params | type | usage | required |
| :-: | :-: | :-: | :-: |
| message | str | input message for LLMs | yes|
| temperature | float | LLM temperature (default 0.9) | no |


## notice
1. add your api keys in .env.example and rename it to .env
2. still in developement. (multi-round conversation not working well now)