import argparse
#import sys; sys.setrecursionlimit(100000)


banner = """
       ___     ___            ___    ___     ___     ___     ___          ___     ___      
      /\  \   /\  \    ___   /\__\  /\  \   /\__\   /\__\   /\  \        /\  \   /\  \    .
     |::\  \ /::\  \  /\  \ /:/ _/_ \:\  \ /:/ _/_ /:/  /  /::\  \  ___ /::\  \ /::\  \   .
     |:::\  \:/\:\  \ \:\  \:/ /\__\ \:\  \:/ /\  \:/  /  /:/\:\  \/\__\:/\:\  \:/\:\__\  .
   __|:|\:\  \  \:\  \ \:\  \ /:/  /  \:\  \ /::\  \  /  _:/ /::\  \/  //  \:\  \ /:/  /   
  /::::|_\:\__\/ \:\__\ \:\__\:/  / \  \:\__\:/\:\__\/  /\__\:/\:\__\_//__/ \:\__\:/__/___ 
  \:\~~\  \/__/\ /:/  / |:|  |/  /\  \ /:/  // /:/  /\ /:/  //  \/__/ \\  \ /:/  /::::/  / 
   \:\  \  \:\  /:/  / \|:|  |__/\:\  /:/  // /:/  /  /:/  //__/:/\:\  \\  /:/  //~~/~~~~  
    \:\  \  \:\/:/  /\__|:|__|  \ \:\/:/  //_/:/  /:\/:/  /:\  \/__\:\  \\/:/  /:\~~\      .
     \:\__\  \::/  /\::::/__/:\__\ \::/  /  /:/  / \::/  / \:\__\   \:\__\:/  / \:\__\    .
      \/__/   \/__/  ~~~~    \/__/  \/__/   \/__/   \/__/   \/__/    \/__/ __/   \/__/    1
"""
                                                                                           
print("\n\n")
print(banner)
print("\nM/o/Vfuscator1                                                         \n\n")
print("github.com/xoreaxeaxeax/movfuscator  :: the single instruction BF compiler   ")
print("github.com/zadewg/remo               :: M/o/Vfuscator1 Reverse engineering \n")
print("chris domas           @xoreaxeaxeax                                          ")
print("mapez                 @zadewg                                              \n")
print("\n\n\n\n")


ID_STACK_SIZE = 8192
BF_DATA_SIZE = (128*1024)
MMIO_SIZE = (128*1024)  # must be <= data_size (could be fixed with more movs) */


