;SIMPLE VOLUME CONVERTER by GROUP 12 
;CS 318 Architecture and Organization 23-1
;Final Project (Computer Program Project)

; Section containing data, including menu messages, conversion constants, and prompts
section .data   
    menu_msg db '========|| SIMPLE VOLUME CONVERTER by GROUP 12 ||========', 0xA
    	     db '[0] Exit', 0xA
    	     db '[1] Liter to Cubic Feet', 0xA
    	     db '[2] Liter to Cubic Inches', 0xA
    	     db '[3] Liter to Cubic Meters', 0xA
   	     db '[4] Cubic Foot to Liters', 0xA
  	     db '[5] Cubic Foot to Cubic Inches', 0xA
    	     db '[6] Cubic Foot to Cubic Meters', 0xA
    	     db '[7] Cubic Inch to Liters', 0xA
    	     db '[8] Cubic Inch to Cubic Feet', 0xA
    	     db '[9] Cubic Inch to Cubic Meters', 0xA
    	     db '[10] Cubic Meter to Liters', 0xA
    	     db '[11] Cubic Meter to Cubic Feet', 0xA
    	     db '[12] Cubic Meter to Cubic Inches', 10, 0
    menuChoice db 'Enter choice (0 - 12): ', 0, 0
    userInputChoice db '%d', 0 
    literToCubicFeetPrompt db '==========|| Liter to Cubic Feet Conversion||==========', 10, 0
    literToCubicInchesPrompt db '==========|| Liter to Cubic Inches Conversion||==========', 10, 0
    literToCubicMetersPrompt db '==========|| Liter to Cubic Meters Conversion||==========', 10, 0
    cubicFootToLitersPrompt db '==========|| Cubic Foot to Liters Conversion||==========', 10, 0
    cubicFootToCubicInchesPrompt db '==========|| Cubic Foot to Cubic Inches Conversion||==========', 10, 0
    cubicFootToCubicMetersPrompt db '==========|| Cubic Foot to Cubic Meters Conversion||==========', 10, 0
    cubicInchToLitersPrompt db '==========|| Cubic Inch to Liters Conversion ||==========', 10, 0
    cubicInchToCubicFeetPrompt db '==========|| Cubic Inch to Cubic Feet Conversion ||==========', 10, 0
    cubicInchToCubicMetersPrompt db '==========|| Cubic Inch to Cubic Meters Conversion ||==========+', 10, 0
    cubicMeterToLitersPrompt db '==========|| Cubic Meter to Liters Conversion ||==========', 10, 0
    cubicMeterToCubicFeetPrompt db '==========|| Cubic Meter to Cubic Feet Conversion ||==========', 10, 0
    cubicMeterToCubicInchesPrompt db '==========|| Cubic Meter to Cubic Inches Conversion ||==========', 10, 0
    userNumber db 'Enter number to convert: ', 0, 0
    userInputNumber dq '%lf', 0
    resultForGeneral dq 'Result: %0.2lf', 10, 0
    newLine db '', 10, 0
    thanks db '========||Bye, thanks for using this VOLUME CONVERTER!||========', 10, 0
    literToCubicFeetConstant dq 0.0353147
    literToCubicInchesConstant dq 61.0237
    literToCubicMetersConstant dq 0.001
    cubicFootToLitersConstant dq 28.3168
    cubicFootToCubicInchesConstant dq 1728.00
    cubicFootToCubicMetersConstant dq 0.0283168
    cubicInchToLitersConstant dq 0.0163871
    cubicInchToCubicFeetConstant dq 0.000578704
    cubicInchToCubicMetersConstant dq 0.0000163871
    cubicMeterToLitersConstant dq 1000.00
    cubicMeterToCubicFeetConstant dq 35.3147
    cubicMeterToCubicInchesConstant dq 61023.7
    invalidInputPrompt db 'Invalid input. Please enter a valid input. [0 - 12].', 10, 0
    invalidInputPrompt1 db 'Invalid input. Please enter any number.', 10, 0
    enterInputToConvertAgain db 'Convert again? [1 - yes /0 - no]: ', 0, 0
    invalidInputPrompt2 db 'Invalid input. Please enter a valid input. [0 or 1].', 10, 0
    enteredInputToConvertAgain db '%d', 0
    invalidInputPrompt3 db 'String input detected. Please enter a numeric input.', 10, 0

; Section for uninitialized data (BSS section) to store variables
section .bss
    inputChoice resd 1
    inputNumber resq 1
    result resq 1
    enteredInputToConvertAgainValue resd 1

; Main program section
section .text
    global _main
    extern _printf
    extern _scanf

_main:

