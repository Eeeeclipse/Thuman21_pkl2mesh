from smplx import SMPLX
import trimesh
from torch import Tensor
import pickle

def init_model(model_path):
    smplx_model = SMPLX(model_path, model_type='smplx', use_pca=False)
    return smplx_model

def read_smplx_paras(pkl_path):
    with open(pkl_path, 'rb') as f:
        params = pickle.load(f)
    for k, v in params.items():
        params[k] = Tensor(v)    
    return params

def generate_mesh(model_path, pkl_path, mesh_out_path):
    smplx_model = init_model(model_path)
    params = read_smplx_paras(pkl_path)
    output = smplx_model(
        global_orient=params['global_orient'],
        transl=params['transl'],
        betas=params['betas'],
        body_pose=params['body_pose'],
        left_hand_pose=params['left_hand_pose'],
        right_hand_pose=params['right_hand_pose'],
        jaw_pose=params['jaw_pose'],
        leye_pose=params['leye_pose'],
        reye_pose=params['reye_pose'],
        scale=params['scale'],
        expression=params['expression']
    )
    vertices = output.vertices[0]
    faces = smplx_model.faces  
    mesh = trimesh.Trimesh(vertices, faces, process=False)
    mesh.export(mesh_out_path)
    
model_path = 'models/smplx/SMPLX_NEUTRAL.npz'
pkl_path = 'smplx/0525/smplx_param.pkl'
mesh_out_path = 'mesh_out.obj'

generate_mesh(model_path, pkl_path, mesh_out_path)