def main(DATA):

	next_id = 1

	id_stack = [0]*ID_STACK_SIZE
	stack_index = 0 
	

	print("MOVfuscator")
	print("domas 2015")
	print("zadew 2018")
	print("")
	print("USE32")
	print("section .data")
	print("")
	print("DATA equ {}".format(BF_DATA_SIZE))
	print("")
	print("%macro c_s 1")
	print("	%1:   dd 0")
	print("	d_%1: dd 0")
	print("	s_%1: dd d_%1, %1")
	print("%endmacro")
	print("")
	print("s_ms: dd s, m")
	print("s_mz: dd z, m")
	print("")
	print("b: dd 0")
	print("t: dd 0")
	print("c: db 0")
	print("")
	print("c_s dp")
	print("")
	print("c_s id")
	print("c_s ot")
	print("")
	print("on: dd 4")
	print("d_on: dd 0")
	print("s_on: dd d_on, on")
	print("")
	print("o: dd o_0, o_1")
	print("o_0: dd 0, 4")
	print("o_1: dd 4, 4")
	print("")
	print("a: dd a_0, a_1")
	print("a_0: dd 0, 0")
	print("a_1: dd 0, 4")
	print("")
	print("n: dd 4, 0")
	print("")
	print("nh: dd 0")
	print("h: dd nh, 0")
	print("")
	print("trim: dd 0")
	print("times 255 dd 1")
	print("")
	print("incb:")
	print("%assign y 1")
	print("%rep    256")
	print("	db y&0xff")
	print("	%assign y y+1")
	print("%endrep")
	print("")
	print("decb:")
	print("%assign y 256-1")
	print("%rep    256")
	print("	db y&0xff")
	print("	%assign y y+1")
	print("%endrep")
	print("")
	print("incw:")
	print("%assign y 1")
	print("%rep    256*256")
	print("	dw y&0xffff")
	print("	%assign y y+1")
	print("%endrep")
	print("")
	print("decw:")
	print("%assign y 256*256-1")
	print("%rep    256*256")
	print("	dw y&0xffff")
	print("	%assign y y+1")
	print("%endrep")
	print("")
	print("%macro eq 3")
	print("	mov eax, 0")
	print("	mov edx, 0")
	print("	mov ax, [%2]")
	print("	mov byte [e+eax], 0")
	print("	mov byte [e+%3], 4")
	print("	mov dl, [e+eax]")
	print("	mov [%1], edx")
	print("%endmacro")
	print("")
	print("%macro neq 3")
	print("	mov eax, 0")
	print("	mov edx, 0")
	print("	mov ax, [%2]")
	print("	mov byte [e+eax], 4")
	print("	mov byte [e+%3], 0")
	print("	mov dl, [e+eax]")
	print("	mov [%1], edx")
	print("%endmacro")
	print("")
	print("%macro or 3")
	print("	mov eax, [%2]")
	print("	mov edx, [o+eax]")
	print("	mov eax, [%3]")
	print("	mov eax, [eax+edx]")
	print("	mov [%1], eax")
	print("%endmacro")
	print("")
	print("%macro and 3")
	print("	mov eax, [%2]")
	print("	mov edx, [a+eax]")
	print("	mov eax, [%3]")
	print("	mov eax, [eax+edx]")
	print("	mov [%1], eax")
	print("%endmacro")
	print("")
	print("%macro not 2")
	print("	mov eax, [%2]")
	print("	mov eax, [n+eax]")
	print("	mov [%1], eax")
	print("%endmacro")
	print("")

	if MMIO: 
		print("src: dd 0")
		print("d_src: dd s")
		print("s_src: dd d_src, src")
		print("dst: dd 0")
		print("d_dst: dd s")
		print("s_dst: dd d_dst, dst")
		print("c_s sri")
		print("c_s dsi")
		print("fdi: dd 0")
		print("fdo: dd 0")
		print("ssi: db /dev/stdin, 0")
		print("sso: db /dev/stdout, 0")
		print("zzz: dd 0")
		print("MMIO_SIZE equ {}".format(MMIO_SIZE))
		print("")

	if NOJMP:

		print("sa: dd loop")          # sa_handler 
		print("    times 0x20 dd 0")  # sa_mask 
		print("    dd 0x40000000")    # sa_flags - sa_nodefer 
		print("    dd 0")             # sa_restorer 
		print("")
		print("dsp: dd 0")

	print("section .bss")
	print("m: resb DATA")
	print("s: resb DATA")
	print("z: resb DATA")
	print("e: resb 256*256")
	print("")

	print("section .text")
	print("global _start")
	print("_start:")
	print("")

	if MMIO:
		print("extern open")
		print("extern lseek")
		print("extern write")
		print("extern mmap")
		print("")
		print("sub esp, 20h")
		print("")
		print(" fdin = open (\"/dev/stdin\", O_RDONLY)")
		print("mov dword [esp], ssi")
		print("mov dword [esp+4], 0  O_RDONLY")
		print("call open")
		print("mov [fdi], eax")
		print("")
		print(" fdprint = open (\"/dev/stdprint\", O_RDWR)")
		print("mov dword [esp], sso")
		print("mov dword [esp+4], 2  O_RDWR")
		print("call open")
		print("mov [fdo], eax")
		print("")
		print(" lseek (fdprint, MMIO_SIZE - 1, SEEK_SET)")
		print("mov eax, [fdo]")
		print("mov [esp], eax")
		print("mov dword [esp+4], MMIO_SIZE-1")
		print("mov dword [esp+8], 0  SEEK_SET")
		print("call lseek")
		print("")
		print(" write (fdprint, "", 1)")
		print("mov eax, [fdo]")
		print("mov [esp], eax")
		print("mov dword [esp+4], zzz")
		print("mov dword [esp+8], 1")
		print("call write")
		print("")
		print(" src = mmap (0, MMIO_SIZE, PROT_READ, MAP_SHARED, fdin, 0)")
		print("mov eax, [fdi]")
		print("mov dword [esp], 0")
		print("mov dword [esp+4], MMIO_SIZE")
		print("mov dword [esp+8], 1  PROT_READ")
		print("mov dword [esp+12], 1  MAP_SHARED")
		print("mov dword [esp+16], eax")
		print("mov dword [esp+20], 0")
		print("call mmap")
		print("mov dword [src], eax")
		print("")
		print(" dst = mmap (0, MMIO_SIZE, PROT_WRITE, MAP_SHARED, fdprint, 0)")
		print("mov eax, [fdo]")
		print("mov dword [esp], 0")
		print("mov dword [esp+4], MMIO_SIZE")
		print("mov dword [esp+8], 2  PROT_WRITE")
		print("mov dword [esp+12], 1  MAP_SHARED")
		print("mov dword [esp+16], eax")
		print("mov dword [esp+20], 0")
		print("call mmap")
		print("mov [dst], eax")
		print("")

	if NOJMP:
		print("extern sigaction")
		print("mov dword [esp], 4")      #sigill 
		print("mov dword [esp+4], sa")
		print("mov dword [esp+8], 0")
		print("call sigaction")
		print("")

	if NOJMP:
		print("mov [dsp], esp")
		print("")

	print("loop:")
	print("")

	if NOJMP:
		print("mov esp, [dsp]")
		print("")
	


	i = 0
	while i < (len(DATA)):
		c = DATA[i]
		next_c = i + 1

		if OPT:
			rep=0
			if c == '+' or c == '-' or c == '<' or c == '>':
				try:
					while c == DATA[next_c]:
						next_c +=1
						rep += 1
				except:
					pass

		i += 1
		next_c += 1

		if c == '.':
			if MMIO:
				print("mov eax, [on]")
				print("mov eax, [s_dst+eax]")
				print("mov eax, [eax]")
				print("mov edx, [dsi]")
				print("mov ecx, [dp]")
				print("mov cl, [m+ecx]")
				print("mov [eax+edx], cl")
				print("")
				print("mov eax, 0")
				print("mov ax, [incw+2*edx]")
				print("mov edx, [on]")
				print("mov edx, [s_dsi+edx]")
				print("mov [edx], eax")
				
			else:
				print("mov eax, [on]")
				print("mov eax, [s_mz+eax]")
				print("")
				print("mov edx, [dp]")
				print("mov al, [eax+edx]")
				print("mov [c], al")
				print("")
				print("mov eax, 4")
				print("mov ebx, 1")
				print("mov ecx, c")
				print("mov edx, 1")
				print("int 0x80")
				
			print("")
			continue

		if c == ',':
			if MMIO:
				print("mov ecx, 0")
				print("mov eax, [src]")
				print("mov edx, [sri]")
				print("mov cl, [eax+edx]")
				print("mov eax, [on]")
				print("mov eax, [s_ms+eax]")
				print("mov edx, [dp]")
				
				if CELL16:
					print("mov [eax+edx], cx")
				
				else:
					print("mov [eax+edx], cl")
				
				print("")
				print("mov edx, [sri]")
				print("mov eax, 0")
				print("mov ax, [incw+2*edx]")
				print("mov edx, [on]")
				print("mov edx, [s_sri+edx]")
				print("mov [edx], eax")
				
			else:
				print("mov edx, [on]")
				print("mov edx, [trim+edx]")
				print("mov eax, 3")
				print("mov ebx, 0")
				print("mov ecx, c")
				print("int 0x80")
				print("")
				print("mov ecx, 0")
				print("mov eax, [on]")
				print("mov eax, [s_ms+eax]")
				print("mov edx, [dp]")
				print("mov cl, [c]")
	
				if CELL16:
					print("mov [eax+edx], cx")
					
				else:
					print("mov [eax+edx], cl")
					
				
			print("")
			continue

		if c == '+':
			print("mov eax, [on]")
			print("mov ebx, [s_ms+eax]")
			print("mov edx, [dp]")
			print("mov eax, 0")

			if CELL16:
				print("mov ax, [ebx+edx]")
				print("mov ax, [incw+2*eax]")
				if OPT:
					while rep:
						print("mov ax, [incw+2*eax]")
						rep -= 1
						
					
				print("mov [ebx+edx], ax")
				
			else:
				print("mov al, [ebx+edx]")
				print("mov al, [incb+eax]")
				if OPT:
					while rep:
						print("mov al, [incb+eax]")
						rep -= 1
						
					
				print("mov [ebx+edx], al")
				
			print("")
			continue

		if c == '-':
			print("mov eax, [on]")
			print("mov ebx, [s_ms+eax]")
			print("mov edx, [dp]")
			print("mov eax, 0")
			if CELL16:
				print("mov ax, [ebx+edx]")
				print("mov ax, [decw+2*eax]")
				if OPT:
					while rep:
						print("mov ax, [decw+2*eax]")
						rep -= 1
						
				
				print("mov [ebx+edx], ax")
			
			else:
				print("mov al, [ebx+edx]")
				print("mov al, [decb+eax]")
				if OPT:
					while rep:
						print("mov al, [decb+eax]")
						rep -= 1
						
					
				print("mov [ebx+edx], al")
				
			print("")
			continue

		if c == '<':
			print("mov eax, [on]")
			print("mov ebx, [s_dp+eax]")
			print("mov eax, [ebx]")
			print("mov edx, 0")
			print("mov dx, [decw+2*eax]")
			if CELL16:
				print("mov dx, [decw+2*edx]")
				
			if OPT:
				while rep:
					print("mov dx, [decw+2*edx]")
					if CELL16:
						print("mov dx, [decw+2*edx]")
						
					rep -= 1
					
				
			print("mov [ebx], edx")
			print("")
			continue

		if c == '>':
			print("mov eax, [on]")
			print("mov ebx, [s_dp+eax]")
			print("mov eax, [ebx]")
			print("mov edx, 0")
			print("mov dx, [incw+2*eax]")
			if CELL16:
				print("mov dx, [incw+2*edx]")
				
			if OPT:
				while rep:
					print("mov dx, [incw+2*edx]")
					if CELL16:
						print("mov dx, [incw+2*edx]")
						
					rep -= 1
					
				
			print("mov [ebx], edx")
			print("")
			continue

		if c == '#':
			continue

		if c == '@':
			print("mov eax, [on]")
			print("mov eax, [h+eax]")
			print("mov eax, [eax]")
			print("")
			continue

		if c == '[':
			id = next_id
			id_stack[stack_index] = id
			stack_index += 1
			next_id += 1

			print("mov [ot], dword 0")
			print("")
			print("mov eax, [dp]")
			print("mov edx, 0")
				
			if CELL16:
				print("mov dx, [m+eax]")
				
			else:
				print("mov dl, [m+eax]")
				
			print("mov [t], edx")
			print("eq t, t, 0")
			print("")
			print("and b, on, t")
			print("mov eax, [b]")
			print("mov eax, [s_id+eax]")
			print("mov [eax], dword {}".format(id))
			print("")
			print("mov eax, [b]")
			print("mov eax, [s_on+eax]")
			print("mov [eax], dword 0")
			print("")
			print("mov eax, [b]")
			print("mov eax, [s_ot+eax]")
			print("mov [eax], dword 4")
			print("")

			print("not t, on")
			print("eq b, id, {}".format(id))
			print("and b, b, t")
			print("not t, ot")
			print("and b, b, t")
			print("mov eax, [b]")
			print("mov eax, [s_on+eax] ")
			print("mov [eax], dword 4 ")
			print("")
			continue

		if c == ']':
			stack_index -= 1
			id = id_stack[stack_index]

			print("mov [ot], dword 0")
			print("")
			print("mov eax, [dp]")
			print("mov edx, 0")
				
			if CELL16:
				print("mov dx, [m+eax]")
			
			else:
				print("mov dl, [m+eax]")
				
			print("mov [t], edx")
			print("neq t, t, 0")
			print("")
			print("and b, on, t")
			print("mov eax, [b]")
			print("mov eax, [s_id+eax]")
			print("mov [eax], dword {}".format(id))
			print("")
			print("mov eax, [b]")
			print("mov eax, [s_on+eax]")
			print("mov [eax], dword 0")
			print("")
			print("mov eax, [b]")
			print("mov eax, [s_ot+eax]")
			print("mov [eax], dword 4")
			print("")

			print("not t, on")
			print("eq b, id, {}".format(id))
			print("and b, b, t")
			print("not t, ot")
			print("and b, b, t")
			print("mov eax, [b]")
			print("mov eax, [s_on+eax]")
			print("mov [eax], dword 4")
			print("")
			continue
		else:
			continue
				
	

	x = "mov cs, ax" if NOJMP else "jmp loop"
	print(x)


