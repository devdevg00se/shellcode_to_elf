# Shellcode to ELF
Python script to generate valid 32 bit ELF to run x86 shellcode without compiler
Replace the `buf` variable in the Python script with your Linux x86 shellcode
Valid ELF headers are based off the ones used here: https://dacvs.neocities.org/handmade
`p_filesz` and `p_memsz` are dynamically populated based on the shellcode size
