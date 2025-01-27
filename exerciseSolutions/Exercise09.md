#Exercise 9-1

**E1 ∩ E2**: both dice are 1  Read: E1 AND E2
**E1 ∪ E2**: at least one of the dice lands on 1. Read: E1 OR E2  
**E1 \ E2**: the first die is a 1 and the second die is not.  

*note: ∩ = AND, ∪ = OR*

The union of two events A and B is the event consisting of all
outcomes that are either in A or in B  

The intersection of two events A and B is the event consisting of all outcomes that are in both A and B.
*du tager ikke fejl, den er god nok*
(a) Sample space = {(D,D,D) (N,D,D),(D,N,D),(D,D,N), (N,N,D)   (N,D,N), (D,N,N), (N,N,N)}  
(b)  
(i) Either pumps 0-4, 3-6 {0,1,2,3,4,5,6}  
(ii) Either pumps 0-4 or all odd pumps in use, {1,2,3,4,5}  
(iii) All pumps {3,4} in use  
(iv) All pump {1,3} in use  
(v) All pumps {5,6} (not A)  
(vi) Only {6} (not A or C)  

(c)  
A={{S1,S2,F3},{S1,F2,S3},{F1,S2,S3}}  
B={{S1, S2, F3}, {S1,F2,S3}, {F1, S2, S3}, {S1,S2,S3}}  
C={{S1,S2,F3}, {S1,F2,S3}, {S1,S2,S3}}  

(iv)   
C' = {F1,F2,S3},{F1,S2,F3},{F1,F2,F3},{F1,S2,S3},{S1,F2,F3}}    
AnC = {{S1,S2,F3}, {S1,F2,S3}}  
AuC = {{S1,S2,F3}, {S1,F2,S3}, {F1,S2,S3}, {S1,S2,S3}}  
BuC ..  
BnC ..  

# Exercise 9-2
*brug slides til denne slags opgaver*
(a)  
Pr(A) = 60%, 0.6 - Individuals that include optional mem card  
Pr(B) = 40%, 0.4 - Include Extra Battery  
Pr(AnB) = 30%, 0.3 - Extra Battery and Optional mem card  
Pr(AnB)/Pr(B) = 30/40 = 0.75 = 75%

(b)
Pr(AnB)/Pr(A) = 30/60 = 0.5 = 50%  

# Exercise 9-3
Answer in Book PDF  

# Exercise 9-4
(a)
Pr(yes) = 4/8 = 50%, 0.5  
Pr(no) = 4/8 = 50%, 0.5  
(b)  
Weather:  
Pr(Sunny|No) = 1/4  
Pr(Sunny|Yes) = 1/4  
Pr(Rainy|No) = 2/4  
Pr(Rainy|Yes) = 1/4  
Pr(Snow|No) = 1/4  
Pr(Snow|Yes) = 2/4  

Snow Level:   
Pr(<50|No) = 3/4  
Pr(<50|Yes) = 1/4  
Pr(>=50|No) = 1/4  
Pr(>=50|Yes) = 3/4  

(c)  
Day A:  
*Normalization = Pr(Sunny) * Pr(>=50) = 2/8 * 1/2 = 0.125*  
Pr(Sunny|Yes) * Pr(>=50|Yes) * Pr(Yes) =   1/4 * 3/4 * 1/2 = 0.9375/0.125 = 0.75 = **75%**   
Pr(Sunny|No) * Pr(>=50|No) * Pr(No) = 1/4 * 1/4 * 1/2 = 0.03125/0.125 = 25%  
Day B:   
*Normalization = Pr(Rainy) * Pr(<50) = 3/8 * 1/2 = 0.1875*  
Pr(Rainy|Yes) * Pr(<50|Yes) * Pr(Yes) = 1/4 * 1/4 * 1/2 =  0.03125/0.1875 = 16%  
Pr(Rainy|No) * Pr(<50|No) * Pr(No) = 2/4 * 3/4 * 1/2 =  0.1875/0.1875 = **100%**  
Day C:  
*Normalization = Pr(Snow) * Pr(<50) = 3/8 * 1/2 = 0.1875*  
Pr(Snow|Yes) * Pr(<50|Yes) * Pr(Yes) = 2/4 * 1/4 * 1/2 =  0.0625/0.1875 = 33%   
Pr(Snow|No) * Pr(<50|No) * Pr(No) = 1/4 * 3/4 * 1/2 =  0.09375/0.1875 = **50%**
