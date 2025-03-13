# stylegan2_pytorch 🔥

repo: https://github.com/lucidrains/stylegan2-pytorch

pros: 🔥

cons: 🔥

## help

```bash
@gan \
	ingest \
	[~cache,dataset=<dataset>,dryrun,upload] \
	[-|<object-name>] \
	<ingest-options>
 . ingest <dataset> -> <object-name>.
   dataset: animal10
   ingest-options
      animal10: animal=<animal-name>,count=<-1>
                animal-name: butterfly, cane, cat, chicken, cow, dog, elefante, elephant, farfalla, gallina, gatto, horse, mucca, ragno, scoiattolo, sheep, squirrel
```
```bash
@gan \
	stylegan2_pytorch \
	[~download,dryrun,~upload] \
	[.|<dataset-object-name>] \
	[-|<results-object-name>] \
	<args>
 . run stylegan2_pytorch.
```

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
