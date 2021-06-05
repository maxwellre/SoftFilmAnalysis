#include <math.h>
#include <stdio.h>
#include <omp.h>

double compute(double stepSize)
{
	int iMax = (int) 1/stepSize;
	double V = 0.0;
	double Vi = 0.0;
	
	// Assign maximum number of threads for parallel computing
	int threadNum = omp_get_max_threads();
	omp_set_num_threads(threadNum); 
	printf("Start parallel computing: Assigned number of threads = %d\n", threadNum);
	
	#pragma omp parallel shared(V) private(Vi)
	{		
		#pragma omp for
		for(int i = 0; i < iMax; i++)//for(double x = x0; x < x1; x += stepSize)
		{
			Vi += 1.0;
		}
		
		printf("Thread %d: Vi = %f\n", omp_get_thread_num(), Vi);
		
		#pragma omp critical
        {
			V += Vi;
        }
	}
	
	printf("V = %f\n", V);
	return V;
}