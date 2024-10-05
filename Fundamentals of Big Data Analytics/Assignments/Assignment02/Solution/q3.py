from mrjob.job import MRJob

class coAuthors(MRJob):
  def mapper(self, _, line):
    if line.startswith('#@'):
      authors = line[2:].strip().split(',')
      for author in authors:
        for coauthor in authors:
          if author != coauthor:
            yield author, coauthor

  def reducer(self, author, coauthors):
    coauthors = list(set(coauthors))
    yield author, coauthors

if __name__ == '__main__':
  coAuthors.run()
