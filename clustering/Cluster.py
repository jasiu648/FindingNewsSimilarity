from sklearn.cluster import KMeans
from kneed import KneeLocator
from sklearn.cluster import AgglomerativeClustering
from scipy.spatial.distance import squareform

class Cluster():

    def create_clusters(self, similarity_matrix, clusers_num):
        pass

    def create_optimal_clusters(similarity_matrix, max_clusters):
        pass

class KMeansCluster(Cluster):
    
    def create_clusters(self, similarity_matrix, clusers_num):

        kmeans = KMeans(n_clusters = clusers_num, random_state=42, n_init=10)
    
        kmeans.fit(similarity_matrix)

        return kmeans.labels_
    
    def create_optimal_clusters(self, similarity_matrix, max_clusters):

        inertia_values = []

        for i in range(1, max_clusters + 1):
            kmeans = KMeans(n_clusters=i, random_state=42, n_init=10)
            kmeans.fit(similarity_matrix)
            inertia_values.append(kmeans.inertia_)

        # Use the KneeLocator to find the "elbow" point automatically
        knee_locator = KneeLocator(range(1, max_clusters + 1), inertia_values, curve="convex", direction="decreasing")
        optimal_num_clusters = knee_locator.elbow
        print(optimal_num_clusters)
        # Perform k-means clustering with the optimal number of clusters
        kmeans = KMeans(n_clusters=optimal_num_clusters, random_state=42, n_init=10)
        cluster_assignments = kmeans.fit_predict(similarity_matrix)
        return cluster_assignments

class HierarchicalCluster(Cluster):
    
    def create_clusters(self, similarity_matrix, clusers_num):
        distance_matrix = 1 - similarity_matrix
        
        for i in range(len(distance_matrix)):
            distance_matrix[i][i] = 0

        #condensed_distance_matrix = squareform(distance_matrix)

        # Perform hierarchical clustering
        clustering = AgglomerativeClustering(n_clusters = clusers_num, linkage='complete', affinity='precomputed')
        labels = clustering.fit_predict(distance_matrix)

        return labels

    def create_optimal_clusters(similarity_matrix, max_clusters):
        pass