; Display the main menu
menu:
    push menu_msg
    call _printf
    add esp, 8   

    ; Prompt the user to enter a choice
    enterChoicePrompt:
    push  menuChoice
    call _printf
    add esp, 4

    ; Read and validate user input for the menu choice
    push inputChoice
    push userInputChoice
    call _scanf
    add esp, 8

    cmp dword [inputChoice], 0
    jl error_1
    cmp dword [inputChoice], 12
    jg error_1
    cmp dword [inputChoice], 0
    je exit

   
    cmp dword [inputChoice], 1
    je literToCubicFeetPrompt1
    cmp dword [inputChoice], 2
    je literToCubicInchesPrompt2
    cmp dword [inputChoice], 3
    je literToCubicMetersPrompt3
    cmp dword [inputChoice], 4
    je cubicFootToLitersPrompt4
    cmp dword [inputChoice], 5
    je cubicFootToCubicInchesPrompt5
    cmp dword [inputChoice], 6
    je cubicFootToCubicMetersPrompt6
    cmp dword [inputChoice], 7
    je cubicInchToLitersPrompt7
    cmp dword [inputChoice], 8
    je cubicInchToCubicFeetPrompt8
    cmp dword [inputChoice], 9
    je cubicInchToCubicMetersPrompt9
    cmp dword [inputChoice], 10
    je cubicMeterToLitersPrompt10
    cmp dword [inputChoice], 11
    je cubicMeterToCubicFeetPrompt11
    cmp dword [inputChoice], 12
    je cubicMeterToCubicInchesPrompt12
    jmp error_1

; Sections for different volume conversion prompts
literToCubicFeetPrompt1:
    ; Print the conversion prompt
    push literToCubicFeetPrompt
    call _printf
    add esp, 8

    ; Jump to the section where the user enters the number
    jmp enterNumber

literToCubicInchesPrompt2:
    ; Print the conversion prompt
    push literToCubicInchesPrompt
    call _printf
    add esp, 8

    ; Jump to the section where the user enters the number
    jmp enterNumber

literToCubicMetersPrompt3:
    ; Print the conversion prompt
    push literToCubicMetersPrompt
    call _printf
    add esp, 8

    ; Jump to the section where the user enters the number
    jmp enterNumber

cubicFootToLitersPrompt4:
    ; Print the conversion prompt
    push cubicFootToLitersPrompt
    call _printf
    add esp, 8

    ; Jump to the section where the user enters the number
    jmp enterNumber

cubicFootToCubicInchesPrompt5:
    ; Print the conversion prompt
    push cubicFootToCubicInchesPrompt
    call _printf
    add esp, 8

    ; Jump to the section where the user enters the number
    jmp enterNumber

cubicFootToCubicMetersPrompt6:
    ; Print the conversion prompt
    push cubicFootToCubicMetersPrompt
    call _printf
    add esp, 8

    ; Jump to the section where the user enters the number
    jmp enterNumber

cubicInchToLitersPrompt7:
    ; Print the conversion prompt
    push cubicInchToLitersPrompt
    call _printf
    add esp, 8

    ; Jump to the section where the user enters the number
    jmp enterNumber

cubicInchToCubicFeetPrompt8:
    ; Print the conversion prompt
    push cubicInchToCubicFeetPrompt
    call _printf
    add esp, 8

    ; Jump to the section where the user enters the number
    jmp enterNumber

cubicInchToCubicMetersPrompt9:
    ; Print the conversion prompt
    push cubicInchToCubicMetersPrompt
    call _printf
    add esp, 8

    ; Jump to the section where the user enters the number
    jmp enterNumber


cubicMeterToLitersPrompt10:
    ; Print the conversion prompt
    push cubicMeterToLitersPrompt
    call _printf
    add esp, 8

    ; Jump to the section where the user enters the number
    jmp enterNumber

cubicMeterToCubicFeetPrompt11:
    ; Print the conversion prompt
    push cubicMeterToCubicFeetPrompt
    call _printf
    add esp, 8

    ; Jump to the section where the user enters the number
    jmp enterNumber

cubicMeterToCubicInchesPrompt12:
    ; Print the conversion prompt
    push cubicMeterToCubicInchesPrompt
    call _printf
    add esp, 8

    ; Jump to the section where the user enters the number
    jmp enterNumber

; Section for user input of the number to be converted
enterNumber:
    push userNumber
    call _printf

    push inputNumber
    push userInputNumber
    call _scanf
    add esp, 8
    
    ; Check if the input is a valid number
    mov eax, dword [userInputNumber]
    cmp eax, 0
    jl error_3
    

    ; Compare the inputChoice to determine the conversion to perform
    cmp dword [inputChoice], 1
    je literToCubicFeetPrompt_1
    cmp dword [inputChoice], 2
    je literToCubicInchesPrompt_2
    cmp dword [inputChoice], 3
    je literToCubicMetersPrompt_3
    cmp dword [inputChoice], 4
    je cubicFootToLitersPrompt_4
    cmp dword [inputChoice], 5
    je cubicFootToCubicInchesPrompt_5
    cmp dword [inputChoice], 6
    je cubicFootToCubicMetersPrompt_6
    cmp dword [inputChoice], 7
    je cubicInchToLitersPrompt_7
    cmp dword [inputChoice], 8
    je cubicInchToCubicFeetPrompt_8
    cmp dword [inputChoice], 9
    je cubicInchToCubicMetersPrompt_9
    cmp dword [inputChoice], 10
    je cubicMeterToLitersPrompt_10
    cmp dword [inputChoice], 11
    je cubicMeterToCubicFeetPrompt_11
    cmp dword [inputChoice], 12
    je cubicMeterToCubicInchesPrompt_12

