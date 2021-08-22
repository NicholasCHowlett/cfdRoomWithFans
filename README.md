# Computational science investigation of airborn viruses within common spaces inside buildings
## Summary
This computation fluid dynamics study aims to determine easily-implemented, cheap interventions that can significantly reduce airborn virus transmission person-to-person, within indoor environments (namely open-plan rooms and smaller workspaces) of buildings. Interventions including fans with differing locations and speeds (separate to to building's air-con system) will be modelled. Virus' distribution at heights of children's heads (1 to 5 year-old kids) will be of particular interest.

## Methodology
The CFD finite volume method will be employed, via OpenFOAM [1, 2], constructed on a predominently rectangular (block-structered) grid. The steady-state flow condition will be modelled, via the standard incompressible _icoFoam_ solver [3], to significantly reduce computational time which will allow a greater number of scenarios (i.e. larger parameter sweep) to be simulated. Grids will be more concentrated nearer the floor to ensure adequate accuracy at these regions.

## Prediction & Validation using methodology
The computational simulation results will be checked against real-world experimental results where available, to ensure accuracy of results and confidence in predictive ability. Specificially, carbon dioxide concentration levels in the spaces will be measured after releasing a known amount of CO2 within them. These measurements will be taken with interventions in place, allowing model predictions of interventions to be validated. 

## Computation infrastructure
Computations will be completed on cloud providers' hardware [4, 5]. Horizontal scaling to increase the number of compute nodes will be attempted if required.

## Licenses
The OpenFOAM software is distributed under the [GNU General Public License](http://www.gnu.org/licenses/gpl-3.0.html). This project's entire written content (not limited to this respository) is released under the [Creative Commons Attribution-NonCommercial 4.0 International License](https://creativecommons.org/licenses/by-nc/4.0/).

### Notes
[1] https://www.openfoam.com/documentation/user-guide/6-solving/6.2-numerical-schemes  
[2] https://github.com/OpenFOAM  
[3] https://cfd.direct/openfoam/user-guide/v9-standard-solvers/  
[4] https://www.digitalocean.com/products/droplets/  
[5] https://www.linode.com/products/dedicated-cpu/