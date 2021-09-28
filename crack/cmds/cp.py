import r2pipe


sha1sum = 'ae6146ce6c7b2c7627a76fb8bfd242b2ed3cfa78'


def crack(path):
    r2 = r2pipe.open(path)
    r2.cmd('oo+')

    r2.cmd('s 0x00400ad6')
    r2.cmd('wa jmp 0x00400b4f;nop;nop;nop')

    r2.cmd('s 0x00400ff2')
    r2.cmd('wa mov eax, 0')

    r2.cmd('s 0x00401040')
    r2.cmd('wa mov eax, 0')
