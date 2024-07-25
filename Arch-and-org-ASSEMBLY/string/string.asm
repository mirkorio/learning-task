;CS 318 Architecture and Organization 23-1
;Learning Task (Strings)
section .data
  ; Prompts and messages
  prompt_names db 'Hi! We are Group #12.', 10, 0
  prompt_sort db 'This program is intended to change all the vowels in the given string to "e".', 10, 0
  prompt_header db '========= VOWEL REPLACEMENT ========', 10, 0
  prompt_input db 'Enter a string: ', 0
  prompt_output db 'Output: ', 0
  prompt_continue db 'Continue? (Y/N): ', 0

  ; Input and output formats
  inputformat_string db '%s', 0
  inputformat_continue db ' %c', 0

section .bss
  ; Reserved memory for strings and menu choice
  input_string resb 80
  output_string resb 80
  menu_choice resb 1

section .text
global _main
extern _printf
extern _scanf
extern _exit

; Vowel replacement function
_vowel_replacement:
  mov esi, input_string ; Initialize the pointer to the input string
  mov edi, output_string ; Initialize the pointer to the output string

.loop:
  mov al, byte [esi] ; Get the current character
  cmp al, 0 ; Check if the end of the string is reached
  je .end_loop

  ; Check if the current character is a vowel
  cmp al, 'A' ; A
  jle .check_next_vowel
  ; (Repeat for 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u')

.check_next_vowel:
  ; If the current character is a vowel, replace it with 'e'
  mov [edi], al
  inc esi
  inc edi
  jmp .loop

.end_loop:
  ; Terminate the output string
  mov BYTE [edi], 0 ; Terminate the output string

_main:
  ; Display header
  push prompt_header
  call _printf
  add esp, 4

  ; Prompt the user to enter a string
  push prompt_input
  call _printf
  add esp, 4

  ; Read the input string
  push input_string
  push inputformat_string
  call _scanf
  add esp, 8

  ; Call the vowel replacement function
  call _vowel_replacement

  ; Display the output string
  push prompt_output
  call _printf
  add esp, 4
  push output_string
  call _printf
  add esp, 4

  ; Ask the user if they want to continue
  push prompt_continue
  call _printf
  add esp, 4

  ; Read the user's choice
  push menu_choice
  push inputformat_continue
  call _scanf
  add esp, 8

  ; Check if the user wants to continue
  movzx eax, byte [menu_choice]
  cmp eax, 'Y'
  je _main ; If yes, go back to the main loop
  jmp _exit ; If no, exit the program
