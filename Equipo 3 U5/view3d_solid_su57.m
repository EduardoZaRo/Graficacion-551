airplane = load('su57_3d_model.mat');
hold on
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
