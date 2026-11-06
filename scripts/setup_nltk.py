import nltk

PACKAGES = [
    "punkt",                            # tokenizer models
    "punkt_tab",                        # needed by newer NLTK for word_tokenize
    "stopwords",                        # stopword list
    "wordnet",                          # lemmatizer dictionary
    "omw-1.4",                          # extra wordnet data
    "averaged_perceptron_tagger_eng",   # NLTK POS tagger
    "vader_lexicon",                    # VADER sentiment
]

for pkg in PACKAGES:
    nltk.download(pkg, quiet=True)
    print(f"downloaded: {pkg}")