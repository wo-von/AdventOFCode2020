#!/usr/bin/python3
import time

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
    start = time.time()
    # Exhaust through all command until we get a loop free sequence
    for n, command in enumerate(seq):
        if command[0] == 'jmp':
            del seq[n]
            seq.insert(n, ['nop', command[1]])
            global_var = loop_checker(seq)
            if global_var:
                break
            else:
                del seq[n]
                seq.insert(n, [command[0], command[1]])
        elif command[0] == 'nop':
            del seq[n]
            seq.insert(n, ['jmp', command[1]])
            global_var = loop_checker(seq)
            if global_var:
                break
            else:
                del seq[n]
                seq.insert(n, [command[0], command[1]])
    
    end = time.time()
    
    if global_var:
        print("fixed in", end - start, "time and the accumulator is", global_var)
    else:
        print("Could not fix it")


if __name__ == "__main__":
    main()