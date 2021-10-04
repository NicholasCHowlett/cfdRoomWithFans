# Computational science investigation of airflow in spaces inside newer buildings
## Summary
This computation fluid dynamics study aims to determine easily-implemented, cheap interventions [1, 2], such as fans, that can possibly significantly reduce COVID-19 airborn transmission, within indoor environments (such as open-plan rooms and smaller workspaces). Fans are a possible alternative intervention for rooms that do not have vents to induce 'air curtains' [3, 4].

## Background
As wind direction affects the airflow patterns within the rooms significantly [5: Figure 14], we posit that sufficient control & modification of the internal flow is important as a COVID-19 risk-reduction measure.

Such modification of the internal flow patterns has been investigated using computational fluid dynamics, proposing the effectiveness of 'air curtains' [3, 4], however no validation or verification activities supporting these studies were shown alongside numerical results.

## Scope
We aim to numerically investigate flow controlling mechanisms such as fans, while providing confidence in our results (and their predictive power) by ideally validating and verifying our results. More specifically, we aim to compare fans in differing positions, operating speeds, fan number, and orientation, upon the air quality within each rooms of a building composing both larger open-plan and smaller rooms. 

## Methodology
A laminar flow regime will be modelled [6a], along with a turbulent flow regime with an appropriate turbulence model [6b]. A comparison of laminar to turbulent regime will be conducted. The turbulence model will involve tuning tubulence-related parameters that are flow-dependent [7]. A more quantitative comparison of the turbulence parameters will also be attempted. 

The CFD finite volume method will be employed, via OpenFOAM [4, 5], meshed using a predominently rectangular (block-structered) grid. The steady-state flow condition will be modelled, via the standard incompressible _simpleFoam_ solver [6], to significantly reduce computational time, allowing a greater number of scenarios to be simulated. The grid size will be more concentrated nearer the heights of kids (approximately 1.0 metres) to ensure adequate accuracy, in addition to other more standard yet important regions.

## Validation of methodology
The computational results will be checked against real-world experimental results where available, to ensure accuracy of results and confidence in predictive capacity of the model. Specificially, carbon dioxide concentration levels in the spaces will be measured after releasing a known amount of CO2 within them, taken with interventions in place. The real-world results will be obtained multiple times by independent parties.

## Licenses
The OpenFOAM software is distributed under the [GNU General Public (version 3) License](http://www.gnu.org/licenses/gpl-3.0.html). This project's written content (not limited to this respository) is released under the [Creative Commons Attribution-NonCommercial 4.0 International License](https://creativecommons.org/licenses/by-nc/4.0/).

## Computation infrastructure
Computations will be completed on cloud providers' hardware [8, 9]. Horizontal scaling to increase the number of compute nodes will be attempted if required.

### Notes
[1] How to use ventilation and air filtration to prevent the spread of coronavirus indoors: https://theconversation.com/how-to-use-ventilation-and-air-filtration-to-prevent-the-spread-of-coronavirus-indoors-143732  

[2] We should install air purifiers with HEPA filters in every classroom. It could help with COVID, bushfire smoke and asthma:https://theconversation.com/we-should-install-air-purifiers-with-hepa-filters-in-every-classroom-it-could-help-with-covid-bushfire-smoke-and-asthma-166332  

[3] CFD Simulation of the Airborne Transmission of COVID-19 Vectors Emitted during Respiratory Mechanisms: Revisiting the Concept of Safe Distance: https://pubs.acs.org/doi/10.1021/acsomega.1c01489

[4] OpenFOAM Coronavirus response: Ventilation in office environments: https://www.openfoam.com/news/openfoam-coronavirus-response

[5]	Using CFD to Evaluate Natural Ventilation through a 3D Parametric Modeling Approach: https://doi.org/10.3390/en14082197

[6] a) simpleFoam with 'laminar' turbulence model: https://cfd.direct/openfoam/user-guide/v9-turbulence/#x37-2770007.2 b) simpleFoam with 'RAS' incompressible turbulence models.
 
[7] Introduction to turbulence: Reynolds averaged equations: Turbulence closure problem and eddy viscosity:https://www.cfd-online.com/Wiki/Introduction_to_turbulence/Reynolds_averaged_equations

[8] https://www.digitalocean.com/products/droplets/  

[9] https://www.linode.com/products/dedicated-cpu/  