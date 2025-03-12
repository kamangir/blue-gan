# stylegan2_pytorch 🔥

repo: https://github.com/lucidrains/stylegan2-pytorch

pros: 🔥

cons: 🔥

## help

```bash
@help @gan ingest
```
--help-- blue_gan ingest


```bash
@help @gan stylegan2_pytorch
```
--help-- blue_gan stylegan2_pytorch

## sample run

🔥 run on GPU (SageMaker)

```bash
runme() {
    local object_name=stylegan2_pytorch-$(@@timestamp)

    @gan ingest \
        dataset=animal10 \
        $object_name \
        animals=cat,count=20

   @gan stylegan2_pytorch \
        ~download \
        $object_name
}

runme
```

🔥