;Learning Task (SAL Part 2 – Modular Programming)pass-by-reference by group 12

section .data

  welcome_msg db " Hi! This is Group 12, and we are here to assist you with LCD and GCF calculations for two-digit numbers (1 to 99)", 10, 0
  menu_msg db " === LCD and GCF CALCULATOR by Group 12 ===", 0xA
         db " [0] Exit", 0xA
         db " [1] LCD", 0xA
         db " [2] GCF", 10, 0
  user_choice_prompt db " Enter your choice: ", 0
  user_choice_format db "%d", 0
  lcd_msg db " === LCD ===", 10, 0
  gcf_msg db " === GCF === ", 10, 0
  first_num_prompt db " Enter First Number: ", 0
  first_num_format db "%d", 0
  second_num_prompt db " Enter Second Number: ", 0
  second_num_format db "%d", 0
  lcd_result_format db " LCD: %d", 10, 0
  gcf_result_format db " GCF: %d", 10, 0
  invalid_choice_msg db " Invalid choice. Please enter a valid option.", 10, 0
  invalid_input_msg db " Input should be between 1 to 99. Please enter a valid input.", 10, 0
  exit_msg db " Thank you! ", 0

; store the user's input
section .bss
  user_choice resd 1
  first_num resd 1
  second_num resd 1
  result resd 1

; section that contains the program logic
section .text

; Function to calculate the Greatest Common Divisor (GCD) using Euclidean algorithm
gcd_function:
    push ebp
    mov ebp, esp

    ; Load values from memory addresses (pass by reference)
    mov eax, [first_num]   ; Load the value from the memory address pointed by first_num
    mov ebx, [second_num]  ; Load the value from the memory address pointed by second_num

gcd_loop:
    cmp ebx, 0
    je gcd_done
    xor edx, edx
    div ebx
    mov eax, ebx
    mov ebx, edx
    jmp gcd_loop

gcd_done:
    ; Store the result at the memory address pointed by result (pass by reference)
    mov [result], eax
    pop ebp
    ret

; Function to calculate LCD using GCD function
calculate_lcd:
    ; Call the GCD function (pass by reference)
    push dword [first_num]
    push dword [second_num]
    call gcd_function

    ; Retrieve results from GCD function
    pop ebx
    pop eax

    ; Calculate LCD using GCD result
    imul eax, ebx
    idiv dword [result]

    ; Display the result
    push eax
    push lcd_result_format
    call _printf
    add esp, 8

    ; Return to the main menu
    jmp display_menu

; Function to calculate GCF using GCD function
calculate_gcf:
    ; Call the GCD function (pass by reference)
    push dword [first_num]
    push dword [second_num]
    call gcd_function

    ; Retrieve GCD result
    push dword [result]

    ; Display the result
    push gcf_result_format
    call _printf
    add esp, 8

    ; Return to the main menu
    jmp display_menu

; Function to handle invalid user choices
invalid_choice_handler:
    ; Check if the user's choice is valid (0-2)
    cmp dword [user_choice], 0
    jl invalid_choice_handler
    cmp dword [user_choice], 2
    jl invalid_choice_handler

    ; Display an error message
    push invalid_choice_msg
    call _printf
    add esp, 4

    ; Return to the main menu
    jmp display_menu

global _main
extern _printf
extern _scanf

_main:
    ; Display a welcome message
    push welcome_msg
    call _printf
    add esp, 4

    ; Jump to the main menu
    jmp display_menu

; Function to display the main menu
display_menu:
    ; Display the main menu options
    push menu_msg
    call _printf
    add esp, 4

    ; Display a prompt and get the user's choice
    push user_choice_prompt
    call _printf
    add esp, 4

    ; Read user's choice and store in user_choice variable
    push user_choice
    push user_choice_format
    call _scanf
    add esp, 8

    ; Check user's choice and perform corresponding action
    cmp dword [user_choice], 0
    je exit_program
    cmp dword [user_choice], 1
    je input_lcd_first_num
    cmp dword [user_choice], 2
    je input_gcf_first_num

    ; Handle invalid choices
    jmp invalid_choice_handler

; Function to get the first number for LCD calculation
input_lcd_first_num:
    ; Display LCD message
    push lcd_msg
    call _printf
    add esp, 4

    ; Display prompt for the first number
    push first_num_prompt
    call _printf
    add esp, 4

    ; Read the first number and store in first_num variable
    push first_num
    push first_num_format
    call _scanf
    add esp, 8

    ; Check if the input is valid (1 to 99)
    cmp dword [first_num], 1
    jl invalid_lcd_input_first_num
    cmp dword [first_num], 99
    jg invalid_lcd_input_first_num

    ; Jump to input_lcd_second_num
    jmp input_lcd_second_num

invalid_lcd_input_first_num:
    ; Display error message for invalid input
    push invalid_input_msg
    call _printf
    add esp, 4

    ; Repeat the input_lcd_first_num section
    jmp input_lcd_first_num

; Function to get the second number for LCD calculation
input_lcd_second_num:
    ; Display prompt for the second number
    push second_num_prompt
    call _printf
    add esp, 4

    ; Read the second number and store in second_num variable
    push second_num
    push second_num_format
    call _scanf
    add esp, 8

    ; Check if the input is valid (1 to 99)
    cmp dword [second_num], 1
    jl invalid_lcd_input_second_num
    cmp dword [second_num], 99
    jg invalid_lcd_input_second_num

    ; Perform LCD calculation
    jmp calculate_lcd

invalid_lcd_input_second_num:
    ; Display error message for invalid input
    push invalid_input_msg
    call _printf
    add esp, 4

    ; Repeat the input_lcd_second_num section
    jmp input_lcd_second_num

; Function to get the first number for GCF calculation
input_gcf_first_num:
    ; Display GCF message
    push gcf_msg
    call _printf
    add esp, 4

    ; Display prompt for the first number
    push first_num_prompt
    call _printf
    add esp, 4

    ; Read the first number and store in first_num variable
    push first_num
    push first_num_format
    call _scanf
    add esp, 8

    ; Check if the input is valid (1 to 99)
    cmp dword [first_num], 1
    jl invalid_gcf_input_first_num
    cmp dword [first_num], 99
    jg invalid_gcf_input_first_num

    ; Jump to input_gcf_second_num
    jmp input_gcf_second_num

invalid_gcf_input_first_num:
    ; Display error message for invalid input
    push invalid_input_msg
    call _printf
    add esp, 4

    ; Repeat the input_gcf_first_num section
    jmp input_gcf_first_num

; Function to get the second number for GCF calculation
input_gcf_second_num:
    ; Display prompt for the second number
    push second_num_prompt
    call _printf
    add esp, 4

    ; Read the second number and store in second_num variable
    push second_num
    push second_num_format
    call _scanf
    add esp, 8

    ; Check if the input is valid (1 to 99)
    cmp dword [second_num], 1
    jl invalid_gcf_input_second_num
    cmp dword [second_num], 99
    jg invalid_gcf_input_second_num

    ; Perform GCF calculation
    jmp calculate_gcf

invalid_gcf_input_second_num:
    ; Display error message for invalid input
    push invalid_input_msg
    call _printf
    add esp, 4

    ; Repeat the input_gcf_second_num section
    jmp input_gcf_second_num

; Function to exit the program
exit_program:
    ; Display exit message
    push exit_msg
    call _printf

    ; Return from the main program
    ret
