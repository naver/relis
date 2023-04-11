### Here we define paths to datasets, model configs and checkpoints

CITYSCAPES_ROOT = 'PATH/TO/DSET'
CITYSCAPES_AUG_ROOT = 'PATH/TO/DSET' # If used
ACDC_ROOT = 'PATH/TO/DSET'
IDD_ROOT = 'PATH/TO/DSET'

mmseg_models_configs = {
    'SETR-PUP': 'mmsegmentation/configs/setr/setr_vit-large_pup_8x1_768x768_80k_cityscapes.py',
    'SETR-Naive': 'mmsegmentation/configs/setr/setr_vit-large_naive_8x1_768x768_80k_cityscapes.py',
    'SETR-MLA': 'mmsegmentation/configs/setr/setr_vit-large_mla_8x1_768x768_80k_cityscapes.py',
    'SegFormer-B0': 'mmsegmentation/configs/segformer/segformer_mit-b0_8x1_1024x1024_160k_cityscapes.py',
    'SegFormer-B1': 'mmsegmentation/configs/segformer/segformer_mit-b1_8x1_1024x1024_160k_cityscapes.py',
    'SegFormer-B2': 'mmsegmentation/configs/segformer/segformer_mit-b2_8x1_1024x1024_160k_cityscapes.py',
    'SegFormer-B3': 'mmsegmentation/configs/segformer/segformer_mit-b3_8x1_1024x1024_160k_cityscapes.py',
    'SegFormer-B4': 'mmsegmentation/configs/segformer/segformer_mit-b4_8x1_1024x1024_160k_cityscapes.py',
    'SegFormer-B5': 'mmsegmentation/configs/segformer/segformer_mit-b5_8x1_1024x1024_160k_cityscapes.py',
    'DLV3+ResNet50': 'mmsegmentation/configs/deeplabv3plus/deeplabv3plus_r50-d8_769x769_80k_cityscapes.py',
    'DLV3+ResNet101': 'mmsegmentation/configs/deeplabv3plus/deeplabv3plus_r101-d8_769x769_80k_cityscapes.py',
    'DLV3+ResNet18': 'mmsegmentation/configs/deeplabv3plus/deeplabv3plus_r18-d8_769x769_80k_cityscapes.py',
    'Segmenter': 'mmsegmentation/configs/segmenter/segmenter_vit-l_mask_4x1_769x769_160k_lr0.005_cityscapes.py', # Trained with mmseg
    'ConvNext': 'mmsegmentation/configs/convnext/upernet_convnext_large_fp16_769x769_80k_cityscapes.py', # Trained with mmseg
    'UpperNetR18': 'mmsegmentation/configs/upernet/upernet_r18_512x1024_80k_cityscapes.py',
    'UpperNetR50': 'mmsegmentation/configs/upernet/upernet_r50_769x769_80k_cityscapes.py',
    'UpperNetR101': 'mmsegmentation/configs/upernet/upernet_r101_769x769_80k_cityscapes.py',
    'ConvNext-B-In1K': 'mmsegmentation/configs/convnext/upernet_convnext_base_in1k_fp16_769x769_80k_cityscapes.py',
    'ConvNext-B-In21K': 'mmsegmentation/configs/convnext/upernet_convnext_base_in21k_fp16_769x769_80k_cityscapes.py',
    'BiT-R50x1-In1K': 'mmsegmentation/configs/bit/resnet50x1_in1k.py',
    'BiT-R50x1-In21K': 'mmsegmentation/configs/bit/resnet50x1_in21k.py',
	'Mask2Former': 'Mask2Former/configs/cityscapes/semantic-segmentation/swin/maskformer2_swin_large_IN21k_384_bs16_90k.yaml',
    'SegFormer-B5_v2': 'mmsegmentation/configs/segformer/segformer_mit-b5_4x1_1024x1024_80k_cityscapes_v2.py',
    'SegFormer-B5_v3': 'mmsegmentation/configs/segformer/segformer_mit-b5_4x1_1024x1024_80k_cityscapes_v3.py',
    'Segmenter_short': 'mmsegmentation/configs/segmenter/segmenter_vit-l_mask_4x1_769x769_80k_cityscapes.py',
    'MaskFormer': 'MaskFormer/configs/cityscapes-19/maskformer_R101c_bs16_90k.yaml',
    'SwinLarge': 'mmsegmentation/configs/swin/upernet_swin_large_patch4_window7_512x512_pretrain_224x224_22K_160k_cityscapes.py',
    }


