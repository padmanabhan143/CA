#include<bits/stdc++.h>
using namespace std;

void luDecomposition(vector<vector<int>> arr, vector<int> &voters){

    int row = arr.size();

    vector<vector<int>> lower(row, vector<int> (row, 0));
    vector<vector<int>> upper(row, vector<int> (row, 0));

    // Decomposition of matrix into lower and upper triangular matrix.
    for(int i=0;i<row;i++){

        // Upper Triangular.
        for(int k=i;k<row;k++){
            int sum=0;
            for(int j=0;j<i;j++){
                sum += (lower[i][j]*upper[j][k]);
            }
            upper[i][k] = arr[i][k] - sum;
        }

        // Lower Triangular.
        for(int k=i;k<row;k++){
            // Diagonal will be 1.
            if(i == k){
                lower[i][k] = 1;
            }
            else{
                int sum=0;
                for(int j=0;j<i;j++){
                    sum += (lower[k][j]*upper[j][i]);
                }
                lower[k][i] = (arr[k][i]-sum)/upper[i][i];
            }
        }
    }
