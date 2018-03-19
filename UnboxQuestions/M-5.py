with open('input.txt',mode='r') as f1:
    sortedfile=sorted(f1);

    with open('output.txt',mode='w') as f2:
        f2.writelines(f1)

import sys
sys.stdout.writelines(sortedfile)