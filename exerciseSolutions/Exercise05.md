#Exercise 5-1\

##Nominal
(categories) = Possible to tell whether two values are equal or not. Examples: sex, eye color, healthy/sick, amino acids \

##Ordinal
= There is an order relation (better/worse) but no uniform distance. Examples grade, quality label, age class, color\

##Metric
= differences and relations between values are meaningful, values can be discrete or continuous. Examples : weight, selling counts, age. \

exaples = n = 5. x=odd numbers y = even.\

(a)\
Reflexive = (1-1) + (2-2) + (3-3) + (4-4) + (5-5) = 0 == **yes reflexive**
Symmetric = (1-2) + (3-4) + (5-6) + (7-8) + (9-10) = (2-1) + (4-3) + (6-5) + (8-7) + (10-9) = -5 != 5 != **not symmetric**
Strict = (1-3) + (3-1) + (1-3) + (3-1) + (1-3) + (3-1) = 0 != **not strict**
Triangle Inequality for n = 2 = \
*x1 = 3, x2 = 10, z1 = 9, z2 = 10, y1 = 15, y2=7*\
d(x,z) = (3-9) + (10-10) = -6. \
d(x,y) = (3-15) + (10-7) = -15\
d(y,z) = (15-9) + (7-10) = 3\
-6<=-12 != falsk = **not triangle inequality**\
**a = Dissimiliarity function.**



(b)\
Reflexive = (1-1)^2 + (2-2)^2 + (3-3)^2 + (4-4)^2 + (5-5)^2 = **yes reflexive**\
Symmetric = (1-2)^2 + (3-4)^2 + (5-6)^2 + (7-8)^2 + (9-10)^2 = (2-1)^2 + (4-3)^2 + (6-5)^2 + (8-7)^2 + (10-9)^2 = 5 == 5 = **yes symmetric**\
Strict = (1-3)^2 + (3-1)^2 + (1-3)^2 + (3-1)^2 + (1-3)^2 + (3-1)^2 = 24 **yes strict** (We will never be able to get 0, unless x=y, because of ^2)\
Triangle inequality = for n=2 \
*x1 = 3, x2 = 10, z1 = 9, z2 = 10, y1 = 15, y2=7*\
d(x,z) = (3-9)^2 + (10-10)^2 = 36. \
d(x,y) = (3-15)^2 + (10-7)^2 = 153\
d(y,z) = (15-9)^2 + (7-10)^2 = 45\
36<=153+45 = **yes triangle inequality** \
**b = Metric** \

(c)\
Reflexive = sqrt((1-1) + (2-2) + (3-3) + (4-4)) = **yes reflexive**\
Symmetric sqrt((1-2)^2 + (3-4)^2 + (5-6)^2 + (7-8)^2) = sqrt((2-1)^2 + (4-3)^2 + (6-5)^2 + (8-7)^2) = 2==2 = **yes symmetric**
Strict = sqrt((1-1)^2 + (3-3)^2 + (10-10)^2 + (2-2)^2 + (6-6)^2) == **yes strict** (samme som i b)\
Triangle inequality = for n=2 \
*x1 = 0, x2 = 0, z1 = 9, z2 = 10, y1 = 0, y2=0*\
d(x,z) = sqrt((3-9)^2 + (10-10)^2) = 6. \
d(x,y) = sqrt((3-15)^2 + (10-7)^2) = 12.36\
d(y,z) = sqrt((15-9)^2 + (7-10)^2) = 6.71\
6<=12.36+6.71 = sandt.\
ex2:\
d(x,z) = sqrt((0-9)^2 + (0-10)^2) = 13.45 \
d(x,y) = sqrt((0-0)^2 + (0-0)^2) = 0\
d(y,z) = sqrt((0-9)^2 + (0-10)^2) = 13.45\
13.45<=13.45 = sandt. = **yes triangle inequality**\
**c = Metric**\

(d)\
Reflexive = (1-1) + (2-2) + (3-3) + (4-4) + (5-5) = 1+1+1+1+1 = **not reflexive**\
Not reflexive, no need to proceed.\
**d = not a distance**\

(e)\
Reflexive = (1,1) + (2,2) + (3,3) + (4,4) + (5,5) = 0+0+0+0+0 = **yes reflexive**\
Symmetric = (1,2) + (3,4) + (5,6) + (7,8) + (9,10) = 1+1+1+1+1 = (2,1) + (4,3) + (6,5) + (8,7) + (10,9) = 1+1+1+1+1 **yes symmetric** (Vi får altid samme resultat, da eneste udfald er 1, eller 0.)\
Strict = (1,3) + (3,1) + (1,3) + (3,1) + (1,3) + (3,1) = 1+1+1+1+1\
Strict = (1,1) + (3,3) + (1,1) + (3,3) + (1,1) + (3,3) = 0+0+0+0+0 = **yes strict**.\
Triangle Inequality for n = 1 = \
*x1 = 0, z1 = 1, y1 = 0*\
d(x,z) = (3,9) + (10,10) = 1 + 0. \
d(x,y) = (3,15) + (10,7) = 1+1\
d(y,z) = (15,9) + (7,10) = 1+1\
1<=2+2 = sandt =
**e = Metric**\


#Exercise 5-2\

(a) ??

(b) ??
