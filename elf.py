"""
# >>>>>>>>>>>>> ELF FILE HEADER <<<<<<<<<<<<<
                # All numbers (except in names) are in base sixteen (hexadecimal)
                # 00 <- number of bytes listed so far
7F 45 4C 46     # 04 e_ident[EI_MAG]: ELF magic number
01              # 05 e_ident[EI_CLASS]: 1: 32-bit, 2: 64-bit
   01           # 06 e_ident[EI_DATA]: 1: little-endian, 2: big-endian
      01        # 07 e_ident[EI_VERSION]: ELF header version; must be 1
         00     # 08 e_ident[EI_OSABI]: Target OS ABI; should be 0

00              # 09 e_ident[EI_ABIVERSION]: ABI version; 0 is ok for Linux
   00 00 00     # 0C e_ident[EI_PAD]: unused, should be 0
00 00 00 00     # 10

02 00           # 12 e_type: object file type; 2: executable
      03 00     # 14 e_machine: instruction set architecture; 3: x86, 3E: amd64
01 00 00 00     # 18 e_version: ELF identification version; must be 1

54 80 04 08     # 1C e_entry: memory address of entry point (where process starts)
34 00 00 00     # 20 e_phoff: file offset where program headers begin

00 00 00 00     # 24 e_shoff: file offset where section headers begin
00 00 00 00     # 28 e_flags: 0 for x86

34 00           # 2A e_ehsize: size of this header (34: 32-bit, 40: 64-bit)
      20 00     # 2C e_phentsize: size of each program header (20: 32-bit, 38: 64-bit)
01 00           # 2E e_phnum: #program headers
      28 00     # 30 e_shentsize: size of each section header (28: 32-bit, 40: 64-bit)

00 00           # 32 e_shnum: #section headers
      00 00     # 34 e_shstrndx: index of section header containing section names

# >>>>>>>>>>>>> ELF PROGRAM HEADER <<<<<<<<<<<<<

01 00 00 00     # 38 p_type: segment type; 1: loadable

54 00 00 00     # 3C p_offset: file offset where segment begins
54 80 04 08     # 40 p_vaddr: virtual address of segment in memory (x86: 08048054)
    
00 00 00 00     # 44 p_paddr: physical address of segment, unspecified by 386 supplement
2C 00 00 00     # 48 p_filesz: size in bytes of the segment in the file image ############

2C 00 00 00     # 4C p_memsz: size in bytes of the segment in memory; p_filesz <= p_memsz
05 00 00 00     # 50 p_flags: segment-dependent flags (1: X, 2: W, 4: R)

00 10 00 00     # 54 p_align: 1000 for x86

# >>>>>>>>>>>>> PROGRAM SEGMENT <<<<<<<<<<<<< 

# Hello, world.

# Linux system calls:   man 2 syscalls; man 2 write
# Instructions:         Intel Vol 2 Chs 3..5
# Values +rd:           Intel Vol 2 Table 3-1
# Opcode map:           Intel Vol 2 Table A-2

                # 54    INTENTION               INSTRUCTION         OPCODE
B8 04 00 00 00  # 59    eax <- 4 (write)        mov r32, imm32      B8+rd id
BB 01 00 00 00  # 5E    ebx <- 1 (stdout)
B9 76 80 04 08  # 63    ecx <- buf
BA 0A 00 00 00  # 68    edx <- count
CD 80           # 6A    syscall                 int imm8            CD ib

B8 01 00 00 00  # 6F    eax <- 1 (exit)
BB 00 00 00 00  # 74    ebx <- 0 (param)
CD 80           # 76    syscall

48 45 4C 4F 20  # 7B    "HELO "
57 52 4C 44 0A  # 80    "WRLD\n"
"""

# >>>>>>>>>>>>> ELF FILE HEADER <<<<<<<<<<<<<