def parsein():

	global FILEIN, MMIO, NOJMP, MOV, CELL16, OPT

	parser = argparse.ArgumentParser(description='https://github.com/zadewg/remo')
	parser.add_argument('-if','--infile', help='File to read from.', required=True)
	parser.add_argument('-mmio','--mmio', help='Use memory mapped I/O.  Allows mov instructions instead of int 0x80 for I/O, but requires I/O streams to be backed by files.', action='store_true')
	parser.add_argument('-nojmp','--nojmp', help='Replace the single jmp instruction with a faulting mov to implement the program loop.', action='store_true')
	parser.add_argument('-mov','--mov', help='Use only mov instructions same as -mmio -nojmp.', action='store_true')
	parser.add_argument('-cell16','--cell16', help='Use 16 bit memory cells.', action='store_true')
	parser.add_argument('-O','--opt', help='Enable optimization.', action='store_true')
	args = vars(parser.parse_args())

	FILEIN = args['infile']
	MMIO = args['mmio']
	NOJMP = args['nojmp']
	MOV = args['mov']
	CELL16 = args['cell16'] 
	OPT = args['opt']


if __name__ ==  "__main__":
	parsein()


	with open(FILEIN, 'r') as infile:
		DATA = infile.read().replace('\n', '')

	main(DATA)
