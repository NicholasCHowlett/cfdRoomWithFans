# Computational study of inside patterns of air which is forced into a room (thru a door opening) by a fan

Two-dimensional computational fluid dynamics simulation results showing airflow patterns within a room, airflow which is driven by an axial fan that is designed with noise reduction, are shown below. These investigations complement other COVID-focussed numerical studies of indoor environments [1], and readers are directed to this article as an example of an accessible computational fluid dynamics methodology. This study simulates a non-probable (likely non-physical) laminar flow regime.

![Computational domain: bounded by verrandah: results: airflow patterns: velocity streamlines](/streamlines.png)

Overall, due to forcing created by the fan, the fluid develops numerous recirculation regions, where fluid within each region circulates numerous times around a fixed point, of which both larger regions extend most of the vertical distance to the floor. Conversely, the air extrained above the fan (external to the large, left recirculation region) tends to exit thru the window or door. 

With regard to transmission of airborn virus particles (which were not simulated), the recirculation region occupying below ~ 1.0 metres is potentially a concern. As kids may exhale COVID-19 at this height, these virus particles may recirculate multiple times within each region (having increased residence time), as opposed to some particles that exit thru the bifold doors. Such recirculation would lead to increased virus exposure opportunity. However, the overall increased risk by larger residence may be offset by the smaller virus concentration.

The above assumption regarding particles following airflow patterns needs verification. Also, the exposure risk assumption due to larger residence time also needs verification. 

From the numerical side, the influence of three-dimensional geometry effects on these recirculation regions should be investigated before taking this 2D 'slice' as representative of the whole space (and as non-variant with depth). Also, validation &verification studies should also be included to provide confidence, and possibly quantification, of any numerical results (including this single study). Note, these results were calculated using an non-physical 'wall' boundary condition imposed at the end of the verrandah (limiting the domain to this vertical), thus a sensitivity study to check the effect of this BC should be conducted.

However, given the likeliness this flow regime is not laminar but turbulent, the above study is by implication of little real-world value. Instead, we propose a novel flow-modifying mechanism added to the fan to constantly induce Kelvin–Helmholtz instability, and hence ensure increased mixing of the flow as compared to our simulations (which show the unlikely, worst-case scenario).

Moreover, COVID-19 has demonstrated the enormous progress that scientists & engineers can make, when working together. Death to the institutions that b(l)ind us, welcome to the internet that unites us. All source code is available in my GitHub repository [2]. Respect to the enlightened commercial companies such as OpenBCI for fostering innovation at their probable financial detriment. This is what I consider real success.

For the next generation. For the kids. 

[1] Computational study on the transmission of the SARS-CoV-2 virus through aerosol in an elevator cabin: Effect of the ventilation system (https://doi.org/10.1063/5.0068244)  

[2] Computational science investigation of airflow inside rooms driven by fans (www.github.com/NicholasCHowlett/cfdRoomWithFans)
