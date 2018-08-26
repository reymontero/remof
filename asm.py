dot = {
	'std' : '''
	mov eax, [on] 
	mov eax, [s_mz+eax] 
			  
	mov edx, [dp] 
	mov al, [eax+edx] 
	mov [c], al 
		  
	mov eax, 4 
	mov ebx, 1 
	mov ecx, c 
	mov edx, 1 
	int 0x80 
	
	''',



	'mimo' : '''
	mov eax, [on] 
	mov eax, [s_dst+eax] 
	mov eax, [eax] 
	mov edx, [dsi] 
	mov ecx, [dp] 
	mov cl, [m+ecx] 
	mov [eax+edx], cl 
	
	mov eax, 0 
	mov ax, [incw+2*edx] 
	mov edx, [on] 
	mov edx, [s_dsi+edx] 
	mov [edx], eax 
	
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

 


	'mmcell' : '''
	mov ecx, 0 
	mov eax, [src] 
	mov edx, [sri] 
	mov cl, [eax+edx] 
	mov eax, [on] 
	mov eax, [s_ms+eax] 
	mov edx, [dp] 
	mov [eax+edx], cx 
	
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
	
	''',


	
	'cell16' : '''
	mov eax, [on] 
	mov ebx, [s_ms+eax] 
	mov edx, [dp] 
	mov eax, 0 
	mov ax, [ebx+edx] 
	mov ax, [decw+2*eax]
	mov [ebx+edx], ax 
	
	''',



	'opt' : '''
	mov eax, [on] 
	mov ebx, [s_ms+eax] 
	mov edx, [dp] 
	mov eax, 0 
	mov al, [ebx+edx] 
	mov al, [decb+eax] 
	mov al, [decb+eax] 
	mov [ebx+edx], al
	
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
	
	''',


	'cell16' : '''
	mov eax, [on] 
	mov ebx, [s_dp+eax] 
	mov eax, [ebx] 
	mov edx, 0 
	mov dx, [incw+2*eax]
	mov dx, [incw+2*edx]
	mov [ebx], edx 
	
	''',


	'opt' : '''
	mov eax, [on] 
	mov ebx, [s_dp+eax] 
	mov eax, [ebx] 
	mov edx, 0 
	mov dx, [incw+2*eax]
	mov dx, [incw+2*edx] 
	mov [ebx], edx 
	
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
	
	''',
}



obrack = {
	'std' : '''
	mov [ot], dword 0 
	  
	mov eax, [dp] 
	mov edx, 0 
	mov dl, [m+eax]
	mov [t], edx 
	eq t, t, 0
		  
	and b, on, t 
	mov eax, [b] 
	mov eax, [s_id+eax] 
	mov [eax], dword {}
		  
	mov eax, [b] 
	mov eax, [s_on+eax] 
	mov [eax], dword 0 
			  
	mov eax, [b] 
	mov eax, [s_ot+eax] 
	mov [eax], dword 4 
	
	not t, on 
	eq b, id, {}
	and b, b, t 
	not t, ot 
	and b, b, t 
	mov eax, [b] 
	mov eax, [s_on+eax]  
	mov [eax], dword 4  
	
	''', 


	'cell16' : '''
	mov [ot], dword 0 
	  
	mov eax, [dp] 
	mov edx, 0 
	mov dx, [m+eax]
	mov [t], edx 
	eq t, t, 0
		  
	and b, on, t 
	mov eax, [b] 
	mov eax, [s_id+eax] 
	mov [eax], dword {}
		  
	mov eax, [b] 
	mov eax, [s_on+eax] 
	mov [eax], dword 0 
			  
	mov eax, [b] 
	mov eax, [s_ot+eax] 
	mov [eax], dword 4 
	
	not t, on 
	eq b, id,  {}
	and b, b, t 
	not t, ot 
	and b, b, t 
	mov eax, [b] 
	mov eax, [s_on+eax]  
	mov [eax], dword 4  
	
	''', 
}






cbrack = {
	'std' : '''
	mov [ot], dword 0 
				  
	mov eax, [dp] 
	mov edx, 0
	mov dl, [m+eax]	
	mov [t], edx 
	neq t, t, 0 
				  
	and b, on, t 
	mov eax, [b] 
	mov eax, [s_id+eax] 
	mov [eax], dword {}
				  
	mov eax, [b] 
	mov eax, [s_on+eax] 
	mov [eax], dword 0 
				  
	mov eax, [b] 
	mov eax, [s_ot+eax] 
	mov [eax], dword 4 			  
	
	not t, on 
	eq b, id, {}
	and b, b, t 
	not t, ot 
	and b, b, t 
	mov eax, [b] 
	mov eax, [s_on+eax] 
	mov [eax], dword 4 
		
	''',	


	'cell16' : '''
	mov [ot], dword 0 
				  
	mov eax, [dp] 
	mov edx, 0
	mov dx, [m+eax]	
	mov [t], edx 
	neq t, t, 0 
				  
	and b, on, t 
	mov eax, [b] 
	mov eax, [s_id+eax] 
	mov [eax], dword {}   
				  
	mov eax, [b] 
	mov eax, [s_on+eax] 
	mov [eax], dword 0 
				  
	mov eax, [b] 
	mov eax, [s_ot+eax] 
	mov [eax], dword 4 			  
	
	not t, on 
	eq b, id, {}
	and b, b, t 
	not t, ot 
	and b, b, t 
	mov eax, [b] 
	mov eax, [s_on+eax] 
	mov [eax], dword 4 
	
	''', 
}	  

	



close = {  
	'std' : 'mov cs, ax',
	'njmp' : 'jmp loop',
}





intro = {

	'std' : '''
	
	USE32
	section .data

	DATA equ {}

	%macro c_s 1
		%1:   dd 0
		d_%1: dd 0
		s_%1: dd d_%1, %1
	%endmacro

	s_ms: dd s, m
	s_mz: dd z, m

	b: dd 0
	t: dd 0
	c: db 0

	c_s dp

	c_s id
	c_s ot

	on: dd 4
	d_on: dd 0
	s_on: dd d_on, on

	o: dd o_0, o_1
	o_0: dd 0, 4
	o_1: dd 4, 4

	a: dd a_0, a_1
	a_0: dd 0, 0
	a_1: dd 0, 4

	n: dd 4, 0

	nh: dd 0
	h: dd nh, 0

	trim: dd 0
	times 255 dd 1

	incb:
	%assign y 1
	%rep    256
		db y&0xff
		%assign y y+1
	%endrep

	decb:
	%assign y 256-1
	%rep    256
		db y&0xff
		%assign y y+1
	%endrep

	incw:
	%assign y 1
	%rep    256*256
		dw y&0xffff
		%assign y y+1
	%endrep

	decw:
	%assign y 256*256-1
	%rep    256*256
		dw y&0xffff
		%assign y y+1
	%endrep

	%macro eq 3
		mov eax, 0
		mov edx, 0
		mov ax, [%2]
		mov byte [e+eax], 0
		mov byte [e+%3], 4
		mov dl, [e+eax]
		mov [%1], edx
	%endmacro

	%macro neq 3
		mov eax, 0
		mov edx, 0
		mov ax, [%2]
		mov byte [e+eax], 4
		mov byte [e+%3], 0
		mov dl, [e+eax]
		mov [%1], edx
	%endmacro

	%macro or 3
		mov eax, [%2]
		mov edx, [o+eax]
		mov eax, [%3]
		mov eax, [eax+edx]
		mov [%1], eax
	%endmacro

	%macro and 3
		mov eax, [%2]
		mov edx, [a+eax]
		mov eax, [%3]
		mov eax, [eax+edx]
		mov [%1], eax
	%endmacro

	%macro not 2
		mov eax, [%2]
		mov eax, [n+eax]
		mov [%1], eax
	%endmacro

	section .bss
	m: resb DATA
	s: resb DATA
	z: resb DATA
	e: resb 256*256

	section .text
	global _start
	_start:

	loop:

	
	''', 





	'nojmp' : '''
	
	USE32
	section .data
	
	DATA equ {}
	
	%macro c_s 1
		%1:   dd 0
		d_%1: dd 0
		s_%1: dd d_%1, %1
	%%endmacro
	
	s_ms: dd s, m
	s_mz: dd z, m
	
	b: dd 0
	t: dd 0
	c: db 0
	
	c_s dp
	
	c_s id
	c_s ot
	
	on: dd 4
	d_on: dd 0
	s_on: dd d_on, on
	
	o: dd o_0, o_1
	o_0: dd 0, 4
	o_1: dd 4, 4
	
	a: dd a_0, a_1
	a_0: dd 0, 0
	a_1: dd 0, 4
	
	n: dd 4, 0
	
	nh: dd 0
	h: dd nh, 0
	
	trim: dd 0
	times 255 dd 1
	
	incb:
	%assign y 1
	%rep    256
		db y&0xff
		%assign y y+1
	%%endrep
	
	decb:
	%assign y 256-1
	%rep    256
		db y&0xff
		%assign y y+1
	%%endrep
	
	incw:
	%assign y 1
	%rep    256*256
		dw y&0xffff
		%assign y y+1
	%%endrep
	
	decw:
	%assign y 256*256-1
	%rep    256*256
		dw y&0xffff
		%assign y y+1
	%%endrep
	
	%macro eq 3
		mov eax, 0
		mov edx, 0
		mov ax, [%2]
		mov byte [e+eax], 0
		mov byte [e+%3], 4
		mov dl, [e+eax]
		mov [%1], edx
	%%endmacro
	
	%macro neq 3
		mov eax, 0
		mov edx, 0
		mov ax, [%2]
		mov byte [e+eax], 4
		mov byte [e+%3], 0
		mov dl, [e+eax]
		mov [%1], edx
	%%endmacro
	
	%macro or 3
		mov eax, [%2]
		mov edx, [o+eax]
		mov eax, [%3]
		mov eax, [eax+edx]
		mov [%1], eax
	%%endmacro
	
	%macro and 3
		mov eax, [%2]
		mov edx, [a+eax]
		mov eax, [%3]
		mov eax, [eax+edx]
		mov [%1], eax
	%%endmacro
	
	%macro not 2
		mov eax, [%2]
		mov eax, [n+eax]
		mov [%1], eax
	%%endmacro
	
	sa: dd loop          
		times 0x20 dd 0  
		dd 0x40000000    
		dd 0             
		
	dsp: dd 0
	section .bss
	m: resb DATA
	s: resb DATA
	z: resb DATA
	e: resb 256*256
	
	section .text
	global _start
	_start:
	
	extern sigaction
	mov dword [esp], 4      
	mov dword [esp+4], sa
	mov dword [esp+8], 0
	call sigaction
	
	mov [dsp], esp
	
	loop:
	
	mov esp, [dsp]
	
	''', 




	'mmio' : '''
	
	USE32
	section .data
	
	DATA equ {}
	
	%macro c_s 1
		%1:   dd 0
		d_%1: dd 0
		s_%1: dd d_%1, %1
	%%endmacro
	
	s_ms: dd s, m
	s_mz: dd z, m
	
	b: dd 0
	t: dd 0
	c: db 0
	
	c_s dp
	
	c_s id
	c_s ot
	
	on: dd 4
	d_on: dd 0
	s_on: dd d_on, on
	
	o: dd o_0, o_1
	o_0: dd 0, 4
	o_1: dd 4, 4
	
	a: dd a_0, a_1
	a_0: dd 0, 0
	a_1: dd 0, 4
	
	n: dd 4, 0
	
	nh: dd 0
	h: dd nh, 0
	
	trim: dd 0
	times 255 dd 1
	
	incb:
	%assign y 1
	%rep    256
		db y&0xff
		%assign y y+1
	%%endrep
	
	decb:
	%assign y 256-1
	%rep    256
		db y&0xff
		%assign y y+1
	%%endrep
	
	incw:
	%assign y 1
	%rep    256*256
		dw y&0xffff
		%assign y y+1
	%%endrep
	
	decw:
	%assign y 256*256-1
	%rep    256*256
		dw y&0xffff
		%assign y y+1
	%%endrep
	
	%macro eq 3
		mov eax, 0
		mov edx, 0
		mov ax, [%2]
		mov byte [e+eax], 0
		mov byte [e+%3], 4
		mov dl, [e+eax]
		mov [%1], edx
	%%endmacro
	
	%macro neq 3
		mov eax, 0
		mov edx, 0
		mov ax, [%2]
		mov byte [e+eax], 4
		mov byte [e+%3], 0
		mov dl, [e+eax]
		mov [%1], edx
	%%endmacro
	
	%macro or 3
		mov eax, [%2]
		mov edx, [o+eax]
		mov eax, [%3]
		mov eax, [eax+edx]
		mov [%1], eax
	%%endmacro
	
	%macro and 3
		mov eax, [%2]
		mov edx, [a+eax]
		mov eax, [%3]
		mov eax, [eax+edx]
		mov [%1], eax
	%%endmacro
	
	%macro not 2
		mov eax, [%2]
		mov eax, [n+eax]
		mov [%1], eax
	%%endmacro
	
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
	MMIO_SIZE equ {}
		
	section .bss
	m: resb DATA
	s: resb DATA
	z: resb DATA
	e: resb 256*256
	
	section .text
	global _start
	_start:
	
	extern open
	extern lseek
	extern write
	extern mmap
	
	sub esp, 20h
	
	 fdin = open (\"/dev/stdin\", O_RDONLY)
	mov dword [esp], ssi
	mov dword [esp+4], 0  O_RDONLY
	call open
	mov [fdi], eax
	
	 fdprint = open (\"/dev/stdprint\", O_RDWR)
	mov dword [esp], sso
	mov dword [esp+4], 2  O_RDWR
	call open
	mov [fdo], eax
	
	 lseek (fdprint, MMIO_SIZE - 1, SEEK_SET)
	mov eax, [fdo]
	mov [esp], eax
	mov dword [esp+4], MMIO_SIZE-1
	mov dword [esp+8], 0  SEEK_SET
	call lseek
	
	 write (fdprint, "", 1)
	mov eax, [fdo]
	mov [esp], eax
	mov dword [esp+4], zzz
	mov dword [esp+8], 1
	call write
	
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
	
	loop:
	
	''',



	'mmjmp' : '''
	
	USE32
	section .data
	
	DATA equ {}
	
	%macro c_s 1
		%1:   dd 0
		d_%1: dd 0
		s_%1: dd d_%1, %1
	%%endmacro
	
	s_ms: dd s, m
	s_mz: dd z, m
	
	b: dd 0
	t: dd 0
	c: db 0
	
	c_s dp
	
	c_s id
	c_s ot
	
	on: dd 4
	d_on: dd 0
	s_on: dd d_on, on
	
	o: dd o_0, o_1
	o_0: dd 0, 4
	o_1: dd 4, 4
	
	a: dd a_0, a_1
	a_0: dd 0, 0
	a_1: dd 0, 4
	
	n: dd 4, 0
	
	nh: dd 0
	h: dd nh, 0
	
	trim: dd 0
	times 255 dd 1
	
	incb:
	%assign y 1
	%rep    256
		db y&0xff
		%assign y y+1
	%%endrep
	
	decb:
	%assign y 256-1
	%rep    256
		db y&0xff
		%assign y y+1
	%%endrep
	
	incw:
	%assign y 1
	%rep    256*256
		dw y&0xffff
		%assign y y+1
	%%endrep
	
	decw:
	%assign y 256*256-1
	%rep    256*256
		dw y&0xffff
		%assign y y+1
	%%endrep
	
	%macro eq 3
		mov eax, 0
		mov edx, 0
		mov ax, [%2]
		mov byte [e+eax], 0
		mov byte [e+%3], 4
		mov dl, [e+eax]
		mov [%1], edx
	%%endmacro
	
	%macro neq 3
		mov eax, 0
		mov edx, 0
		mov ax, [%2]
		mov byte [e+eax], 4
		mov byte [e+%3], 0
		mov dl, [e+eax]
		mov [%1], edx
	%%endmacro
	
	%macro or 3
		mov eax, [%2]
		mov edx, [o+eax]
		mov eax, [%3]
		mov eax, [eax+edx]
		mov [%1], eax
	%%endmacro
	
	%macro and 3
		mov eax, [%2]
		mov edx, [a+eax]
		mov eax, [%3]
		mov eax, [eax+edx]
		mov [%1], eax
	%%endmacro
	
	%macro not 2
		mov eax, [%2]
		mov eax, [n+eax]
		mov [%1], eax
	%%endmacro
	
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
	MMIO_SIZE equ {}	
	
	sa: dd loop          
	    times 0x20 dd 0  
	    dd 0x40000000    
	    dd 0           
	
	dsp: dd 0
	section .bss
	m: resb DATA
	s: resb DATA
	z: resb DATA
	e: resb 256*256
	
	section .text
	global _start
	_start:
	
	extern open
	extern lseek
	extern write
	extern mmap
	
	sub esp, 20h
	
	 fdin = open (\"/dev/stdin\", O_RDONLY)
	mov dword [esp], ssi
	mov dword [esp+4], 0  O_RDONLY
	call open
	mov [fdi], eax
	
	 fdprint = open (\"/dev/stdprint\", O_RDWR)
	mov dword [esp], sso
	mov dword [esp+4], 2  O_RDWR
	call open
	mov [fdo], eax
	
	 lseek (fdprint, MMIO_SIZE - 1, SEEK_SET)
	mov eax, [fdo]
	mov [esp], eax
	mov dword [esp+4], MMIO_SIZE-1
	mov dword [esp+8], 0  SEEK_SET
	call lseek
	
	 write (fdprint, "", 1)
	mov eax, [fdo]
	mov [esp], eax
	mov dword [esp+4], zzz
	mov dword [esp+8], 1
	call write
	
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
	
	extern sigaction
	mov dword [esp], 4     
	mov dword [esp+4], sa
	mov dword [esp+8], 0
	call sigaction
	
	mov [dsp], esp
	
	loop:
	
	mov esp, [dsp]
	
	''', 
}





