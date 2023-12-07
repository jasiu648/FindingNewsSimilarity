from sklearn.cluster import KMeans

class Cluster():

    def create_clusters(self, similarity_matrix, clusers_num):
        pass

class KMeansCluster(Cluster):
    
    def create_clusters(self, similarity_matrix, clusers_num):

        kmeans = KMeans(n_clusters = clusers_num, random_state=42)
    
        kmeans.fit(similarity_matrix)

        return kmeans.labels_