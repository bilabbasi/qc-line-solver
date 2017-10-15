# Level set convex hulls using a line-solver  

The ideas behind the code are from the notion that quasiconvexity of a function, over a (convex) domain, is equivalent to quasiconvexity along lines partioning that domain.

## Getting Started

There are two folders: matlab and python. Each folder has (analogously) written code in each language.

### Python

All of the needed functions are contained in the *linesolver.py*. In particular, use *quasiconvex_rotate* to compute the quasiconvex envelope along a given slope (including it's rotation).

### Matlab

Use *ndim_linesolver.m* to generate convex hulls of a given obstacle *g*.

## Examples

Examples
## Authors

* **Bilal Abbasi** - [LinkedIn](https://www.linkedin.com/in/bilal-abbasi-51948655/)

* **Adam Oberman** - [Personal Website](http://www.adamoberman.net/)

## References
[Computing the level set convex hull](https://link.springer.com/epdf/10.1007/s10915-017-0522-8?author_access_token=JnmJ60gsLcGVYBUk5YOHQfe4RwlQNchNByi7wbcMAY4q8AK9yRT_34Luo0ewQQvaIbok4C6M-tOz6nND-LBp0wwaj-w0BFOm8Tkquc1IdL1NsVIMJXgfJjyeoRDaaQfjlJksXJIMT6E4ssVfKHeJuQ\%3D\%3D)

If you use the paper in your work, please use the following citation:

> @article{abbasi2017qcline, 
   author="Abbasi, Bilal and Oberman, Adam M.",
        title="Computing the Level Set Convex Hull", 
       journal="Journal of Scientific Computing", 
        year="2017", issn="1573-7691"}
