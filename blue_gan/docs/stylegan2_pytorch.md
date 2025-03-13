# stylegan2_pytorch

Repo: https://github.com/lucidrains/stylegan2-pytorch

- Generates novel images based on a set of training images. 
- Recent and stable.
- Basic implementation.

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


| 0-ema | 0-mr | 0 |
|-|-|-|
| ![image](https://github.com/kamangir/assets/blob/main/results-2025-03-12-15nxc4/0-ema.jpg?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/results-2025-03-12-15nxc4/0-mr.jpg?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/results-2025-03-12-15nxc4/0.jpg?raw=true) |

### `--num_train_steps 100`


| 0-ema | 0-mr | 0 |
|-|-|-|
| ![image](https://github.com/kamangir/assets/blob/main/results-2025-03-12-476vr7/0-ema.jpg?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/results-2025-03-12-476vr7/0-mr.jpg?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/results-2025-03-12-476vr7/0.jpg?raw=true) |

Results are expected at `--num_train_steps 150000` 🤔
