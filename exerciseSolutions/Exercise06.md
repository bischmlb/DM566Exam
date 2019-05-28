# Exercise 6-1
2:2,3  
4:4  
6:10,11,12,20,25,30  

u1 = 2+3/2 = 2,5  
u2 = 4/1 = 4  
u3 = 10+11+12+20+25+30/6 = 18  

2.5: 2,3  
4: 4, 10, 11  
18: 12, 20, 25, 30  

u1 = 2+3/2 = 2,5  
u2 = 4+10+11/3 = 8,33  
u3 = 12+20+25+30/4 = 21,75  

2.5: 2,3,4/3  
8.33: 10,11,12/3  
21.75: 20,25,30/3  

u1 = 3  
u2 = 11  
u3 = 25  


**3: 2,3,4  
11: 10,11,12  
25: 20,25,30  

u1 = 2,3,4/3 = 3  
u2 = 10,11,12/3 = 11  
u3 = 20,25,30/3 = 25  

convergence !****  




*5.0,6.4 = 1.0,5.0 , 7.0,7.0 , 7.0, 8.0 , 6.0,8.0 , 7.0,9.0  
ny centroid = 1+7+7+6+7/5 = 5.4 5+7+8+8+9 = 7.4 = (5.6, 7.4) slide eksempel*   






# Exercise 6-2
## Clustering vs Classification!
clustering = we cannot learn rules to sort points into clusters  
we do not know how many clusters there are  
we do not know how the clusters are characterized  
there is no unique criterion to judge on the quality of a derived clustering solution (evaluation)

classification = we CAN learn rules to sort points into clusters.  
we DO now how many clusters there are(classes)  
we DO know how classes are characterized. ..  

Classification is the process of classifying the data with the help of class labels. On
the other hand, Clustering is similar to classification but there are no predefined
class labels.  
Classification is geared with supervised learning. As against, clustering is also known
as unsupervised learning.  
Training sample is provided in classification method while in case of clustering
training data is not provided.  

(a) Classification  
(b) Classification  
(c) Clustering  
(d) Clustering  
(e) Clustering (Classification?)  
(f) Clustering  
(g) Classification  

# Exercise 6-3
Silhouette Coefficient: -1 equals *bad*, 1 equals *good*  
a(o) = gennemsnitlige afstand fra means-punkt til omkringliggende punkter fra samme cluster.  
b(o) = gennemsnitlige afstand fra means-punkt til omkringliggende punkter fra tætteste nabo cluster.  
## b(o) - a(o)/max(a(o), b(o)) ---- (slides p. 167)
llouyd example(1):   
a(o) = 49.70   
b(o) = 0.70   
silhouette Coefficient u1 = 0.70-49.70/49.70 = **-0.9859154929577464**  

a(o) = 0.70   
b(o) = 49.70   
silhouette coeffiecient u2 = 49.70-0.70/49.70 = **0.9859154929577464**   

macqueen example(2):   
a(o) = 0  
b(o) = 10.41  
silhouette Coefficient u1 = 10.41-0/10.41 = **1**  
a(o) = 10.41  
b(o) = 0  
silhouette Coefficient u2 = 0-10.41/10.41 = **-1**  

example(3):   
a(o) = 1.33  
b(o) = 50.4  
silhouette Coefficient u1 = 50.4-1.33/50.4 = **0.9736111111111111**  

a(o) = 50.4  
b(o) = 1.33  
silhouette Coefficient u2 = 1.33-50.4/50.4 = **-0.9736111111111111**  

We can see that the result of TD2 on slides matches the quality outcome of our silhouette coefficients.
