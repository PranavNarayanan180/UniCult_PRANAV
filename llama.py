import ollama
import time

def title_module(set1,set2,set3):
    print("ANALYZING SENTENCES...")
    content="Classify the given sentence semantically into topics sentence1='{set1}' , sentence2='{set2}' , sentence3='{set3}".format(set1=set1,set2=set2,set3=set3)
    stream = ollama.chat(
        model="llama2",
        messages=[{"role": "user",
                   "content":content}],
        stream=True
    )
    time.sleep(3)
    for chunk in stream:
        print(chunk["message"]["content"], end="", flush=True)
