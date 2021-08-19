# Computational science investigation of airborn viruses within commonly enclosed spaces
## summary
This computation fluid dynamics study aims to determine if there are easily implemented and cheap interventions that can significantly reduce viral transmission from person-to-person, within indoor environments (namely open-plan rooms and smaller workspaces).

## methodology
The CFD finite volume method will be employed, via OpenFOAM [1], constructed on a predominently rectangular (block-structered) grid. The steady-state flow condition will be modelled, via the standard incompressible _icoFoam_ solver [2], to significantly reduce computational time which will allow a greater number of scenarios (i.e. larger parameter sweep) to be simulated. 

## prediction & validation using methodology
This computational methodology will be validated against real-world experimental results where available, to ensure accuracy of computations. Interventions such as fans with differing locations and speeds (separate to to building's air-con system) will be predicted using the modelling, and validated where possible. 

## computation hardware
Computations will be completed on cloud providers' infrastructure [3, 4]. Horizontal scaling to increase the number of compute nodes will be attempted if required.

### notes
[1] https://www.openfoam.com/documentation/user-guide/6-solving/6.2-numerical-schemes  
[2] https://cfd.direct/openfoam/user-guide/v9-standard-solvers/  
[3] https://www.digitalocean.com/products/droplets/  
[4] https://www.linode.com/products/dedicated-cpu/