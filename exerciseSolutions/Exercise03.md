#Exercise 3-1\
{1,2,3},{1,2,4},{1,2,5},{1,3,4},{1,3,5},{2,3,4},{2,3,5},{3,4,5}\

list all candidate 4 items:\
{1,2,3} = **{1,2,3,4}**, **{1,2,3,5}**\
{1,2,4} = {1,2,4,5}\
{1,2,5} = no new extensions\
{1,3,4} = {1,3,4,5}\
{1,3,5} = no new extensions\
{2,3,4} = {2,3,4,5}\
{2,3,5} = no new extensions\
{3,4,5} = no new extensions\

pruning: remove {1,2,4,5} (vi har ikke 2,4,5), remove {2,3,4,5} (fordi vi har ikke 2,4,5), remove {1,3,4,5} (vi har ikke 1,4,5).\

result is highlighted\

#Exercise 3-3\
##Closed Frequent Itemsets\
An itemset X is closed if none of its
immediate supersets has exactly the same support as
X.\
An itemset is a closed frequent
itemset (w.r.t. some σ) if it is a closed itemset and is
frequent (w.r.t. σ).\

CFI support 4: {A} {B} {C} {CD} {ACE}, {AB}, {ACD}\
CFI support 2: {ABCD}, {ABCE}\
