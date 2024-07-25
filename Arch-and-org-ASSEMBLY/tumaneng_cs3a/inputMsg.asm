section .data
    prompt_name db 'What is your name? ', 0
    input_name db '%s', 0
    
    prompt_age db 'How old are you? ', 0
    input_age db '%s', 0
 
    prompt_address db 'Where do you live? ', 0
    input_address db '%s', 0

    newline db 10, 0

    output_message db 'Nice to meet you, %s, %s years old, who lives at %s', 10, 0

section .bss
    userInput resb 100    ; Buffer to store user input
    name resb 100
    age resb 100
    address resb 100

section .text
    global _main
    extern _printf
    extern _scanf

_main:
    ; Display a prompt for the name
    push prompt_name
    call _printf
    add esp, 4

    ; Read user input for the name
    push name
    push input_name
    call _scanf
    add esp, 8

    ; Display a prompt for the age
    push prompt_age
    call _printf
    add esp, 4

    ; Read user input for the age
    push age
    push input_age
    call _scanf
    add esp, 8

    ; Display a prompt for the address
    push prompt_address
    call _printf
    add esp, 4

    ; Read user input for the address
    push address
    push input_address
    call _scanf
    add esp, 8

    ; Display the formatted output message
    push address
    push age
    push name
    push output_message
    call _printf
    add esp, 16

    ; Print a new line
    push newline
    call _printf
    add esp, 4

    ret
