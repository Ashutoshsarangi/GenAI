from gensim.models import Word2Vec

sentences = [
    ["this", "is", "a", "sample", "sentence"],
    ["word2vec", "is", "used", "for", "embeddings"],
    ["another", "example", "sentence"]
]

# Train a Word2Vec model
model = Word2Vec(sentences, vector_size=100000, window=5, min_count=1, workers=4)

# Get the embedding for a word
vector = model.wv['sample']
# print(vector)

# Find similar words
similar = model.wv.most_similar('sample')
print(similar)

# this is not giving proper result, 