elf_fh  = b'\x7F\x45\x4C\x46'   # 04 e_ident[EI_MAG]: ELF magic number
elf_fh += b'\x01'               # 05 e_ident[EI_CLASS]: 1: 32-bit, 2: 64-bit
elf_fh += b'\x01'               # 06 e_ident[EI_DATA]: 1: little-endian, 2: big-endian
elf_fh += b'\x01'               # 07 e_ident[EI_VERSION]: ELF header version; must be 1
elf_fh += b'\x00'               # 08 e_ident[EI_OSABI]: Target OS ABI; should be 0
elf_fh += b'\x00'               # 09 e_ident[EI_ABIVERSION]: ABI version; 0 is ok for Linux
elf_fh += b'\x00\x00\x00'       # 0C e_ident[EI_PAD]: unused, should be 0
elf_fh += b'\x00\x00\x00\x00'   # 10
elf_fh += b'\x02\x00'           # 12 e_type: object file type; 2: executable
elf_fh += b'\x03\x00'           # 14 e_machine: instruction set architecture; 3: x86, 3E: amd64
elf_fh += b'\x01\x00\x00\x00'   # 18 e_version: ELF identification version; must be 1
elf_fh += b'\x54\x80\x04\x08'   # 1C e_entry: memory address of entry point (where process starts)
elf_fh += b'\x34\x00\x00\x00'   # 20 e_phoff: file offset where program headers begin
elf_fh += b'\x00\x00\x00\x00'   # 24 e_shoff: file offset where section headers begin
elf_fh += b'\x00\x00\x00\x00'   # 28 e_flags: 0 for x86
elf_fh += b'\x34\x00'           # 2A e_ehsize: size of this header (34: 32-bit, 40: 64-bit)
elf_fh += b'\x20\x00'           # 2C e_phentsize: size of each program header (20: 32-bit, 38: 64-bit)
elf_fh += b'\x01\x00'           # 2E e_phnum: #program headers
elf_fh += b'\x28\x00'           # 30 e_shentsize: size of each section header (28: 32-bit, 40: 64-bit)
elf_fh += b'\x00\x00'           # 32 e_shnum: #section headers
elf_fh += b'\x00\x00'           # 34 e_shstrndx: index of section header containing section names

# >>>>>>>>>>>>> ELF PROGRAM HEADER <<<<<<<<<<<<<

elf_ph  = b'\x01\x00\x00\x00'     # 38 p_type: segment type; 1: loadable
elf_ph += b'\x54\x00\x00\x00'     # 3C p_offset: file offset where segment begins
elf_ph += b'\x54\x80\x04\x08'     # 40 p_vaddr: virtual address of segment in memory (x86: 08048054)
elf_ph += b'\x00\x00\x00\x00'     # 44 p_paddr: physical address of segment, unspecified by 386 supplement
elf_ph += b'\x2C\x00\x00\x00'     # 48 p_filesz: size in bytes of the segment in the file image ############
elf_ph += b'\x2C\x00\x00\x00'     # 4C p_memsz: size in bytes of the segment in memory; p_filesz <= p_memsz
elf_ph += b'\x05\x00\x00\x00'     # 50 p_flags: segment-dependent flags (1: X, 2: W, 4: R)
elf_ph += b'\x00\x10\x00\x00'     # 54 p_align: 1000 for x86

# >>>>>>>>>>>>> PROGRAM SEGMENT <<<<<<<<<<<<<

# Hello, world.

# Linux system calls:   man 2 syscalls; man 2 write
# Instructions:         Intel Vol 2 Chs 3..5
# Values +rd:           Intel Vol 2 Table 3-1
# Opcode map:           Intel Vol 2 Table A-2

#                                    54    INTENTION               INSTRUCTION         OPCODE
elf_ps  = b'\xB8\x04\x00\x00\x00'  # 59    eax <- 4 (write)        mov r32, imm32      B8+rd id
elf_ps += b'\xBB\x01\x00\x00\x00'  # 5E    ebx <- 1 (stdout)
elf_ps += b'\xB9\x76\x80\x04\x08'  # 63    ecx <- buf
elf_ps += b'\xBA\x0A\x00\x00\x00'  # 68    edx <- count
elf_ps += b'\xCD\x80'              # 6A    syscall                 int imm8            CD ib
elf_ps += b'\xB8\x01\x00\x00\x00'  # 6F    eax <- 1 (exit)
elf_ps += b'\xBB\x00\x00\x00\x00'  # 74    ebx <- 0 (param)
elf_ps += b'\xCD\x80'              # 76    syscall
elf_ps += b'\x48\x45\x4C\x4F\x20'  # 7B    "HELO "
elf_ps += b'\x57\x52\x4C\x44\x0A'  # 80    "WRLD\n"

program = elf_fh + elf_ph + elf_ps

with open("./test", "wb") as binary:
    binary.write(program)