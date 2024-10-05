from mrjob.job import MRJob

class invertedIndex(MRJob):
  def mapper(self, _, line):
    if not hasattr(self, 'title'):
      self.title = None

    if line.startswith('#*'):
      self.title = line[2:].strip()
    if line.startswith('#t'):
      year = line[2:].strip()
      yield year, self.title
      self.title = None

  def reducer(self, year, title):
    yield year, list(title)

if __name__ == '__main__':
  invertedIndex.run()
