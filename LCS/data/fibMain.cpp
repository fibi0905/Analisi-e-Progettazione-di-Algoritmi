#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>
using namespace std;

enum Direction { U, LE, D };

Direction getDirection(unsigned int l[32][40], int i, int j) {
    if (l[i][j-1] > l[i-1][j]) return LE;
    else return U;
}

void move(Direction mv, unsigned int &i, unsigned int &j) {
    switch (mv) {
        case U:  i--; break;
        case LE: j--; break;
        case D:  i--; j--; break;
        default: break;
    }
}

string readfile(const string &fileName) {
    ifstream file(fileName);
    if (!file.is_open()) {
        cerr << "Errore: impossibile aprire il file " << fileName << endl;
        return "";
    }
    ostringstream buffer;
    buffer << file.rdbuf();
    return buffer.str();
}

int main() {
    string s1 = readfile("fib2.txt");
    string s2 = readfile("fib1.txt");

    unsigned int L[32][40];
    Direction R[32][40];

    for (unsigned int i = 0; i < 32; i++) L[i][0] = 0;
    for (unsigned int j = 0; j < 40; j++) L[0][j] = 0;

    for (unsigned int i = 1; i < 32; i++) {
        for (unsigned int j = 1; j < 40; j++) {
            if (s2[i-1] == s1[j-1]) {
                L[i][j] = L[i-1][j-1] + 1;
                R[i][j] = D;
            } else {
                R[i][j] = getDirection(L, i, j);
                if (R[i][j] == LE){

                    L[i][j] =  L[i][j-1];
                }
                else{
                    L[i][j] =  L[i-1][j];

                }
            }
        }
    }

    unsigned int dim = L[31][39]; 

    string seq;
    unsigned int i = 31, j = 39; 

    while (i > 0 && j > 0) {
        if (R[i][j] == D) seq.push_back(s1[j-1]);
        move(R[i][j], i, j);
    }

    reverse(seq.begin(), seq.end()); //sequenza era invertita

    cout << "LCS: " << seq << "\nLunghezza: " << dim << endl;

    // Scrittura su file di output 
    ofstream out("lcs_output.txt");
    out << "LCS: " << seq << "\nLunghezza: " << dim << endl;
    out.close();

    return 0;
}