from mrjob.job import MRJob
from heapq import nlargest

STOPWORDS = set([
    'the', 'is', 'in', 'it', 'and', 'to', 'a', 'of', 'that', 'with', 'as',
    'for', 'was', 'on', 'but', 'by', 'this', 'at', 'from', 'or', 'an', 'be',
    'if', 'not', 'are', 'we', 'they', 'he', 'she', 'you', 'i', 'has', 'have',
    'had', 'my', 'your', 'his', 'her', 'its', 'their', 'me', 'him', 'them'
])

class top10FrequentWords(MRJob):
  def mapper(self, _, line):
    words = line.strip().split()
    for word in words:
      word = word.lower()
      if word not in STOPWORDS:
        yield word, 1

  def combiner(self, word, count):
    yield word, sum(count)

  def reducer(self, word, count):
    frequent_words = nlargest(10, [(word, sum(count))], key=lambda x: x[1])
    for word, count in frequent_words:
      yield word, count

if __name__ == '__main__':
  top10FrequentWords.run()
