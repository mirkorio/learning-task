section .data
    ; Data section for defining messages and prompts
    welcome db 'Hi! This is YourName and I am here to help you determine the LCD and GCF for two-digit numbers (1 to 99).',10,0
    title db '==== LCD and GCF CALCULATOR by Group 12 ====',10, 0
    exit_prompt db '[0] Exit',10, 0
    lcd_prompt db '[1] LCD',10, 0
    gcf_prompt db '[2] GCF',10, 0
    choice_prompt db 'Enter choice: ', 0
    choice_format db '%d', 0
    first_num_prompt db 'Enter the first number: ', 0
    second_num_prompt db 'Enter the second number: ', 0
    number_format db '%d', 0
    lcd_msg db '==== LCD ====', 10, 0
    gcf_msg db '==== GCF ====', 10, 0
    input_range_msg db 'Input should only be between 1 to 99. Please enter again a valid input.',10, 0
    lcd_result_msg db 'LCD: %d', 10, 0
    gcf_result_msg db 'GCF: %d', 10, 0
    invalid_choice_msg db 'Entered Choice is not on the menu. Please enter a valid choice.', 10, 0
    exit_msg db 'Thank you!', 10, 0

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
    push lcd_prompt
    call _printf
    add esp, 4
    push gcf_prompt
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

    ; Check if the user's choice is a valid integer
    cmp dword [menu_choice], 0
    jl .invalid_choice
    cmp dword [menu_choice], 2
    jg .invalid_choice

    ; Check user's choice and jump to its corresponding menu
    cmp dword [menu_choice], 1
    je .lcd
    cmp dword [menu_choice], 2
    je .gcf
    je .invalid_choice

.exit:
    ; Display exit message and exit the program
    push exit_msg
    call _printf
    call _exit

.lcd:
    ; LCD operation
    push lcd_msg
    call _printf
    add esp, 4

    ; Read the first number
    push first_num_prompt
    call _printf
    add esp, 4
    push first_num
    push number_format
    call _scanf
    add esp, 8

    ; Read the second number
    push second_num_prompt
    call _printf
    add esp, 4
    push second_num
    push number_format
    call _scanf
    add esp, 8

    ; Check if the numbers are within the valid range (1 to 99)
    cmp dword [first_num], 1
    jl .invalid_range_first
    cmp dword [first_num], 99
    jg .invalid_range_first
    cmp dword [second_num], 1
    jl .invalid_range_second
    cmp dword [second_num], 99
    jg .invalid_range_second

    ; Calculate and display LCD
    push dword [first_num]
    push dword [second_num]
    call .calculate_lcd
    push eax
    push lcd_result_msg
    call _printf
    add esp, 8
    jmp .menu_loop

.gcf:
    ; GCF operation
    push gcf_msg
    call _printf
    add esp, 4

    ; Read the first number
    push first_num_prompt
    call _printf
    add esp, 4
    push first_num
    push number_format
    call _scanf
    add esp, 8

    ; Read the second number
    push second_num_prompt
    call _printf
    add esp, 4
    push second_num
    push number_format
    call _scanf
    add esp, 8

    ; Check if the numbers are within the valid range (1 to 99)
    cmp dword [first_num], 1
    jl .invalid_range_first
    cmp dword [first_num], 99
    jg .invalid_range_first
    cmp dword [second_num], 1
    jl .invalid_range_second
    cmp dword [second_num], 99
    jg .invalid_range_second

    ; Calculate and display GCF
    push dword [first_num]
    push dword [second_num]
    call .calculate_gcf
    push eax
    push gcf_result_msg
    call _printf
    add esp, 8
    jmp .menu_loop

.calculate_lcd:
    ; Calculate LCD (updated for pass by reference)
    mov eax, [esp+4]
    imul eax, [esp+8]
    ret

.calculate_gcf:
    ; Calculate GCF using Euclidean algorithm (updated for pass by reference)
    mov eax, [esp+4]
    mov ebx, [esp+8]
    .gcf_loop:
        cmp ebx, 0
        je .done
        xor edx, edx
        div ebx
        mov eax, ebx
        mov ebx, edx
        jmp .gcf_loop
    .done:
        ret

.invalid_range_first:
    ; Display invalid range message for the first number
    push input_range_msg
    call _printf
    add esp, 4
    jmp .menu_loop

.invalid_range_second:
    ; Display invalid range message for the second number
    push input_range_msg
    call _printf
    add esp, 4
    jmp .menu_loop

.invalid_choice:
    ; Display invalid choice message
    push invalid_choice_msg
    call _printf
    add esp, 4
    jmp .menu_loop


