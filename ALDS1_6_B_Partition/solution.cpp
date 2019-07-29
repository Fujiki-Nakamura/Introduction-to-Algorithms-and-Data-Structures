#include<iostream>
using namespace std;

int A[100000];

int partition(int A[], int p, int r) {
    int x = A[r];
    int i = p - 1;
    int tmp;

    for (int j = p; j < r; j++) {
        if (A[j] <= x) {
            i = i + 1;
            tmp = A[i];
            A[i] = A[j];
            A[j] = tmp;
        }
    }
    tmp = A[r];
    A[r] = A[i + 1];
    A[i + 1] = tmp;
    return i + 1;
}


int main() {
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) cin >> A[i];
    int pivot_i = partition(A, 0, n - 1);
    for (int i = 0; i < n; i++) {
        if (i == pivot_i) {
            cout << '[' << A[i] << ']';
        } else {
            cout << A[i];
        }
        if (i < n - 1) cout << ' ';
    }
    cout << endl;

    return 0;
}
