a = [1,2,3,2,1,5,6,5,5,5]

import collections
print [item for item, count in collections.Counter(a).items() if count > 1]
seen = set()
uniq = []
for x in a:
    if x not in seen:
        uniq.append(x)
        seen.add(x)
