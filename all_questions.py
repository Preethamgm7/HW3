# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Hierarchical clustering methods like agglomerative clustering have an advantage over k-means when it comes to dealing with outliers. This is because they gradually combine clusters, giving outliers a chance to be grouped at higher levels of the hierarchy instead of forcing them into individual clusters like k-means does."

    # type: bool (True/False)
    answers["(b)"] = False

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Various iterations of agglomerative hierarchical clustering may yield distinct cluster arrangements because of differences in the distance measurement or the method used to connect clusters, among other influences."

    # type: bool (True/False)
    answers["(c)"] = False

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "K-means isn't always the best choice for clustering data. Even though it might be faster and use less memory compared to certain versions of agglomerative hierarchical clustering, its performance can vary depending on factors like how big and complex the data is, what distance measure is used, and how many clusters you're aiming for."

    # type: bool (True/False)
    answers["(d)"] = False

    # type: explanatory string (at least four words)
    answers["(d) explain"] = "When you divide a cluster in the final phase of K-means, it might not always lower the sum of squared errors (SSE) for the clustering. This outcome hinges on things like how the data points are spread within the cluster and which point gets chosen as the new center."

    # type: bool (True/False)
    answers["(e)"] = True

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "In K-means clustering, we aim to minimize the sum of squared errors (SSE) by adjusting the centroids to bring data points closer to their assigned centers. So, whenever the SSE goes down, it means the cohesion, or similarity within each cluster, is getting stronger."

    # type: bool (True/False)
    answers["(f)"] = False

    # type: explanatory string (at least four words)
    answers["(f) explain"] = "The between sum of squares (SSB) in K-means clustering gauges how much space there is between clusters. So, when the SSB goes up, it means there's more distance between the clusters."

    # type: bool (True/False)
    answers["(g)"] = False

    # type: explanatory string (at least four words)
    answers["(g) explain"] = "In K-means clustering, cohesion and separation aren't completely separate. When we work on improving cohesion by reducing the sum of squared errors (SSE), it often results in better separation between clusters, as reducing the variance within each cluster usually makes the clusters more distinct from each other."

    # type: bool (True/False)
    answers["(h)"] = False

    # type: explanatory string (at least four words)
    answers["(h) explain"] = "The sum of squared errors (SSE) plus the between sum of squares (BSS) isn't always fixed in K-means clustering. It can change as we update the centroids throughout the iterative process of optimizing K-means."

    # type: bool (True/False)
    answers["(i)"] = False

    # type: explanatory string (at least four words)
    answers["(i) explain"] = "Even though making clusters more cohesive by reducing the sum of squared errors (SSE) can help make them clearer, it doesn't always mean the clusters will be more separate. Whether the separation (increasing the between sum of squares, SSB) goes up or down depends on how the centroids move in relation to each other and the data points throughout the clustering process."

    return answers




# -----------------------------------------------------------
def question2():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "The centroid shifts closer to where there's a bunch of points clustered together because the k-means algorithm works to shrink the distance between the centroid and each point in that cluster."

    # type: bool (True/False)
    answers["(b)"] = False

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "The goal of the k-means algorithm is to shrink the differences within each cluster, so the centroids will probably end up at the centers of the two dense areas. However, depending on where the points and centroids are exactly, some points from one cluster might end up closer to the centroid of the other cluster after the centroids move."

    # type: bool (True/False)
    answers["(c)"] = True

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "It looks like all the points are nearer to the centroid on the right side, which suggests that the centroid on the left won't have any points closer to it than the other centroid. So, after the algorithm finishes, there would be one cluster with no points associated with the left centroid."

    return answers




# -----------------------------------------------------------
def question3():
    answers = {}

    # type: a string that evaluates to a float
    answers["(a) SSE"] = "4*R^2"

    # type: a string that evaluates to a float
    answers["(b) SSE"] = "4*(a^2+b^2+r^2)"

    # type: a string that evaluates to a float
    answers["(c) SSE"] = "10*R^2"

    return answers




