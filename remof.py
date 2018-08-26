import asm
import re
import argparse
import time


print("      ___           ___           ___           ___           ___           ")
print("     /\  \         /\__\         /\  \         /\  \         /\__\          ")
print("    /::\  \       /:/ _/_       |::\  \       /::\  \       /:/ _/_         ")
print("   /:/\:\__\     /:/ /\__\      |:|:\  \     /:/\:\  \     /:/ /\__\        ")
print("  /:/ /:/  /    /:/ /:/ _/_   __|:|\:\  \   /:/  \:\  \   /:/ /:/  /        ")
print(" /:/_/:/__/___ /:/_/:/ /\__\ /::::|_\:\__\ /:/__/ \:\__\ /:/_/:/  /         ")
print(" \:\/:::::/  / \:\/:/ /:/  / \:\~~\  \/__/ \:\  \ /:/  / \:\/:/  /          ")
print("  \::/~~/~~~~   \::/_/:/  /   \:\  \        \:\  /:/  /   \::/__/           ")
print("   \:\~~\        \:\/:/  /     \:\  \        \:\/:/  /     \:\  \           ")
print("    \:\__\        \::/  /       \:\__\        \::/  /       \:\__\          ")
print("     \/__/         \/__/         \/__/         \/__/         \/__/          ")
print("                                                                            ")
print("                                                                            ")
print("                                                                            ")
print("github.com/xoreaxeaxeax/movfuscator  :: The single instruction BF compiler  ") 
print("github.com/zadewg/remof              :: M/o/Vfuscator1 Reverse engineering  ")
print("                                                                            ")
print("chris domas           @xoreaxeaxeax                                         ") 
print("mapez                 @zadewg                                               ")
time.sleep(0.5)

def preprocess(DATA):
	DATA = DATA.replace('\n', '').replace('\t', '').replace(' ','')
	return DATA


def detect_flags(DATA):

	global NOJMP, MMIO, CELL16, OPT

	print("[*] Detecting flags...\n")
	time.sleep(1)
	
	NOJMP = True if "jmploop" not in DATA else False;
	MMIO = True if "MMIO" in DATA else False;

	CELL_ARR = {
			'cell16' : ['comma', 'plus', 'minus', 'bthan', 'lthan'], 
			'opcell' : ['plus', 'minus', 'lthan', 'bthan'], 
			'mmcell' : ['comma'],
		    }


	OPT_ARR = {
			'opt' : ['plus', 'minus', 'lthan', 'bthan'], 
			'opcell' : ['plus', 'minus', 'lthan', 'bthan'], 
		  }

	CELL16, OPT = False, False

	for key, values in CELL_ARR.items():
		for v in values:
			XCELL16 = True if eval("asm.{}['{}']".format(v, key)) in DATA else False
			if XCELL16 == True:
				CELL16 = True


	for key, values in OPT_ARR.items():
		for v in values:
			XOPT = True if eval("asm.{}['{}']".format(v, key)) in DATA else False
			if XOPT == True:
				OPT = True




