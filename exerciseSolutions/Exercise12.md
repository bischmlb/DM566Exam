# Exercise 12-1

*because points belongings to a cluster have a low reachability distance to their nearest neighbor, valleys correspond to clusters. The deeper the valley, the denser the cluster.*  

I OPTICS vil histogrammerne være præget af den maximale afstand for, at det givne punkt kan nå minpts. Det vil sige hvis minpts = 4, og A kun kan se 4 punkter inden for afstand 2. Vil alle punkter som A kan se være sat til = 4, medmindre bedre findes før punktet vil blive evalueret. (se slides)

(a) We dont get three valleys, because they are part of the same cluster in a sense.  

(b) Valleys from left the right: D, E, C(D and E), A, B  

# Exercise 12-2  
*dont do exercise like this if u have many points*  
**LOF using k=2**  
  dist2(E) = dist(E,F) = |3-3| + |5-9| = 4  
  dist2(K) = dist(K,H) = 3  
  dist2(O) = dist(O,M) = 1  

  N2(E) = {D,F}  
  N2(K) = {J,H}  
  N2(O) = {N,M,P,R}

lrd2(E) = 2/reachdist2(D <- E) + reachdist2(F <- E)  
reachdist2(D <- E) = max{dist2(D), dist(D,E)} = max{1,4} = 4  
reachdist2(F <- E) = max{dist2(F), dist(F,E)} = max{2,4} = 4  
**lrd2(E) = 2/(4+4) = 0.25**  

lrd2(K) = 2/reachdist2(J <- K) + reachdist2(H <- K)  
reachdist2(J <- K) = 2  
reachdist2(H <- K) = 3  
**lrd2(K) = 2/(2+3) = 0.4**  

lrd2(O) = 4/reachdist2(N <- O) + reachdist2(M <- O) + reachdist2(P <- O) + reachdist2(R <- O)  
reachdist2(N <- O) = 1  
reachdist2(M <- O) = 2  
reachdist2(P <- O) = 1  
reachdist2(R <- O) = 1  
**lrd2(O) = 4/(1+2+1+1) = 0.8**  

LOF2(E) = (lrd2(D)+lrd2(F) * (reachdist(D <- E) + reachdist2(F <- E)))  
lrd2(D):  
N2(D) = {C,B}  
2/reachdist2(C <- D) + reachdist2(B <- D) = 2/2 = 1.0  
lrd2(F):  
N2(F) = {G,H}  
2/reachdist(G <- F) + reachdist2(H <- D) = 2/(1+2) = 0.66  
**= (1.0+0.66) * (4 + 4) = 13.280000000000001/4**

LOF2(K):  

N2(J) = {H, I, G, K}  
N2(H) = {G, I, J}  

lrd2(J) =  4/reachdist2(H <- J) + reachdist2(I <- J) + reachdist2(G <- J) + reachdist2(K <- J).  
**GOT THE POINT, MAKE THIS IN ELKI?? or R??** -- ELKI og export


# Exercise 12-3

top k = 2  
S1:  
A5 og A4.  
TP: 1  
TN: 7  
FN: 1  
FP: 1  
S2:
A8 og A9.  
TP: 1  
TN: 7
FN: 1
FP: 1  
(samme)  
Precision = TP/TP+FP = 1/2 = 0.5
Recall = 1/2 = 0.5
