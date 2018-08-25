
intro = {
	'std' : '''
	#blank
	USE32
	section .data
	#blank
	DATA equ {}".format(BF_DATA_SIZE))
	#blank
	%macro c_s 1
		%1:   dd 0
		d_%1: dd 0
		s_%1: dd d_%1, %1
	%endmacro
	#blank
	s_ms: dd s, m
	s_mz: dd z, m
	#blank
	b: dd 0
	t: dd 0
	c: db 0
	#blank
	c_s dp
	#blank
	c_s id
	c_s ot
	#blank
	on: dd 4
	d_on: dd 0
	s_on: dd d_on, on
	#blank
	o: dd o_0, o_1
	o_0: dd 0, 4
	o_1: dd 4, 4
	#blank
	a: dd a_0, a_1
	a_0: dd 0, 0
	a_1: dd 0, 4
	#blank
	n: dd 4, 0
	#blank
	nh: dd 0
	h: dd nh, 0
	#blank
	trim: dd 0
	times 255 dd 1
	#blank
	incb:
	%assign y 1
	%rep    256
		db y&0xff
		%assign y y+1
	%endrep
	#blank
	decb:
	%assign y 256-1
	%rep    256
		db y&0xff
		%assign y y+1
	%endrep
	#blank
	incw:
	%assign y 1
	%rep    256*256
		dw y&0xffff
		%assign y y+1
	%endrep
	#blank
	decw:
	%assign y 256*256-1
	%rep    256*256
		dw y&0xffff
		%assign y y+1
	%endrep
	#blank
	%macro eq 3
		mov eax, 0
		mov edx, 0
		mov ax, [%2]
		mov byte [e+eax], 0
		mov byte [e+%3], 4
		mov dl, [e+eax]
		mov [%1], edx
	%endmacro
	#blank
	%macro neq 3
		mov eax, 0
		mov edx, 0
		mov ax, [%2]
		mov byte [e+eax], 4
		mov byte [e+%3], 0
		mov dl, [e+eax]
		mov [%1], edx
	%endmacro
	#blank
	%macro or 3
		mov eax, [%2]
		mov edx, [o+eax]
		mov eax, [%3]
		mov eax, [eax+edx]
		mov [%1], eax
	%endmacro
	#blank
	%macro and 3
		mov eax, [%2]
		mov edx, [a+eax]
		mov eax, [%3]
		mov eax, [eax+edx]
		mov [%1], eax
	%endmacro
	#blank
	%macro not 2
		mov eax, [%2]
		mov eax, [n+eax]
		mov [%1], eax
	%endmacro
	#blank
	section .bss
	m: resb DATA
	s: resb DATA
	z: resb DATA
	e: resb 256*256
	#blank

	section .text
	global _start
	_start:
	#blank
	loop:
	#blank
	''',





	'nojmp' : '''
	#blank
	USE32
	section .data
	#blank
	DATA equ {}".format(BF_DATA_SIZE))
	#blank
	%macro c_s 1
		%1:   dd 0
		d_%1: dd 0
		s_%1: dd d_%1, %1
	%endmacro
	#blank
	s_ms: dd s, m
	s_mz: dd z, m
	#blank
	b: dd 0
	t: dd 0
	c: db 0
	#blank
	c_s dp
	#blank
	c_s id
	c_s ot
	#blank
	on: dd 4
	d_on: dd 0
	s_on: dd d_on, on
	#blank
	o: dd o_0, o_1
	o_0: dd 0, 4
	o_1: dd 4, 4
	#blank
	a: dd a_0, a_1
	a_0: dd 0, 0
	a_1: dd 0, 4
	#blank
	n: dd 4, 0
	#blank
	nh: dd 0
	h: dd nh, 0
	#blank
	trim: dd 0
	times 255 dd 1
	#blank
	incb:
	%assign y 1
	%rep    256
		db y&0xff
		%assign y y+1
	%endrep
	#blank
	decb:
	%assign y 256-1
	%rep    256
		db y&0xff
		%assign y y+1
	%endrep
	#blank
	incw:
	%assign y 1
	%rep    256*256
		dw y&0xffff
		%assign y y+1
	%endrep
	#blank
	decw:
	%assign y 256*256-1
	%rep    256*256
		dw y&0xffff
		%assign y y+1
	%endrep
	#blank
	%macro eq 3
		mov eax, 0
		mov edx, 0
		mov ax, [%2]
		mov byte [e+eax], 0
		mov byte [e+%3], 4
		mov dl, [e+eax]
		mov [%1], edx
	%endmacro
	#blank
	%macro neq 3
		mov eax, 0
		mov edx, 0
		mov ax, [%2]
		mov byte [e+eax], 4
		mov byte [e+%3], 0
		mov dl, [e+eax]
		mov [%1], edx
	%endmacro
	#blank
	%macro or 3
		mov eax, [%2]
		mov edx, [o+eax]
		mov eax, [%3]
		mov eax, [eax+edx]
		mov [%1], eax
	%endmacro
	#blank
	%macro and 3
		mov eax, [%2]
		mov edx, [a+eax]
		mov eax, [%3]
		mov eax, [eax+edx]
		mov [%1], eax
	%endmacro
	#blank
	%macro not 2
		mov eax, [%2]
		mov eax, [n+eax]
		mov [%1], eax
	%endmacro
	#blank
	sa: dd loop          
		times 0x20 dd 0  
		dd 0x40000000    
		dd 0             
	#blank	
	dsp: dd 0
	section .bss
	m: resb DATA
	s: resb DATA
	z: resb DATA
	e: resb 256*256
	#blank
	section .text
	global _start
	_start:
	#blank
	extern sigaction
	mov dword [esp], 4      
	mov dword [esp+4], sa
	mov dword [esp+8], 0
	call sigaction
	#blank
	mov [dsp], esp
	#blank
	loop:
	#blank
	mov esp, [dsp]
	#blank
	''',




	'mmio' : '''
	#blank
	USE32
	section .data
	#blank
	DATA equ {}".format(BF_DATA_SIZE))
	#blank
	%macro c_s 1
		%1:   dd 0
		d_%1: dd 0
		s_%1: dd d_%1, %1
	%endmacro
	#blank
	s_ms: dd s, m
	s_mz: dd z, m
	#blank
	b: dd 0
	t: dd 0
	c: db 0
	#blank
	c_s dp
	#blank
	c_s id
	c_s ot
	#blank
	on: dd 4
	d_on: dd 0
	s_on: dd d_on, on
	#blank
	o: dd o_0, o_1
	o_0: dd 0, 4
	o_1: dd 4, 4
	#blank
	a: dd a_0, a_1
	a_0: dd 0, 0
	a_1: dd 0, 4
	#blank
	n: dd 4, 0
	#blank
	nh: dd 0
	h: dd nh, 0
	#blank
	trim: dd 0
	times 255 dd 1
	#blank
	incb:
	%assign y 1
	%rep    256
		db y&0xff
		%assign y y+1
	%endrep
	#blank
	decb:
	%assign y 256-1
	%rep    256
		db y&0xff
		%assign y y+1
	%endrep
	#blank
	incw:
	%assign y 1
	%rep    256*256
		dw y&0xffff
		%assign y y+1
	%endrep
	#blank
	decw:
	%assign y 256*256-1
	%rep    256*256
		dw y&0xffff
		%assign y y+1
	%endrep
	#blank
	%macro eq 3
		mov eax, 0
		mov edx, 0
		mov ax, [%2]
		mov byte [e+eax], 0
		mov byte [e+%3], 4
		mov dl, [e+eax]
		mov [%1], edx
	%endmacro
	#blank
	%macro neq 3
		mov eax, 0
		mov edx, 0
		mov ax, [%2]
		mov byte [e+eax], 4
		mov byte [e+%3], 0
		mov dl, [e+eax]
		mov [%1], edx
	%endmacro
	#blank
	%macro or 3
		mov eax, [%2]
		mov edx, [o+eax]
		mov eax, [%3]
		mov eax, [eax+edx]
		mov [%1], eax
	%endmacro
	#blank
	%macro and 3
		mov eax, [%2]
		mov edx, [a+eax]
		mov eax, [%3]
		mov eax, [eax+edx]
		mov [%1], eax
	%endmacro
	#blank
	%macro not 2
		mov eax, [%2]
		mov eax, [n+eax]
		mov [%1], eax
	%endmacro
	#blank
	src: dd 0
	d_src: dd s
	s_src: dd d_src, src
	dst: dd 0
	d_dst: dd s
	s_dst: dd d_dst, dst
	c_s sri
	c_s dsi
	fdi: dd 0
	fdo: dd 0
	ssi: db /dev/stdin, 0
	sso: db /dev/stdout, 0
	zzz: dd 0
	MMIO_SIZE equ {}".format(MMIO_SIZE))
	#blank	
	section .bss
	m: resb DATA
	s: resb DATA
	z: resb DATA
	e: resb 256*256
	#blank
	section .text
	global _start
	_start:
	#blank
	extern open
	extern lseek
	extern write
	extern mmap
	#blank
	sub esp, 20h
	#blank
	 fdin = open (\"/dev/stdin\", O_RDONLY)
	mov dword [esp], ssi
	mov dword [esp+4], 0  O_RDONLY
	call open
	mov [fdi], eax
	#blank
	 fdprint = open (\"/dev/stdprint\", O_RDWR)
	mov dword [esp], sso
	mov dword [esp+4], 2  O_RDWR
	call open
	mov [fdo], eax
	#blank
	 lseek (fdprint, MMIO_SIZE - 1, SEEK_SET)
	mov eax, [fdo]
	mov [esp], eax
	mov dword [esp+4], MMIO_SIZE-1
	mov dword [esp+8], 0  SEEK_SET
	call lseek
	#blank
	 write (fdprint, "", 1)
	mov eax, [fdo]
	mov [esp], eax
	mov dword [esp+4], zzz
	mov dword [esp+8], 1
	call write
	#blank
	 src = mmap (0, MMIO_SIZE, PROT_READ, MAP_SHARED, fdin, 0)
	mov eax, [fdi]
	mov dword [esp], 0
	mov dword [esp+4], MMIO_SIZE
	mov dword [esp+8], 1  PROT_READ
	mov dword [esp+12], 1  MAP_SHARED
	mov dword [esp+16], eax
	mov dword [esp+20], 0
	call mmap
	mov dword [src], eax
	#blank
	 dst = mmap (0, MMIO_SIZE, PROT_WRITE, MAP_SHARED, fdprint, 0)
	mov eax, [fdo]
	mov dword [esp], 0
	mov dword [esp+4], MMIO_SIZE
	mov dword [esp+8], 2  PROT_WRITE
	mov dword [esp+12], 1  MAP_SHARED
	mov dword [esp+16], eax
	mov dword [esp+20], 0
	call mmap
	mov [dst], eax
	#blank
	loop:
	#blank
	''',





	'mmjmp' : '''
	#blank
	USE32
	section .data
	#blank
	DATA equ {}".format(BF_DATA_SIZE))
	#blank
	%macro c_s 1
		%1:   dd 0
		d_%1: dd 0
		s_%1: dd d_%1, %1
	%endmacro
	#blank
	s_ms: dd s, m
	s_mz: dd z, m
	#blank
	b: dd 0
	t: dd 0
	c: db 0
	#blank
	c_s dp
	#blank
	c_s id
	c_s ot
	#blank
	on: dd 4
	d_on: dd 0
	s_on: dd d_on, on
	#blank
	o: dd o_0, o_1
	o_0: dd 0, 4
	o_1: dd 4, 4
	#blank
	a: dd a_0, a_1
	a_0: dd 0, 0
	a_1: dd 0, 4
	#blank
	n: dd 4, 0
	#blank
	nh: dd 0
	h: dd nh, 0
	#blank
	trim: dd 0
	times 255 dd 1
	#blank
	incb:
	%assign y 1
	%rep    256
		db y&0xff
		%assign y y+1
	%endrep
	#blank
	decb:
	%assign y 256-1
	%rep    256
		db y&0xff
		%assign y y+1
	%endrep
	#blank
	incw:
	%assign y 1
	%rep    256*256
		dw y&0xffff
		%assign y y+1
	%endrep
	#blank
	decw:
	%assign y 256*256-1
	%rep    256*256
		dw y&0xffff
		%assign y y+1
	%endrep
	#blank
	%macro eq 3
		mov eax, 0
		mov edx, 0
		mov ax, [%2]
		mov byte [e+eax], 0
		mov byte [e+%3], 4
		mov dl, [e+eax]
		mov [%1], edx
	%endmacro
	#blank
	%macro neq 3
		mov eax, 0
		mov edx, 0
		mov ax, [%2]
		mov byte [e+eax], 4
		mov byte [e+%3], 0
		mov dl, [e+eax]
		mov [%1], edx
	%endmacro
	#blank
	%macro or 3
		mov eax, [%2]
		mov edx, [o+eax]
		mov eax, [%3]
		mov eax, [eax+edx]
		mov [%1], eax
	%endmacro
	#blank
	%macro and 3
		mov eax, [%2]
		mov edx, [a+eax]
		mov eax, [%3]
		mov eax, [eax+edx]
		mov [%1], eax
	%endmacro
	#blank
	%macro not 2
		mov eax, [%2]
		mov eax, [n+eax]
		mov [%1], eax
	%endmacro
	#blank
	src: dd 0
	d_src: dd s
	s_src: dd d_src, src
	dst: dd 0
	d_dst: dd s
	s_dst: dd d_dst, dst
	c_s sri
	c_s dsi
	fdi: dd 0
	fdo: dd 0
	ssi: db /dev/stdin, 0
	sso: db /dev/stdout, 0
	zzz: dd 0
	MMIO_SIZE equ {}".format(MMIO_SIZE))	
	#blank
	sa: dd loop          
	    times 0x20 dd 0  
	    dd 0x40000000    
	    dd 0           
	#blank
	dsp: dd 0
	section .bss
	m: resb DATA
	s: resb DATA
	z: resb DATA
	e: resb 256*256
	#blank
	section .text
	global _start
	_start:
	#blank
	extern open
	extern lseek
	extern write
	extern mmap
	#blank
	sub esp, 20h
	#blank
	 fdin = open (\"/dev/stdin\", O_RDONLY)
	mov dword [esp], ssi
	mov dword [esp+4], 0  O_RDONLY
	call open
	mov [fdi], eax
	#blank
	 fdprint = open (\"/dev/stdprint\", O_RDWR)
	mov dword [esp], sso
	mov dword [esp+4], 2  O_RDWR
	call open
	mov [fdo], eax
	#blank
	 lseek (fdprint, MMIO_SIZE - 1, SEEK_SET)
	mov eax, [fdo]
	mov [esp], eax
	mov dword [esp+4], MMIO_SIZE-1
	mov dword [esp+8], 0  SEEK_SET
	call lseek
	#blank
	 write (fdprint, "", 1)
	mov eax, [fdo]
	mov [esp], eax
	mov dword [esp+4], zzz
	mov dword [esp+8], 1
	call write
	#blank
	 src = mmap (0, MMIO_SIZE, PROT_READ, MAP_SHARED, fdin, 0)
	mov eax, [fdi]
	mov dword [esp], 0
	mov dword [esp+4], MMIO_SIZE
	mov dword [esp+8], 1  PROT_READ
	mov dword [esp+12], 1  MAP_SHARED
	mov dword [esp+16], eax
	mov dword [esp+20], 0
	call mmap
	mov dword [src], eax
	#blank
	 dst = mmap (0, MMIO_SIZE, PROT_WRITE, MAP_SHARED, fdprint, 0)
	mov eax, [fdo]
	mov dword [esp], 0
	mov dword [esp+4], MMIO_SIZE
	mov dword [esp+8], 2  PROT_WRITE
	mov dword [esp+12], 1  MAP_SHARED
	mov dword [esp+16], eax
	mov dword [esp+20], 0
	call mmap
	mov [dst], eax
	#blank
	extern sigaction
	mov dword [esp], 4     
	mov dword [esp+4], sa
	mov dword [esp+8], 0
	call sigaction
	#blank
	mov [dsp], esp
	#blank
	loop:
	#blank
	mov esp, [dsp]
	#blank
	''',
	}





