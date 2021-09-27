import r2pipe


sha1sum = 'c4703ab2c555b4e8bd3509bfc109bad32a1e1670'


def crack(path):
    print('LICENCE KEY: \'B O\'')
    r2 = r2pipe.open(path)
    r2.cmd('oo+')

   # r2.cmd('s 0x00400ad6')
   # r2.cmd('wa jmp 0x00400b4f;nop;nop;nop')

    # r2.cmd('s 0x00400ff2')
    # r2.cmd('wa mov eax, 0')

    # r2.cmd('s 0x00401040')
    # r2.cmd('wa mov eax, 0')
