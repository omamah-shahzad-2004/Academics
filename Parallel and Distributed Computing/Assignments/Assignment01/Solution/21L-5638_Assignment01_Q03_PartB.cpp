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

//Function to calculate the product of the complete matrix
int matrixProduct(int** matrix, int m, int n) {
    int product = 1;
    //#pragma omp parallel for schedule(static) reduction(*: product)
    //#pragma omp parallel for schedule(dynamic) reduction(*: product)
    //#pragma omp parallel for schedule(guided) reduction(*: product)
    //int num_threads = omp_get_num_threads();
    //#pragma omp parallel for schedule(static, num_threads) reduction(*: product)
    //#pragma omp parallel for schedule(dynamic, num_threads) reduction(*: product)
    //#pragma omp parallel for schedule(guided, num_threads) reduction(*: product)
    //#pragma omp parallel for schedule(static, 1) reduction(*: product)
    //#pragma omp parallel for schedule(dynamic, 1) reduction(*: product)
    //#pragma omp parallel for schedule(guided, 1) reduction(*: product)
    //int random = rand() % 10;
    //#pragma omp parallel for schedule(static, random) reduction(*: product)
    //#pragma omp parallel for schedule(dynamic, random) reduction(*: product)
    //#pragma omp parallel for schedule(guided, random) reduction(*: product)
    int random = rand() % 100;
    //#pragma omp parallel for schedule(static, random) reduction(*: product)
    //#pragma omp parallel for schedule(dynamic, random) reduction(*: product)
    #pragma omp parallel for schedule(guided, random) reduction(*: product)
    for(int i = 0; i < m; i++){
        for(int j = 0; j < n; j++){
            product *= matrix[i][j];
        }
    }
    return product;
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

    //Calculating the product of the complete matrix
    double startTime = omp_get_wtime();
    int mat_product = matrixProduct(matrix, m, n);
    double endTime = omp_get_wtime();
    //Calculating elapsed time
    double elapsedTime = endTime - startTime;

    cout << "Product of the matrix is: " << mat_product << endl;

    //Printing elapsed time
    cout << "Elapsed Time: " << elapsedTime << endl;

    //Freeing dynamically allocated memory
    for(int i = 0; i < m; i++){
        delete[] matrix[i];
    }
    delete[] matrix;

    return 0;
}