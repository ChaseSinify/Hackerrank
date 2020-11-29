#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int n;
    int i = 0;
    cin >> n;
    int *a = new int[n];
    while(cin>>a[i++]);
    while(cout<<a[--n]<<' ' && n);
    delete[] a;
    return 0;
}