import argparse


BF_DATA_SIZE = (128*1024)
MMIO_SIZE = (128*1024)  # must be <= data_size (could be fixed with more movs) */


def main(DATA):

	next_id = 1

	id_stack = 0
	stack_index = 0 
	

	evaluate("MOVfuscator")
	evaluate("domas 2015")
	evaluate("zadew 2018")
	evaluate("")
	evaluate("USE32")
	evaluate("section .data")
	evaluate("")
	evaluate("DATA equ {}".format(BF_DATA_SIZE))
	evaluate("")
	evaluate("%macro c_s 1")
	evaluate("	%1:   dd 0")
	evaluate("	d_%1: dd 0")
	evaluate("	s_%1: dd d_%1, %1")
	evaluate("%endmacro")
	evaluate("")
	evaluate("s_ms: dd s, m")
	evaluate("s_mz: dd z, m")
	evaluate("")
	evaluate("b: dd 0")
	evaluate("t: dd 0")
	evaluate("c: db 0")
	evaluate("")
	evaluate("c_s dp")
	evaluate("")
	evaluate("c_s id")
	evaluate("c_s ot")
	evaluate("")
	evaluate("on: dd 4")
	evaluate("d_on: dd 0")
	evaluate("s_on: dd d_on, on")
	evaluate("")
	evaluate("o: dd o_0, o_1")
	evaluate("o_0: dd 0, 4")
	evaluate("o_1: dd 4, 4")
	evaluate("")
	evaluate("a: dd a_0, a_1")
	evaluate("a_0: dd 0, 0")
	evaluate("a_1: dd 0, 4")
	evaluate("")
	evaluate("n: dd 4, 0")
	evaluate("")
	evaluate("nh: dd 0")
	evaluate("h: dd nh, 0")
	evaluate("")
	evaluate("trim: dd 0")
	evaluate("times 255 dd 1")
	evaluate("")
	evaluate("incb:")
	evaluate("%assign y 1")
	evaluate("%rep    256")
	evaluate("	db y&0xff")
	evaluate("	%assign y y+1")
	evaluate("%endrep")
	evaluate("")
	evaluate("decb:")
	evaluate("%assign y 256-1")
	evaluate("%rep    256")
	evaluate("	db y&0xff")
	evaluate("	%assign y y+1")
	evaluate("%endrep")
	evaluate("")
	evaluate("incw:")
	evaluate("%assign y 1")
	evaluate("%rep    256*256")
	evaluate("	dw y&0xffff")
	evaluate("	%assign y y+1")
	evaluate("%endrep")
	evaluate("")
	evaluate("decw:")
	evaluate("%assign y 256*256-1")
	evaluate("%rep    256*256")
	evaluate("	dw y&0xffff")
	evaluate("	%assign y y+1")
	evaluate("%endrep")
	evaluate("")
	evaluate("%macro eq 3")
	evaluate("	mov eax, 0")
	evaluate("	mov edx, 0")
	evaluate("	mov ax, [%2]")
	evaluate("	mov byte [e+eax], 0")
	evaluate("	mov byte [e+%3], 4")
	evaluate("	mov dl, [e+eax]")
	evaluate("	mov [%1], edx")
	evaluate("%endmacro")
	evaluate("")
	evaluate("%macro neq 3")
	evaluate("	mov eax, 0")
	evaluate("	mov edx, 0")
	evaluate("	mov ax, [%2]")
	evaluate("	mov byte [e+eax], 4")
	evaluate("	mov byte [e+%3], 0")
	evaluate("	mov dl, [e+eax]")
	evaluate("	mov [%1], edx")
	evaluate("%endmacro")
	evaluate("")
	evaluate("%macro or 3")
	evaluate("	mov eax, [%2]")
	evaluate("	mov edx, [o+eax]")
	evaluate("	mov eax, [%3]")
	evaluate("	mov eax, [eax+edx]")
	evaluate("	mov [%1], eax")
	evaluate("%endmacro")
	evaluate("")
	evaluate("%macro and 3")
	evaluate("	mov eax, [%2]")
	evaluate("	mov edx, [a+eax]")
	evaluate("	mov eax, [%3]")
	evaluate("	mov eax, [eax+edx]")
	evaluate("	mov [%1], eax")
	evaluate("%endmacro")
	evaluate("")
	evaluate("%macro not 2")
	evaluate("	mov eax, [%2]")
	evaluate("	mov eax, [n+eax]")
	evaluate("	mov [%1], eax")
	evaluate("%endmacro")
	evaluate("")

	if MMIO: 
		evaluate("src: dd 0")
		evaluate("d_src: dd s")
		evaluate("s_src: dd d_src, src")
		evaluate("dst: dd 0")
		evaluate("d_dst: dd s")
		evaluate("s_dst: dd d_dst, dst")
		evaluate("c_s sri")
		evaluate("c_s dsi")
		evaluate("fdi: dd 0")
		evaluate("fdo: dd 0")
		evaluate("ssi: db /dev/stdin, 0")
		evaluate("sso: db /dev/stdevaluate, 0")
		evaluate("zzz: dd 0")
		evaluate("MMIO_SIZE equ {}".format(MMIO_SIZE))
		evaluate("")

	if NOJMP:

		evaluate("sa: dd loop")          # sa_handler 
		evaluate("    times 0x20 dd 0")  # sa_mask 
		evaluate("    dd 0x40000000")    # sa_flags - sa_nodefer 
		evaluate("    dd 0")             # sa_restorer 
		evaluate("")
		evaluate("dsp: dd 0")

	evaluate("section .bss")
	evaluate("m: resb DATA")
	evaluate("s: resb DATA")
	evaluate("z: resb DATA")
	evaluate("e: resb 256*256")
	evaluate("")

	evaluate("section .text")
	evaluate("global _start")
	evaluate("_start:")
	evaluate("")

	if MMIO:
		evaluate("extern open")
		evaluate("extern lseek")
		evaluate("extern write")
		evaluate("extern mmap")
		evaluate("")
		evaluate("sub esp, 20h")
		evaluate("")
		evaluate(" fdin = open (\"/dev/stdin\", O_RDONLY)")
		evaluate("mov dword [esp], ssi")
		evaluate("mov dword [esp+4], 0  O_RDONLY")
		evaluate("call open")
		evaluate("mov [fdi], eax")
		evaluate("")
		evaluate(" fdevaluate = open (\"/dev/stdevaluate\", O_RDWR)")
		evaluate("mov dword [esp], sso")
		evaluate("mov dword [esp+4], 2  O_RDWR")
		evaluate("call open")
		evaluate("mov [fdo], eax")
		evaluate("")
		evaluate(" lseek (fdevaluate, MMIO_SIZE - 1, SEEK_SET)")
		evaluate("mov eax, [fdo]")
		evaluate("mov [esp], eax")
		evaluate("mov dword [esp+4], MMIO_SIZE-1")
		evaluate("mov dword [esp+8], 0  SEEK_SET")
		evaluate("call lseek")
		evaluate("")
		evaluate(" write (fdevaluate, "", 1)")
		evaluate("mov eax, [fdo]")
		evaluate("mov [esp], eax")
		evaluate("mov dword [esp+4], zzz")
		evaluate("mov dword [esp+8], 1")
		evaluate("call write")
		evaluate("")
		evaluate(" src = mmap (0, MMIO_SIZE, PROT_READ, MAP_SHARED, fdin, 0)")
		evaluate("mov eax, [fdi]")
		evaluate("mov dword [esp], 0")
		evaluate("mov dword [esp+4], MMIO_SIZE")
		evaluate("mov dword [esp+8], 1  PROT_READ")
		evaluate("mov dword [esp+12], 1  MAP_SHARED")
		evaluate("mov dword [esp+16], eax")
		evaluate("mov dword [esp+20], 0")
		evaluate("call mmap")
		evaluate("mov dword [src], eax")
		evaluate("")
		evaluate(" dst = mmap (0, MMIO_SIZE, PROT_WRITE, MAP_SHARED, fdevaluate, 0)")
		evaluate("mov eax, [fdo]")
		evaluate("mov dword [esp], 0")
		evaluate("mov dword [esp+4], MMIO_SIZE")
		evaluate("mov dword [esp+8], 2  PROT_WRITE")
		evaluate("mov dword [esp+12], 1  MAP_SHARED")
		evaluate("mov dword [esp+16], eax")
		evaluate("mov dword [esp+20], 0")
		evaluate("call mmap")
		evaluate("mov [dst], eax")
		evaluate("")

	if NOJMP:
		evaluate("extern sigaction")
		evaluate("mov dword [esp], 4")      #sigill 
		evaluate("mov dword [esp+4], sa")
		evaluate("mov dword [esp+8], 0")
		evaluate("call sigaction")
		evaluate("")

	if NOJMP:
		evaluate("mov [dsp], esp")
		evaluate("")

	evaluate("loop:")
	evaluate("")

	if NOJMP:
		evaluate("mov esp, [dsp]")
		evaluate("")
	


	c = 0
	next_c = 0
	while c < (len(DATA)+1):
		c = data[next_c]
		next_c = data[c+1]

		if OPT:
			rep=0
			if c == '+' or c == '-' or c == '<' or c == '>':
				while c == next_c:
					next_c = data[next_c+1]
					rep += 1


		if c == '.':
			if MMIO:
				evaluate("mov eax, [on]")
				evaluate("mov eax, [s_dst+eax]")
				evaluate("mov eax, [eax]")
				evaluate("mov edx, [dsi]")
				evaluate("mov ecx, [dp]")
				evaluate("mov cl, [m+ecx]")
				evaluate("mov [eax+edx], cl")
				evaluate("")
				evaluate("mov eax, 0")
				evaluate("mov ax, [incw+2*edx]")
				evaluate("mov edx, [on]")
				evaluate("mov edx, [s_dsi+edx]")
				evaluate("mov [edx], eax")
				
			else:
				evaluate("mov eax, [on]")
				evaluate("mov eax, [s_mz+eax]")
				evaluate("")
				evaluate("mov edx, [dp]")
				evaluate("mov al, [eax+edx]")
				evaluate("mov [c], al")
				evaluate("")
				evaluate("mov eax, 4")
				evaluate("mov ebx, 1")
				evaluate("mov ecx, c")
				evaluate("mov edx, 1")
				evaluate("int 0x80")
				
			evaluate("")
			continue

		if c == ',':
			if MMIO:
				evaluate("mov ecx, 0")
				evaluate("mov eax, [src]")
				evaluate("mov edx, [sri]")
				evaluate("mov cl, [eax+edx]")
				evaluate("mov eax, [on]")
				evaluate("mov eax, [s_ms+eax]")
				evaluate("mov edx, [dp]")
				
				if CELL16:
					evaluate("mov [eax+edx], cx")
				
				else:
					evaluate("mov [eax+edx], cl")
				
				evaluate("")
				evaluate("mov edx, [sri]")
				evaluate("mov eax, 0")
				evaluate("mov ax, [incw+2*edx]")
				evaluate("mov edx, [on]")
				evaluate("mov edx, [s_sri+edx]")
				evaluate("mov [edx], eax")
				
			else:
				evaluate("mov edx, [on]")
				evaluate("mov edx, [trim+edx]")
				evaluate("mov eax, 3")
				evaluate("mov ebx, 0")
				evaluate("mov ecx, c")
				evaluate("int 0x80")
				evaluate("")
				evaluate("mov ecx, 0")
				evaluate("mov eax, [on]")
				evaluate("mov eax, [s_ms+eax]")
				evaluate("mov edx, [dp]")
				evaluate("mov cl, [c]")
	
				if CELL16:
					evaluate("mov [eax+edx], cx")
					
				else:
					evaluate("mov [eax+edx], cl")
					
				
			evaluate("")
			continue

		if c == '+':
			evaluate("mov eax, [on]")
			evaluate("mov ebx, [s_ms+eax]")
			evaluate("mov edx, [dp]")
			evaluate("mov eax, 0")

			if CELL16:
				evaluate("mov ax, [ebx+edx]")
				evaluate("mov ax, [incw+2*eax]")
				if OPT:
					while rep:
						evaluate("mov ax, [incw+2*eax]")
						rep -= 1
						
					
				evaluate("mov [ebx+edx], ax")
				
			else:
				evaluate("mov al, [ebx+edx]")
				evaluate("mov al, [incb+eax]")
				if OPT:
					while rep:
						evaluate("mov al, [incb+eax]")
						rep -= 1
						
					
				evaluate("mov [ebx+edx], al")
				
			evaluate("")
			continue

		if c == '-':
			evaluate("mov eax, [on]")
			evaluate("mov ebx, [s_ms+eax]")
			evaluate("mov edx, [dp]")
			evaluate("mov eax, 0")
			if CELL16:
				evaluate("mov ax, [ebx+edx]")
				evaluate("mov ax, [decw+2*eax]")
				if OPT:
					while rep:
						evaluate("mov ax, [decw+2*eax]")
						rep -= 1
						
				
				evaluate("mov [ebx+edx], ax")
			
			else:
				evaluate("mov al, [ebx+edx]")
				evaluate("mov al, [decb+eax]")
				if OPT:
					while rep:
						evaluate("mov al, [decb+eax]")
						rep -= 1
						
					
				evaluate("mov [ebx+edx], al")
				
			evaluate("")
			continue

		if c == '<':
			evaluate("mov eax, [on]")
			evaluate("mov ebx, [s_dp+eax]")
			evaluate("mov eax, [ebx]")
			evaluate("mov edx, 0")
			evaluate("mov dx, [decw+2*eax]")
			if CELL16:
				evaluate("mov dx, [decw+2*edx]")
				
			if OPT:
				while rep:
					evaluate("mov dx, [decw+2*edx]")
					if CELL16:
						evaluate("mov dx, [decw+2*edx]")
						
					rep -= 1
					
				
			evaluate("mov [ebx], edx")
			evaluate("")
			continue

		if c == '>':
			evaluate("mov eax, [on]")
			evaluate("mov ebx, [s_dp+eax]")
			evaluate("mov eax, [ebx]")
			evaluate("mov edx, 0")
			evaluate("mov dx, [incw+2*eax]")
			if CELL16:
				evaluate("mov dx, [incw+2*edx]")
				
			if OPT:
				while rep:
					evaluate("mov dx, [incw+2*edx]")
					if CELL16:
						evaluate("mov dx, [incw+2*edx]")
						
					rep -= 1
					
				
			evaluate("mov [ebx], edx")
			evaluate("")
			continue

		if c == '#':
			continue

		if c == '@':
			evaluate("mov eax, [on]")
			evaluate("mov eax, [h+eax]")
			evaluate("mov eax, [eax]")
			evaluate("")
			continue

		if c == '[':
			id = next_id
			id_stack[stack_index] = id
			stack_index += 1
			next_id += 1

			evaluate("mov [ot], dword 0")
			evaluate("")
			evaluate("mov eax, [dp]")
			evaluate("mov edx, 0")
				
			if CELL16:
				evaluate("mov dx, [m+eax]")
				
			else:
				evaluate("mov dl, [m+eax]")
				
			evaluate("mov [t], edx")
			evaluate("eq t, t, 0")
			evaluate("")
			evaluate("and b, on, t")
			evaluate("mov eax, [b]")
			evaluate("mov eax, [s_id+eax]")
			evaluate("mov [eax], dword {}".format(id))
			evaluate("")
			evaluate("mov eax, [b]")
			evaluate("mov eax, [s_on+eax]")
			evaluate("mov [eax], dword 0")
			evaluate("")
			evaluate("mov eax, [b]")
			evaluate("mov eax, [s_ot+eax]")
			evaluate("mov [eax], dword 4")
			evaluate("")

			evaluate("not t, on")
			evaluate("eq b, id, {}".format(id))
			evaluate("and b, b, t")
			evaluate("not t, ot")
			evaluate("and b, b, t")
			evaluate("mov eax, [b]")
			evaluate("mov eax, [s_on+eax] ")
			evaluate("mov [eax], dword 4 ")
			evaluate("")
			continue

		if c == ']':
			stack_index -= 1
			id = id_stack[stack_index]

			evaluate("mov [ot], dword 0")
			evaluate("")
			evaluate("mov eax, [dp]")
			evaluate("mov edx, 0")
				
			if CELL16:
				evaluate("mov dx, [m+eax]")
			
			else:
				evaluate("mov dl, [m+eax]")
				
			evaluate("mov [t], edx")
			evaluate("neq t, t, 0")
			evaluate("")
			evaluate("and b, on, t")
			evaluate("mov eax, [b]")
			evaluate("mov eax, [s_id+eax]")
			evaluate("mov [eax], dword {}".format(id))
			evaluate("")
			evaluate("mov eax, [b]")
			evaluate("mov eax, [s_on+eax]")
			evaluate("mov [eax], dword 0")
			evaluate("")
			evaluate("mov eax, [b]")
			evaluate("mov eax, [s_ot+eax]")
			evaluate("mov [eax], dword 4")
			evaluate("")

			evaluate("not t, on")
			evaluate("eq b, id, {}".format(id))
			evaluate("and b, b, t")
			evaluate("not t, ot")
			evaluate("and b, b, t")
			evaluate("mov eax, [b]")
			evaluate("mov eax, [s_on+eax]")
			evaluate("mov [eax], dword 4")
			evaluate("")
			continue
		else:
			continue
		

		c += 1
		next_c += 1
		
	

	x = "mov cs, ax" if NOJMP else "jmp loop"
	evaluate(x)


