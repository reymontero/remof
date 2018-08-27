import argparse
import time


print("\n\n")

print(" /$$      /$$  /$$$$$$  /$$    /$$  /$$$$$$  /$$$$$$ /$$$$$$$   /$$$$$$  /$$   /$$  /$$$$$$     ")
print("| $$$    /$$$ /$$__  $$| $$   | $$ /$$__  $$|_  $$_/| $$__  $$ /$$__  $$| $$  | $$ /$$__  $$    ")
print("| $$$$  /$$$$| $$  \ $$| $$   | $$| $$  \__/  | $$  | $$  \ $$| $$  \__/| $$  | $$| $$  \__/    ")
print("| $$ $$/$$ $$| $$  | $$|  $$ / $$/| $$        | $$  | $$$$$$$/| $$      | $$  | $$|  $$$$$$     ")
print("| $$  $$$| $$| $$  | $$ \  $$ $$/ | $$        | $$  | $$__  $$| $$      | $$  | $$ \____  $$    ")
print("| $$\  $ | $$| $$  | $$  \  $$$/  | $$    $$  | $$  | $$  \ $$| $$    $$| $$  | $$ /$$  \ $$    ")
print("| $$ \/  | $$|  $$$$$$/   \  $/   |  $$$$$$/ /$$$$$$| $$  | $$|  $$$$$$/|  $$$$$$/|  $$$$$$/    ")
print("|__/     |__/ \______/     \_/     \______/ |______/|__/  |__/ \______/  \______/  \______/     ")
                                                      
print("\n\ngithub.com/xoreaxeaxeax/movfuscator  :: The single instruction BF compiler   ")
print("github.com/zadewg/remof              :: M/o/Vfuscator Python implementation    \n")
print("chris domas           @xoreaxeaxeax                                              ")
print("mapez                 @zadewg                                                  \n")
print("\n\n")
time.sleep(3)

ID_STACK_SIZE = 8192
BF_DATA_SIZE = (128*1024)
MMIO_SIZE = (128*1024)  # must be <= data_size (could be fixed with more movs) */


def out(string, counter):

	HEX = ''.join([hex(ord(x))[2:] + ' ' for x in string]).ljust(60, ' ')
	print((('0x%0*X' % (8, counter)).lower() + '\t' + HEX + '\t' + string))

	