dot = {
	'std' : '''
	mov eax, [on] 
	mov eax, [s_mz+eax] 
	#blank		  
	mov edx, [dp] 
	mov al, [eax+edx] 
	mov [c], al 
	#blank	  
	mov eax, 4 
	mov ebx, 1 
	mov ecx, c 
	mov edx, 1 
	int 0x80 
	#blank
	''',



	'mimo' : '''
	mov eax, [on] 
	mov eax, [s_dst+eax] 
	mov eax, [eax] 
	mov edx, [dsi] 
	mov ecx, [dp] 
	mov cl, [m+ecx] 
	mov [eax+edx], cl 
	#blank
	mov eax, 0 
	mov ax, [incw+2*edx] 
	mov edx, [on] 
	mov edx, [s_dsi+edx] 
	mov [edx], eax 
	# blank
	''',
	}




comma = {
	'std' : '''
	mov edx, [on] 
	mov edx, [trim+edx] 
	mov eax, 3 
	mov ebx, 0 
	mov ecx, c 
	int 0x80 
	#blank			  
	mov ecx, 0 
	mov eax, [on] 
	mov eax, [s_ms+eax] 
	mov edx, [dp] 
	mov cl, [c] 
	mov [eax+edx], cl 
	''',

	


	'cell16' : '''
	mov edx, [on] 
	mov edx, [trim+edx] 
	mov eax, 3 
	mov ebx, 0 
	mov ecx, c 
	int 0x80 
	#blank			  
	mov ecx, 0 
	mov eax, [on] 
	mov eax, [s_ms+eax] 
	mov edx, [dp] 
	mov cl, [c] 
	mov [eax+edx], cx
	''',




	'mimo' : '''
	mov ecx, 0 
	mov eax, [src] 
	mov edx, [sri] 
	mov cl, [eax+edx] 
	mov eax, [on] 
	mov eax, [s_ms+eax] 
	mov edx, [dp] 
	mov [eax+edx], cl 
	#bank
	mov edx, [sri] 
	mov eax, 0 
	mov ax, [incw+2*edx] 
	mov edx, [on] 
	mov edx, [s_sri+edx] 
	mov [edx], eax
	''',

 


	'opcell' : '''
	mov ecx, 0 
	mov eax, [src] 
	mov edx, [sri] 
	mov cl, [eax+edx] 
	mov eax, [on] 
	mov eax, [s_ms+eax] 
	mov edx, [dp] 
	mov [eax+edx], cx 
	#blank
	mov edx, [sri] 
	mov eax, 0 
	mov ax, [incw+2*edx] 
	mov edx, [on] 
	mov edx, [s_sri+edx] 
	mov [edx], eax 
	''',
	}



