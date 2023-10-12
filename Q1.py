pip install nltk

import nltk
from nltk.corpus import wordnet

# Download WordNet data if not already downloaded
nltk.download("wordnet")

def get_word_meaning(word):
    # Get the synsets for the given word
    synsets = wordnet.synsets(word)
    meanings = []
    if synsets:
        for synset in synsets:
            # Get the definition of the word
            definition = synset.definition()
            meanings.append(definition)
        return meanings
    else:
        return None

def suggest_word(word):
    # Get similar words (suggestions) for the given word
    suggestions = []
    for synset in wordnet.synsets(word):
        for lemma in synset.lemmas():
            suggestions.append(lemma.name())
    return suggestions

def main():
    while True:
        word = input("Enter a word to look up (or 'q' to quit): ").lower()
        if word == "q":
            break
        
        meanings = get_word_meaning(word)
        if meanings:
            print("Meanings:")
            for meaning in meanings:
                print("- " + meaning)
        else:
            print("Word not found. Suggestions:")
            suggestions = suggest_word(word)
            if suggestions:
                print(", ".join(suggestions))
            else:
                print("No suggestions found.")

if __name__ == "__main__":
    main()
    
