#Exercise 4-1\

Support threshold = 2

| TransID | Items |
|---------|-------|
| A       | 6     |
| B       | 6     |
| C       | 7     |
| D       | 5     |
| E       | 6     |
| F       | 3     | \

| TransID | Items |
|---------|-------|
| AB      | 4     |
| AC      | 4     |
| AD      | 2     |
| AE      | 4     |
| AF      | 1     |
| BC      | 4     |
| BD      | 4     |
| BE      | 4     |
| BF      | 2     |
| CD      | 3     |
| CE      | 5     |
| CF      | 3     |
| DE      | 1     |
| DF      | 2     |
| EF      | 1     |\
Her fjerner vi altså AF, DE, EF fordi de er under 2:

| TransID | Items |
|---------|-------|
| AB      | 4     |
| AC      | 4     |
| AD      | 2     |
| AE      | 4     |
| BC      | 4     |
| BD      | 4     |
| BE      | 4     |
| BF      | 2     |
| CD      | 3     |
| CE      | 5     |
| CF      | 3     |
| DF      | 2     |\

| TransID | Items |
|---------|-------|
| ABC     | 2     |
| ABD     | 2     |
| ABE     | 2     |
| ACD     | 1     |
| ACE     | 3     |
| ADE     | 0     |
| BCD     | 2     |
| BCE     | 3     |
| BCF     | 2     |
| BDE     | 1     |
| BDF     | 1     |
| BEF     | 1     |
| CDE     | 1     |
| CDF     | 2     |
| CEF     | 1     |\
Nu fjerner vi ACD, ADE, BDE, BDF, BEF, CDE, CEF

| TransID | Items |
|---------|-------|
| ABC     | 2     |
| ABD     | 2     |
| ABE     | 2     |
| ACE     | 3     |
| BCD     | 2     |
| BCE     | 3     |
| BCF     | 2     |
| CDF     | 2     |\


| TransID | Items |
|---------|-------|
| ABCD    | 1     |
| ABCE    | 1     |
| ABDE    | 0     |
| BCDE    | 1     |
| BCDF    | 1     |
| BCEF    | 1     |\
Her skal alle fjernes, og tabellen er derfor irrelevant. Vi bruger forrige.\

Result: ABC, ABD, ABE, ACE, BCD, BCE, BCF, CDF\

| TransID | Items |
|---------|-------|
| ABC     | 2     |
| ABD     | 2     |
| ABE     | 2     |
| ACE     | 3     |
| BCD     | 2     |
| BCE     | 3     |
| BCF     | 2     |
| CDF     | 2     |\


#Exercise 4-2
Warmup exercise...: \
dist2(p, q) = 5.3851 . . .\
dist1(p, q) = 9\
dist∞(p, q) = 4\
distw(p, q) = 7.1063\
distM1(p, q) = 5.3851 . . .\
distM2(p, q) = 8.4261 . .\
**ColorhistorgramsAndDistancefunctions.py** \




(a) a (1, 4, 4), b(8, 1, 7), c(2, 4, 10), d(1, 2, 13), q(1, 8, 7)\

(b) \
Color histograms (red, orange, blue); distance\
q = (1, 8, 7)\
a = (1, 4, 4);dist(q, a) = 5\
b = (8, 1, 7);dist(q, b) = 9.9\
c = (2, 4, 10);dist(q, c) = 5.1\
d = (1, 2, 13);dist(q, d) = 8.5 \

ranking = a,c,d,b\

(c)The results are not entirely satisfactory. What could you change in the feature extractionor  
in the distance function to get better results? Report the improved feature extraction and
features or the improved 
distance function.\
Debatably, picture b is more similar to q than a or d are. The problem is that the Euclidean
distance takes each color individually to compute the distance but does not take similarity
between different colors (i.e., bins in the histogram) into account.\
A solution would be to use the quadratic form (a.k.a. Mahalanobis-) distance. We need a
similarity matrix to define the (subjective) similarity of bins with each other\

se **ExtrasolutionsDistanceMeasuring.pdf**