plus = {
	'std' : '''
	mov eax, [on] 
	mov ebx, [s_ms+eax] 
	mov edx, [dp] 
	mov eax, 0 
	mov al, [ebx+edx] 
	mov al, [incb+eax] 
	mov [ebx+edx], al 
	''',



	'cell16' : '''
	mov eax, [on] 
	mov ebx, [s_ms+eax] 
	mov edx, [dp] 
	mov eax, 0 
	mov ax, [ebx+edx] 
	mov ax, [incw+2*eax] 
	mov [ebx+edx], ax
	#blank
	''',



	'opt' : '''
	mov eax, [on] 
	mov ebx, [s_ms+eax] 
	mov edx, [dp] 
	mov eax, 0 
	mov al, [ebx+edx] 
	mov al, [incb+eax] 
	mov al, [incb+eax] 
	mov [ebx+edx], al 
	''',



	'opcell' : '''
	mov eax, [on] 
	mov ebx, [s_ms+eax] 
	mov edx, [dp] 
	mov eax, 0 
	mov ax, [ebx+edx] 
	mov ax, [incw+2*eax] 
	mov ax, [incw+2*eax] 
	mov [ebx+edx], ax
	''',	
	}





minus = {
	'std' : '''
	mov eax, [on] 
	mov ebx, [s_ms+eax] 
	mov edx, [dp] 
	mov eax, 0 
	mov al, [ebx+edx] 
	mov al, [decb+eax] 
	mov [ebx+edx], al
	#blank
	'''


	
	'cell16' : '''
	mov eax, [on] 
	mov ebx, [s_ms+eax] 
	mov edx, [dp] 
	mov eax, 0 
	mov ax, [ebx+edx] 
	mov ax, [decw+2*eax]
	mov [ebx+edx], ax 
	#blank
	'''



	'opt' : '''
	mov eax, [on] 
	mov ebx, [s_ms+eax] 
	mov edx, [dp] 
	mov eax, 0 
	mov al, [ebx+edx] 
	mov al, [decb+eax] 
	mov al, [decb+eax] 
	mov [ebx+edx], al
	#blank
	''',



	'opcell' : '''
	mov eax, [on] 
	mov ebx, [s_ms+eax] 
	mov edx, [dp] 
	mov eax, 0 
	mov ax, [ebx+edx] 
	mov ax, [decw+2*eax]
	mov ax, [decw+2*eax] 
	mov [ebx+edx], ax 
	#blank
	''',
	}




