section .data
	sum db "sum = %d", 10, 0
	diff db "difference = %d", 10, 0
	prod db "product = %d", 10, 0
	quo db "quotient = %d", 10, 0

section .text
	global _main
	extern _printf

_main:
	;adding 45 and 55
  	mov eax, 45
  	mov ebx, 55
  	add eax,ebx
  	push eax
  	push sum
  	call _printf
  	add esp, 8

	;subtract 10 with 8
  	mov eax, 10
  	mov ebx, 8
  	sub eax,ebx
  	push eax
  	push diff
  	call _printf
  	add esp, 8

	;multiply 4*5
	mov eax, 4
	mov ebx, 5
  	mul ebx
  	push eax
  	push prod
  	call _printf
  	add esp, 8

	;divide 16 by 8
	mov eax, 16
  	mov ebx, 8
  	div ebx
  	push eax
  	push quo
  	call _printf
  	add esp, 8

	ret

