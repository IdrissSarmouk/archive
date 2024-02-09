It’s always useful to plan your conditional code in terms of a higher level language, then
replace it with the assembly instructions. Have a go at converting this pseudo assembly
code into full assembly code, using cmp and appropriate jump instructions. Test it with
different values of bx. Fully comment your code, in your own words.
mov bx , 30
if (bx <= 4) {
mov al , ’A ’
} else if (bx < 40) {
mov al , ’B ’
} else {
mov al , ’C ’
}
mov ah , 0 x0e ; int =10/ ah =0 x0e -> BIOS tele - type output
int 0 x10 ; print the character in al
jmp $
; Padding and magic number.
times 510 -( $ - $$ ) db 0
dw 0 xaa55
