import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules


dataset = [["Milk", "Beer", "Diapers"],
    ["Bread", "Butter", "Milk"],
    ["Milk", "Diapers", "Cookies"],
    ["Bread", "Butter", "Cookies"],
    ["Beer", "Cookies", "Diapers"],
    ["Milk", "Diapers", "Bread", "Butter"],
    ["Bread", "Butter", "Diapers"],
    ["Beer", "Diapers"],
    ["Milk", "Diapers", "Bread", "Butter"],
    ["Beer, Cookies"]]

te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)
frequent_itemsets = apriori(df, min_support=0.4, use_colnames=True)
rules = association_rules(frequent_itemsets, metric="support", min_threshold=0)
print(rules)
print(frequent_itemsets)
print("----------------")
print(association_rules(frequent_itemsets, metric="confidence", min_threshold=0))
print("----------------")
print(rules[rules['antecedents'] == {'Milk', 'Diapers'}])
print("----------------")
print(rules)
