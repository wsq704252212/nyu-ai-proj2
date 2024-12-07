from utils import read_input, write_output
from back_trace_search import backtrace
import sys

"""
Team members:
Zan Ni (zn2161)
Siqi Wan (sw6195)
"""

def main():
    """
    main function
    """
    # 1. read input
    input_file = sys.argv[1]
    board, vertiDots, horiDots = read_input(input_file)

    # 2. backtrace
    result, board = backtrace(board, vertiDots, horiDots)

    if result:
        # 3. write output
        output_file = sys.argv[2]
        write_output(output_file, board)
    else:
        print("No solution found!")


if __name__ == "__main__":
    main()