def main(DATA):

	next_id = 1

	id_stack = [0]*ID_STACK_SIZE
	stack_index = 0 

	counter = 0
	out("MOVfuscator",  counter)
	counter += 1
	out("domas 2015",  counter)
	counter += 1
	out("zadew 2018",  counter)
	counter += 1
	out("",  counter)
	counter += 1
	out("USE32",  counter)
	counter += 1
	out("section .data",  counter)
	counter += 1
	out("",  counter)
	counter += 1
	out("DATA equ {}".format(BF_DATA_SIZE), counter)
	counter += 1
	out("",  counter)
	counter += 1
	out("%macro c_s 1",  counter)
	counter += 1
	out("	%1:   dd 0",  counter)
	counter += 1
	out("	d_%1: dd 0",  counter)
	counter += 1
	out("	s_%1: dd d_%1, %1",  counter)
	counter += 1
	out("%endmacro",  counter)
	counter += 1
	out("",  counter)
	counter += 1
	out("s_ms: dd s, m",  counter)
	counter += 1
	out("s_mz: dd z, m",  counter)
	counter += 1
	out("",  counter)
	counter += 1
	out("b: dd 0",  counter)
	counter += 1
	out("t: dd 0",  counter)
	counter += 1
	out("c: db 0",  counter)
	counter += 1
	out("",  counter)
	counter += 1
	out("c_s dp",  counter)
	counter += 1
	out("",  counter)
	counter += 1
	out("c_s id",  counter)
	counter += 1
	out("c_s ot",  counter)
	counter += 1
	out("",  counter)
	counter += 1
	out("on: dd 4",  counter)
	counter += 1
	out("d_on: dd 0",  counter)
	counter += 1
	out("s_on: dd d_on, on",  counter)
	counter += 1
	out("",  counter)
	counter += 1
	out("o: dd o_0, o_1",  counter)
	counter += 1
	out("o_0: dd 0, 4",  counter)
	counter += 1
	out("o_1: dd 4, 4",  counter)
	counter += 1
	out("",  counter)
	counter += 1
	out("a: dd a_0, a_1",  counter)
	counter += 1
	out("a_0: dd 0, 0",  counter)
	counter += 1
	out("a_1: dd 0, 4",  counter)
	counter += 1
	out("",  counter)
	counter += 1
	out("n: dd 4, 0",  counter)
	counter += 1
	out("",  counter)
	counter += 1
	out("nh: dd 0",  counter)
	counter += 1
	out("h: dd nh, 0",  counter)
	counter += 1
	out("",  counter)
	counter += 1
	out("trim: dd 0",  counter)
	counter += 1
	out("times 255 dd 1",  counter)
	counter += 1
	out("",  counter)
	counter += 1
	out("incb:",  counter)
	counter += 1
	out("%assign y 1",  counter)
	counter += 1
	out("%rep    256",  counter)
	counter += 1
	out("	db y&0xff",  counter)
	counter += 1
	out("	%assign y y+1",  counter)
	counter += 1
	out("%endrep",  counter)
	counter += 1
	out("",  counter)
	counter += 1
	out("decb:",  counter)
	counter += 1
	out("%assign y 256-1",  counter)
	counter += 1
	out("%rep    256",  counter)
	counter += 1
	out("	db y&0xff",  counter)
	counter += 1
	out("	%assign y y+1",  counter)
	counter += 1
	out("%endrep",  counter)
	counter += 1
	out("",  counter)
	counter += 1
	out("incw:",  counter)
	counter += 1
	out("%assign y 1",  counter)
	counter += 1
	out("%rep    256*256",  counter)
	counter += 1
	out("	dw y&0xffff",  counter)
	counter += 1
	out("	%assign y y+1",  counter)
	counter += 1
	out("%endrep",  counter)
	counter += 1
	out("",  counter)
	counter += 1
	out("decw:",  counter)
	counter += 1
	out("%assign y 256*256-1",  counter)
	counter += 1
	out("%rep    256*256",  counter)
	counter += 1
	out("	dw y&0xffff",  counter)
	counter += 1
	out("	%assign y y+1",  counter)
	counter += 1
	out("%endrep",  counter)
	counter += 1
	out("",  counter)
	counter += 1
	out("%macro eq 3",  counter)
	counter += 1
	out("	mov eax, 0",  counter)
	counter += 1
	out("	mov edx, 0",  counter)
	counter += 1
	out("	mov ax, [%2]",  counter)
	counter += 1
	out("	mov byte [e+eax], 0",  counter)
	counter += 1
	out("	mov byte [e+%3], 4",  counter)
	counter += 1
	out("	mov dl, [e+eax]",  counter)
	counter += 1
	out("	mov [%1], edx",  counter)
	counter += 1
	out("%endmacro",  counter)
	counter += 1
	out("",  counter)
	counter += 1
	out("%macro neq 3",  counter)
	counter += 1
	out("	mov eax, 0",  counter)
	counter += 1
	out("	mov edx, 0",  counter)
	counter += 1
	out("	mov ax, [%2]",  counter)
	counter += 1
	out("	mov byte [e+eax], 4",  counter)
	counter += 1
	out("	mov byte [e+%3], 0",  counter)
	counter += 1
	out("	mov dl, [e+eax]",  counter)
	counter += 1
	out("	mov [%1], edx",  counter)
	counter += 1
	out("%endmacro",  counter)
	counter += 1
	out("",  counter)
	counter += 1
	out("%macro or 3",  counter)
	counter += 1
	out("	mov eax, [%2]",  counter)
	counter += 1
	out("	mov edx, [o+eax]",  counter)
	counter += 1
	out("	mov eax, [%3]",  counter)
	counter += 1
	out("	mov eax, [eax+edx]",  counter)
	counter += 1
	out("	mov [%1], eax",  counter)
	counter += 1
	out("%endmacro",  counter)
	counter += 1
	out("",  counter)
	counter += 1
	out("%macro and 3",  counter)
	counter += 1
	out("	mov eax, [%2]",  counter)
	counter += 1
	out("	mov edx, [a+eax]",  counter)
	counter += 1
	out("	mov eax, [%3]",  counter)
	counter += 1
	out("	mov eax, [eax+edx]",  counter)
	counter += 1
	out("	mov [%1], eax",  counter)
	counter += 1
	out("%endmacro",  counter)
	counter += 1
	out("",  counter)
	counter += 1
	out("%macro not 2",  counter)
	counter += 1
	out("	mov eax, [%2]",  counter)
	counter += 1
	out("	mov eax, [n+eax]",  counter)
	counter += 1
	out("	mov [%1], eax",  counter)
	counter += 1
	out("%endmacro",  counter)
	counter += 1
	out("",  counter)
	counter += 1

	if MMIO: 
		out("src: dd 0",  counter)
		counter += 1
		out("d_src: dd s",  counter)
		counter += 1
		out("s_src: dd d_src, src",  counter)
		counter += 1
		out("dst: dd 0",  counter)
		counter += 1
		out("d_dst: dd s",  counter)
		counter += 1
		out("s_dst: dd d_dst, dst",  counter)
		counter += 1
		out("c_s sri",  counter)
		counter += 1
		out("c_s dsi",  counter)
		counter += 1
		out("fdi: dd 0",  counter)
		counter += 1
		out("fdo: dd 0",  counter)
		counter += 1
		out("ssi: db /dev/stdin, 0",  counter)
		counter += 1
		out("sso: db /dev/stdout, 0",  counter)
		counter += 1
		out("zzz: dd 0",  counter)
		counter += 1
		out("MMIO_SIZE equ {}".format(MMIO_SIZE), counter)
		counter += 1
		out("",  counter)
		counter += 1

	if NOJMP:

		out("sa: dd loop",  counter)          # sa_handler 
		counter += 1		
		out("    times 0x20 dd 0",  counter)  # sa_mask 
		counter += 1
		out("    dd 0x40000000",  counter)    # sa_flags - sa_nodefer 
		counter += 1
		out("    dd 0",  counter)             # sa_restorer 
		counter += 1
		out("",  counter)
		counter += 1
		out("dsp: dd 0",  counter)
		counter += 1

	out("section .bss",  counter)
	counter += 1
	out("m: resb DATA",  counter)
	counter += 1
	out("s: resb DATA",  counter)
	counter += 1
	out("z: resb DATA",  counter)
	counter += 1
	out("e: resb 256*256",  counter)
	counter += 1
	out("",  counter)
	counter += 1

	out("section .text",  counter)
	counter += 1
	out("global _start",  counter)
	counter += 1
	out("_start:",  counter)
	counter += 1
	out("",  counter)
	counter += 1

	if MMIO:
		out("extern open",  counter)
		counter += 1
		out("extern lseek",  counter)
		counter += 1
		out("extern write",  counter)
		counter += 1
		out("extern mmap",  counter)
		counter += 1
		out("",  counter)
		counter += 1
		out("sub esp, 20h",  counter)
		counter += 1
		out("",  counter)
		counter += 1
		out(" fdin = open (\"/dev/stdin\", O_RDONLY)",  counter)
		counter += 1
		out("mov dword [esp], ssi",  counter)
		counter += 1
		out("mov dword [esp+4], 0  O_RDONLY",  counter)
		counter += 1
		out("call open",  counter)
		counter += 1
		out("mov [fdi], eax",  counter)
		counter += 1
		out("",  counter)
		counter += 1
		out(" fdout = open (\"/dev/stdout\", O_RDWR)",  counter)
		counter += 1
		out("mov dword [esp], sso",  counter)
		counter += 1
		out("mov dword [esp+4], 2  O_RDWR",  counter)
		counter += 1
		out("call open",  counter)
		counter += 1
		out("mov [fdo], eax",  counter)
		counter += 1
		out("",  counter)
		counter += 1
		out(" lseek (fdout, MMIO_SIZE - 1, SEEK_SET)",  counter)
		counter += 1
		out("mov eax, [fdo]",  counter)
		counter += 1
		out("mov [esp], eax",  counter)
		counter += 1
		out("mov dword [esp+4], MMIO_SIZE-1",  counter)
		counter += 1
		out("mov dword [esp+8], 0  SEEK_SET",  counter)
		counter += 1
		out("call lseek",  counter)
		counter += 1
		out("",  counter)
		counter += 1
		out(" write (fdout, "", 1)",  counter)
		counter += 1
		out("mov eax, [fdo]",  counter)
		counter += 1
		out("mov [esp], eax",  counter)
		counter += 1
		out("mov dword [esp+4], zzz",  counter)
		counter += 1
		out("mov dword [esp+8], 1",  counter)
		counter += 1
		out("call write",  counter)
		counter += 1
		out("",  counter)
		counter += 1
		out(" src = mmap (0, MMIO_SIZE, PROT_READ, MAP_SHARED, fdin, 0)",  counter)
		counter += 1
		out("mov eax, [fdi]",  counter)
		counter += 1
		out("mov dword [esp], 0",  counter)
		counter += 1
		out("mov dword [esp+4], MMIO_SIZE",  counter)
		counter += 1
		out("mov dword [esp+8], 1  PROT_READ",  counter)
		counter += 1
		out("mov dword [esp+12], 1  MAP_SHARED",  counter)
		counter += 1
		out("mov dword [esp+16], eax",  counter)
		counter += 1
		out("mov dword [esp+20], 0",  counter)
		counter += 1
		out("call mmap",  counter)
		counter += 1
		out("mov dword [src], eax",  counter)
		counter += 1
		out("",  counter)
		counter += 1
		out(" dst = mmap (0, MMIO_SIZE, PROT_WRITE, MAP_SHARED, fdout, 0)",  counter)
		counter += 1
		out("mov eax, [fdo]",  counter)
		counter += 1
		out("mov dword [esp], 0",  counter)
		counter += 1
		out("mov dword [esp+4], MMIO_SIZE",  counter)
		counter += 1
		out("mov dword [esp+8], 2  PROT_WRITE",  counter)
		counter += 1
		out("mov dword [esp+12], 1  MAP_SHARED",  counter)
		counter += 1
		out("mov dword [esp+16], eax",  counter)
		counter += 1
		out("mov dword [esp+20], 0",  counter)
		counter += 1
		out("call mmap",  counter)
		counter += 1
		out("mov [dst], eax",  counter)
		counter += 1
		out("",  counter)
		counter += 1

	if NOJMP:
		out("extern sigaction",  counter)
		counter += 1
		out("mov dword [esp], 4",  counter)      #sigill 
		counter += 1
		out("mov dword [esp+4], sa",  counter)
		counter += 1
		out("mov dword [esp+8], 0",  counter)
		counter += 1
		out("call sigaction",  counter)
		counter += 1
		out("",  counter)
		counter += 1

	if NOJMP:
		out("mov [dsp], esp",  counter)
		counter += 1	
		out("",  counter)
		counter += 1

	out("loop:",  counter)
	counter += 1
	out("",  counter)
	counter += 1

	if NOJMP:
		out("mov esp, [dsp]",  counter)
		counter += 1
		out("",  counter)
		counter += 1
	


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
				out("mov eax, [on]",  counter)
				counter += 1
				out("mov eax, [s_dst+eax]",  counter)
				counter += 1
				out("mov eax, [eax]",  counter)
				counter += 1
				out("mov edx, [dsi]",  counter)
				counter += 1
				out("mov ecx, [dp]",  counter)
				counter += 1
				out("mov cl, [m+ecx]",  counter)
				counter += 1
				out("mov [eax+edx], cl",  counter)
				counter += 1
				out("",  counter)
				counter += 1
				out("mov eax, 0",  counter)
				counter += 1
				out("mov ax, [incw+2*edx]",  counter)
				counter += 1
				out("mov edx, [on]",  counter)
				counter += 1
				out("mov edx, [s_dsi+edx]",  counter)
				counter += 1
				out("mov [edx], eax",  counter)
				counter += 1
				
			else:
				out("mov eax, [on]",  counter)
				counter += 1
				out("mov eax, [s_mz+eax]",  counter)
				counter += 1
				out("",  counter)
				counter += 1
				out("mov edx, [dp]",  counter)
				counter += 1
				out("mov al, [eax+edx]",  counter)
				counter += 1
				out("mov [c], al",  counter)
				counter += 1
				out("",  counter)
				counter += 1
				out("mov eax, 4",  counter)
				counter += 1
				out("mov ebx, 1",  counter)
				counter += 1
				out("mov ecx, c",  counter)
				counter += 1
				out("mov edx, 1",  counter)
				counter += 1
				out("int 0x80",  counter)
				counter += 1
				
			out("",  counter)
			counter += 1
			
			continue

		if c == ',':
			if MMIO:
				out("mov ecx, 0",  counter)
				counter += 1
				out("mov eax, [src]",  counter)
				counter += 1
				out("mov edx, [sri]",  counter)
				counter += 1
				out("mov cl, [eax+edx]",  counter)
				counter += 1
				out("mov eax, [on]",  counter)
				counter += 1
				out("mov eax, [s_ms+eax]",  counter)
				counter += 1
				out("mov edx, [dp]",  counter)
				counter += 1
				
				if CELL16:
					out("mov [eax+edx], cx",  counter)
					counter += 1
				
				else:
					out("mov [eax+edx], cl",  counter)
					counter += 1
				
				out("",  counter)
				counter += 1
				out("mov edx, [sri]",  counter)
				counter += 1
				out("mov eax, 0",  counter)
				counter += 1
				out("mov ax, [incw+2*edx]",  counter)
				counter += 1
				out("mov edx, [on]",  counter)
				counter += 1
				out("mov edx, [s_sri+edx]",  counter)
				counter += 1
				out("mov [edx], eax",  counter)
				counter += 1
				
			else:
				out("mov edx, [on]",  counter)
				counter += 1
				out("mov edx, [trim+edx]",  counter)
				counter += 1
				out("mov eax, 3",  counter)
				counter += 1
				out("mov ebx, 0",  counter)
				counter += 1
				out("mov ecx, c",  counter)
				counter += 1
				out("int 0x80",  counter)
				counter += 1
				out("",  counter)
				counter += 1
				out("mov ecx, 0",  counter)
				counter += 1
				out("mov eax, [on]",  counter)
				counter += 1
				out("mov eax, [s_ms+eax]",  counter)
				counter += 1
				out("mov edx, [dp]",  counter)
				counter += 1
				out("mov cl, [c]",  counter)
				counter += 1
	
				if CELL16:
					out("mov [eax+edx], cx",  counter)
					counter += 1
					
				else:
					out("mov [eax+edx], cl",  counter)
					counter += 1
					
				
			out("",  counter)
			counter += 1
			continue

		if c == '+':
			out("mov eax, [on]",  counter)
			counter += 1
			out("mov ebx, [s_ms+eax]",  counter)
			counter += 1		
			out("mov edx, [dp]",  counter)
			counter += 1
			out("mov eax, 0",  counter)
			counter += 1

			if CELL16:
				out("mov ax, [ebx+edx]",  counter)
				counter += 1
				out("mov ax, [incw+2*eax]",  counter)
				counter += 1

				if OPT:
					while rep:
						out("mov ax, [incw+2*eax]",  counter)
						counter += 1
						rep -= 1
						
					
				out("mov [ebx+edx], ax",  counter)
				counter += 1
				
			else:
				out("mov al, [ebx+edx]",  counter)
				counter += 1
				out("mov al, [incb+eax]",  counter)
				counter += 1

				if OPT:
					while rep:
						out("mov al, [incb+eax]",  counter)
						counter += 1
						rep -= 1
						
					
				out("mov [ebx+edx], al",  counter)
				counter += 1
				
			out("",  counter)
			counter += 1

			continue

		if c == '-':
			out("mov eax, [on]",  counter)
			counter += 1
			out("mov ebx, [s_ms+eax]",  counter)
			counter += 1
			out("mov edx, [dp]",  counter)
			counter += 1
			out("mov eax, 0",  counter)
			counter += 1

			if CELL16:
				out("mov ax, [ebx+edx]",  counter)
				counter += 1
				out("mov ax, [decw+2*eax]",  counter)
				counter += 1
				if OPT:
					while rep:
						out("mov ax, [decw+2*eax]",  counter)
						counter += 1
						rep -= 1
						
				
				out("mov [ebx+edx], ax",  counter)
				counter += 1
			
			else:
				out("mov al, [ebx+edx]",  counter)
				counter += 1
				out("mov al, [decb+eax]",  counter)
				counter += 1
				if OPT:
					while rep:
						out("mov al, [decb+eax]",  counter)
						counter += 1
						rep -= 1
						
					
				out("mov [ebx+edx], al",  counter)
				counter += 1
				
			out("",  counter)
			counter += 1
			continue

		if c == '<':
			out("mov eax, [on]",  counter)
			counter += 1
			out("mov ebx, [s_dp+eax]",  counter)
			counter += 1
			out("mov eax, [ebx]",  counter)
			counter += 1
			out("mov edx, 0",  counter)
			counter += 1
			out("mov dx, [decw+2*eax]",  counter)
			counter += 1

			if CELL16:
				out("mov dx, [decw+2*edx]",  counter)
				counter += 1
				
			if OPT:
				while rep:
					out("mov dx, [decw+2*edx]",  counter)
					counter += 1
					if CELL16:
						out("mov dx, [decw+2*edx]",  counter)
						counter += 1
						
					rep -= 1
					
				
			out("mov [ebx], edx",  counter)
			counter += 1
			out("",  counter)
			counter += 1
			continue

		if c == '>':
			out("mov eax, [on]",  counter)
			counter += 1
			out("mov ebx, [s_dp+eax]",  counter)
			counter += 1
			out("mov eax, [ebx]",  counter)
			counter += 1
			out("mov edx, 0",  counter)
			counter += 1
			out("mov dx, [incw+2*eax]",  counter)
			counter += 1

			if CELL16:
				out("mov dx, [incw+2*edx]",  counter)
				counter += 1
				
			if OPT:
				while rep:
					out("mov dx, [incw+2*edx]",  counter)
					counter += 1
					if CELL16:
						out("mov dx, [incw+2*edx]",  counter)
						counter += 1
						
					rep -= 1
					
				
			out("mov [ebx], edx",  counter)
			counter += 1
			out("",  counter)
			counter += 1
			continue

		if c == '#':
			continue

		if c == '@':
			out("mov eax, [on]",  counter)
			counter += 1
			out("mov eax, [h+eax]",  counter)
			counter += 1
			out("mov eax, [eax]",  counter)
			counter += 1
			out("",  counter)
			counter += 1
			continue

		if c == '[':
			id = next_id
			id_stack[stack_index] = id
			stack_index += 1
			next_id += 1

			out("mov [ot], dword 0",  counter)
			counter += 1
			out("",  counter)
			counter += 1
			out("mov eax, [dp]",  counter)
			counter += 1
			out("mov edx, 0",  counter)
			counter += 1
				
			if CELL16:
				out("mov dx, [m+eax]",  counter)
				counter += 1
				
			else:
				out("mov dl, [m+eax]",  counter)				
				counter += 1			
	
			out("mov [t], edx",  counter)
			counter += 1
			out("eq t, t, 0",  counter)
			counter += 1
			out("",  counter)
			counter += 1
			out("and b, on, t",  counter)
			counter += 1
			out("mov eax, [b]",  counter)
			counter += 1
			out("mov eax, [s_id+eax]",  counter)
			counter += 1
			out("mov [eax], dword {}".format(id))
			counter += 1
			out("",  counter)
			counter += 1
			out("mov eax, [b]",  counter)
			counter += 1
			out("mov eax, [s_on+eax]",  counter)
			counter += 1
			out("mov [eax], dword 0",  counter)
			counter += 1
			out("",  counter)
			counter += 1
			out("mov eax, [b]",  counter)
			counter += 1
			out("mov eax, [s_ot+eax]",  counter)
			counter += 1
			out("mov [eax], dword 4",  counter)
			counter += 1
			out("",  counter)
			counter += 1

			out("not t, on",  counter)
			counter += 1
			out("eq b, id, {}".format(id))
			counter += 1
			out("and b, b, t",  counter)
			counter += 1
			out("not t, ot",  counter)
			counter += 1
			out("and b, b, t",  counter)
			counter += 1
			out("mov eax, [b]",  counter)
			counter += 1
			out("mov eax, [s_on+eax] ",  counter)
			counter += 1
			out("mov [eax], dword 4 ",  counter)
			counter += 1
			out("",  counter)
			counter += 1

			continue

		if c == ']':
			stack_index -= 1
			id = id_stack[stack_index]

			out("mov [ot], dword 0",  counter)
			counter += 1
			out("",  counter)
			counter += 1
			out("mov eax, [dp]",  counter)
			counter += 1
			out("mov edx, 0",  counter)
			counter += 1
				
			if CELL16:
				out("mov dx, [m+eax]",  counter)
				counter += 1
			
			else:
				out("mov dl, [m+eax]",  counter)
				counter += 1
				
			out("mov [t], edx",  counter)
			counter += 1
			out("neq t, t, 0",  counter)
			counter += 1
			out("",  counter)
			counter += 1
			out("and b, on, t",  counter)
			counter += 1
			out("mov eax, [b]",  counter)
			counter += 1
			out("mov eax, [s_id+eax]",  counter)
			counter += 1
			out("mov [eax], dword {}".format(id))
			counter += 1
			out("",  counter)
			counter += 1
			out("mov eax, [b]",  counter)
			counter += 1
			out("mov eax, [s_on+eax]",  counter)
			counter += 1
			out("mov [eax], dword 0",  counter)
			counter += 1
			out("",  counter)
			counter += 1
			out("mov eax, [b]",  counter)
			counter += 1
			out("mov eax, [s_ot+eax]",  counter)
			counter += 1
			out("mov [eax], dword 4",  counter)
			counter += 1
			out("",  counter)
			counter += 1

			out("not t, on",  counter)
			counter += 1
			out("eq b, id, {}".format(id))
			counter += 1
			out("and b, b, t",  counter)
			counter += 1
			out("not t, ot",  counter)
			counter += 1
			out("and b, b, t",  counter)
			counter += 1
			out("mov eax, [b]",  counter)
			counter += 1
			out("mov eax, [s_on+eax]",  counter)
			counter += 1
			out("mov [eax], dword 4",  counter)
			counter += 1
			out("",  counter)
			counter += 1

			continue
		else:
			continue
				
	

	x = "mov cs, ax" if NOJMP else "jmp loop"
	out(x, counter)


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
	
	if MOV:
		MMIO = True
		NOJMP = True


if __name__ ==  "__main__":
	parsein()


	with open(FILEIN, 'r') as infile:
		DATA = infile.read().replace('\n', '').replace(' ','')
		
	main(DATA)