lthan = {
	'std' : '''
	mov eax, [on] 
	mov ebx, [s_dp+eax] 
	mov eax, [ebx] 
	mov edx, 0 
	mov dx, [decw+2*eax] 
	mov [ebx], edx 
	''',


	'cell16' : '''
	mov eax, [on] 
	mov ebx, [s_dp+eax] 
	mov eax, [ebx] 
	mov edx, 0 
	mov dx, [decw+2*eax] 
	mov dx, [decw+2*edx] 
	mov [ebx], edx 
	''',


	'opt' : '''
	mov eax, [on] 
	mov ebx, [s_dp+eax] 
	mov eax, [ebx] 
	mov edx, 0 
	mov dx, [decw+2*eax] 
	mov dx, [decw+2*edx] 
	mov [ebx], edx 
	''',


	'opcell' : '''
	mov eax, [on] 
	mov ebx, [s_dp+eax] 
	mov eax, [ebx] 
	mov edx, 0 
	mov dx, [decw+2*eax] 
	mov dx, [decw+2*edx] 
	mov dx, [decw+2*edx] 
	mov dx, [decw+2*edx] 
	mov [ebx], edx 
	''',
	}






bthan = {
	'std' : '''
	mov eax, [on] 
	mov ebx, [s_dp+eax] 
	mov eax, [ebx] 
	mov edx, 0 
	mov dx, [incw+2*eax]
	mov [ebx], edx 
	#blank
	''',


	'cell16' : '''
	mov eax, [on] 
	mov ebx, [s_dp+eax] 
	mov eax, [ebx] 
	mov edx, 0 
	mov dx, [incw+2*eax]
	mov dx, [incw+2*edx]
	mov [ebx], edx 
	#blank
	''',


	'opt' : '''
	mov eax, [on] 
	mov ebx, [s_dp+eax] 
	mov eax, [ebx] 
	mov edx, 0 
	mov dx, [incw+2*eax]
	mov dx, [incw+2*edx] 
	mov [ebx], edx 
	#blank
	''',


	'opcell' : '''
	mov eax, [on] 
	mov ebx, [s_dp+eax] 
	mov eax, [ebx] 
	mov edx, 0 
	mov dx, [incw+2*eax]
	mov dx, [incw+2*edx]
	mov dx, [incw+2*edx] 
	mov dx, [incw+2*edx]
	mov [ebx], edx
	''',
	}




