# Exercise 7-1

Initial Centroids:  
Square(black): 2+1/2, 5+3/2  = **1.5, 4.0**  
Triangle(orange): 3+10+7/3, 4+1+7/3  = **6.67, 4.0**  
Circle(purple): 6+7+7/3, 8+8+9/3 = **6.67, 8.33**  

Recomputation1:  
Square: 2+1+3/3, 3+5+4/3 = **2,4**  
Triangle: 10, 1 = **10.1**  
Circle: 7+6+7+7/4, 7+8+8+9/4 = **6.75, 8**  

After this recomputation, we reach convergence.

TD2 Measurement for k = 3 vs k = 2.  
In lecture k = 2 td2 = 61,5.  

for k = 3:  
SSQ(p1, Sc) = |2 - 2|^2 + |4 - 3|^2 = 1  
SSQ(p2, Sc) = |2 - 1|^2 + |4 - 5|^2 = 2  
SSQ(p3, Sc) = |2 - 3|^2 + |4 - 4|^2 = 1

SSQ(p1, Tc) = |10 - 10|^2 + |1 - 1|^2 = 0

SSQ(p1, Cc) = |6.75 - 7|^2 + |8 - 7|^2 = 1.0625  
SSQ(p2, Cc) = |6.75 - 6|^2 + |8 - 8|^2 = 0.5625  
SSQ(p3, Cc) = |6.75 - 7|^2 + |8 - 8|^2 = 0.0625  
SSQ(p4, Cc) = |6.75 - 7|^2 + |8 - 9|^2 = 1.0625  

TD2 = 1+2+1+0+1.0625+0.5625+0.0625+1.0625 = **6.75**. This means TD2 quality is way better, and way more compact, and we can conclude that the result is better for k=3.

# Exercise 7-2  
*note: For hver class (A,B,C), tjek hvor mange TP,TN,FN,FP vi har.*  

**True Positives (TP)** - These are the correctly predicted positive values which means that the value of actual class is yes and the value of predicted class is also yes. E.g. if actual class value indicates that this passenger survived and predicted class tells you the same thing.  

**True Negatives (TN)** - These are the correctly predicted negative values which means that the value of actual class is no and value of predicted class is also no. E.g. if actual class says this passenger did not survive and predicted class tells you the same thing.  

**False positives and false negatives, these values occur when your actual class contradicts with the predicted class.**  

**False Positives (FP)** – When actual class is no and predicted class is yes. E.g. if actual class says this passenger did not survive but predicted class tells you that this passenger will survive.  

**False Negatives (FN)** – When actual class is yes but predicted class in no. E.g. if actual class value indicates that this passenger survived and predicted class tells you that passenger will die.  



**Accuracy** = TP+TN/TP+FP+FN+TN  
**Precision** =  TP/TP+FP  
**Recall** =  TP/TP+FN  
**F1 Score** = 2*(Recall * Precision) / (Recall + Precision)  

--   
*Confusion Matrix*:

|  | A | B | C |
|---|---|---|---|
| A | **4** | 0 | 1 |
| B | 2 | **2** | 1 |
| C | 1 | 1 | **3** |

**recall**: proportion of test objects of
some class ci that have been predicted
correctly  
**precision**: proportion of test objects predicted as class ci that actually belong to class ci  

recall(A) = 4/5 = **0.8** - *4/(4+1)*  
recall(B) = 2/5 = **0.4** - *2/(2+3)*  
recall(C) = 3/5 = **0.6** - *3/(3+2)*  

precision(A) = 4/7 = **0.57** - *4/(4+3)*  
precision(B) = 2/3 = **0.66** - *2/(2+1)*  
precision(C) = 3/5 = **0.66** - *3/(3+2)*  

F1(A) = 2*(0.8 0.57)/(0.8+0.57) =**0.665**  
F1(B) = 2*(0.4 0.66)/(0.4+0.66) =**0.498**  
F1(C) = 2*(0.6 0.66)/(0.6+0.66) = **0.628**

**HUSK MARKDOWN IKKE VISER GANGETEGN**

Macro Average F1:  
aRecall = 0.8+0.4+0.6/3 =  0.6  
aPrecision = 0.57+0.66+0.66/3 = 0.63    
**= 2*(0.6 0.63)/(0.6+0.63) = 0.615**

Micro Average F1:  
A: 4 B: 2 C: 3 = 9 TP     
A: 3 B: 1 C: 2 = 6 FP  
A: 1 B: 3 C: 2 = 6 FN  
15 Total.   
Precision = 9/(9+6) = 0.6   
Recall = 9/(9+6) = 0.6  
**2*(0.6 0.6)/(0.6+0.6) = 0.6**  

The micro- and macro-Average f1-measures are not far from each other. However Micro is probably the most accurate for this particular example.  

# Exercise 7-3
Go back
