from difflib import SequenceMatcher, get_close_matches

word_a = 'rain'
word_b = 'rainn'
word_c = 'rain n'
possibilities = ['rain', 'paranormal', 'as', 'cloud', 'rainy']

# Caculate similarity score between words
score_1 = SequenceMatcher(None, word_b, word_a).ratio()
score_2 = SequenceMatcher(lambda x: x == ' ', word_c, word_a).ratio()
print(score_1)
print(score_2)

# Calculate similarity score between a word and items in a list
matches_1 = get_close_matches(word_a, possibilities, n=1, cutoff=0.8)
matches_2 = get_close_matches(word_a, possibilities, n=5, cutoff=0.8)
print(matches_1)
print(matches_2)
