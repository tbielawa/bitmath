import bitmath
import progressbar.widgets


class BitmathFileTransferSpeed(progressbar.widgets.Widget):
    """Widget for showing the transfer speed (useful for file transfers)."""
    __slots__ = ('system', 'format')

    def __init__(self, system=bitmath.NIST, format="{value:.2f} {unit}/s"):
        self.system = system
        self.format = format

    def update(self, pbar):
        """Updates the widget with the current NIST/SI speed.

Basically, this calculates the average rate of update and figures out
how to make a "pretty" prefix unit"""

        if pbar.seconds_elapsed < 2e-6 or pbar.currval < 2e-6:
            scaled = bitmath.Byte()
        else:
            speed = pbar.currval / pbar.seconds_elapsed
            scaled = bitmath.Byte(speed).best_prefix(system=self.system)

        return scaled.format(self.format)
