# PyTorch_GAN 🛑

Repo: https://github.com/eriklindernoren/PyTorch-GAN

- Implementation of 32 algo.
- 6+ years old, missing assets, bugs. 🛑

## help

```bash
@help @gan PyTorch_GAN
```
--help-- blue_gan PyTorch_GAN

## sample run

```bash
@gan PyTorch_GAN - bicyclegan
```

```
WARNING: timestamping does nothing in combination with -O. See the manual
for details.

--2025-03-11 16:10:56--  https://people.eecs.berkeley.edu/~tinghuiz/projects/pix2pix/datasets/edges2shoes.tar.gz
Resolving people.eecs.berkeley.edu (people.eecs.berkeley.edu)... 128.32.244.190
Connecting to people.eecs.berkeley.edu (people.eecs.berkeley.edu)|128.32.244.190|:443... connected.
HTTP request sent, awaiting response... 301 Moved Permanently
Location: https://tinghuiz.github.io/projects/pix2pix/datasets/edges2shoes.tar.gz [following]
--2025-03-11 16:10:56--  https://tinghuiz.github.io/projects/pix2pix/datasets/edges2shoes.tar.gz
Resolving tinghuiz.github.io (tinghuiz.github.io)... 2606:50c0:8001::153, 2606:50c0:8000::153, 2606:50c0:8002::153, ...
Connecting to tinghuiz.github.io (tinghuiz.github.io)|2606:50c0:8001::153|:443... connected.
HTTP request sent, awaiting response... 404 Not Found
2025-03-11 16:10:57 ERROR 404: Not Found. ⚠️

mkdir: ./edges2shoes/: File exists
Namespace(epoch=0, n_epochs=200, dataset_name='edges2shoes', batch_size=8, lr=0.0002, b1=0.5, b2=0.999, n_cpu=8, img_height=128, img_width=128, channels=3, latent_dim=8, sample_interval=400, checkpoint_interval=-1, lambda_pixel=10, lambda_latent=0.5, lambda_kl=0.01)
/opt/anaconda3/envs/roofai/lib/python3.9/site-packages/torchvision/models/_utils.py:208: UserWarning: The parameter 'pretrained' is deprecated since 0.13 and may be removed in the future, please use 'weights' instead.
  warnings.warn(
/opt/anaconda3/envs/roofai/lib/python3.9/site-packages/torchvision/models/_utils.py:223: UserWarning: Arguments other than a weight enum or `None` for 'weights' are deprecated since 0.13 and may be removed in the future. The current behavior is equivalent to passing `weights=None`.
  warnings.warn(msg)
Traceback (most recent call last):
  File "/Users/kamangir/git/PyTorch-GAN/implementations/bicyclegan/bicyclegan.py", line 58, in <module>
    D_VAE = MultiDiscriminator(input_shape)
  File "/Users/kamangir/git/PyTorch-GAN/implementations/bicyclegan/models.py", line 153, in __init__
    self.downsample = nn.AvgPool2d(in_channels, stride=2, padding=[1, 1], count_include_pad=False)
NameError: name 'in_channels' is not defined ⚠️
```

failed. 🛑