from collections import defaultdict
import nltk
import string
nltk.download('punkt')
nltk.download('punkt_tab')

raw_vocab = ["I think" , "Maybe" , "I'm not sure" , "I'm not sure" , "Perhaps" , "I don't know" , "I'm not certain","It could be" , "I'm not an expert, but" , "This might be wrong, but"]

def remove_punctuation(text):
    translator = str.maketrans('', '', string.punctuation)
    text_removed_punctuation = text.translate(translator)
    text_removed_punctuation = text_removed_punctuation.lower()
    return text_removed_punctuation.lstrip()
preprocessed_word = remove_punctuation("I don't know")
preprocessed_word

preprocessed_vocab = [remove_punctuation(word) for word in raw_vocab]
preprocessed_vocab

def get_confidence_rate(vocab_bigrams , no_of_words_in_content , no_of_bigrams_in_content , words_rate = 5):
  confidence_rate = 100
  minimum_words_for_bigrams = no_of_bigrams_in_content * words_rate
  confidence_ = (no_of_bigrams_in_content / vocab_bigrams) * (minimum_words_for_bigrams / no_of_words_in_content) * 100
  confidence_rate = confidence_rate - confidence_
  return confidence_rate

def get_tokens(corpus):
  tokens = nltk.word_tokenize(corpus)
  return tokens

def generate_bigrams(words):
    bigrams = [(words[i], words[i + 1]) for i in range(len(words) - 1)]
    return bigrams

def calculate_bigram_probabilities(corpus):
    bigram_counts = defaultdict(int)
    unigram_counts = defaultdict(int)

    for sentence in corpus:
        tokens = get_tokens(sentence)
        sentence_bigrams = generate_bigrams(tokens)
        for bigram in sentence_bigrams:
            bigram_counts[bigram] += 1
            unigram_counts[bigram[0]] += 1

    bigram_probabilities = {}
    for bigram, count in bigram_counts.items():
        previous_word = bigram[0]
        probability = count / unigram_counts[previous_word]
        bigram_probabilities[bigram] = probability

    return bigram_probabilities

vocab_probabilities = calculate_bigram_probabilities(preprocessed_vocab)
vocab_probabilities

def test_review(test_content):
  preprocessed_content = remove_punctuation(test_content)
  print(preprocessed_content)
  tokens = get_tokens(preprocessed_content)
  test_content_bigrams = generate_bigrams(tokens)
  print(test_content_bigrams)
  score = sum(vocab_probabilities.get(bigram, 0) for bigram in test_content_bigrams)
  print(f"Score: {score}")
  return score

def get_confidence_rate_final(test_content):
  global vocab_probabilities
  no_of_words_in_content = len(get_tokens(test_content))
  no_of_bigrams_in_content = test_review(test_content=test_content)
  vocab_bigrams = len(vocab_probabilities.keys())
  confidence_rate = get_confidence_rate(vocab_bigrams , no_of_words_in_content , no_of_bigrams_in_content)
  return confidence_rate

#get_confidence_rate_final(test_content)