at = {
	'std' : '''
	mov eax, [on]
	mov eax, [h+eax]
	mov eax, [eax]
	#blank
	''',
	}


obrack = {
	'std' : '''
	mov [ot], dword 0 
	#blank  
	mov eax, [dp] 
	mov edx, 0 
	mov dl, [m+eax]
	mov [t], edx 
	eq t, t, 0
	#blank	  
	and b, on, t 
	mov eax, [b] 
	mov eax, [s_id+eax] 
	mov [eax], dword {}".format(id))
	#blank	  
	mov eax, [b] 
	mov eax, [s_on+eax] 
	mov [eax], dword 0 
	#blank		  
	mov eax, [b] 
	mov eax, [s_ot+eax] 
	mov [eax], dword 4 
	#blank
	not t, on 
	eq b, id, {}".format(id))
	and b, b, t 
	not t, ot 
	and b, b, t 
	mov eax, [b] 
	mov eax, [s_on+eax]  
	mov [eax], dword 4  
	#blank
	''',


	'cell16' : '''
	mov [ot], dword 0 
	#blank  
	mov eax, [dp] 
	mov edx, 0 
	mov dx, [m+eax]
	mov [t], edx 
	eq t, t, 0
	#blank	  
	and b, on, t 
	mov eax, [b] 
	mov eax, [s_id+eax] 
	mov [eax], dword {}".format(id))
	#blank	  
	mov eax, [b] 
	mov eax, [s_on+eax] 
	mov [eax], dword 0 
	#blank		  
	mov eax, [b] 
	mov eax, [s_ot+eax] 
	mov [eax], dword 4 
	#blank
	not t, on 
	eq b, id, {}".format(id))
	and b, b, t 
	not t, ot 
	and b, b, t 
	mov eax, [b] 
	mov eax, [s_on+eax]  
	mov [eax], dword 4  
	#blank
	''',
	}





