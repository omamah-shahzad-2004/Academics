from mrjob.job import MRJob

class papersWithoutVenue(MRJob):
  def mapper(self, _, line):
    if line.startswith('#*'):
      self.title = line[2:].strip()
    if line.startswith('#c'):
      venue = line[2:].strip()
      if not venue:
        yield self.title, None

  def reducer(self, title, _):
      yield title, None

if __name__ == '__main__':
  papersWithoutVenue.run()
