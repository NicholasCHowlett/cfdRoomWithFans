# Computational science investigation of airborn viruses within common spaces inside buildings
## Summary
This computation fluid dynamics study aims to determine easily-implemented, cheap interventions [-1, 0] that can significantly reduce airborn virus transmission person-to-person, within schools' indoor environments (such as open-plan rooms and smaller workspaces). Interventions including fans with differing locations, speeds, and orientations will be modelled. Virus' distribution at heights of children's heads will be of particular interest.

## Methodology
The CFD finite volume method will be employed, via OpenFOAM [1, 2], constructed on a predominently rectangular (block-structered) grid. The steady-state flow condition will be modelled, via the standard incompressible _icoFoam_ solver [3], to significantly reduce computational time which will allow a greater number of scenarios (i.e. larger parameter sweep) to be simulated. Grids will be more concentrated nearer the floor to ensure adequate accuracy at these regions.

## Validation of methodology
The computational simulation results will be checked against real-world experimental results where available, to ensure accuracy of results and confidence in predictive ability. Specificially, carbon dioxide concentration levels in the spaces will be measured after releasing a known amount of CO2 within them. These measurements will be taken with interventions in place, allowing model predictions of interventions to be validated. 

## Licenses
The OpenFOAM software is distributed under the [GNU General Public License](http://www.gnu.org/licenses/gpl-3.0.html). This project's entire written content (not limited to this respository) is released under the [Creative Commons Attribution-NonCommercial 4.0 International License](https://creativecommons.org/licenses/by-nc/4.0/).

## Computation infrastructure
Computations will be completed on cloud providers' hardware [4, 5]. Horizontal scaling to increase the number of compute nodes will be attempted if required.

### Notes
[-1] https://theconversation.com/how-to-use-ventilation-and-air-filtration-to-prevent-the-spread-of-coronavirus-indoors-143732  
[0] https://theconversation.com/we-should-install-air-purifiers-with-hepa-filters-in-every-classroom-it-could-help-with-covid-bushfire-smoke-and-asthma-166332  
[1] https://www.openfoam.com/documentation/user-guide/6-solving/6.2-numerical-schemes  
[2] https://github.com/OpenFOAM  
[3] https://cfd.direct/openfoam/user-guide/v9-standard-solvers/  
[4] https://www.digitalocean.com/products/droplets/  
[5] https://www.linode.com/products/dedicated-cpu/