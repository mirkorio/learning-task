;CS 318 – Architecture and Organization || LEARNING TASK (ARRAYS)

section .data
    ; Data section with prompt messages and variables
    prompt_welcome db "Hi! We are Peter, Robert, and Marc.", 10, 0
    prompt_welcome2 db "This program is intended to sort numbers using Selection Sort.", 10, 0
    prompt_title db "===== SELECTION SORT by Peter, Robert, and Marc =====", 10, 0
    prompt_input db "Enter one-digit number: ", 0
    instr db '%d', 0
    prompt_output dd "Sorted array: ", 0
    outstr dd '%d ', 0
    prompt_continue db "Continue? (Y/N): ", 0
    choice db '%s', 0
    exit_msg db "Thank you!", 10, 0
    error_msg db "Input should be a one-digit number. Please enter a valid input.", 10, 0
    inv_msg db "Please type Y/N only", 10, 0
    newline db 10, 0

    ; Arrays and variables
    sort times 20 db 1
    sortednum times 200 db 0
    val dd 0
    val1 dd 0
    val2 dd 10

section .bss
    ; Uninitialized variables
    array resb 1  ; Assuming a maximum of 10 elements in the array
    user_choice resb 2
    sorted_values resb 100
    
section .text
    global _main
    extern _printf
    extern _scanf
    extern _exit

_main:
    ; Program entry point
    ; Display welcome messages
    push newline
    call _printf
    add esp, 4

    push prompt_welcome
    call _printf
    add esp, 4

    push newline
    call _printf
    add esp, 4

    push prompt_welcome2
    call _printf
    add esp, 4

main_loop:

    ; Main loop
    push newline
    call _printf
    add esp, 4

    push prompt_title
    call _printf
    add esp, 4

    push newline
    call _printf
    add esp, 4

    push prompt_input
    call _printf
    add esp, 4

    ; Input handling
    push array
    push instr
    call _scanf
    add esp, 8

    push newline
    call _printf
    add esp, 4

    ; Validate input
    cmp byte [array], 1
    je valid_input
    cmp byte [array], 2
    je valid_input
    cmp byte [array], 3
    je valid_input
    cmp byte [array], 4
    je valid_input
    cmp byte [array], 5
    je valid_input
    cmp byte [array], 6
    je valid_input
    cmp byte [array], 7
    je valid_input
    cmp byte [array], 8
    je valid_input
    cmp byte [array], 9
    je valid_input
   
    call msg_function
    
    jmp main_loop

    ; Display error message for invalid input
    push newline
    call _printf
    add esp, 4

msg_function:   
    push error_msg
    call _printf
    add esp, 4
    
    jmp main_loop

valid_input:
    ; Display prompt for sorted output
    push prompt_output
    call _printf
    add esp, 4

    jmp append

append:
     ; Append an element to the array
     mov eax, [array]
     mov ebx, [val]
     mov [sort+ebx], eax
     mov ecx, ebx ; this is to increment or add 4 to the counter
     add ecx, 4
     mov [val], ecx
     mov edx, [val1] ; this is to increment or add 1 to counter1
     add edx, 1
     mov [val1], edx
     add esp, 8

selection_sort:
    ; Selection sort algorithm
    mov ecx, [val1]       
    dec ecx
    
    mov esi, 0

outer_loop:
    mov edi, esi
    inc edi
inner_loop:
    mov eax, [sort + esi * 4] ; num1[i]
    mov ebx, [sort + edi * 4] ; num1[j]

    cmp eax, ebx
    jng not_greater ; jump if not greater (unsigned comparison)

    ; swap num1[i] and num1[j]
    mov edx, eax
    mov [sort + esi * 4], ebx
    mov [sort + edi * 4], edx

not_greater:
    inc edi ; move to the next element in the inner loop
    cmp edi, ecx ; check if we reached the end of the array
    jl inner_loop ; jump to the inner loop if not

    inc esi ; move to the next element in the outer loop
    cmp esi, ecx ; check if we reached the end of the array
    jl outer_loop ; jump to the outer loop if not

print_array_loop:

    ; Print sorted array
    push ebp
    mov ebp, esp
    mov eax, [val1]
    mov ebx, sort ; point bx to the first number
    mov ecx, 0    ; load 0

loop:
    ; store the value because external function like printf modify the value
    push ebx
    push eax
    push ecx

    ; print the value stored on the stack
    push dword [ebx]
    push outstr
    call _printf
    ; clear the stack
    add esp, 8

    ; restore these values
    pop ecx
    pop eax
    pop ebx

    ; increment the counter
    inc ecx
    ; add 4 bytes to ebx
    add ebx, 4
    ; compare value stored in ecx and eax
    cmp ecx, eax
    jne loop

    ; destroy the stack
    mov esp, ebp
    pop ebp

    push newline
    call _printf
    add esp, 4

continue_prompt:

    ; Continue prompt
    push newline
    call _printf
    add esp, 4
    
    push prompt_continue
    call _printf
    add esp, 4

    ; User input for continuing or exiting
    push user_choice
    push choice
    call _scanf
    add esp, 8

    cmp byte [user_choice], 'N'
    je exit
    cmp byte [user_choice], 'n'
    je exit

    cmp byte [user_choice], 'Y'
    je next_iteration
    cmp byte [user_choice], 'y'
    je next_iteration

    call error_function
    jmp continue_prompt

next_iteration:
    ; Jump to the next iteration of the main loop
    jmp main_loop

error_function:
    ; Display error message for invalid choice
    push inv_msg
    call _printf
    add esp, 4
    
    ret
      
exit:
    ; Display exit message and terminate program
    push exit_msg
    call _printf
    add esp, 4

    call _exit

