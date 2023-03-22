#include <bits/stdc++.h>

using namespace std;

int main(int argc, char *argv[]) {
    FILE *infile, *outfile, *keyfile;
    infile = fopen(argv[2], "rb");
    outfile = fopen(argv[3], "wb");
    keyfile = fopen("/home/cilostomy/Documents/Projects/PyCharm Projects/TI2/testfiles/key.txt", "wb");
    if (infile) {
        int reg = (1 << 24) - 1;
        if (argc == 4) reg = atoi(argv[1]);
        char block;
        while (fread(&block, sizeof(char), 1, infile) == 1) {
            char key = 0;
            for (int i = 0; i < 8; i++) {
                key += (reg >> 23) & 1;
                if (i != 7) key <<= 1;
                bool feed = ((reg >> 23) & 1) ^ ((reg >> 3) & 1) ^ ((reg >> 2) & 1) ^ (reg & 1);
                reg <<= 1;
                reg += feed;
            }
            block ^= key;
            putc(block, outfile);
            putc(key, keyfile);
        }
    }
    fclose(infile);
    fclose(outfile);
    fclose(keyfile);
    return 0;
}
