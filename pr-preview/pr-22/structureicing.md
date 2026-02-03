
---
title: StructureIcing
theme: theme_name
cover-image: https://raw.githubusercontent.com/gtif-cerulean/cif-stories/35ad041149bc014b205f9515224e10c0421d41df/assets/OffShoreWindmillIcing-1770134061946.jpg
date: 2025-01-01
tags: tag1
official: true
---

# CIF Capability: Structure Icing on off-shore infrastructure <!--{ as="img" data-fallback-src="https://raw.githubusercontent.com/BlackCA/cif-stories/BlackCA/structureicing/assets/BlackCA/OffShoreWindmillIcing-1770134061946.jpg" mode="hero" src="https://raw.githubusercontent.com/gtif-cerulean/cif-stories/35ad041149bc014b205f9515224e10c0421d41df/assets/OffShoreWindmillIcing-1770134061946.jpg" }-->
 <!--{ style="font-size:1rem;opacity:0.7;margin-top:1rem;" }-->
## A capability of the CIF Dashboard, the Structure Icing algorithm links atmospheric and ocean conditions to estimate how quickly ice can accumulate on offshore structures such as wind turbines, ships, and platforms.  

#
<div>
  <div style="text-align: center;">
    <img src="https://raw.githubusercontent.com/BlackCA/cif-stories/BlackCA/cif-projectoverviewstory/assets/BlackCA/CIF-wordmark1-1759774247335.png"
         alt="CIF logo"
         width="50%"
         style="margin-bottom: 0.5em;">
  </div>
  <br>
</div>

As offshore activity expands into colder ocean environments, ice is no longer only something that floats on the sea. In many environments, it grows directly on the structures themselves.    
		
For offshore wind turbines, ships, and platforms, atmospheric icing can quietly change how these structures behave. Ice accumulation can reduce turbine power production, damage blades, create hazards for personnel as ice sheds from height, and—even more critically for floating turbines—create dangerous balance issues. For ships and offshore platforms, heavy ice build-up can affect stability, access, and safety.


Understanding when, where, and how fast ice can accumulate on structures is therefore an important part of operating safely in cold marine environments.

Why Structure Icing Matters

Cold climates offer advantages for wind energy. Colder air is denser, which increases potential power production. But these same environments also create ideal conditions for atmospheric icing.

Most icing events do not occur in extreme cold. Instead, they happen in the temperature range between −15°C and 0°C, when air contains enough moisture for droplets to freeze on contact with surfaces.

Ice build-up on turbine blades can:
	•	Reduce aerodynamic efficiency and lower power output
	•	Force turbines to shut down for safety reasons
	•	Increase mechanical wear and structural fatigue
	•	Cause ice to fall from height, posing risks to nearby vessels and personnel
	•	Create mass imbalances that are especially hazardous for floating turbines

For operators, icing can also lead to overly optimistic power forecasts if not properly anticipated.

The Three Ways Ice Forms on Offshore Structures

Atmospheric icing of offshore structures occurs through three main mechanisms:
	1.	Sea spray icing
Wind and waves throw super-cooled saltwater droplets into the air. When these droplets strike a cold surface, they freeze instantly. This is often the most severe form of icing for offshore structures.
	2.	Precipitation icing
Freezing rain or wet snow can accumulate on turbine blades and structures. When temperatures drop slightly below freezing, this wet accumulation hardens into dense, strongly adhered ice.
	3.	Frost icing
Water vapor in the air can freeze directly onto surfaces. While visually striking, this form of icing is generally light and not considered a major operational concern.

Different combinations of temperature, wind speed, droplet size, and moisture content produce different kinds of ice, such as soft rime, hard rime, or dense glaze ice. These ice types behave very differently: some are light and brittle, while others form heavy, solid layers that are difficult to remove and more damaging to equipment.

Structure Icing on Offshore Wind Turbines 

Who Needs Structure Icing Information?

Several groups rely on understanding icing risks:
	1.	Wind farm operators:
To anticipate power losses, plan turbine shutdowns, and schedule maintenance safely.
	2.	Marine operators and service crews:
To assess whether it is safe to approach or work near iced structures.
	3.	Design engineers and planners:
To understand long-term icing exposure when planning new offshore installations in cold regions.
	4.	Researchers and policymakers:
To evaluate how icing risks change seasonally and geographically as offshore activity expands northward.

What Data the CIF Dashboard Uses to Assess Icing

Assessing icing risk requires combining several environmental variables that control how quickly ice can form on a surface:
	•	2 m air temperature
	•	Sea surface temperature
	•	Wind speed
	•	Sea ice concentration (to determine when sea spray is possible)
	•	Occurrence of freezing rain or wet snow
	•	Sea surface salinity (which determines the freezing point of seawater)

These variables are obtained from the ECMWF ERA5 reanalysis and global ocean reanalysis products and are processed into daily spatial averages for the region of interest.

How the CIF Dashboard Assesses Structure Icing

The CIF Dashboard combines two well-established scientific models:
	•	A sea spray icing model, originally developed for vessels and now widely used operationally, which estimates how quickly super-cooled sea spray can freeze onto a structure based on wind speed, air temperature, sea temperature, and seawater freezing point.
	•	A precipitation icing model, which estimates ice accumulation from freezing rain and wet snow based on wind speed, droplet size, and the efficiency with which turbine blades collect freezing droplets.

Together, these models estimate how rapidly ice can accumulate on exposed structures such as turbine blades and offshore platforms under given environmental conditions.

What CIF’s Dashboard Produces

For every location and time period, the CIF Dashboard calculates:
	•	The potential rate of ice accretion on offshore structures
	•	Whether icing is likely driven by sea spray or precipitation
	•	Maps showing where icing risks are low, moderate, or severe
	•	Inputs for operational planning, forecasting, and long-term risk assessment

These outputs can be viewed as map layers and integrated with other CIF datasets to support decision-making.

Structure Icing in the CIF Dashboard

On the CIF Dashboard, users can explore historical and real-time icing risk maps, examine how icing potential varies across regions and seasons, and assess how environmental conditions translate into operational risks for offshore wind turbines and other marine structures.