# Computational science investigation of airborn viruses within common spaces inside buildings
## Summary
This computation fluid dynamics study aims to determine easily-implemented, cheap interventions that can significantly reduce airborn virus transmission person-to-person, within indoor environments (namely open-plan rooms and smaller workspaces) of buildings. Virus' distribution at heights of children's heads (1 to 5 year-old kids) will be of particular interest.

## Methodology
The CFD finite volume method will be employed, via OpenFOAM [1], constructed on a predominently rectangular (block-structered) grid. The steady-state flow condition will be modelled, via the standard incompressible _icoFoam_ solver [2], to significantly reduce computational time which will allow a greater number of scenarios (i.e. larger parameter sweep) to be simulated. Grids will be more concentrated nearer the floor to ensure adequate accuracy at these regions.

## Prediction & Validation using methodology
The computational simulation results will be checked against real-world experimental results where available, to ensure accuracy of results and confidence in predictive ability. Then, interventions such as fans with differing locations and speeds (separate to to building's air-con system) will be predicted using the modelling, and validated where possible. 

## Computation infrastructure
Computations will be completed on cloud providers' hardware [3, 4]. Horizontal scaling to increase the number of compute nodes will be attempted if required.

### Notes
[1] https://www.openfoam.com/documentation/user-guide/6-solving/6.2-numerical-schemes  
[2] https://cfd.direct/openfoam/user-guide/v9-standard-solvers/  
[3] https://www.digitalocean.com/products/droplets/  
[4] https://www.linode.com/products/dedicated-cpu/