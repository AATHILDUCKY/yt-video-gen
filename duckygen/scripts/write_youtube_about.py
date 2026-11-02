#!/usr/bin/env python3
"""Format authored, video-specific metadata into about-<video-name>.md; never upload."""
import argparse,json,re,unicodedata
from pathlib import Path

def stamp(seconds):
 seconds=int(seconds);h,rem=divmod(seconds,3600);m,s=divmod(rem,60)
 return f'{h}:{m:02}:{s:02}' if h else f'{m:02}:{s:02}'

def build(data):
 title=data['title'].strip();description=data['description'].strip()
 if not title or len(title)>100 or any(c in title for c in '<>\n\r'):raise ValueError('Use a nonempty title up to 100 characters without angle brackets or line breaks.')
 if not description or '<' in description or '>' in description:raise ValueError('Provide the actual video description without angle brackets.')
 if not isinstance(data['keywords'],list) or not data['keywords'] or not all(isinstance(x,str) for x in data['keywords']):raise ValueError('Provide keywords as a nonempty array of individual strings.')
 keywords=[]
 for raw in data['keywords']:
  word=raw.strip()
  if not word or any(c in word for c in ',\n\r'):raise ValueError('Provide nonempty individual keywords without commas or line breaks.')
  if word.casefold() not in {x.casefold() for x in keywords}:keywords.append(word)
 # YouTube counts separators and implicit quotation marks around multiword tags.
 if sum(len(x)+(2 if ' ' in x else 0) for x in keywords)+max(0,len(keywords)-1)>500:raise ValueError('Keywords exceed the 500-character tags budget.')
 chapters=data.get('chapters',[])
 if chapters:
  starts=[x['start'] for x in chapters];duration=data['duration']
  if len(starts)<3 or starts[0]!=0 or any(not isinstance(s,(int,float)) or s!=int(s) or s<0 for s in starts):raise ValueError('Use at least three whole-second chapter starts beginning at zero.')
  if any(b-a<10 for a,b in zip(starts,starts[1:]+[duration])):raise ValueError('Chapters must be ordered and at least 10 seconds long, including the final chapter.')
  description+='\n\n'+ '\n'.join(stamp(c['start'])+' '+c['label'].strip() for c in chapters)
 sources=data.get('sources',[])
 if sources:description+='\n\nSources:\n'+'\n'.join(x['title']+': '+x['url'] for x in sources)
 if data.get('credits'):description+='\n\nCredits:\n'+data['credits'].strip()
 if data.get('disclosure'):description+='\n\n'+data['disclosure'].strip()
 hashtags=data.get('hashtags',[])
 if any(not re.fullmatch(r'#[\w]+',tag) for tag in hashtags):raise ValueError('Use hashtags beginning with # and containing no spaces.')
 if hashtags:description+='\n\n'+' '.join(hashtags)
 if len(description)>5000 or len(description.encode('utf-8'))>5000:raise ValueError('Description exceeds the conservative 5,000-byte upload/API budget.')
 sections=['# YouTube upload information','## Video title\n\n'+title,'## Description — copy into YouTube\n\n'+description,'## Keywords / tags — comma separated\n\n'+', '.join(keywords)]
 for key,label in [('thumbnail_text','Thumbnail text suggestion'),('pinned_comment','Pinned comment suggestion'),('language','Video language'),('category','Suggested category'),('audience_note','Audience setting note')]:
  if data.get(key):sections.append('## '+label+'\n\n'+data[key].strip())
 sections.append('## Files\n\n- Video: final.mp4\n- English captions: captions.srt\n- Full sources/provenance: SOURCES.md\n\nMetadata is drafted from the finished film. Review upload settings and any required synthetic-content disclosure against the actual content; no upload has been performed.')
 return title,'\n\n'.join(sections)+'\n'

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('metadata',type=Path);p.add_argument('--project',type=Path,required=True);p.add_argument('--name',help='Optional lowercase hyphenated video filename');p.add_argument('--replace',action='store_true');a=p.parse_args()
 data=json.loads(a.metadata.read_text());title,text=build(data)
 name=a.name or re.sub(r'[^a-z0-9]+','-',unicodedata.normalize('NFKD',title).encode('ascii','ignore').decode().lower()).strip('-')[:90].rstrip('-')
 if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',name):p.error('Provide --name with a lowercase hyphenated video name.')
 a.project.mkdir(parents=True,exist_ok=True);out=a.project/f'about-{name}.md'
 if out.exists() and not a.replace:p.error('Output exists; use --replace after reviewing changes.')
 out.write_text(text);print(out)

if __name__=='__main__':main()
