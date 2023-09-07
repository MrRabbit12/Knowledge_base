import requests

url  = 'http://localhost:7861/chat/knowledge_base_chat'
url2 = 'http://localhost:7861/'
json = {
  "query": "有姓双的老师吗",
  "knowledge_base_name": "samples",
  "top_k": 5,
  "score_threshold": 1,
  "history": [
    {
      "role": "user",
      "content": "我们来玩成语接龙，我先来，生龙活虎"
    },
    {
      "role": "assistant",
      "content": "虎头虎脑"
    }
  ],
  "stream": "false",
  "local_doc_url": "false"
}

resp = requests.post(url = url,json=json)
# resp = requests.get(url2)
print(resp.text)
