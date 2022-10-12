clearvars;
load su57_3d_model;
clf
hold on


for i = 1: length(Model3D.Aircraft)
    patch('Faces',Model3D.Aircraft(i).stl_data.faces,...
    'Vertices',Model3D.Aircraft(i).stl_data.vertices,...
    'FaceColor',Model3D.Aircraft(i).color,...
    'EdgeColor', 'none',...
    'FaceLighting', 'gouraud',...
    'FaceAlpha', Model3D.Aircraft(i).alpha);
end


for i = 1: length(Model3D.Control)
    patch('Faces',Model3D.Control(i).stl_data.faces,...
    'Vertices',Model3D.Control(i).stl_data.vertices,...
    'FaceColor',Model3D.Control(i).color,...
    'EdgeColor', 'none',...
    'FaceLighting', 'gouraud');
end

hold off
material('metal');
camlight('headlight');

L = [0 0 -150]/norm([0 0 -150]);
light('Position',L)
axis equal
axis off
view(15,-15)
grid on
