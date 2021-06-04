#include <math.h>
#include <stdio.h>
#include "stdlib.h"

double compute(double x0, double x1, double y0, double z0, double R, double m, double c, double stepSize)
{
	double a, b, R2, V; // y = ax + b, R2 = R square, V is the volume computed
	a = m/c;
	b = a * -x0;
	R2 = R*R;
	
	V = 0.0; 
	
	for(double x = x0; x < x1; x += stepSize)
	{
		double y1 = a * x + b;
		double temp = R2- x*x; // Temp variable stores part of the computation
		
		for(double y = y0; y < y1; y += stepSize)
		{
			V += (sqrt(temp - y*y) - z0) * stepSize * stepSize;
		}
	}
	
	return V;
}