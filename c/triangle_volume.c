/*
"Program to compute the volume of a triangle pouch"
"Unit: mm"
"Author: Yitian Shao"
"Created on 2021.06.04"
*/
#include <math.h>
#include <stdio.h>
#include <omp.h>

double compute(double x0, double x1, double y0, double z0, double R, double m, double c, double stepSize)
{
	double a = 0.0, b = 0.0, R2 = 0.0, V = 0.0, Vi = 0.0; // y = ax + b, R2 = R square, V is the volume computed (half-triangle), Vi is used for parallel computing
	
	a = m/c;
	b = a * -x0;
	R2 = R*R;
	
	int iMax = (int)((x1 - x0)/stepSize); // Need integer index for parallel computing 
	
	/* Assign maximum number of threads for parallel computing */
	int threadNum = omp_get_max_threads();
	omp_set_num_threads(threadNum); 
	printf("Start parallel computing: Assigned number of threads = %d\n", threadNum);
	
	#pragma omp parallel shared(V) private(Vi)
	{		
		#pragma omp for
		for(int i = 0; i < iMax; i++) // OMP Alternative of: for(double x = x0; x < x1; x += stepSize)
		{
			double x = (double)i * stepSize + x0;
			double y1 = a * x + b;
			double temp = R2- x*x; // Temp variable facilitates the computation
			
			for(double y = y0; y < y1; y += stepSize)
			{
				Vi += (sqrt(temp - y*y) - z0) * stepSize * stepSize;
			}
		}
		
		//printf("Thread %d: Vi = %f\n", omp_get_thread_num(), Vi); // For debug only
		
		#pragma omp critical
        {
			V += Vi;
        }
	}
	return (2*V); // Note that only half of the volume is computed by the for loop since the triangle pouch is symmetric about x-axis
}