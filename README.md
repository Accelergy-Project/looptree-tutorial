# LoopTree Tutorial
This is the tutorial repository for "[LoopTree: Exploring the Fused-layer Dataflow Accelerator Design Space](https://arxiv.org/abs/2409.13625)" by Michael Gilbert, Yannan Nellie Wu, Joel S. Emer, and Vivienne Sze.

The tutorial can be easily setup using Docker by following the steps described below.

## Quick Start
Please make a copy of the `docker-compose.template.yaml` file named `docker-compose.yaml` and update the file as instructed (instructions are within the template).

Then, run the following command.

```
docker compose up
```

## More Resources
You might find the following resources useful.
- [The LoopTree paper](https://arxiv.org/abs/2409.13625).
- [Timeloop/Accelergy v4 documentation](https://timeloop.csail.mit.edu/v4).
- [The PyTimeloop code](https://github.com/Accelergy-Project/timeloop-python).
- [The Timeloop code](https://github.com/NVlabs/timeloop).

## Citation
If you use LoopTree in your research, please cite the LoopTree paper.
> M. Gilbert, Y. N. Wu, J. S. Emer and V. Sze, "LoopTree: Exploring the Fused-layer Dataflow Accelerator Design Space," in IEEE Transactions on Circuits and Systems for Artificial Intelligence, doi: 10.1109/TCASAI.2024.3461716.
keywords: {System-on-chip;Filters;Tensors;Space exploration;Taxonomy;Shape;Energy consumption},

Or, use the following BibTex.
```
@ARTICLE{looptree,
  author   = {Gilbert, Michael and Wu, Yannan Nellie and Emer, Joel S. and Sze, Vivienne},
  journal  = {IEEE Transactions on Circuits and Systems for Artificial Intelligence}, 
  title    = {LoopTree: Exploring the Fused-layer Dataflow Accelerator Design Space}, 
  year     = {2024},
  volume   = {},
  number   = {},
  pages    = {1-15},
  keywords = {System-on-chip;Filters;Tensors;Space exploration;Taxonomy;Shape;Energy consumption},
  doi      = {10.1109/TCASAI.2024.3461716}}
```