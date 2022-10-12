%Meta 2b Equipo 1
clearvars;
load su57_3d_model;
clf
hold on
%su57 Model3D Aircraft
for i = 1: length(Model3D.Aircraft)
    patch('Faces',Model3D.Aircraft(i).stl_data.faces,...
    'Vertices',Model3D.Aircraft(i).stl_data.vertices,...
    'FaceColor',Model3D.Aircraft(i).color,...
    'EdgeColor', 'none',...
    'FaceLighting', 'gouraud',...
    'FaceAlpha', Model3D.Aircraft(i).alpha);
end

%Rotacion de los los elevadores
theta = 15;
rotMatrix = [1, 0, 0; 0, cos(pi*theta/180), -sin(pi*theta/180); 0,  sin(pi*theta/180), cos(pi*theta/180)];


rotA = (Model3D.Control(5).stl_data.vertices - Model3D.Control(5).rot_point) * rotMatrix;
rotA = rotA + Model3D.Control(5).rot_point;
Model3D.Control(5).stl_data.vertices = rotA;

theta = -15;
rotMatrix = [1, 0, 0; 0, cos(pi*theta/180), -sin(pi*theta/180); 0,  sin(pi*theta/180), cos(pi*theta/180)];

rotA = (Model3D.Control(6).stl_data.vertices - Model3D.Control(6).rot_point) * rotMatrix;
rotA = rotA + Model3D.Control(6).rot_point;
Model3D.Control(6).stl_data.vertices = rotA;


%Su578 Model3D Control
for i = 1: length(Model3D.Control)
    patch('Faces',Model3D.Control(i).stl_data.faces,...
    'Vertices',Model3D.Control(i).stl_data.vertices,...
    'FaceColor',Model3D.Control(i).color,...
    'EdgeColor', 'none',...
    'FaceLighting', 'gouraud');
end

hold off
% material metal
material('dull');
camlight('headlight');
% add light
L = [0 0 -150]/norm([0 0 -150]);
light('Position',L)
axis equal
axis on
xlabel('X')
ylabel('Y')
zlabel('Z')
view(-30,30)
grid on