cbrack = {
	'std' : '''
	mov [ot], dword 0 
	#blank			  
	mov eax, [dp] 
	mov edx, 0
	mov dl, [m+eax]	
	mov [t], edx 
	neq t, t, 0 
	#blank			  
	and b, on, t 
	mov eax, [b] 
	mov eax, [s_id+eax] 
	mov [eax], dword {}".format(id))
	#blank			  
	mov eax, [b] 
	mov eax, [s_on+eax] 
	mov [eax], dword 0 
	#blank			  
	mov eax, [b] 
	mov eax, [s_ot+eax] 
	mov [eax], dword 4 			  
	#blank
	not t, on 
	eq b, id, {}".format(id))
	and b, b, t 
	not t, ot 
	and b, b, t 
	mov eax, [b] 
	mov eax, [s_on+eax] 
	mov [eax], dword 4 
	#blank	
	''',	


	'cell16' : '''
	mov [ot], dword 0 
	#blank			  
	mov eax, [dp] 
	mov edx, 0
	mov dx, [m+eax]	
	mov [t], edx 
	neq t, t, 0 
	#blank			  
	and b, on, t 
	mov eax, [b] 
	mov eax, [s_id+eax] 
	mov [eax], dword {}".format(id))
	#blank			  
	mov eax, [b] 
	mov eax, [s_on+eax] 
	mov [eax], dword 0 
	#blank			  
	mov eax, [b] 
	mov eax, [s_ot+eax] 
	mov [eax], dword 4 			  
	#blank
	not t, on 
	eq b, id, {}".format(id))
	and b, b, t 
	not t, ot 
	and b, b, t 
	mov eax, [b] 
	mov eax, [s_on+eax] 
	mov [eax], dword 4 
	#blank
	''',
	}	  

	
close = {  
	'std' : 'mov cs, ax',
	'njmp' : 'jmp loop',
	}

