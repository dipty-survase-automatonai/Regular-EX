automaton@AutomatonAI:~$ python3
Python 3.5.2 (default, Nov 12 2018, 13:43:14) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import re
>>> re.match
<function match at 0x7f56adaafea0>


>>> re.match("h","hello")
<_sre.SRE_Match object; span=(0, 1), match='h'>

>>> re.match("h","Hhello")
>>> re.search("h","Hhello")
<_sre.SRE_Match object; span=(1, 2), match='h'>

>>> re.search("h","Hhelhlo")
<_sre.SRE_Match object; span=(1, 2), match='h'>

>>> re.search("h","Hhelhlo[2:]")
<_sre.SRE_Match object; span=(1, 2), match='h'>

>>> re.search("h","Hhelhlo"[2:0])
>>> re.findall("h","Hhelhlo")
['h', 'h']
>>> for match in re.finditer("h","Hhelhlo"):
...     print(match)
... 
<_sre.SRE_Match object; span=(1, 2), match='h'>
<_sre.SRE_Match object; span=(4, 5), match='h'>


>>> re.sub("h","8","Hhelhlo")
'H8el8lo'

>>> re.subn("h","8","Hhelhlo",1)
('H8elhlo', 1)

>>> re.subn("h","8","Hhelhlo",1,re.IGNORECASE)
('8helhlo', 1)

>>> re.subn("h","8","Hhelhlo",re.IGNORECASE)
('H8el8lo', 2)

>>> re.sub("h","8","Hhelhlo",re.IGNORECASE)
'H8el8lo'

>>> re.sub("h","8","Hhelhlo",3,re.IGNORECASE)
'88el8lo'

>>> re.subn("h","8","Hhelhlo",3,re.IGNORECASE)
('88el8lo', 3)

>>> re.subn("h","*","Hhelhlo",re.IGNORECASE)
('H*el*lo', 2)

>>> re.subn("h","*","Hhelhlo",flags=re.IGNORECASE)
('**el*lo', 3)


>>> re.split("h","*","Hhello",flags=re.IGNORECASE)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python3.5/re.py", line 203, in split
    return _compile(pattern, flags).split(string, maxsplit)
TypeError: 'str' object cannot be interpreted as an integer



>>> match=re.findall("x.f","xjfx#fxjjjf")
>>> 
>>> match
['xjf', 'x#f']

>>> match=re.findall("x...f","xjfx#fxjjjf")
>>> match
['xjjjf']

>>> match=re.findall("^x.f","xjfx#fxjjjf")
>>> match
['xjf']

>>> match=re.findall("x.f$","xjfx#fxjjjf")
>>> match
[]

>>> match=re.findall("j.f$","xjfx#fxjjjf")
>>> match
['jjf']

>>> match=re.findall("x*f","xjfx#fxjjjf")
>>> match
['f', 'f', 'f']

>>> match=re.search("x*f","xjfx#fxjjjf")
>>> match
<_sre.SRE_Match object; span=(2, 3), match='f'>


>>> match=re.search("x*f","a xxf xxfxffx")
>>> match
<_sre.SRE_Match object; span=(2, 5), match='xxf'>


>>> match=re.search("x+f","a xxf xxfxffx")
>>> match
<_sre.SRE_Match object; span=(2, 5), match='xxf'>



>>> match=re.search("x+f","x xxf xxfxffx")
>>> match
<_sre.SRE_Match object; span=(2, 5), match='xxf'>


>>> match=re.findall("xf+","x xxf xxfffffxffx")
>>> match
['xf', 'xfffff', 'xff']

>>> match=re.findall("xf+?","x xxf xxfffffxffx")
>>> match
['xf', 'xf', 'xf']

