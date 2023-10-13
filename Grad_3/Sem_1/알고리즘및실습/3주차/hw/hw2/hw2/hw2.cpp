#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

int longestSubstring(string s, int k) {
    int n = s.length();
    unordered_map<char, int> freq;
    for (char c : s) {
        freq[c]++;
    }
    int left = 0, right = n - 1;
    while (left <= right && freq[s[left]] < k) {
        left++;
    }
    while (left <= right && freq[s[right]] < k) {
        right--;
    }
    if (left > right) {
        return 0;
    }
    for (int i = left; i <= right; i++) {
        if (freq[s[i]] < k) {
            return max(longestSubstring(s.substr(left, i - left), k), longestSubstring(s.substr(i + 1, right - i), k));
        }
    }
    return right - left + 1;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        string s;
        cin >> s;
        int k;
        cin >> k;
        int result = longestSubstring(s, k);
        cout << result << "\n";
    }
    return 0;
}
