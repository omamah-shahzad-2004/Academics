from mrjob.job import MRJob

class papersPublishedDecade(MRJob):
  def mapper(self, _, line):
    if line.startswith('#t'):
      year = line[2:].strip()
      year = int(year)
      decade = (year // 10) * 10
      decade = f"{decade}s"
      yield decade, 1

  def reducer(self, decade, count):
    yield decade, sum(count)

if __name__ == '__main__':
  papersPublishedDecade.run()
