#include <iostream>
#include <cstdlib>
#include <omp.h>
using namespace std;

//Function to initialize the matrix by some random values
void initializeMatrix(int** matrix, int m, int n) {
    for(int i = 0; i < m; i++){
        matrix[i] =  new int[n];
        for(int j = 0; j < n; j++){
            matrix[i][j] = rand() % 100;
        }
    }
}

//Function to print the original matrix
void printMatrix(int** matrix, int m, int n) {
    for(int i = 0; i < m; i++){
        for(int j = 0; j < n; j++){
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }
}

//Swap function to use in partition function
void swap(int* arr, int i, int j) {
    int temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
}

//Partition function to use in Quick Sort
int partition(int* arr, int l, int r) {
    int pivot = arr[r];
    int i = l-1;
    for(int j = l; j <= r; j++){
        if(arr[j] > pivot){
            i++;
            swap(arr, i, j);
        }
    }
    swap(arr, i+1, r);
    return i+1;
}

//Function for Quick Sort in Descending order
void quickSortDescending(int* arr, int l, int r) {
    if(l < r){
        int pivot = partition(arr, l, r);
        #pragma omp task
        quickSortDescending(arr, l, pivot-1);
        #pragma omp task
        quickSortDescending(arr, pivot+1, r);
    }
}

int main() {
    int m, n;
    cout << "Enter the number of rows: ";
    cin >> m;
    cout << "Enter the number of columns: ";
    cin >> n;
    
    //Initializing the matrix by some random values
    int** matrix = new int* [m];
    initializeMatrix(matrix, m, n);

    //Printing the original matrix
    cout << "Original Matrix:" << endl;
    printMatrix(matrix, m, n);
    cout << endl;

    //Since the last digit of my student ID is 8 so i have to create number of threads equal to number of rows ‘m’ and each thread will sort a row using Quick Sort in Descending order
    #pragma omp parallel for num_threads(m) shared(matrix)
    for(int i = 0; i < m; i++){
        //Quick Sort in Descending order
        quickSortDescending(matrix[i], 0, n-1);
    }

    //Printing the sorted matrix
    cout << "Sorted Matrix:" << end;
    printMatrix(matrix, m, n);
    cout << endl;

    return 0;
}