airplane = load('su57_3d_model.mat');
hold on

%ROTACIONES BORRAR DE LINEA 4 A 21 PARA TENER EL AVION ORIGINAL
%Cambio de color los componentes a rotar para ser mas vistoso
airplane.Model3D.Control(5).color = [0.9290 0.6940 0.1250];
airplane.Model3D.Control(6).color = [0.9290 0.6940 0.1250];
%Rotacion 15 grados izq
theta = 15;
rotMatrix = [1, 0, 0; 0, cos(pi*theta/180), -sin(pi*theta/180); 0,  sin(pi*theta/180), cos(pi*theta/180)];
a = bsxfun(@minus, airplane.Model3D.Control(5).stl_data.vertices, airplane.Model3D.Control(5).rot_point);
rotA = a*rotMatrix;
rotA=bsxfun(@plus, rotA, airplane.Model3D.Control(5).rot_point);
airplane.Model3D.Control(5).stl_data.vertices = rotA;
%Rotacion -15 grados der
theta = -15;
rotMatrix = [1, 0, 0; 0, cos(pi*theta/180), -sin(pi*theta/180); 0,  sin(pi*theta/180), cos(pi*theta/180)];
a = bsxfun(@minus, airplane.Model3D.Control(6).stl_data.vertices, airplane.Model3D.Control(6).rot_point);
rotA = a*rotMatrix;
rotA=bsxfun(@plus, rotA, airplane.Model3D.Control(6).rot_point);
airplane.Model3D.Control(6).stl_data.vertices = rotA;

for i = 1: length(airplane.Model3D.Aircraft)

patch('faces', airplane(1).Model3D(1).Aircraft(i).stl_data.faces,'vertices', airplane(1).Model3D(1).Aircraft(i).stl_data.vertices,...
    'FaceColor',airplane(1).Model3D(1).Aircraft(i).color,'EdgeColor', 'none','FaceLighting', 'gouraud','AmbientStrength', 0.15,...
    'FaceAlpha',airplane(1).Model3D(1).Aircraft(i).alpha);
end

for i = 1: length(airplane.Model3D.Control)

patch('faces', airplane(1).Model3D(1).Control(i).stl_data.faces,'vertices', airplane(1).Model3D(1).Control(i).stl_data.vertices,...
    'FaceColor',airplane(1).Model3D(1).Control(i).color,'EdgeColor', 'none','FaceLighting', 'gouraud','AmbientStrength', 0.15);
end

camlight('headlight')
L = [0 0 -1500]/norm([0 0 -1500]); %Luz por debajo del avion
light('Position',L);
view(0,90) % change the orientation
grid on; box on
xlabel('x'); ylabel('y'); zlabel('z');
set(gca,'DataAspectRatio',[1 1 1])
hold off
