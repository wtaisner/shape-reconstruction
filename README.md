# shape-reconstruction
Shape reconstruction from RGBD images from ShapeNet dataset.

## Milestone X - 12.05.2023
| Prediction vs ground truth                                                                                      | IOU @ [0.2, 0.3, 0.4, 0.5]                                                        |
|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| ![example 1](static/example_predictions/prediction_02933112_depth_2f0a56c30e384642c59350d819542ec7_0720001.png) | [0.662952184677124, 0.678329348564148, 0.670099139213562, 0.6430394649505615]     |
 | ![example 2](static/example_predictions/prediction_02958343_depth_6e0e38fa4613df14af3abff6cd36a38e_2520001.png) | [0.7360618710517883, 0.7447314858436584, 0.7390680909156799, 0.7052906155586243]  |
 | ![example 3](static/example_predictions/prediction_03001627_depth_284463280e6a4d003719086e0b4ab8be_2880001.png) | [0.2536977529525757, 0.2402084320783615, 0.2236427366733551, 0.1977536380290985]  |
 | ![example 4](static/example_predictions/prediction_03691459_depth_a58fe03c817fd0311ad88f716ea80910_1440001.png) | [0.5040155053138733, 0.49083250761032104, 0.4773334562778473, 0.4625006318092346] |


## Milestone 1 - 21.04.2023
Activities performed:
- implementation of ShapeNet sampling script (`scripts/sample_shapenet.py`)
- implementation of RenderBlender(TM) - a script parsing meshes into RGB and depth images (`scripts/render_blender.py`)
- preprocessing of the sampled pared of the dataset (10%)

| RGB                            | DEPTH                              |
|--------------------------------|------------------------------------|
| ![rgb](static/example_rgb.png) | ![depth](static/example_depth.png) |

## Literature / useful sources:
- [POCO](https://github.com/valeoai/poco)
- [3D Reconstruction of Novel Object Shapes from Single Images](https://github.com/rehg-lab/3dshapegen)
- [3D Reconstruction from RGB-D](https://openaccess.thecvf.com/content_ICCV_2017_workshops/papers/w13/Yang_3D_Object_Reconstruction_ICCV_2017_paper.pdf)
- [Papers with code](https://paperswithcode.com/task/single-view-3d-reconstruction)
- [Large-Scale 3D Shape Reconstruction and Segmentation from ShapeNet Core55](https://arxiv.org/pdf/1710.06104.pdf)
