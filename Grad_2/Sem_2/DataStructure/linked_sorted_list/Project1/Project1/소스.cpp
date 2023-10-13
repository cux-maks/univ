#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>
#include <math.h>

#define ESP 0.001

double get_root(double (*f)(double, double, double, double, double), double x0, double x1, double a, double b, double c, double d);
double func(double x, double a, double b, double c, double d)
{
	return (a*x*x*x) + (b*x*x) + (c*x) + d;
}
int main()
{
	double x0, x1;
	double a, b, c, d;
	double r;
	printf("y = ax^3 + bx^2 + cx + d ������ �Լ��� �ִ�.\n");
	printf("a�� ���� �Է��Ͻÿ� : ");
	scanf("%lf", &a);
	printf("b�� ���� �Է��Ͻÿ� : ");
	scanf("%lf", &b);
	printf("c�� ���� �Է��Ͻÿ� : ");
	scanf("%lf", &c);
	printf("d�� ���� �Է��Ͻÿ� : ");
	scanf("%lf", &d);

	printf("x0�� �Է��Ͻÿ� : ");
	scanf("%lf", &x0);
	printf("x1�� �Է��Ͻÿ� : ");
	scanf("%lf", &x1);

	r = get_root(func, x0, x1, a, b, c, d);
	printf("���� %lf\n", r);
	return 0;
}

double get_root(double (*f)(double, double, double, double, double), double x0, double x1, double a, double b, double c, double d)
{
	double x2;
	int i = 1;
	double f0, f1, f2;
	do
	{
		x2 = (x0 + x1) / 2.0;
		f0 = f(x0, a, b, c, d);
		f1 = f(x1, a, b, c, d);
		f2 = f(x2, a, b, c, d);
		if (f0 * f2 < 0)
			x1 = x2;
		else
			x0 = x2;
		i++;
	} while (fabs(f2) > ESP);
	return x2;
}