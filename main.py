import sys
import argparse

from vgmm import vgmm

# Main call
if __name__ == '__main__':
    argument_parser = argparse.ArgumentParser(prog = 'VGMM',
                                              description = 'Vägmärkesmakaren - makes signs',
                                              epilog = 'Have fun!')
    argument_parser.add_argument('input_file', metavar = 'IN', help = 'The path and file name of the input XML file')
    argument_parser.add_argument('output_file', metavar = 'OUT', help = 'The path and file name of the output SVG file')
    argument_parser.add_argument('-v', '--verbose', action = 'store_true', help = 'Be verbose (print debugging info)')
    args = argument_parser.parse_args()

    # Call to vgmm with parsed arguments, returns exit status when done
    sys.exit(vgmm(args))
