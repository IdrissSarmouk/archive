#A Hello, World boot sector assembly program
#For good marks, make sure the function is careful when modifying registers and that
you fully comment the code to demonstrate your understanding.

#Put together all of the ideas in this section to make a self-contained function for printing
null-terminated strings, that can be used as follows:


#Put together all of the ideas in this section to make a self-contained function for printing
null-terminated strings, that can be used as follows:


#A boot sector that prints a string using our function.
;
[ org 0 x7c00 ] ; Tell the assembler where this code will be loaded
mov bx , HELLO_MSG ; Use BX as a parameter to our function , so
call print_string ; we can specify the address of a string.
mov bx , GOODBYE_MSG
call print_string
jmp $ ; Hang
% include " print_string.asm "
; Data
HELLO_MSG :
db ’ Hello , World ! ’ , 0 ; <-- The zero on the end tells our routine
; when to stop printing characters.
GOODBYE_MSG :
db ’ Goodbye ! ’, 0
; Padding and magic number.
times 510 -( $ - $$ ) db 0
dw 0 xaa55
