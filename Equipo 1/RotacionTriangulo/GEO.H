/*
    Nombre:         GEO.H
    Equipo:
                    Amezquita Becerra Carlos Daniel (1262695)
                    Rivera Soto Dayanara            (1271872)
                    Soto Elenes Brian Ramiro        (1254563)

    Descripcion:    Biblioteca con funciones graficas.
    Fecha:          28 de septiembre
*/

# include<math.h>
# define PI 3.14159265358979323846

void rotatePoint(float *X, float *Y, int angle);
void rotatePointR(float *X, float *Y, int angle, float ejeX, float ejeY);
void scalePoint(float *X, float *Y, int scale);
void translatePoint(float *X, float *Y, float dx, float dy);

void linea(int x0, int y0, int x1, int y1);

void rotatePointR(float *X, float *Y, int angle, float ejeX, float ejeY){
    float x,y;
    x = *X;
    y = *Y;
    //printf("%.0f\t%.0f\n",x,y);
    translatePoint(&x,&y,-ejeX,-ejeY);
    //printf("%.0f\t%.0f\n",x,y);
    rotatePoint(&x,&y,angle);
    //printf("%.0f\t%.0f\n",x,y);
    translatePoint(&x,&y,ejeX,ejeY);
    //printf("%d\t%d\n",(int)x,(int)y);
    *X = x;
    *Y = y;
}

void rotatePoint(float *X, float *Y, int angle){
    float x,y;
    x = (*X) * cos(PI / 180 * angle) - (*Y) * sin(PI / 180 * angle);
    y = (*X) * sin(PI / 180 * angle) + (*Y) * cos(PI / 180 * angle);
    *X = x;
    *Y = y;
}

float rotatePointX(float X, float Y, int angle){
    return X * cos(PI / 180 * angle) - Y * sin(PI / 180 * angle);
}
float rotatePointY(float X, float Y, int angle){
    return X * sin(PI / 180 * angle) + Y * cos(PI / 180 * angle);
}

void scalePoint(float *X, float *Y, int scale){
    float x,y;
    x = (*X) * scale;
    y = (*Y) * scale;
    *X = x;
    *Y = y;
}

void translatePoint(float *X, float *Y, float dx, float dy){
    *X = *X + dx;
    *Y = *Y + dy;
}

void linea(int x0, int y0, int x1, int y1)
{
    int dx, dy, p, x, y;

	dx = x1 - x0;
	dy = y1 - y0;

	x = x0;
	y = y0;

	p = 2 * dy - dx;

	while(x < x1)
	{
		if(p >= 0)
		{
			putpixel(x,y,GREEN);
			y = y + 1;
			p = p + 2 * dy - 2 * dx;
		}
		else
		{
			putpixel(x,y,GREEN);
			p = p + 2 * dy;
		}
		x = x + 1;
	}
}

