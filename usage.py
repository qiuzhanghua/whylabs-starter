import whylogs as why
from langkit import llm_metrics

results = why.log({"prompt": "Hello!", "response": "World!"}, schema=llm_metrics.init())

print(results)

# 还不能正常运行，原因待查
