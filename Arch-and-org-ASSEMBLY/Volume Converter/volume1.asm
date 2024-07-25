section .data
    titlePrompt db '========|| SIMPLE VOLUME CONVERTER by GROUP 12 ||========', 10, 0
    literToCubicFeetPrompt db '========== Liter to Cubic Feet Conversion ==========', 10, 0
    literToCubicInchesPrompt db '========== Liter to Cubic Inches Conversion ==========', 10, 0
    literToCubicMetersPrompt db '========== Liter to Cubic Meters Conversion ==========', 10, 0
    cubicFootToLitersPrompt db '========== Cubic Foot to Liters Conversion ==========', 10, 0
    cubicFootToCubicInchesPrompt db '========== Cubic Foot to Cubic Inches Conversion ==========', 10, 0
    cubicFootToCubicMetersPrompt db '========== Cubic Foot to Cubic Meters Conversion ==========', 10, 0
    cubicInchToLitersPrompt db '========== Cubic Inch to Liters Conversion ==========', 10, 0
    cubicInchToCubicFeetPrompt db '========== Cubic Inch to Cubic Feet Conversion ==========', 10, 0
    cubicInchToCubicMetersPrompt db '========== Cubic Inch to Cubic Meters Conversion ==========+', 10, 0
    cubicMeterToLitersPrompt db '========== Cubic Meter to Liters Conversion ==========', 10, 0
    cubicMeterToCubicFeetPrompt db '========== Cubic Meter to Cubic Feet Conversion ==========', 10, 0
    cubicMeterToCubicInchesPrompt db '========== Cubic Meter to Cubic Inches Conversion ==========', 10, 0
    menuChoice0 db '[0] Exit', 10, 0
    menuChoice1 db '[1] Liter to Cubic Feet', 10, 0
    menuChoice2 db '[2] Liter to Cubic Inches', 10, 0
    menuChoice3 db '[3] Liter to Cubic Meters', 10, 0
    menuChoice4 db '[4] Cubic Foot to Liters', 10, 0
    menuChoice5 db '[5] Cubic Foot to Cubic Inches', 10, 0
    menuChoice6 db '[6] Cubic Foot to Cubic Meters', 10, 0
    menuChoice7 db '[7] Cubic Inch to Liters', 10, 0
    menuChoice8 db '[8] Cubic Inch to Cubic Feet', 10, 0
    menuChoice9 db '[9] Cubic Inch to Cubic Meters', 10, 0
    menuChoice10 db '[10] Cubic Meter to Liters', 10, 0
    menuChoice11 db '[11] Cubic Meter to Cubic Feet', 10, 0
    menuChoice12 db '[12] Cubic Meter to Cubic Inches', 10, 0
    menuChoice13 db 'Please enter choice (0 - 13): ', 0, 0
    userInputChoice db '%d', 0 
    userNumber db 'Please enter your number: ', 0, 0
    userInputNumber dq '%lf', 0
    resultForGeneral dq 'Result: %0.2lf', 10, 0
    newLine db '', 10, 0
    thanks db 'Thanks for using this converter!', 10, 0
    literToCubicFeetConstant dq 0.0353147
    literToCubicInchesConstant dq 61.0237
    literToCubicMetersConstant dq 0.001
    cubicFootToLitersConstant dq 28.3168
    cubicFootToCubicInchesConstant dq 1728
    cubicFootToCubicMetersConstant dq 0.0283168
    cubicInchToLitersConstant dq 0.0163871
    cubicInchToCubicFeetConstant dq 0.000578704
    cubicInchToCubicMetersConstant dq 0.0000163871
    cubicMeterToLitersConstant dq 1000
    cubicMeterToCubicFeetConstant dq 35.3147
    cubicMeterToCubicInchesConstant dq 61023.7
    invalidInputPrompt db 'Invalid input. Please enter a valid input. (0 - 13).', 10, 0
    invalidInputPrompt1 db 'Invalid input. Please enter any number.', 10, 0
    enterInputToConvertAgain db 'Do you want to convert again? (1/0): ', 0, 0
    invalidInputPrompt2 db 'Invalid input. Please enter a valid input. (0 or 1).', 10, 0
    enteredInputToConvertAgain db '%d', 0
    invalidInputPrompt3 db 'String input detected. Please enter a numeric input.', 10, 0

section .bss
    inputChoice resd 1
    inputNumber resq 1
    result resq 1
    enteredInputToConvertAgainValue resd 1

section .text
    global _main
    extern _printf
    extern _scanf

_main:

title:
    push titlePrompt
    call _printf
    add esp, 4

