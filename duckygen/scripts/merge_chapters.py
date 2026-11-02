#!/usr/bin/env python3
"""Join measured chapter stems/timelines at 1×, streaming WAV blocks."""
import argparse,json,math,wave
from pathlib import Path

def stamp(t):
 m=round(t*1000);return f'{m//3600000:02}:{m//60000%60:02}:{m//1000%60:02},{m%1000:03}'
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('chapters',nargs='+',type=Path);p.add_argument('--out',required=True,type=Path);a=p.parse_args();out=a.out.resolve()
 if out.exists() and any(out.iterdir()):p.error('Use a new/empty output folder; preserve chapter sources.')
 records=[];offset=0;timelines=[];formats={}
 for index,folder in enumerate(a.chapters):
  folder=folder.resolve();meta=json.loads((folder/'timeline.json').read_text())
  with wave.open(str(folder/'soundtrack.wav')) as w:duration=w.getnframes()/w.getframerate()
  if abs(duration-float(meta['duration']))>.001:raise ValueError('Stale chapter timing: '+str(folder))
  for name in ['voice.wav','effects.wav','soundtrack.wav']:
   with wave.open(str(folder/name)) as w:
    fmt=(w.getnchannels(),w.getsampwidth(),w.getframerate());length=w.getnframes()/w.getframerate()
   if abs(length-duration)>.001:raise ValueError('Stem length differs: '+str(folder/name))
   if name in formats and formats[name]!=fmt:raise ValueError('Matching stems need consistent channel/rate formats.')
   formats[name]=fmt
  for scene in meta['scenes']:
   if not 0<=scene['start']<scene['voice_end']<=scene['end']<=duration+.001:raise ValueError('Invalid chapter phrase timing.')
   s=dict(scene);s['id']=f'chapter-{index+1}-'+s['id'];s['source_chapter']=str(folder)
   for key in ['start','voice_end','end']:s[key]+=offset
   s['sounds']=[{**x,'at':x['at']+offset} for x in scene.get('sounds',[])];timelines.append(s)
  records.append({'chapter':str(folder),'start':offset,'duration':duration});offset+=duration
 out.mkdir(parents=True,exist_ok=True)
 for name,fmt in formats.items():
  with wave.open(str(out/name),'wb') as dst:
   dst.setparams((*fmt,0,'NONE',''))
   for folder in a.chapters:
    with wave.open(str(folder/name)) as src:
     while block:=src.readframes(16384):dst.writeframesraw(block)
 meta={'duration':offset,'scenes':timelines,'chapters':records,'caption_timing':'measured phrase clips; not word alignment'};(out/'timeline.json').write_text(json.dumps(meta,indent=2));(out/'captions.srt').write_text('\n\n'.join(f'{i+1}\n{stamp(s["start"])} --> {stamp(s["voice_end"])}\n{s["text"]}' for i,s in enumerate(timelines))+'\n');(out/'narration.txt').write_text('\n\n'.join(s['text'] for s in timelines)+'\n');print(json.dumps({'duration':offset,'chapters':len(records),'voice_speed':1,'normalization':'not performed; inspect final joined mix'}))
if __name__=='__main__':main()
