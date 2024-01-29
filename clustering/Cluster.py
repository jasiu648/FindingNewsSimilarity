from sklearn.cluster import KMeans
from kneed import KneeLocator
from sklearn.cluster import AgglomerativeClustering
from scipy.spatial.distance import squareform
from sklearn.metrics import pairwise_distances_argmin_min
import numpy as np

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

    def create_optimal_clusters(self, similarity_matrix, max_clusters, num_simulations=20):
        distance_matrix = 1 - similarity_matrix
        for i in range(len(distance_matrix)):
            distance_matrix[i][i] = 0

        # Calculate the within-cluster sum of squares for the actual data
        wcss_actual = self.calculate_wcss(distance_matrix)

        # Calculate the Gap Statistic for different numbers of clusters
        gap_values = []
        for k in range(1, max_clusters + 1):
            wcss_random_mean, wcss_random_std = self.simulate_random_clusters(distance_matrix, num_simulations, k)
            gap_value = np.log(wcss_random_mean) - np.log(wcss_actual)
            gap_values.append(gap_value)

        # Find the optimal number of clusters based on the Gap Statistic
        optimal_clusters = np.argmax(gap_values) + 1  # Add 1 because of zero-based indexing

        # Perform hierarchical clustering with the optimal number of clusters
        clustering = AgglomerativeClustering(n_clusters=optimal_clusters, linkage='complete', affinity='precomputed')
        labels = clustering.fit_predict(distance_matrix)

        return labels

    def calculate_wcss(self, distance_matrix):
        # Helper function to calculate the within-cluster sum of squares (WCSS)
        clustering = AgglomerativeClustering(n_clusters=1, linkage='complete', affinity='precomputed')
        labels = clustering.fit_predict(distance_matrix)
        cluster_centers = [np.mean(distance_matrix[labels == j], axis=0) for j in range(1)]
        wcss = sum(pairwise_distances_argmin_min(cluster_centers, distance_matrix)[1])
        return wcss

    def simulate_random_clusters(self, distance_matrix, num_simulations, k):
        # Helper function to simulate random clusters and calculate mean and std of WCSS
        wcss_values = []
        for _ in range(num_simulations):
            random_labels = np.random.randint(0, k, len(distance_matrix))
            random_cluster_centers = [np.mean(distance_matrix[random_labels == j], axis=0) for j in range(k)]
            wcss_values.append(sum(pairwise_distances_argmin_min(random_cluster_centers, distance_matrix)[1]))

        wcss_mean = np.mean(wcss_values)
        wcss_std = np.std(wcss_values)

        return wcss_mean, wcss_std