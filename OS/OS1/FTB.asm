#Find The Byte Program reserves a byte of data for a character then prints out that character on the screen

mov ah , 0 x0e 

#First attempt
mov al , the_secret
int 0 x10 

#Second attempt
mov al , [ the_secret ]
int 0 x10 

#Third attempt
mov bx , the_secret
add bx , 0 x7c00
mov al , [bx]
int 0 x10


#Fourth attempt
mov al , [0 x7c1e ]
int 0 x10 
jmp $ 
the_secret :
db "X "


times 510 -( $ - $$ ) db 0
dw 0 xaa55
