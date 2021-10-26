# Computational science investigation of airflow in spaces inside newer buildings

*Current development is focussed on modelling the laminar flow regime while changing the angle of fan with the intention of forcing flow out the door. This implicitly requires changing the 'door' boundary condition from a wall to open type.*

*The hypothesis of numerical instability due to insufficient computational domain & open-type boundary condition was incorrect, as convergence was achieved without changing either parameters.*

## Summary
This computation fluid dynamics study aims to determine easily-implemented, cheap interventions [1, 2], such as fans, that can possibly significantly reduce COVID-19 airborn transmission, within indoor environments (such as open-plan rooms and smaller workspaces) of education-based buildings. Fans are possibly a quicker alternative intervention for rooms that do not have vents to induce 'air curtains' [3, 4].

## Background
Current COVID19 risk-reduction measures inside buildings include promoting cross-ventilation (opening multiple windows and doors within a single room, for example) to enhance the ventilation of air within the room. 

Such measures rely on the assumptions that the fluid convection momentum outside is significant enough to actually induce an adequate ventilation 'rate', in addition to such momentum being large enough to induce turbulent flow (thus increasing the flow's diffusivity, as compared to laminar flow).

We posit that both aspects are questionable at the least, and simply using these measures, as is, may be inadequate for some poorly-designed rooms. We also tentatively posit that the Australian Government may be promoting such indiscriminate measures to pre-empt any significant concern from the general public, as they seemingly push their economy-first imperative. 

If current measures are insufficient to improve ventilation to a sufficient amount, we posit that modification of the air flow by other measures (interventions) would help cover this deficit.

Such modification of the air flow patterns has been investigated using computational fluid dynamics, proposing the effectiveness of 'air curtains' [3, 4], however no validation or verification activities supporting these studies were shown alongside numerical results.

As wind direction affects the airflow patterns within the rooms significantly [5: Figure 14], we posit that modification of the internal flow using interventions such as fans could be an effective COVID-19 risk-reduction measure.

## Scope
With these concerns in mind, we aim to numerical investigate the fluid flow within educational buildings, where the 'building design' as related to natural ventilation has been critised (in an Australian context). Both schools and early-learning centres will be the focus, where the flow of air within rooms will be simulated. 

As turbulent flow increases ventilation (as above), a computational fluid dynamics study of laminar flow will be modelled [6] to determine areas where further interventions (measures) would be most beneficial. Beneficial is defined as reducing the likelihood of transmission person-to-person, if the virus was exhaled by someone within a room.

We aim to numerically investigate flow controlling mechanisms such as fans, while providing confidence in our results (and their predictive power) by ideally validating and verifying our results. More specifically, we aim to compare fans in differing positions, operating speeds, fan number, and orientation, focussing on the 'air quality' within each room.  

## Methodology
The steady-state flow condition will be modelled, via the open-source OpenFOAM software [6], to significantly reduce computational time, allowing a greater number of scenarios to be simulated. The grid size will be more concentrated nearer the heights of kids (approximately 1.0 metres) to ensure adequate accuracy, in addition to other more standard-practice regions. 

OpenFOAM 9 running on Ubuntu 20.04 LTS [8], via the Windows Subsystem for Linux (WSL), is used for all numerical investigations. Note you may need to update Ubuntu's certification package before installing OpenFOAM: `sudo apt install ca-certificates`, then restart Ubuntu from PowerShell: `wsl --shutdown Ubuntu-20.04`.

You will need to install additional software to allow graphical output from WSL (plotting real-time flow quantities while running an OpenFOAM solver, for example). One option is configuring the VcXsrv software [9]. Tutorials for setting up VcXsrv are available [10].

## Computational domain
Current case geometry with triangular mesh visible that outlines the simplified two-dimensional domain is shown below. Left lower vertical line represents door opened to outside, angled line represents fan blowing at an angle, and high right (small) vertical line represents window opened to outside. Both geometry and meshing were completed within the open-source Salome 9.7 software [11]. 

![Computational domain: bounded by door: mesh_case-01](/mesh_case-01.PNG)

## Validation of methodology
The computational results will be checked against real-world experimental results where available, to ensure accuracy of results and confidence in predictive capacity of the model. Specificially, carbon dioxide concentration levels in the spaces will be measured after releasing a known amount of CO2 within them, taken with fan(s) in place. The real-world results will ideally be obtained multiple times by independent parties.

## Licenses
The OpenFOAM software is distributed under the [GNU General Public (version 3) License](http://www.gnu.org/licenses/gpl-3.0.html). This project's written content (not limited to this respository) is released under the [Creative Commons Attribution-NonCommercial 4.0 International License](https://creativecommons.org/licenses/by-nc/4.0/).

## Computation infrastructure
Computations will be completed on cloud providers' hardware [12, 13]. Horizontal scaling to increase the number of compute nodes will be attempted if required.

### Notes
[1] How to use ventilation and air filtration to prevent the spread of coronavirus indoors: https://theconversation.com/how-to-use-ventilation-and-air-filtration-to-prevent-the-spread-of-coronavirus-indoors-143732  

[2] We should install air purifiers with HEPA filters in every classroom. It could help with COVID, bushfire smoke and asthma:https://theconversation.com/we-should-install-air-purifiers-with-hepa-filters-in-every-classroom-it-could-help-with-covid-bushfire-smoke-and-asthma-166332  

[3] CFD Simulation of the Airborne Transmission of COVID-19 Vectors Emitted during Respiratory Mechanisms: Revisiting the Concept of Safe Distance: https://pubs.acs.org/doi/10.1021/acsomega.1c01489  

[4] OpenFOAM Coronavirus response: Ventilation in office environments: https://www.openfoam.com/news/openfoam-coronavirus-response  

[5]	Using CFD to Evaluate Natural Ventilation through a 3D Parametric Modeling Approach: https://doi.org/10.3390/en14082197  

[6] simpleFoam with: a) 'laminar' turbulence model. https://cfd.direct/openfoam/user-guide/v9-turbulence/#x37-2770007.2   

[8] https://openfoam.org/download/9-ubuntu/  

[9] https://sourceforge.net/projects/vcxsrv/  

[10] https://www.youtube.com/watch?v=VrDW1LOno_I&t=0s  

[11] https://www.salome-platform.org/  

[12] https://www.digitalocean.com/products/droplets/  

[13] https://www.linode.com/products/dedicated-cpu/  