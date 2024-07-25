;Learning Task (Structured Assembly Language Part 1)|| Simple Calculator
;Marc Christian D. Tumaneng BSCS 3A

section .data
	; Data section for defining messages and prompts
	welcome db 'Hi! This is Marc Christian and I am here to help you perform operations for 2 signed two-digit numbers (-99 to 99).',10,0
	title db '==== SIMPLE CALCULATOR by Marc Christian ====',10, 0
	exit_prompt db '[0] Exit',10, 0
	add_prompt db '[1] Add',10, 0
	sub_prompt db '[2] Subtract',10, 0
	mul_prompt db '[3] Multiply',10, 0
	div_prompt db '[4] Divide',10, 0
	choice_prompt db 'Enter choice: ', 0
	choice_format db '%d', 0
	first_num_prompt db 'Enter the first number: ', 0
	second_num_prompt db 'Enter the second number: ', 0
	number_format db '%d', 0
	result_msg db 'Result: %d', 10, 0
	div_zero_msg db 'You cannot divide by 0. Please enter a valid divisor.',10, 0
	invalid_range_msg db 'Input should only be between -99 to 99. Please enter a valid input.',10, 0
	add_op_msg db '===ADDITION===', 10, 0
	sub_op_msg db '===SUBTRACTION===', 10, 0
	mul_op_msg db '===MULTIPLICATION===', 10, 0
	div_op_msg db '===DIVISION===', 10, 0
	exit_msg db 'Thank You!', 10, 0
	sum_msg db 'Sum: %d', 10, 0
	diff_msg db 'Difference: %d', 10, 0
	prod_msg db 'Product: %d', 10, 0
	quotient_msg db 'Quotient: %d', 10, 0
	remainder_msg db 'Remainder: %d', 10, 0

section .bss
	; BSS section for defining variables to store user input and results
	menu_choice resd 1
	first_num resd 1
	second_num resd 1
	result resd 1

section .text
	global _main
	extern _printf
	extern _scanf
	extern _exit

_main:
	; Display welcome message
	push welcome
	call _printf
	add esp, 4

.menu_loop:
	; Display program title 
	push title
	call _printf
	add esp, 4

	; Display menu options
	push exit_prompt
	call _printf
	add esp, 4
	push add_prompt
	call _printf
	add esp, 4
	push sub_prompt
	call _printf
	add esp, 4
	push mul_prompt
	call _printf
	add esp, 4
	push div_prompt
	call _printf
	add esp, 4
	push choice_prompt
	call _printf
	add esp, 4

	; Read user's choice
	push menu_choice
	push choice_format
	call _scanf
	add esp, 8

	; Check user's choice and jump to the its corresponding menu
	cmp dword [menu_choice], 1
	je .addition
	cmp dword [menu_choice], 2
	je .subtraction
	cmp dword [menu_choice], 3
	je .multiplication
	cmp dword [menu_choice], 4
	je .division
	cmp dword [menu_choice], 0
	je .exit

	; If the choice is invalid, loop back to the menu
	jmp .menu_loop

.addition:
	; Addition operation
	push add_op_msg
	call _printf
	add esp, 4
	call .perform_operation
	jmp .menu_loop

.subtraction:
	; Subtraction operation
	push sub_op_msg
	call _printf
	add esp, 4
	call .perform_operation
	jmp .menu_loop

.multiplication:
	; Multiplication operation
	push mul_op_msg
	call _printf
	add esp, 4
	call .perform_operation
	jmp .menu_loop

.division:
	; Division operation
	push div_op_msg
	call _printf
	add esp, 4
	call .perform_operation
	jmp .menu_loop

.perform_operation:
	push first_num_prompt
	call _printf
	add esp, 4

	; Read the first number
	push first_num
	push number_format
	call _scanf
	add esp, 8

	; Check if the first number is within the valid range
	cmp dword [first_num], -99
	jl .invalid_range_first
	cmp dword [first_num], 99
	jg .invalid_range_first
	push second_num_prompt
	call _printf
	add esp, 4

	; Read the second number
	push second_num
	push number_format
	call _scanf
	add esp, 8

	; Check if the second number is within the valid range
	cmp dword [second_num], -99
	jl .invalid_range_second
	cmp dword [second_num], 99
	jg .invalid_range_second

	; Perform the selected operation
	cmp dword [menu_choice], 1
	je .addition_operation
	cmp dword [menu_choice], 2
	je .subtraction_operation
	cmp dword [menu_choice], 3
	je .multiplication_operation
	cmp dword [menu_choice], 4
	je .division_operation
	jmp .menu_loop

.addition_operation:
	; Perform addition
	mov eax, [first_num]
	add eax, [second_num]
	push eax
	push sum_msg
	call _printf
	add esp, 8
	ret

.subtraction_operation:
	; Perform subtraction
	mov eax, [first_num]
	sub eax, [second_num]
	push eax
	push diff_msg
	call _printf
	add esp, 8
	ret

.multiplication_operation:
	; Perform multiplication
	mov eax, [first_num]
	imul eax, [second_num]
	push eax
	push prod_msg
	call _printf
	add esp, 8
	ret

.division_operation:
	; Perform division
	cmp dword [second_num], 0
	je .division_zero
	mov eax, [first_num]
	cdq
	mov ebx, [second_num]
	idiv ebx

	; Display the quotient
	push eax
	push quotient_msg
	call _printf
	add esp, 8

	; Calculate and display the remainder
	mov eax, dword [first_num]
	add eax, dword [second_num]
	mov edx, 0
	div ebx

	; Display the remainder
	push edx
	push remainder_msg
	call _printf
	add esp, 8
	ret

.invalid_range_first:
	; Display invalid range message for the first number
	push invalid_range_msg
	call _printf
	add esp, 4
	ret

.invalid_range_second:
	; Display invalid range message for the second number
	push invalid_range_msg
	call _printf
	add esp, 4
	ret

.division_zero:
	; Display division by zero message
	push div_zero_msg
	call _printf
	add esp, 4

	; Re-prompt for the second number
	push second_num_prompt
	call _printf
	add esp, 4

	; Read input for the second number
	push second_num
	push number_format
	call _scanf
	add esp, 8

	; Check if the second number is within the valid range
	cmp dword [second_num], -99
	jl .invalid_range_second
	cmp dword [second_num], 99
	jg .invalid_range_second

	; Re-calculate the division
	call .division_operation
	ret

.exit:
	; Display exit message and exit the program
	push exit_msg
	call _printf
	call _exit