menu:
    push menuChoice0
    call _printf
    add esp, 8
    push menuChoice1
    call _printf
    add esp, 8
    push menuChoice2
    call _printf
    add esp, 8
    push menuChoice3
    call _printf
    add esp, 8
    push menuChoice4
    call _printf
    add esp, 8
    push menuChoice5
    call _printf
    add esp, 8
    push menuChoice6
    call _printf
    add esp, 8
    push menuChoice7
    call _printf
    add esp, 8
    push menuChoice8
    call _printf
    add esp, 8
    push menuChoice9
    call _printf
    add esp, 8
    push menuChoice10
    call _printf
    add esp, 8
    push menuChoice11
    call _printf
    add esp, 8
    push menuChoice12
    call _printf
    add esp, 8

enterChoicePrompt:
    push menuChoice13
    call _printf
    add esp, 4

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
    je literToCubicFeetPromptReal
    cmp dword [inputChoice], 2
    je literToCubicInchesPromptReal
    cmp dword [inputChoice], 3
    je literToCubicMetersPromptReal
    cmp dword [inputChoice], 4
    je cubicFootToLitersPromptReal
    cmp dword [inputChoice], 5
    je cubicFootToCubicInchesPromptReal
    cmp dword [inputChoice], 6
    je cubicFootToCubicMetersPromptReal
    cmp dword [inputChoice], 7
    je cubicInchToLitersPromptReal
    cmp dword [inputChoice], 8
    je cubicInchToCubicFeetPromptReal
    cmp dword [inputChoice], 9
    je cubicInchToCubicMetersPromptReal
    cmp dword [inputChoice], 10
    je cubicMeterToLitersPromptReal
    cmp dword [inputChoice], 11
    je cubicMeterToCubicFeetPromptReal
    cmp dword [inputChoice], 12
    je cubicMeterToCubicInchesPromptReal
    jmp error_1

literToCubicFeetPromptReal:
    ; Print the conversion prompt
    push literToCubicFeetPrompt
    call _printf
    add esp, 8

    ; Jump to the section where the user enters the number
    jmp enterNumber

literToCubicInchesPromptReal:
    ; Print the conversion prompt
    push literToCubicInchesPrompt
    call _printf
    add esp, 8

    ; Jump to the section where the user enters the number
    jmp enterNumber

literToCubicMetersPromptReal:
    ; Print the conversion prompt
    push literToCubicMetersPrompt
    call _printf
    add esp, 8

    ; Jump to the section where the user enters the number
    jmp enterNumber

cubicFootToLitersPromptReal:
    ; Print the conversion prompt
    push cubicFootToLitersPrompt
    call _printf
    add esp, 8

    ; Jump to the section where the user enters the number
    jmp enterNumber

cubicFootToCubicInchesPromptReal:
    ; Print the conversion prompt
    push cubicFootToCubicInchesPrompt
    call _printf
    add esp, 8

    ; Jump to the section where the user enters the number
    jmp enterNumber

cubicFootToCubicMetersPromptReal:
    ; Print the conversion prompt
    push cubicFootToCubicMetersPrompt
    call _printf
    add esp, 8

    ; Jump to the section where the user enters the number
    jmp enterNumber

cubicInchToLitersPromptReal:
    ; Print the conversion prompt
    push cubicInchToLitersPrompt
    call _printf
    add esp, 8

    ; Jump to the section where the user enters the number
    jmp enterNumber

cubicInchToCubicFeetPromptReal:
    ; Print the conversion prompt
    push cubicInchToCubicFeetPrompt
    call _printf
    add esp, 8

    ; Jump to the section where the user enters the number
    jmp enterNumber

cubicInchToCubicMetersPromptReal:
    ; Print the conversion prompt
    push cubicInchToCubicMetersPrompt
    call _printf
    add esp, 8

    ; Jump to the section where the user enters the number
    jmp enterNumber


cubicMeterToLitersPromptReal:
    ; Print the conversion prompt
    push cubicMeterToLitersPrompt
    call _printf
    add esp, 8

    ; Jump to the section where the user enters the number
    jmp enterNumber

cubicMeterToCubicFeetPromptReal:
    ; Print the conversion prompt
    push cubicMeterToCubicFeetPrompt
    call _printf
    add esp, 8

    ; Jump to the section where the user enters the number
    jmp enterNumber

cubicMeterToCubicInchesPromptReal:
    ; Print the conversion prompt
    push cubicMeterToCubicInchesPrompt
    call _printf
    add esp, 8

    ; Jump to the section where the user enters the number
    jmp enterNumber

