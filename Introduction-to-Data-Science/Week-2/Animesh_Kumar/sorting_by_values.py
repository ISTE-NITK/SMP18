
from collections import OrderedDict
def sorting_values(d):
    dd = OrderedDict(sorted(d.items(), key=lambda x: x[1]))
    return(dd)


  
    