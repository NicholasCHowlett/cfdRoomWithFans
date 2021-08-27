# Computational science investigation of airborn viruses within common spaces inside buildings
## Summary
This computation fluid dynamics study aims to determine easily-implemented, cheap interventions [1, 2] that can significantly reduce airborn virus transmission person-to-person, within schools' indoor environments (such as open-plan rooms and smaller workspaces). 

## Background
As this computational scientist agrees that there appear to be deficiencies in the Doherty Institute's predictions of COVID-19's new infection numbers into the future [3: Figure 1], once restrictions are severely relaxed due to hitting vaccination thresholds, this open-research/science team will attempt to model distribution of the virus at a more granular level. This will allow organisations controlling building spaces/rooms, which are to be modelled in this investigation, insight into the potential spread of COVID. 

Moreover our investigation will possibly allow targetted interventions to be implemented within buildings that are directly under the occupiers' control. Interventions including fans with differing locations, speeds, and orientations will be modelled. Virus' distribution at heights of children's heads will be of particular interest.

## Methodology
The CFD finite volume method will be employed, via OpenFOAM [4, 5], constructed on a predominently rectangular (block-structered) grid. The steady-state flow condition will be modelled, via the standard incompressible _icoFoam_ solver [6], to significantly reduce computational time which will allow a greater number of scenarios (i.e. larger parameter sweep) to be simulated. Grids will be more concentrated nearer the floor to ensure adequate accuracy at these regions.

## Validation of methodology
The computational results will be checked against real-world experimental results where available, to ensure accuracy of results and confidence in predictive capacity of the model. Specificially, carbon dioxide concentration levels in the spaces will be measured after releasing a known amount of CO2 within them, taken with interventions in place. The real-world results will be obtained multiple times by independent parties.

## Licenses
The OpenFOAM software is distributed under the [GNU General Public License](http://www.gnu.org/licenses/gpl-3.0.html). This project's entire written content (not limited to this respository) is released under the [Creative Commons Attribution-NonCommercial 4.0 International License](https://creativecommons.org/licenses/by-nc/4.0/).

## Computation infrastructure
Computations will be completed on cloud providers' hardware [7, 8]. Horizontal scaling to increase the number of compute nodes will be attempted if required.

### Notes
[1] https://theconversation.com/how-to-use-ventilation-and-air-filtration-to-prevent-the-spread-of-coronavirus-indoors-143732  
[2] https://theconversation.com/we-should-install-air-purifiers-with-hepa-filters-in-every-classroom-it-could-help-with-covid-bushfire-smoke-and-asthma-166332  
[3] https://medium.com/@matt_11659/australian-public-fed-nonsense-as-country-heads-to-irreversible-decision-99350b80125c  
[4] https://www.openfoam.com/documentation/user-guide/6-solving/6.2-numerical-schemes  
[5] https://github.com/OpenFOAM  
[6] https://cfd.direct/openfoam/user-guide/v9-standard-solvers/  
[7] https://www.digitalocean.com/products/droplets/  
[8] https://www.linode.com/products/dedicated-cpu/  