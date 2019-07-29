#include<iostream>
using namespace std;

struct Card{
    char suit;
    int value;
};

struct Card A[100000];

int partition(struct Card A[], int p, int r) {
    struct Card x = A[r];
    int i = p - 1;
    struct Card tmp;

    for (int j = p; j < r; j++) {
        if (A[j].value <= x.value) {
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

void quickSort(struct Card A[], int p, int r) {
    if (p < r) {
        int pivot_i = partition(A, p, r);
        quickSort(A, p, pivot_i - 1);
        quickSort(A, pivot_i + 1, r);
    }
}

int main() {
    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> A[i].suit;
        cin >> A[i].value;
    }
    /*
    cout << endl;
    for (int i = 0; i < n; i++) {
        cout << A[i].suit << ' ' << A[i].value << endl;
    }
    return 0;
    */
    quickSort(A, 0, n - 1);
    for (int i = 0; i < n; i++) {
        cout << A[i].suit << ' ' << A[i].value << endl;
    }

    return 0;
}
