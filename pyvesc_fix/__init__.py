import sys
if sys.version_info < (3, 3):
    raise SystemExit(
        "Invalid Python version. PyVESC requires Python 3.3 or greater.")

from .protocol import *
from .VESC import *

from . import protocol as PO
from . import VESC as VE


class PyvescFix:
    """ The pyvesc class rebind """

    def __init__(self) -> None:
        self.protocol = PO
        self.vesc = VE
