section .data
    greetingPrompt db '=-=-=-=-=- Simple Temperature Converter -=-=-=-=-=', 10, 0
    celsiusToKelvinPrompt db '+_+_+_+_+_ Celsius to Kelvin Conversion _+_+_+_+_+', 10, 0
    kelvinToCelsiusPrompt db '+_+_+_+_+ Kelvin to Celsius Conversion +_+_+_+_+', 10, 0
    fahrenheitToKelvinPrompt db '+=+=+=+=+= Fahrenheit to Kelvin Conversion =+=+=+=+=+', 10, 0
    kelvinToFahrenheitPrompt db '=+=+=+=+=+ Kelvin to Fahrenheit Conversion +=+=+=+=+=', 10, 0
    celsiusToFahrenheitPrompt db '-+-+-+-+-+ Celsius to Fahrenheit Conversion +-+-+-+-+-', 10, 0
    fahrenheitToCelsiusPrompt db '+-+-+-+-+- Fahrenheit to Celsius Conversion -+-+-+-+-+', 10, 0
    menuChoice0 db '[0] Exit', 10, 0
    menuChoice1 db '[1] Celsius to Kelvin', 10, 0
    menuChoice2 db '[2] Celsius to Fahrenheit', 10, 0
    menuChoice3 db '[3] Kelvin to Celsius', 10, 0
    menuChoice4 db '[4] Kelvin to Fahrenheit', 10, 0
    menuChoice5 db '[5] Fahrenheit to Celsius', 10, 0
    menuChoice6 db '[6] Fahrenheit to Kelvin', 10, 0
    menuChoice7 db 'Please enter choice (0 - 6): ', 0, 0
    userInputChoice db '%d', 0 
    userNumber db 'Please enter your number: ', 0, 0
    userInputNumber dq '%lf', 0
    resultForGeneral dq 'Result: %0.2lf', 0
    newLine db '', 10, 0
    thanks db 'Thanks for using this converter!', 10, 0
    additionConversionConstant dq 273.15
    additionConversionConstant1 dq 32.0
    multiplicationConversionConstant dq 1.8
    conversionConstantMultiplier dq 5.0
    conversionConstantDivisor dq 9.0
    invalidInputPrompt db 'Invalid input. Please enter a valid input. (0 - 6).', 10, 0
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

greeting:
    push greetingPrompt
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

enterChoicePrompt:
    push menuChoice7
    call _printf
    add esp, 4

    push inputChoice
    push userInputChoice
    call _scanf
    add esp, 8

    cmp dword [inputChoice], 0
    jl error_1
    cmp dword [inputChoice], 6
    jg error_1
    cmp dword [inputChoice], 0
    je exit
    cmp dword [inputChoice], 1
    je celsiusToKelvinPromptReal
    cmp dword [inputChoice], 2
    je celsiusToFahrenheitPromptReal
    cmp dword [inputChoice], 3
    je kelvinToCelsiusPromptReal
    cmp dword [inputChoice], 4
    je kelvinToFahrenheitPromptReal
    cmp dword [inputChoice], 5
    je fahrenheitToKelvinPromptReal
    cmp dword [inputChoice], 6
    je fahrenheitToCelsiusPromptReal

celsiusToKelvinPromptReal:
    push celsiusToKelvinPrompt
    call _printf
    add esp, 8

    jmp enterNumber

celsiusToFahrenheitPromptReal:
    push celsiusToFahrenheitPrompt
    call _printf
    add esp, 8

    jmp enterNumber

kelvinToCelsiusPromptReal:
    push kelvinToCelsiusPrompt
    call _printf
    add esp, 8

    jmp enterNumber

kelvinToFahrenheitPromptReal:
    push kelvinToFahrenheitPrompt
    call _printf
    add esp, 8

    jmp enterNumber

fahrenheitToKelvinPromptReal:
    push fahrenheitToKelvinPrompt
    call _printf
    add esp, 8

    jmp enterNumber

fahrenheitToCelsiusPromptReal:
    push fahrenheitToCelsiusPrompt
    call _printf
    add esp, 8

    jmp enterNumber

enterNumber:
    push userNumber
    call _printf

    push inputNumber
    push userInputNumber
    call _scanf
    add esp, 8

    cmp dword [inputChoice], 1
    je celsiusToKelvinPromptReallyReal
    cmp dword [inputChoice], 2
    je celsiusToFahrenheitPromptReallyReal
    cmp dword [inputChoice], 3
    je kelvinToCelsiusPromptReallyReal
    cmp dword [inputChoice], 4
    je kelvinToFahrenheitPromptReallyReal
    cmp dword [inputChoice], 5
    je fahrenheitToKelvinPromptReallyReal
    cmp dword [inputChoice], 6
    je fahrenheitToCelsiusPromptReallyReal

celsiusToKelvinPromptReallyReal:
    movsd xmm0, qword [inputNumber]
    movsd xmm1, qword [additionConversionConstant]
    addsd xmm0, xmm1

    jmp realResults

celsiusToFahrenheitPromptReallyReal:
    movsd xmm0, qword [inputNumber]
    movsd xmm1, qword [additionConversionConstant1]
    movsd xmm2, qword [multiplicationConversionConstant]
    mulsd xmm0, xmm2
    addsd xmm0, xmm1

    jmp realResults

kelvinToCelsiusPromptReallyReal:
    movsd xmm0, qword [inputNumber]
    movsd xmm1, qword [additionConversionConstant]
    subsd xmm0, xmm1

    jmp realResults

kelvinToFahrenheitPromptReallyReal:
    movsd xmm0, qword [inputNumber]
    movsd xmm1, qword [additionConversionConstant]
    movsd xmm2, qword [multiplicationConversionConstant]
    movsd xmm3, qword [additionConversionConstant1]
    subsd xmm0, xmm1
    mulsd xmm0, xmm2
    addsd xmm0, xmm3

    jmp realResults

fahrenheitToKelvinPromptReallyReal:
    movsd xmm0, qword [inputNumber]
    movsd xmm1, qword [conversionConstantDivisor]
    movsd xmm2, qword [conversionConstantMultiplier]
    movsd xmm3, qword [additionConversionConstant1]
    subsd xmm0, xmm3
    mulsd xmm0, xmm2
    divsd xmm0, xmm1    

    jmp realResults

fahrenheitToCelsiusPromptReallyReal:
    movsd xmm0, qword [inputNumber]
    movsd xmm1, qword [additionConversionConstant1]
    movsd xmm2, qword [conversionConstantMultiplier]
    movsd xmm3, qword [conversionConstantDivisor]
    movsd xmm4, qword [additionConversionConstant]
    subsd xmm0, xmm1
    mulsd xmm0, xmm2
    divsd xmm0, xmm3
    addsd xmm0, xmm4

    jmp realResults

realResults:
    sub esp, 8  ; Adjust the stack pointer to make space for the float value
    movsd qword [esp], xmm0  ; Store the double-precision value on the stack
    push dword [esp + 4]
    push dword [esp]  ; Push the address of the double-precision value on the stack
    push resultForGeneral
    call _printf
    add esp, 8  ; Adjust the stack pointer to remove the double-precision value
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

error_1:
    push invalidInputPrompt
    call _printf
    add esp, 4

    jmp enterChoicePrompt

error_2:   
    push invalidInputPrompt1
    call _printf
    add esp, 4

    jmp enterNumber

exit:
    push thanks
    call _printf
    add esp, 4
    
    ret