# -----------------------------------------------------------
def question4():
    answers = {}

    # type: int
    answers["(a) Circle (a)"] = 1

    # type: int
    answers["(a) Circle (b)"] = 1

    # type: int
    answers["(a) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "It's probable that each circle (A, B, and C) will have one centroid at the end, since each circle starts with its own centroid and they're all the same distance from each other. So, we'd end up with a total of three centroids."

    # type: int
    answers["(b) Circle (a)"] = 1

    # type: int
    answers["(b) Circle (b)"] = 1

    # type: int
    answers["(b) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Because the distances between circles A and B and between circles B and C are about the same, each centroid should end up in the middle of its own circle."
    # type: int
    answers["(c) Circle (a)"] = 1 

    # type: int
    answers["(c) Circle (b)"] = 0

    # type: int
    answers["(c) Circle (c)"] = 2

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "For the best clustering outcome, this setup ensures that each centroid ends up closest to the cluster it initially belonged to."
    return answers




# -----------------------------------------------------------
def question5():
    answers = {}

    # type: set
    answers["(a)"] = {"Group A","Group B"}

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "The shortest path that separates the top left point in Group A from the top right point in Group B is the distance between them."

    # type: set
    answers["(b)"] = {'Group A','Group C'}

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "The longest distance between the bottom left point in Group C and the bottom right point in Group A is the one that separates them."

    return answers




# -----------------------------------------------------------
def question6():
    answers = {}

    # type: set
    answers["(a) core"] = {'E','B','F','G','C','L','M','I'}

    # type: set
    answers["(a) boundary"] = {'D','G'}

    # type: set
    answers["(a) noise"] = {'A','H'}

    # type: set
    answers["(b) cluster 1"] = {'B','C','E','F','G','E','D'}

    # type: set
    answers["(b) cluster 2"] = {'I','J','L','M'}

    # type: set
    answers["(b) cluster 3"] = set()

    # type: set
    answers["(b) cluster 4"] = set()

    # type: set
    answers["(c)-a core"] = {'B','C','D','E','F','G','I','J','L','M'}

    # type: set
    answers["(c)-a boundary"] = {'A','H'}

    # type: set
    answers["(c)-a noise"] = set()

    # type: set
    answers["(c)-b cluster 1"] = {'A','B','C','D','E','F','G','H','I','J','L','M'}

    # type: set
    answers["(c)-b cluster 2"] = {'A'}

    # type: set
    answers["(c)-b cluster 3"] = set()

    # type: set
    answers["(c)-b cluster 4"] = set()

    return answers




# -----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    answers["(a)"] = "Cluster 4"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Cluster 4 has the highest clustering entropy because it has a fairly even spread of various land cover types, showing that it's mixed up and not very pure."

    # type: string
    answers["(b)"] = "Cluster 1"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Cluster 1 has the lowest clustering entropy because it's mostly just 'Water' land cover type, showing that it's very uniform and doesn't have much variety with other types."

    return answers




# -----------------------------------------------------------
def question8():
    answers = {}

    # type: string
    answers["(a) Matrix 1"] = "Dataset-z"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 1"] = "The blue color shows short distances, indicating that the clusters are nicely spread apart."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 1"] = "The various colors show different patterns, indicating another arrangement of clusters."

    # type: string
    answers["(a) Matrix 2"] = "Dataset-x"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 2"] = "The blue color shows short distances, suggesting that the clusters are nicely spread apart."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 2"] = "All the other colors indicate long distances, suggesting that there are clear boundaries between the clusters."

    # type: string
    answers["(a) Matrix 3"] = "Dataset-y"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 3"] = "The diagonal entry shows the distance of a point from itself."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 3"] = "The areas that are green and yellow show where the clusters overlap or aren't as clearly separated."

    # type: string
    answers["(b) Row 1"] = "Cluster-a"

    # type: string
    answers["(b) Row 2"] = "Cluster-b"

    # type: string
    answers["(b) Row 3"] = "Cluster-c"

    # type: string
    answers["(b) Row 4"] = "Cluster-d"

    # type: explanatory string (at least four words)
    answers["(b) Row 1 explain"] = "The diagonal entry isn't as clear, suggesting that the cluster isn't as tightly grouped. All the off-diagonal entries have different colors, showing that each cluster is at a different distance from it (closest to B, then C, and farthest from A)."

    # type: explanatory string (at least four words)
    answers["(b) Row 2 explain"] = "The diagonal entry is clearer, showing that the cluster is tightly knit. Two out of three off-diagonal entries are the same color, suggesting that two other clusters are closer to it (A and C, even though the distances to A are less clear), and it's farthest from one other cluster (D)."

    # type: explanatory string (at least four words)
    answers["(b) Row 3 explain"] = "The explanation is similar to what we observed in row 2."

    # type: explanatory string (at least four words)
    answers["(b) Row 4 explain"] = "The explanation is like what we saw in row 1, but in reverse order."

    return answers




# -----------------------------------------------------------
def question9():
    answers = {}

    # type: list
    answers["(a)"] = ['hierarchical', 'overlapping', 'partial']

    # type: list
    answers["(b)"] = ['partitional', 'exclusive', 'complete']

    # type: list
    answers["(c)"] = ['partitional', 'fuzzy', 'complete']

    # type: list
    answers["(d)"] = ['hierarchical','overlapping', 'partial']

    # type: list
    answers["(e)"] = ['partitional', 'exclusive', 'complete']

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "Partitioning clustering would be used for assigning letter grades in a class, where each student falls into exactly one grade category, and there is no overlap between the categories"

    return answers




# -----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    answers["(a) Figure (a)"] = "Yes"

    # type: string
    answers["(a) Figure (b)"] = "Yes"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "DBSCAN is effective at finding clusters that have irregular shapes and can pinpoint the areas where there are lots of points packed together, while disregarding the sparser regions and treating them as background noise."
    # type: string
    answers["(b) Figure (a)"] = "No"

    # type: string
    answers["(b) Figure (b)"] = "Yes"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "It's a method that groups similar data points to spot trends in a dataset. When it comes to facial features, k-means can be used to uncover patterns based on things like size, position, and shape."

    # type: string
    answers["(c)"] = "DBSCAN"

    return answers

# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()
    print('end code')

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
