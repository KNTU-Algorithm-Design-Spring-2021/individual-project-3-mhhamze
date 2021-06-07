import requests

def dictionaryContains(word,res):
	if res.get(word):
		return 1
	else:
		return 0

def wordBreak(string,res):
	wordBreakUtil(string, len(string), "",res)

def wordBreakUtil(string, n, result,res):
	for i in range(1, n + 1):
		prefix = string[:i]
		if dictionaryContains(prefix,res):
			if i == n:
				result += prefix
				print(result)
				return
			wordBreakUtil(string[i:], n - i, result+prefix+" ",res)

if __name__ == "__main__":
	sentence = input()
	sentence = sentence.lower()
	print("Dictionary is downloading....")
	req = requests.get("https://raw.githubusercontent.com/dwyl/english-words/master/words_dictionary.json")
	res = dict(req.json())
	wordBreak(sentence,res)
