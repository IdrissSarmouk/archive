#What will be printed in what order by the code in Figure 3.6? And at what absolute
memory address will the ASCII character ’C’ be stored? You may find it useful to modify
the code to confirm your expectation, but be sure to explain why it is this address.

;
; A simple boot sector program that demonstrates the stack.
;
mov ah , 0 x0e ; int 10/ ah = 0eh -> scrolling teletype BIOS routine
mov bp , 0 x8000 ; Set the base of the stack a little above where BIOS
mov sp , bp ; loads our boot sector - so it won ’t overwrite us.
push ’A ’ ; Push some characters on the stack for later
push ’B ’ ; retreival. Note , these are pushed on as
push ’C ’ ; 16 - bit values , so the most significant byte
; will be added by our assembler as 0 x00.
pop bx ; Note , we can only pop 16 - bits , so pop to bx
mov al , bl ; then copy bl ( i.e. 8- bit char ) to al
int 0 x10 ; print (al)
pop bx ; Pop the next value
mov al , bl
int 0 x10 ; print (al)
mov al , [0 x7ffe ] ; To prove our stack grows downwards from bp ,
; fetch the char at 0 x8000 - 0x2 ( i.e. 16 - bits )
int 0 x10 ; print (al)
jmp $ ; Jump forever.
; Padding and magic BIOS number.
times 510 -( $ - $$ ) db 0
dw 0 xaa55
