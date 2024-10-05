from mrjob.job import MRJob

class wordLengthDistribution(MRJob):
  def mapper(self, _, line):
    words = line.strip().split()
    for word in words:
      yield len(word), 1

  def reducer(self, wordLength, count):
    yield wordLength, sum(count)

if __name__ == '__main__':
  wordLengthDistribution.run()