def parsein():

	global FILEIN, FILEOUT, MMIO, NOJMP, MOV, CELL16, OPT

	parser = argparse.ArgumentParser(description='https://github.com/zadewg/remo')
	parser.add_argument('-if','--infile', help='File to read from.', required=True)
	parser.add_argument('-of','--outfile', help='File to write to.', required=True)
	parser.add_argument('-mmio','--1mmio', help='Use memory mapped I/O.  Allows mov instructions instead of int 0x80 for I/O, but requires I/O streams to be backed by files.', action='store_true')
	parser.add_argument('-nojmp','--nojmp', help='Replace the single jmp instruction with a faulting mov to implement the program loop.', action='store_true')
	parser.add_argument('-mov','--mov', help='Use only mov instructions same as -mmio -nojmp.', action='store_true')
	parser.add_argument('-cell16','--cell16', help='Use 16 bit memory cells.', action='store_true')
	parser.add_argument('-O','--opt', help='Enable optimization.', action='store_true')
	args = vars(parser.parse_args())

	FILEIN = args['infile']
	FILEOUT = args['outfile']
	MMIO = args['mmio']
	NOJMP = args['nojmp']
	MOV = args['mov']
	CELL16 = args['cell16'] 
	OPT = args['opt']


if __name__ ==  "__main__":
	parsein()


	with open(FILEIN, 'r') as infile:
		DATA = infile.read().replace('\n', '')

	fileout = open(FILEOUT, "w")
	def evaluate (data):
		evaluate(data)
		fileout.write(data)

	main(DATA)
	fileout.close
