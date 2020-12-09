#!/usr/bin/python3
import copy

def loop_checker(seq):
    cur = global_var = 0
    visited  = []
    while cur < len(seq):
        
        if cur in visited: # check if we have started to loop
            return 0
        else:
            visited.append(cur)
        if seq[cur][0] == 'nop':
            cur += 1
        elif seq[cur][0] == 'jmp':
            cur += seq[cur][1]
        elif seq[cur][0] == 'acc':
            global_var += seq[cur][1]
            cur += 1
        else:
            raise SystemExit("unrecognized instruction", seq[cur][0])
    return global_var


def main():

    f = open("input.txt")
    seq = f.read().split('\n')
    f.close()

    global_var = 0
    seq = [[func(e) for func, e in zip([str, int], elem)] for elem in [s.split() for s in seq if s != '']]

    # Exhaust through all command until we get a loop free sequence
    for n, command in enumerate(seq):
        seq_copy = copy.deepcopy(seq)
        if command[0] == 'jmp':
            seq_copy[n][0] = 'nop'
            global_var = loop_checker(seq_copy)
            if global_var:
                break
        elif command[0] == 'nop':
            seq_copy[n][0] = 'jmp'
            global_var = loop_checker(seq_copy)
            if global_var:
                break
    print(global_var)


if __name__ == "__main__":
    main()