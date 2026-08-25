
print("========================================")
print("       LANGUAGE TRANSLATION TOOL")
print("========================================")

text = input("Enter text to translate: ")
target = input("Translate to (bn/en): ").lower()
import urllib.parse
import urllib.request
import json

url = "https://api.mymemory.translated.net/get?q=" + urllib.parse.quote(text) + "&langpair=en|" + target

response = urllib.request.urlopen(url)
data = json.loads(response.read())

translation = data["responseData"]["translatedText"]
print("========================================")
print("Translated Text:", translation)
print("========================================")
if target == "bn":
    print("Language: Bangla")

elif target == "en":
    print("Language: English")

else:
    print("Language code not supported.")