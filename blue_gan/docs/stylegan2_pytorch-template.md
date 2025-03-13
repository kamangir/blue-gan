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
runme() {
    local object_name=stylegan2_pytorch-$(@@timestamp)

    @gan ingest \
        dataset=animal10 \
        $object_name \
        animal=cat,count=20

   @gan stylegan2_pytorch \
        ~download \
        $object_name \
        --num_train_steps 100
}

runme
```

🔥