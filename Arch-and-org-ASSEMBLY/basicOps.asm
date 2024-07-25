section .data
	prompt db 'This program computes for the average of 3 two-digit numbers (00-55).', 0
	firstNum db 'Enter the first number:', 10, 0
	inputformat_firstNum db '%d', 0
	secondNum db 'Enter the second number:', 10, 0
	inputformat_secondNum db '%d', 0
	thirdNum db 'Enter the thirdnumber:', 10, 0
	inputformat_thirdNum db '%d', 0
	avg db 'Average is: %d', 10, 0
	rmndr db 'With remainder: %d', 10, 0
	try db 'fNum is %d, sNum is %d, tNum is %d.', 10, 0

	fNum times 4 db 0
	sNum times 4 db 0
	tNum times 4 db 0
	
 	newline db 10, 0

section .bss
	
	sum resb 4

section .text
	global _main
	extern _printf
	extern _scanf

_main:
 	; Display a prompt
 	push prompt
 	call _printf
	add esp, 4	
 
	; Print a new line 
 	push newline
 	call _printf
 	add esp, 4

 	; Display a prompt to ask first number
 	push firstNum
 	call _printf
 	add esp, 4

 	; Print a new line 
 	push newline
 	call _printf
 	add esp, 4

 	; Read firstNum input
 	push fNum
 	push inputformat_firstNum
 	call _scanf
 	add esp, 8
	
	; Print a new line 
 	push newline
 	call _printf
 	add esp, 4

 	; Display a prompt to ask second number
 	push secondNum
 	call _printf
 	add esp, 4

 	; Print a new line 
 	push newline
 	call _printf
 	add esp, 4

 	; Read secondNum input
 	push sNum
 	push inputformat_secondNum
 	call _scanf
 	add esp, 8

	; Print a new line 
 	push newline
 	call _printf
 	add esp, 4

 	; Display a prompt to ask third number
 	push thirdNum
 	call _printf
 	add esp, 4

 	; Print a new line 
 	push newline
 	call _printf
 	add esp, 4

 	; Read thirdNum input
 	push tNum
 	push inputformat_thirdNum
 	call _scanf
 	add esp, 8
	
	; Print a new line 
 	push newline
 	call _printf
 	add esp, 4
	
	push dword [tNum]
	push dword [sNum]
	push dword [fNum]
	push try
	call _printf
	add esp, 16

	; Print a new line 
 	push newline
 	call _printf
 	add esp, 4
	
	; add
	mov eax, dword [fNum]
	add eax, dword [sNum]
	add eax, dword [tNum]
	mov [sum], eax
	
	; div the sum by 3
	mov ebx, 3
	mov edx, 0
	div ebx
	
	; display the average
	push eax
	push avg
	call _printf
	add esp, 8
	

	ret