import requests, os, openai
from bs4 import BeautifulSoup

url = input("Paste wiki URL > ")

#url = "https://en.wikipedia.org/wiki/Hair_loss"
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")

#div
#mw-parser-output
#p

text = ""

article = soup.find_all("div", {"class": "mw-parser-output"})

for articles in article:
  content = articles.find_all("p")


  for p in content:
    text += p.text

#print(text)
#todo - send this text to openAI for summary in 3 paragraphs

openai.organisation = os.environ['organisationID']
openai.api_key = os.environ['openai']
openai.Model.list()

prompt = f"Summarise the text below in no more than 3 paragraphs. {text}"

response = openai.Completion.create(model="text-davinci-002", prompt=prompt, temperature=0, max_tokens=150)


refs = soup.find_all("ol", {"class": "references"})
for ref in refs:
  print(ref.text.replace("^ ",""))

print(response["choices"][0]["text"].strip())