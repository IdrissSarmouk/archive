#include <bits/stdc++.h>
using namespace std;

int const n = 8; 
int main() {
	vector <vector <int> > G { { 0, 1, 0, 0, 0, 0, 0, 0 }, { 1, 0, 1, 0, 0, 0, 1, 0 },
	{0, 1, 0, 1, 0, 0, 0, 0 }, { 0, 0, 1, 0, 1, 0, 0, 0 }, { 0, 0, 0, 1, 0, 1, 0, 1 },
	{0, 0, 0, 0, 1, 0, 1, 0 }, { 0, 1, 0, 0, 0, 1, 0, 0 }, { 0, 0, 0, 0, 1, 0, 0, 0 } };
	
	vector<bool> visited(n, 0);
	int root = 5;
 vector<list <int>> AdjList(n);
 queue<int> myqueue;
 
for (auto i = 0; i < n; i++) {
 for (auto j = i; j < n; j++)
 if (G[i][j]) {
 AdjList[i].push_back(j);
 AdjList[j].push_back(i);
 }
 }
 
 myqueue.push(root);
 visited[root] = 1;
while (!myqueue.empty()) {
 auto vertex = myqueue.front();
 myqueue.pop(); // Dequeue a vertex from queue and print it
 cout << " " << vertex + 1 << " ";
 for (auto neigbor : AdjList[vertex])
 if (!visited[neigbor]) {
 // Mark the current vertex as visited and enqueue it
 myqueue.push(neigbor);;
 visited[neigbor] = 1;
 }
 }
 
 //Connectivity 
  bool con = true;
    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            con = false;
            break;
        }
    }
 if (con) {
        cout << "\nConnected\n";
    } else {
        cout << "\nNot Connected\n";
    }

  //Bipartite
int x = 0;
for (int i = 0; i < n; i++) {
    for ( int j=i; j<n; j++){
        if (G[i][j]){
        x = x + 1;
    }
    }
    
} if ( x % 2 == 0) {
    cout << "Bipartite";
} else { cout<< "Not Bipartite";}


return 0;
}
