Convert smplx parameter of Thuman2.1 to smplx mesh.

1. Download SMPLX model from https://smpl-x.is.tue.mpg.de/

2. Download Thuman2.1 smplx fittings from https://github.com/ytrock/THuman2.0-Dataset

3. Create python environment and install requirements.

```bash
conda create --name pkl2mesh python=3.11

conda activate pkl2mesh

pip install -r requirements.txt
```

4. 
```bash
python pkl2mesh.py
```