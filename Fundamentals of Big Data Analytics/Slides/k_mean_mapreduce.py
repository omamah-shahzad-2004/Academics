from mrjob.job import MRJob
import numpy as np
import math
import json

class KMeansMRJob(MRJob):

    centroid = []

    def configure_args(self):
        super(KMeansMRJob, self).configure_args()
        self.add_file_arg('--clusters', help='File containing cluster centroids')

    def mapper_init(self):
        # Load cluster centroids from the file
        self.centroid=[]
        with open(self.options.clusters, 'r') as f:
            for line in f:
                data1 = []
                for s in line.strip().split(","):
                    data1.append(float(s))
                self.centroid.append(data1)

    def mapper(self, _, line):
        data1 = []
        data = []
        for s in line.strip().split(","):
            data1.append(float(s))
        data.append(data1)

        Output = [elem for twod in data for elem in twod]

        # data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        # Output = [elem for twod in data for elem in twod]
        #[1, 2, 3, 4, 5, 6, 7, 8, 9]

        #####  calculate distance
        nearest_cluster = []
        for i in data:
            dis = []
            for j in self.centroid:
                dist = math.dist(i, j)
                dis.append(dist)

            nearest_cluster.append(dis.index(min(dis)) + 1)

        # yield nearest_cluster , Output        // also write data instead of Output see what happen
        yield nearest_cluster, Output

    def reducer(self, nearest_cluster, data):

        cluster_points = list(data)
        new_centroid = np.mean(cluster_points, axis=0)


        yield list(new_centroid),cluster_points

        #yield list(nearest_cluster), list(data)    it return   [2]     [[10.0, 8.0], [12.0, 4.0]]
                                                               #[1]     [[2.0, 5.0], [4.0, 7.0]]


if __name__ == '__main__':
    KMeansMRJob.run()




