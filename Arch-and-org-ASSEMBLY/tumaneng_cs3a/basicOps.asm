;Marc Christian D. Tumaneng_bscs3a
;Learning Task (Basic Assembly Instructions Part 2)

section .data
	
    message db 'This program computes for the average of 3 two-digit numbers (00-55).', 0

    ; Prompts for user input
    prompt_firstNum db 'Enter the first number: ',10, 0
    input_firstNum db '%d', 0

    prompt_secondNum db 'Enter the second number: ',10, 0
    input_secondNum db '%d', 0 

    prompt_thirdNum db 'Enter the third number: ',10, 0
    input_thirdNum db '%d', 0   	

    ;prompts for average
    average db 'Average is: %d',10,0
    ;prompts for remainder
    ;remainder db 'With remainder: %d',10,0

    firstNumber times 4 db 0
    secondNumber times 4 db 0
    thirdNumber times 4 db 0

    newline db 10, 0

section .bss
	
        sum resb 4
	
section .text
	global _main
	extern _printf
	extern _scanf

_main:

	; Display a message
 	push message
 	call _printf
	add esp, 4	
 
	; Print a new line 
 	push newline
 	call _printf
 	add esp, 4
	
       ;display prompt for firstNum
	push prompt_firstNum
  	call _printf
    	add esp, 4
	
       ;read user input for firstNum
	push firstNum
	push input_firstNum
	call _scanf
	add esp,8
	
	;display prompt for secondNum
	push prompt_secondNum
  	call _printf
    	add esp, 4
	
        ;read user input for secondNum
	push secondNum
	push input_secondNum
	call _scanf
	add esp,8
	
	;display prompt for thirdNum
	push prompt_thirdNum
  	call _printf
    	add esp, 4
	
        ;read user input for thirdNum
	push thirdNum
	push input_thirdNum
	call _scanf
	add esp,8
	
	push dword [firstNum]
	push dword [secondNum]
	push dword [thirdNum]
	push try
	call _printf
	add esp, 16

	;adding firstNum, secondNum and thirdNum
	mov eax, dword [firstNum]
	add eax, dword [secondNum]
	add eax, dword [thirdNum]
	mov [sum], eax
	
	;deviding firstNum, secondNum and thirdNum to 3
	mov ebx, 3
	mov edx, 0
	div ebx

	; display the average
	push eax
	push average
	call _printf
	add esp, 8

        ret
