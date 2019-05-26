#Exercise 2-1\

##Cartesian Product\
(a) Cartesian Product of A{a,b,c} X Z{1,2,3,4}:\
A x Z = {(a,1), (a,2), (a,3), (a,4), (b,1), (b,2), (b,3), (b,4), (c,1), (c,2), (c,3), (c,4)}\
**CartesianProduct.py**

|   | 1   | 2   | 3   | 4   |
|---|-----|-----|-----|-----|
| *a* | (a,1) | (a,2) | (a,3) | (a,4) |
| *b* | (b,1) | (b,2) | (b,3) | (b,4) |
| *c* | (c,1) | (c,2) | (c,3) | (c,4) |

##Binary Relation\
(b) The binary relation over A and Z is a subset of the cartesian product of AxZ. \ If for example A was linked to all odd numbers, b was linked to even numbers, and c was linked to even and odd numbers, we would have a binary relation that looked like this: \
**L = {(a,1), (a,3), (b,2), (b,4), (c,1), (c,2), (c,3), (c,4)}** Which clearly is a subset of Cartesian product AxZ.

##Non-total function A->Z\
Non-total functions or partial functions, does not have a result for every possible outcome.\
It generalizes the concept of a function f : X → Y by not forcing f to map every element of X to an element of Y (only some subset X′ of X). If X′ = X, then f is called a total function for emphasizing that its domain is not a proper subset of X. **A(b) -> z(2)** **A(c) -> Z(1)**

##Total Function \
**A(a) -> Z(1) A(b) -> Z(2)** **A(c) -> Z(1)**

#Exercise 2-2\
(a)supp({Milk} -> {Diapers}) = 40%, conf({Milk} -> {Diapers}) = supp({Milk} -> {Diapers}/supp({Milk}) = 40%/50% = 80%.\
(b)supp({Diapers} -> {Milk}) = 40%, conf({Diapers} -> {Milk}) = supp({Diapers} -> {Milk}/supp({Diapers}) = 40%/70% = 57%\
(c) ∀x ∈ T : σ(x) = *6*, given that σ(x) = max support of size 3\
(d)  6 unique items, 3^6-2^(6+1)+1 = 3-2+1 = 602 possible rules\
(e) itemset {Milk, Diapers, Bread, Butter} has the biggest size with 4 items and is frequent\
(sup({Milk, Diapers, Bread, Butter})
(f) {Diapers, Milk}. Find de individuelle frequencies først, og gå efter det.\
(g) {Bread, butter}\
