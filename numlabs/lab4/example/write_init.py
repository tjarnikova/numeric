import json

initialVals={'yinitial': 1,'t_beg':0.,'t_end':1.,'dt':0.2,'c1':-1.,'c2':1.,'c3':1.}
initialVals['comment'] = 'simple exponential run 1'

with open('run_1.json','w') as f:
      f.write(json.dumps(initialVals,indent=4))
