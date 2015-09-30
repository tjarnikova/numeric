import json
from collections import namedtuple

with open('run_1.json','r') as f:
      init_dict=json.load(f)

print(init_dict)

#either use this as a dict or convert to a namedtuple
initvals=namedtuple('initvals','dt c1 c2 c3 t_beg t_end yinitial comment')
theCoeff=initvals(**init_dict)

print(theCoeff)
