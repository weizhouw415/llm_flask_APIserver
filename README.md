# llm_flask_APIserver

This is a python flask api server for using llm supporting 
1. openai
2. qianfan 

## usage
#### curl
curl -X POST http://localhost:5000/llm/reply -H "Content-Type: application/json" -d '{"model": "qianfan", "message": "enter your question here", "temperature": 0.9}'
#### html
visit http://localhost:5000/llm/index


## remember
1. add your api keys in .env.example and rename it to .env
2. still in developement. only 1 api avaliable now. some of the files are not in use right now. might be used soon