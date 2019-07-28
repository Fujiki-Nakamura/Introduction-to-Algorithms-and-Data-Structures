#include<stdio.h>
#include<iostream>
#define LEN 100005
using namespace std;

typedef struct pp {
    // char name[100];
    string name;
    int t;
} P;

P Q[LEN];
int head, tail;

void enqueue(P x) {
    Q[tail] = x;
    tail = (tail + 1) % LEN;
}

P dequeue() {
    P x = Q[head];
    head = (head + 1) % LEN;
    return x;
}

int min(int a, int b) {return a < b ? a : b;}

int main() {
    int n, q, t, c;
    int elaps = 0;
    // char name[100];
    string name;
    P u;
    cin >> n >> q;
    for (int i = 0; i < n; i++) {
        cin >> name;
        cin >> t;
        Q[i].name = name;
        Q[i].t = t;
    }
    head = 0;
    tail = n;
    while (head != tail) {
        u = dequeue();
        c = min(q, u.t);
        u.t = u.t - c;
        elaps += c;
        // cout << ' ' << u.name << ' ' << u.t << ' ' << c << endl;
        if (u.t > 0) enqueue(u);
        else {
            cout << u.name << ' ' << elaps << endl;
        }
    }
    /*
    for (int i = 0; i < n; i++) {
        cout << Q[i].name << ' ' << Q[i].t << endl;
    }
    */
    return 0;
}
