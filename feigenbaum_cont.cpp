#include <fstream>
#include <iomanip>

// Programa para obtener el diagrama de Feigenbaum de un sistema de tiempo continuo
// Compilación: g++ -o feigenbaum_cont feigenbaum_cont.cpp -O3
// El flag de optimización ayuda bastante, tarda menos de 10 segundos, sin él tarda más
// Guarda los datos en el fichero feigenbaum_cont.dat
// También hay un programa de Python para visualizarlo si se desea, feigenbaum_cont.py

const int N = 3;
const double A = 0.2, B = 0.2, h = 0.01;
double C = 2.5;
double x[N];
double k[5][N];

// ejemplo con las ecuaciones de Rossler
void f(double v[]){
	double x = v[0], y = v[1], z = v[2];
	v[0] = -y -z;
	v[1] = x + A * y;
	v[2] = B + z * (x - C);
}

// pasos de Runge-Kutta
void rk(int which){
	switch(which){
		case 1:
			for(int i = 0; i < N; ++i) 
				k[which][i] = x[i];
			break;
		case 2:
		case 3:
			for(int i = 0; i < N; ++i) 
				k[which][i] = x[i] + h/2 * k[which-1][i];
			break;
		case 4:
			for(int i = 0; i < N; ++i) 
				k[which][i] = x[i] + h * k[which-1][i];
			break;
	}
	f(k[which]);
}

// iteración del sistema
void it(){
	for(int i = 1; i <= 4; ++i) 
		rk(i);

	for(int i = 0; i < N; ++i) 
		k[0][i] = x[i] + h/6 * (k[1][i] + 2*(k[2][i] + k[3][i]) + k[4][i]);

	for(int i = 0; i < N; ++i) 
		x[i] = k[0][i];
}

int main(){
	const double mn = C, mx = 6;
	// son iteraciones, no tiempo (t = h * it)
	const int trans = 5000, its = 100000;
	// coordenada sobre la que hacer el diagrama con los máximos (x = 0, y = 1, z = 2)
	const int coord = 2;
	const double dc = (mx - mn)/2000;
 	x[0] = 0.3;
	x[1] = 0.5;
	x[2] = 0.2;

	std::fstream fs("feigenbaum_cont.dat", std::fstream::out);
	fs << std::setprecision(10);

	while(C <= mx){
		for(int i = 0; i < trans; ++i) 
			it();

		double x0 = x[coord], x1 = x[coord];

		for(int i = 0; i < its; ++i){
			it();
			double x2 = x[coord];
			// puntos del diagrama serán los máximos de una de las coordenadas
			if(x0 < x1 && x1 > x2){
				// interpolación cuadrática (fórmula simplificada obtenida del profesor)
            			double xmx = x1 - (x2-x0)*(x2-x0)/((x2-2*x1+x0)*8);
				fs << C << " " << xmx << "\n";
			}
			x0 = x1;
			x1 = x2;
		}
		C += dc;
	}

	return 0;
}
