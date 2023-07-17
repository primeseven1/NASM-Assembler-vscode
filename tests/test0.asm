bits 16
org 0x7c00

section .data

section .text
start:
    mov ah, 0x00
    int 0x16
    
    call print
    jmp start

print:
    mov ah, 0x0e
    int 0x10
    ret

times 510-($-$$) db 0
dw 0xAA55