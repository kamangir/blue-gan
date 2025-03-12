# stylegan2_pytorch 🔥

repo: https://github.com/lucidrains/stylegan2-pytorch

pros: 🔥

cons: 🔥

## help

```bash
@help @gan ingest
```
```bash
@gan \
	ingest \
	[~cache,dataset=<dataset>,dryrun,upload] \
	[-|<object-name>] \
	<ingest-options>
 . browse blue_plugin.
   dataset: animal10
   ingest-options
      animal=butterfly | cane | cat | chicken | cow | dog | elefante | elephant | farfalla | gallina | gatto | horse | mucca | ragno | scoiattolo | sheep | squirrel,count=<-1>
```


```bash
@help @gan stylegan2_pytorch
```
```bash
@gan \
	stylegan2_pytorch \
	[dryrun,~upload] \
	[-|<object-name>]
 . run stylegan2_pytorch.
```

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
