import crack_commands.cp
import crack_commands.tp
import crack_commands.game
from crack_commands.exceptions import *


sha1sum = {
    cp.sha1sum:     cp,
    tp.sha1sum:     tp,
    game.sha1sum: game,
}

flags = {
    '-cp':     cp,
    '-tp':     tp,
    '-game': game,
}