enterNumber:
    push userNumber
    call _printf

    push inputNumber
    push userInputNumber
    call _scanf
    add esp, 8

    ; Compare the inputChoice to determine the conversion to perform
    cmp dword [inputChoice], 1
    je literToCubicFeetPromptReallyReal
    cmp dword [inputChoice], 2
    je literToCubicInchesPromptReallyReal
    cmp dword [inputChoice], 3
    je literToCubicMetersPromptReallyReal
    cmp dword [inputChoice], 4
    je cubicFootToLitersPromptReallyReal
    cmp dword [inputChoice], 5
    je cubicFootToCubicInchesPromptReallyReal
    cmp dword [inputChoice], 6
    je cubicFootToCubicMetersPromptReallyReal
    cmp dword [inputChoice], 7
    je cubicInchToLitersPromptReallyReal
    cmp dword [inputChoice], 8
    je cubicInchToCubicFeetPromptReallyReal
    cmp dword [inputChoice], 9
    je cubicInchToCubicMetersPromptReallyReal
    cmp dword [inputChoice], 10
    je cubicMeterToLitersPromptReallyReal
    cmp dword [inputChoice], 11
    je cubicMeterToCubicFeetPromptReallyReal
    cmp dword [inputChoice], 12
    je cubicMeterToCubicInchesPromptReallyReal

literToCubicFeetPromptReallyReal:
    ; Implement the conversion logic for Liter to Cubic Feet
    movsd xmm0, qword [inputNumber]
    mulsd xmm0, qword [literToCubicFeetConstant]
    jmp realResults

literToCubicInchesPromptReallyReal:
    ; Implement the conversion logic for Liter to Cubic Inches
    movsd xmm0, qword [inputNumber]
    mulsd xmm0, qword [literToCubicInchesConstant]
    jmp realResults

literToCubicMetersPromptReallyReal:
    ; Implement the conversion logic for Liter to Cubic Meters
    movsd xmm0, qword [inputNumber]
    mulsd xmm0, qword [literToCubicMetersConstant]
    jmp realResults

cubicFootToLitersPromptReallyReal:
    ; Implement the conversion logic for Cubic Foot to Liters
    movsd xmm0, qword [inputNumber]
    mulsd xmm0, qword [cubicFootToLitersConstant]
    jmp realResults

cubicFootToCubicInchesPromptReallyReal:
    ; Implement the conversion logic for Cubic Foot to Cubic Inches
    movsd xmm0, qword [inputNumber]
    mulsd xmm0, qword [cubicFootToCubicInchesConstant]
    jmp realResults

cubicFootToCubicMetersPromptReallyReal:
    ; Implement the conversion logic for Cubic Foot to Cubic Meters
    movsd xmm0, qword [inputNumber]
    mulsd xmm0, qword [cubicFootToCubicMetersConstant]
    jmp realResults

cubicInchToLitersPromptReallyReal:
    ; Implement the conversion logic for Cubic Inch to Liters
    movsd xmm0, qword [inputNumber]
    mulsd xmm0, qword [cubicInchToLitersConstant]
    jmp realResults

cubicInchToCubicFeetPromptReallyReal:
    ; Implement the conversion logic for Cubic Inch to Cubic Feet
    movsd xmm0, qword [inputNumber]
    mulsd xmm0, qword [cubicInchToCubicFeetConstant]
    jmp realResults

cubicInchToCubicMetersPromptReallyReal:
    ; Implement the conversion logic for Cubic Inch to Cubic Meters
    movsd xmm0, qword [inputNumber]
    mulsd xmm0, qword [cubicInchToCubicMetersConstant]
    jmp realResults

cubicMeterToLitersPromptReallyReal:
    ; Implement the conversion logic for Cubic Meter to Liters
    movsd xmm0, qword [inputNumber]
    mulsd xmm0, qword [cubicMeterToLitersConstant]
    jmp realResults

cubicMeterToCubicFeetPromptReallyReal:
    ; Implement the conversion logic for Cubic Meter to Cubic Feet
    movsd xmm0, qword [inputNumber]
    mulsd xmm0, qword [cubicMeterToCubicFeetConstant]
    jmp realResults

cubicMeterToCubicInchesPromptReallyReal:
    ; Implement the conversion logic for Cubic Meter to Cubic Inches
    movsd xmm0, qword [inputNumber]
    mulsd xmm0, qword [cubicMeterToCubicInchesConstant]
    jmp realResults

realResults:
    ; Display the result
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

error_2:   
    ; Display an error message for invalid input
    push invalidInputPrompt2
    call _printf
    add esp, 4

    ; Go back to the main menu
    jmp enterChoicePrompt

error_1:
    ; Display an error message for invalid input
    push invalidInputPrompt
    call _printf
    add esp, 4

    ; Go back to the main menu
    jmp enterChoicePrompt

exit:
    ; Display a farewell message
    push thanks
    call _printf
    add esp, 4
    
    ; Exit the program
    ret
