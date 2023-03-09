import open3d as o3d

# Load PCD file
pcd_filename = "transformed_174.pcd"
pcd = o3d.io.read_point_cloud(pcd_filename)

# Define the cuboid vertices in the correct order to create six rectangular faces
point1 = [0, 0, 0]
point2 = [1, 0, 0]
point3 = [1, 1, 0]
point4 = [0, 1, 0]
point5 = [0, 0, 1]
point6 = [1, 0, 1]
point7 = [1, 1, 1]
point8 = [0, 1, 1]

# Create an Open3D mesh object
cuboid = o3d.geometry.TriangleMesh()
cuboid.vertices = o3d.utility.Vector3dVector([point1, point2, point3, point4, point5, point6, point7, point8])
cuboid.triangles = o3d.utility.Vector3iVector([[0, 1, 2], [0, 2, 3], [0, 4, 1], [1, 4, 5], [1, 5, 2], [2, 5, 6], [2, 6, 3], [3, 6, 7], [0, 3, 7], [0, 7, 4], [4, 7, 6], [4, 6, 5]])

# Create a Visualizer object and add the mesh to it
vis = o3d.visualization.Visualizer()
vis.create_window()
vis.add_geometry(pcd)
vis.add_geometry(cuboid)

# Create a ViewControl object and set the initial position of the camera
view_control = vis.get_view_control()
view_control.set_lookat([0.5, 0.5, 0.25])
view_control.set_up([0, 0, 1])
view_control.set_front([1, 0, 0])

# Create a RenderOption object and set the show_coordinate_frame property to True
option = vis.get_render_option()
option.show_coordinate_frame = True

# Run the visualizer
vis.run()
vis.destroy_window()