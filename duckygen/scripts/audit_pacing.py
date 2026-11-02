#!/usr/bin/env python3
"""Report visual hold lengths and gaps between measured narration phrases."""
import argparse,json,math
from pathlib import Path

def audit(plan,max_shot,max_gap):
 result={'shot_count':0,'phrase_count':0,'long_shots':[],'narration_gaps':[],'errors':[]}
 for key in ['shots','phrases']:
  values=plan.get(key,[])
  if not isinstance(values,list):result['errors'].append(key+' must be a list');continue
  previous=None
  for i,v in enumerate(values):
   try:
    start,end=float(v['start']),float(v['end'])
    if not math.isfinite(start+end) or start<0 or end<=start:raise ValueError()
   except (TypeError,ValueError,KeyError):result['errors'].append(f'{key}[{i}]: invalid bounds');continue
   if previous is not None and start<previous-.001:result['errors'].append(f'{key}[{i}]: overlap or unsorted')
   if key=='shots' and end-start>max_shot+.001:result['long_shots'].append({'index':i,'duration':round(end-start,3)})
   if key=='phrases' and previous is not None and start-previous>max_gap+.001:result['narration_gaps'].append({'before':i,'start':previous,'duration':round(start-previous,3)})
   previous=end
  result['shot_count' if key=='shots' else 'phrase_count']=len(values)
 result['review_flags']=len(result['long_shots'])+len(result['narration_gaps'])
 return result

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('plan',type=Path);p.add_argument('--max-shot',type=float,default=5);p.add_argument('--max-gap',type=float,default=.65);a=p.parse_args()
 if a.max_shot<=0 or a.max_gap<0:p.error('Thresholds must be positive (gap may be zero).')
 result=audit(json.loads(a.plan.read_text()),a.max_shot,a.max_gap);print(json.dumps(result,indent=2));return 1 if result['errors'] else 0
if __name__=='__main__':raise SystemExit(main())
