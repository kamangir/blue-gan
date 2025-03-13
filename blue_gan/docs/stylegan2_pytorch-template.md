# stylegan2_pytorch 🔥

repo: https://github.com/lucidrains/stylegan2-pytorch

pros: 🔥

cons: 🔥

## help

--help-- blue_gan ingest
--help-- blue_gan stylegan2_pytorch

## sample run

🔥 run on GPU (SageMaker)

```bash
@select dataset-$(@@timestamp)

@gan ingest \
    dataset=animal10 . \
    animal=cat,count=20

@select results-$(@@timestamp)

@gan stylegan2_pytorch \
    ~download,~upload .. . \
    --num_train_steps 100
```

🔥