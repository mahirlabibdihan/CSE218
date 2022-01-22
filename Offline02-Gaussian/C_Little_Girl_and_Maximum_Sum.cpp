#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#define ll long long
using namespace std;
#define MAX 4 * 2 * 100000 - 1

void updateRangeUtil(int si, int ss, int se, int us, int ue, ll diff, ll *tree, ll *lazy)
{
    if (ss >= us && se <= ue)
    {
        tree[si] += (se - ss + 1) * diff;
        if (ss != se)
        {
            lazy[si * 2 + 1] += diff;
            lazy[si * 2 + 2] += diff;
        }
        return;
    }
    if (ss > se || ss > ue || se < us)
    {
        return;
    }
    int mid = (ss + se) / 2;
    updateRangeUtil(si * 2 + 1, ss, mid, us, ue, diff, tree, lazy);
    updateRangeUtil(si * 2 + 2, mid + 1, se, us, ue, diff, tree, lazy);
    tree[si] = tree[si * 2 + 1] + tree[si * 2 + 2];
}
void updateRange(int n, int us, int ue, ll diff, ll *tree, ll *lazy)
{
    updateRangeUtil(0, 0, n - 1, us, ue, diff, tree, lazy);
}

ll getSumUtil(int ss, int se, int qs, int qe, int si, ll *tree, ll *lazy)
{
    if (lazy[si] != 0)
    {
        tree[si] += (se - ss + 1) * lazy[si];
        if (ss != se)
        {
            lazy[si * 2 + 1] += lazy[si];
            lazy[si * 2 + 2] += lazy[si];
        }
        lazy[si] = 0;
    }
    if (ss > se || ss > qe || se < qs)
    {
        return 0;
    }
    if (ss >= qs && se <= qe)
    {
        return tree[si];
    }
    int mid = (ss + se) / 2;
    return getSumUtil(ss, mid, qs, qe, 2 * si + 1, tree, lazy) +
           getSumUtil(mid + 1, se, qs, qe, 2 * si + 2, tree, lazy);
}
ll getSum(int n, int qs, int qe, ll *tree, ll *lazy)
{
    return getSumUtil(0, n - 1, qs, qe, 0, tree, lazy);
}
ll get(int n, int q, ll *tree, ll *lazy)
{
    return getSum(n, q, q, tree, lazy);
}
void constructSTUtil(int arr[], int ss, int se, int si, ll *tree, ll *lazy)
{
    if (ss > se)
    {
        return;
    }
    if (ss == se)
    {
        tree[si] = arr[ss];
        return;
    }
    int mid = (ss + se) / 2;
    constructSTUtil(arr, ss, mid, si * 2 + 1, tree, lazy);
    constructSTUtil(arr, mid + 1, se, si * 2 + 2, tree, lazy);
    tree[si] = tree[si * 2 + 1] + tree[si * 2 + 2];
}
void constructST(int arr[], int n, ll *tree, ll *lazy)
{
    constructSTUtil(arr, 0, n - 1, 0, tree, lazy);
}
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(nullptr);
    int n, q;
    cin >> n >> q;
    int a[200000];

    // O(n)
    for (int i = 0; i < n; i++)
        cin >> a[i];

    int count[n] = {};

    // O(n^2)
    ll tree[MAX] = {};
    ll lazy[MAX] = {};
    constructST(count, n, tree, lazy);
    while (q--)
    {
        int l, r;
        cin >> l >> r;
        updateRange(n, l - 1, r - 1, 1, tree, lazy);
    }

    // O(nlogn)
    sort(a, a + n);

    // O(nlogn)
    for (int i = 0; i < n; i++)
    {
        count[i] = get(n, i, tree, lazy);
    }
    sort(count, count + n);

    long long result = 0;

    // O(n)
    for (int i = 0; i < n; i++)
    {
        result += (long long)a[i] * count[i];
    }
    cout << result;
}