literToCubicFeetPrompt_1:
    ; Implement the conversion logic for Liter to Cubic Feet
    movsd xmm0, qword [inputNumber]
    mulsd xmm0, qword [literToCubicFeetConstant]
    jmp realResults

literToCubicInchesPrompt_2:
    ; Implement the conversion logic for Liter to Cubic Inches
    movsd xmm0, qword [inputNumber]
    mulsd xmm0, qword [literToCubicInchesConstant]
    jmp realResults

literToCubicMetersPrompt_3:
    ; Implement the conversion logic for Liter to Cubic Meters
    movsd xmm0, qword [inputNumber]
    mulsd xmm0, qword [literToCubicMetersConstant]
    jmp realResults

cubicFootToLitersPrompt_4:
    ; Implement the conversion logic for Cubic Foot to Liters
    movsd xmm0, qword [inputNumber]
    mulsd xmm0, qword [cubicFootToLitersConstant]
    jmp realResults

cubicFootToCubicInchesPrompt_5:
    ; Implement the conversion logic for Cubic Foot to Cubic Inches
    movsd xmm0, qword [inputNumber]
    mulsd xmm0, qword [cubicFootToCubicInchesConstant]
    jmp realResults

cubicFootToCubicMetersPrompt_6:
    ; Implement the conversion logic for Cubic Foot to Cubic Meters
    movsd xmm0, qword [inputNumber]
    mulsd xmm0, qword [cubicFootToCubicMetersConstant]
    jmp realResults

cubicInchToLitersPrompt_7:
    ; Implement the conversion logic for Cubic Inch to Liters
    movsd xmm0, qword [inputNumber]
    mulsd xmm0, qword [cubicInchToLitersConstant]
    jmp realResults

cubicInchToCubicFeetPrompt_8:
    ; Implement the conversion logic for Cubic Inch to Cubic Feet
    movsd xmm0, qword [inputNumber]
    mulsd xmm0, qword [cubicInchToCubicFeetConstant]
    jmp realResults

cubicInchToCubicMetersPrompt_9:
    ; Implement the conversion logic for Cubic Inch to Cubic Meters
    movsd xmm0, qword [inputNumber]
    mulsd xmm0, qword [cubicInchToCubicMetersConstant]
    jmp realResults

cubicMeterToLitersPrompt_10:
    ; Implement the conversion logic for Cubic Meter to Liters
    movsd xmm0, qword [inputNumber]
    mulsd xmm0, qword [cubicMeterToLitersConstant]
    jmp realResults

cubicMeterToCubicFeetPrompt_11:
    ; Implement the conversion logic for Cubic Meter to Cubic Feet
    movsd xmm0, qword [inputNumber]
    mulsd xmm0, qword [cubicMeterToCubicFeetConstant]
    jmp realResults

cubicMeterToCubicInchesPrompt_12:
    ; Implement the conversion logic for Cubic Meter to Cubic Inches
    movsd xmm0, qword [inputNumber]
    mulsd xmm0, qword [cubicMeterToCubicInchesConstant]
    jmp realResults

realResults:
    ; Display the converted result
    sub esp, 8
    movsd qword [esp], xmm0
    push dword [esp + 4]
    push dword [esp]
    push resultForGeneral
    call _printf
    add esp, 8
    push newLine
    call _printf
    add esp, 8
    jmp enterInputToConvert

; Read and validate user input to continue or exit
enterInputToConvert:
    push enterInputToConvertAgain
    call _printf
    
    push enteredInputToConvertAgainValue
    push enteredInputToConvertAgain
    call _scanf
    add esp, 8

    cmp dword [enteredInputToConvertAgainValue], 0
    je menu
    cmp dword [enteredInputToConvertAgainValue], 1
    je enterNumber
    cmp dword [enteredInputToConvertAgainValue], 1
    jg error_2
    cmp dword [enteredInputToConvertAgainValue], 0
    jl error_2

error_1:
    ; Display an error message for invalid input
    push invalidInputPrompt
    call _printf
    add esp, 4

    ; Go back to the main menu
    jmp enterChoicePrompt

error_2:   
    ; Display an error message for invalid input to continue or exit
    push invalidInputPrompt2
    call _printf
    add esp, 4

    ; Go back to the main menu
    jmp enterChoicePrompt

error_3:
    ; Display an error message for string input
    push invalidInputPrompt3
    call _printf
    add esp, 4

    ; Go back to the main menu
    jmp enterChoicePrompt

exit:
    ; Display a exit message
    push thanks
    call _printf
    add esp, 4
    
    ; Exit the program
    ret
