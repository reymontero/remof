import asm
import re

ID = []

with open('out2.asm', 'r') as infile:
	DATA = (infile.read().replace('\n', '').replace('\t', '').replace(' ',''))
	DATA = DATA[DATA.find('USE32') : ] # PRE-CLEANING


PATTERN = re.escape(asm.obrack['std'].replace('\n', '').replace('\t', '').replace(' ','').replace('{}', 'XXXXX')).replace('XXXXX', '([0-9]+)')

result = (re.search(PATTERN, DATA))
if result:
	print(result.group())


print(re.findall(PATTERN, DATA))