# Paths to model checkpoints: Models should be downloaded from mmseg or locally trained
mmseg_models_checkpoints = {
    'SETR-PUP': '/gfs-ssd/project/uss/pre_trained_models/SETR/setr_pup_vit-large_8x1_768x768_80k_cityscapes_20211122_155115-f6f37b8f.pth',
    'SETR-Naive': '/gfs-ssd/project/uss/pre_trained_models/SETR/setr_naive_vit-large_8x1_768x768_80k_cityscapes_20211123_000505-20728e80.pth',
    'SETR-MLA': '/gfs-ssd/project/uss/pre_trained_models/SETR/setr_mla_vit-large_8x1_768x768_80k_cityscapes_20211119_101003-7f8dccbe.pth',
    'SegFormer-B0': '/gfs-ssd/project/uss/pre_trained_models/SegFormer/segformer_mit-b0_8x1_1024x1024_160k_cityscapes_20211208_101857-e7f88502.pth',
    'SegFormer-B1': '/gfs-ssd/project/uss/pre_trained_models/SegFormer/segformer_mit-b1_8x1_1024x1024_160k_cityscapes_20211208_064213-655c7b3f.pth',
    'SegFormer-B2': '/gfs-ssd/project/uss/pre_trained_models/SegFormer/segformer_mit-b2_8x1_1024x1024_160k_cityscapes_20211207_134205-6096669a.pth',
    'SegFormer-B3': '/gfs-ssd/project/uss/pre_trained_models/SegFormer/segformer_mit-b3_8x1_1024x1024_160k_cityscapes_20211206_224823-a8f8a177.pth',
    'SegFormer-B4': '/gfs-ssd/project/uss/pre_trained_models/SegFormer/segformer_mit-b4_8x1_1024x1024_160k_cityscapes_20211207_080709-07f6c333.pth',
    'SegFormer-B5': '/gfs-ssd/project/uss/pre_trained_models/SegFormer/segformer_mit-b5_8x1_1024x1024_160k_cityscapes_20211206_072934-87a052ec.pth',
    'DLV3+ResNet50': '/gfs-ssd/project/uss/pre_trained_models/DeepLabV3+/R-50-D8_769x769_80K/deeplabv3plus_r50-d8_769x769_80k_cityscapes_20200606_210233-0e9dfdc4.pth',
    'DLV3+ResNet101': '/gfs-ssd/project/uss/pre_trained_models/DeepLabV3+/R-101-D8_769x769_80K/deeplabv3plus_r101-d8_769x769_80k_cityscapes_20200607_000405-a7573d20.pth',
    'DLV3+ResNet18': '/gfs-ssd/project/uss/pre_trained_models/DeepLabV3+/R-18-D8_769x769_80K/deeplabv3plus_r18-d8_769x769_80k_cityscapes_20201226_083346-f326e06a.pth',
    'Segmenter': '/gfs-ssd/project/uss/pre_trained_models/Segmenter/segmenter_vit-l_mask_4x1_769x769_160k_lr0.005_cityscapes.pth',
    'ConvNext': '/gfs-ssd/project/uss/pre_trained_models/ConvNext/upernet_convnext_large_4x1_fp16_769x769_80k_cityscapes.pth',
    'UpperNetR18': '/gfs-ssd/project/uss/pre_trained_models/UpperNet/R18/upernet_r18_512x1024_80k_cityscapes_20220614_110712-c89a9188.pth',
    'UpperNetR50': '/gfs-ssd/project/uss/pre_trained_models/UpperNet/R50/upernet_r50_769x769_80k_cityscapes_20200607_005107-82ae7d15.pth',
    'UpperNetR101': '/gfs-ssd/project/uss/pre_trained_models/UpperNet/R101/upernet_r101_769x769_80k_cityscapes_20200607_001014-082fc334.pth',
    'ConvNext-B-In1K': '/gfs-ssd/project/uss/pre_trained_models/ConvNext/upernet_convnext_base_in1k_cityscapes.pth',
    'ConvNext-B-In21K': '/gfs-ssd/project/uss/pre_trained_models/ConvNext/upernet_convnext_base_in21k_cityscapes.pth',
    'BiT-R50x1-In1K': '/gfs-ssd/project/uss/pre_trained_models/BiT/upernet_bit_r50x1_in1k_cityscapes.pth',
    'BiT-R50x1-In21K': '/gfs-ssd/project/uss/pre_trained_models/BiT/upernet_bit_r50x1_in21k_cityscapes.pth',
	'Mask2Former': '/gfs-ssd/project/uss/pre_trained_models/Mask2Former/model_final_17c1ee.pkl',
    'SegFormer-B5_v2': '/gfs-ssd/project/uss/results/train_segformer_short_v2/iter_80000.pth',
    'SegFormer-B5_v3': '/gfs-ssd/project/uss/results/train_segformer_short_v3/iter_80000.pth',
    'Segmenter_short': '/gfs-ssd/project/uss/results/train_segmenter_short/iter_80000.pth',
    'MaskFormer': '/gfs-ssd/project/uss/pre_trained_models/MaskFormer/model_final_4f8ff9.pkl',
    'SwinLarge': '/gfs-ssd/project/uss/results/swin_large/iter_160000.pth',
    }
