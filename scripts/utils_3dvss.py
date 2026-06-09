import numpy as np

def create_cam_to_world_matrix(cam_position, cam_target, cam_up):
    """
    Create a camera-to-world transformation matrix.

    Parameters:
    - cam_position: A 3D vector representing the camera's position in world space.
    - cam_target: A 3D vector representing the point the camera is looking at.
    - cam_up: A 3D vector representing the up direction for the camera.

    Returns:
    - A 4x4 numpy array representing the camera-to-world transformation matrix.
    """
    # Compute the forward, right, and up vectors
    forward = (cam_position - cam_target)
    forward /= np.linalg.norm(forward)

    right = np.cross(cam_up, forward)
    right /= np.linalg.norm(right)

    up = np.cross(forward, right)

    # Create the rotation matrix
    rotation_matrix = np.array([right, up, forward]).T

    # Create the translation vector
    translation_vector = cam_position

    # Combine rotation and translation into a single 4x4 matrix
    cam_to_world_matrix = np.eye(4)
    cam_to_world_matrix[:3, :3] = rotation_matrix
    cam_to_world_matrix[:3, 3] = translation_vector

    return cam_to_world_matrix
