#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

struct point {
    int x, y;
};

double distance(point a, point b) {
    return sqrt(pow(a.x - b.x, 2) + pow(a.y - b.y, 2));
}

bool compareX(point a, point b) {
    if (a.x != b.x) return a.x < b.x;
    else if(a.x == b.x) return a.y < b.y;
}

bool compareY(point a, point b) {
    if (a.y != b.y) return a.y < b.y;
    else if (a.y == b.y) return a.x < b.x;
}

pair<point, point> bfsp(vector<point> p) {

    double min = INFINITY;
    pair<point, point> ret;
    for (int i = 0; i < p.size() - 1; i++) {
        for (int j = i + 1; j < p.size(); j++) {
            double d = distance(p[i], p[j]);
            if (min > d && i != j) {
                min = d;
                ret.first = p[i];
                ret.second = p[j];
            }
        }
    }
    return ret;
}

pair<point, point> closestSplitPair(vector<point> px, vector<point> py, double d, pair<point, point> ret) {


    double x = px[px.size() / 2].x;
    vector<point> S;
    for (int i = 0; i < py.size(); i++) {
        if (py[i].x > x - d && py[i].x < x + d) {
            S.push_back(py[i]);
        }
    }
    double best = d;
    if (S.size() != 0) {
        for (int i = 0; i < S.size(); i++) {
            for (int j = 0; j < min(7, int(S.size()) - i); j++) {
                if (i != i + j) {
                    double di = distance(S[i], S[i + j]);
                    if (di < best) {
                        best = di;
                        ret.first = S[i];
                        ret.second = S[i + j];
                    }
                }
            }
        }
    }
    
    return ret;
}

pair<point, point> closestPair(vector<point> px, vector<point> py) {


    if (px.size() <= 3) {
        return bfsp(px);
    }

    vector<point> Lx(px.begin(), px.begin() + (px.size() / 2));
    vector<point> Ly;

    vector<point> Rx(px.begin() + (px.size() / 2), px.end());
    vector<point> Ry;

    for (int i = 0; i < py.size(); i++) {
        if (py[i].x < Lx[Lx.size() - 1].x) {
            Ly.push_back(py[i]);
        }
        else if (py[i].x > Lx[Lx.size() - 1].x) {
            Ry.push_back(py[i]);
        }
        else {
            if (py[i].y <= Lx[Lx.size() - 1].y) {
                Ly.push_back(py[i]);
            }
            else {
                Ry.push_back(py[i]);
            }
        }
    }

    pair<point, point> L = closestPair(Lx, Ly);
    pair<point, point> R = closestPair(Rx, Ry);
    double d = min(distance(L.first, L.second), distance(R.first, R.second));
 
    pair<point, point> ret;
    if (d == distance(L.first, L.second)) {
        ret = L;
    }
    else {
        ret = R;
    }
    return closestSplitPair(px, py, d, ret);

}
   
int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int N;
        cin >> N;
        vector<point> points(N);
        for (int j = 0; j < N; j++) {
            cin >> points[j].x >> points[j].y;
        }
        sort(points.begin(), points.end(), compareX);
        vector<point> Px(points);
        sort(points.begin(), points.end(), compareY);
        vector<point> Py(points);
        pair<point, point> ret = closestPair(Px, Py);
        double result = distance(ret.first, ret.second);
        printf("%.2f\n", result);

    }
    return 0;
}