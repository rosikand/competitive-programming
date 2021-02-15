#include <iostream>
using namespace std;

int main() {
	int n; 
	cin >> n; 

	int s = n/5; 

	if (s * 5 == n) {
		cout << s; 
	} else {
		cout << s + 1; 
	}
}