def main(DATA):

	BF_DATA_SIZE = DATA[(DATA.find('DATAequ')+7) : (DATA.find('%macroc_s1'))]
	INTRO = preprocess(asm.intro['std'])
	INTRO = INTRO.format(BF_DATA_SIZE)

	AT    = preprocess(asm.at['std'])
	CLOSE = preprocess(asm.close['std'])
	DOT   = preprocess(asm.dot['std'])
	COMMA = preprocess(asm.comma['std'])
	PLUS  = preprocess(asm.plus['std'])
	MINUS = preprocess(asm.minus['std'])
	LTHAN = preprocess(asm.lthan['std'])
	BTHAN = preprocess(asm.bthan['std'])

	OBRACK = re.escape(preprocess(asm.obrack['std']).replace('{}', 'XXXXX')).replace('XXXXX', '([0-9]+)')
	CBRACK = re.escape(preprocess(asm.cbrack['std']).replace('{}', 'XXXXX')).replace('XXXXX', '([0-9]+)')


	if MMIO: 
		MMIO_SIZE = DATA[(DATA.find('MMIO_SIZEequ')+12) : DATA.find('section.bss')]

		INTRO = preprocess(asm.intro['mmio'])
		INTRO = INTRO.format(BF_DATA_SIZE, MMIO_SIZE)

		DOT = preprocess(asm.dot['mmio'])
		COMMA = preprocess(asm.comma['mmio'])



	if NOJMP:
		INTRO = preprocess(asm.intro['nojmp'])
		INTRO = INTRO.format(BF_DATA_SIZE)

		CLOSE = preprocess(asm.close['nojmp'])


	if CELL16:
		COMMA = preprocess(asm.comma['cell16'])
		PLUS = preprocess(asm.plus['cell16'])
		MINUS = preprocess(asm.minus['cell16'])
		LTHAN = preprocess(asm.lthan['cell16'])
		BTHAN = preprocess(asm.bthan['cell16'])
		#OBRACK = re.escape(asm.obrack['cell16'].replace('\n', '').replace('\t', '').replace(' ','').replace('{}', 'XXXXX')).replace('XXXXX', '([0-9]+)')
		#CBRACK = re.escape(asm.cbrack['cell16'].replace('\n', '').replace('\t', '').replace(' ','').replace('{}', 'XXXXX')).replace('XXXXX', '([0-9]+)')


	if OPT:
		PLUS = preprocess(asm.plus['opt'])
		MINUS = preprocess(asm.minus['opt'])
		LTHAN = preprocess(asm.lthan['opt'])
		BTHAN = preprocess(asm.bthan['opt'])


	if MMIO and NOJMP:
		INTRO = preprocess(asm.intro['mmjmp'])
		INTRO = INTRO.format(BF_DATA_SIZE, MMIO_SIZE)


	if OPT and CELL16:
		PLUS = preprocess(asm.plus['opcell'])
		MINUS = preprocess(asm.minus['opcell'])
		LTHAN = preprocess(asm.lthan['opcell'])
		BTHAN = preprocess(asm.bthan['opcell'])


	if MMIO and CELL16:
		COMMA = preprocess(asm.comma['mmcell'])



	print("\nMMIO Flag: {}".format(MMIO))
	print("NOJMP Flag: {}".format(NOJMP))
	print("CELL16 Flag: {}".format(CELL16))
	print("OPT Flag: {}".format(OPT if OPT == False else "True  OPTIMIZED CODE NOT YET SUPPORTED, OUTPUT SUSCEPTIBLE TO ERRORS")) #fix this with regex
	print("")



	if DATA[:len(INTRO)] == INTRO:
		counter = len(INTRO)
	else:
		print("[!] Missing or malformed macros, exiting.\n")
		raise SystemExit

	time.sleep(0.4)
	out = []
	while counter < len(DATA):
		time.sleep(0.00002)

		if DATA[counter : counter + len(DOT)] == DOT:
			counter += len(DOT)
			print(('0x%0*X' % (8, counter)).lower() + ':     .')
			out.append('.')

		if DATA[counter : counter + len(COMMA)] == COMMA:
			counter += len(COMMA)
			print(('0x%0*X' % (8, counter)).lower() + ':     ,')
			out.append(',')

		if DATA[counter : counter + len(PLUS)] == PLUS:
			counter += len(PLUS)
			print(('0x%0*X' % (8, counter)).lower() + ':     +')
			out.append('+')

		if DATA[counter : counter + len(MINUS)] == MINUS:
			counter += len(MINUS)
			print(('0x%0*X' % (8, counter)).lower() + ':     -')
			out.append('-')

		if DATA[counter : counter + len(LTHAN)] == LTHAN:
			counter += len(LTHAN)
			print(('0x%0*X' % (8, counter)).lower() + ':     <')
			out.append('<')

		if DATA[counter : counter + len(BTHAN)] == BTHAN:
			counter += len(BTHAN)
			print(('0x%0*X' % (8, counter)).lower() + ':     >')
			out.append('>')

		if DATA[counter : counter + len(AT)] == AT:
			counter += len(AT)
			print(('0x%0*X' % (8, counter)).lower() + ':     @')
			out.append('@')

		if DATA[counter : counter + len(CLOSE)] == CLOSE:
			counter += len(CLOSE)
			print("\n[+] {} Bytes decompiled succesfuly".format(len(DATA)))

		else:
			continue
			#print("\n[!] Decompilation Failed")
			#break




	DECOMPILED = ''.join(out)
	with open('{}.bf'.format(FILEOUT), 'w+') as outfile:
		outfile.write(DECOMPILED)

	print("[+] Ouput saved to {}.bf".format(FILEOUT))




def parsein():

	global FILEIN, FILEOUT

	parser = argparse.ArgumentParser(description='https://github.com/zadewg/remo')
	parser.add_argument('-if','--infile', help='File to read from.', required=True)
	parser.add_argument('-of','--outfile', help='File to write to.', required=True)

	args = vars(parser.parse_args())

	FILEIN = args['infile']
	FILEOUT = args['outfile']


if __name__ ==  "__main__":
	parsein()

	
	with open('{}.asm'.format(FILEIN), 'r') as infile:
		DATA = (infile.read().replace('\n', '').replace('\t', '').replace(' ',''))
		
	try:
		DATA = DATA[DATA.find('USE32') : ]
		print("\n\n\n\n[*] Sanitizing imput...")
		time.sleep(0.4)

	except:
		print("[!] Missing or malformed macros, exiting.\n")
		raise SystemExit
		

	detect_flags(DATA)

	main(DATA)

