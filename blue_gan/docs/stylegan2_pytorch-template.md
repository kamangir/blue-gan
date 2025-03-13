# stylegan2_pytorch

Repo: https://github.com/lucidrains/stylegan2-pytorch

- Generates novel images based on a set of training images. 
- Recent and stable.
- Basic implementation.

## help

--help-- blue_gan ingest
--help-- blue_gan stylegan2_pytorch

## sample run

🔋 on GPU (SageMaker)

```bash
@select dataset-$(@@timestamp)

@gan ingest \
    dataset=animal10 . \
    animal=cat,count=20

@select results-$(@@timestamp)

@gan stylegan2_pytorch \
    ~download .. . \
    --num_train_steps 100

mv -v default/* ./

@assets publish \
    extensions=jpg,push .
```

### `--num_train_steps 10`

set:::object_name results-2025-03-12-15nxc4

| 0-ema | 0-mr | 0 |
|-|-|-|
| assets:::get:::object_name/0-ema.jpg | assets:::get:::object_name/0-mr.jpg | assets:::get:::object_name/0.jpg |

### `--num_train_steps 100`

set:::object_name results-2025-03-12-476vr7

| 0-ema | 0-mr | 0 |
|-|-|-|
| assets:::get:::object_name/0-ema.jpg | assets:::get:::object_name/0-mr.jpg | assets:::get:::object_name/0.jpg |

Results are expected at `--num_train_steps 150000` 🤔