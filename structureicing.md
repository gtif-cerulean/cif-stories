
---
title: StructureIcing
theme: theme_name
cover-image: https://raw.githubusercontent.com/gtif-cerulean/cif-stories/35ad041149bc014b205f9515224e10c0421d41df/assets/OffShoreWindmillIcing-1770134061946.jpg
date: 2025-01-01
tags: tag1
official: true
---

# CIF Capability: Structure icing on off-shore infrastructure <!--{ as="img" data-fallback-src="https://raw.githubusercontent.com/BlackCA/cif-stories/BlackCA/structureicing/assets/BlackCA/OffShoreWindmillIcing-1770134061946.jpg" mode="hero" src="https://raw.githubusercontent.com/gtif-cerulean/cif-stories/35ad041149bc014b205f9515224e10c0421d41df/assets/OffShoreWindmillIcing-1770134061946.jpg" }-->
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

As offshore activity expands in cold ocean environments, ice – not only on the sea surface – becomes a threat to safety and proper functioning of infrastructure. In the right conditions, ice grows directly on the structures themselves.    
		
For offshore wind turbines, ships, and platforms, atmospheric icing and icing due to sea spray can quietly change how these structures behave. Ice accumulation can reduce turbine power production, damage blades, create hazards for personnel as ice sheds from height, and—even more critically for floating turbines—create dangerous balance issues. For ships and offshore platforms, heavy ice build-up can affect stability, access, and safety.

Understanding when, where, and how fast ice can accumulate on structures is an important part of operating safely in cold marine environments.

### Why Structure Icing Matters

Cold climates offer advantages for wind energy. Colder air is denser, which increases potential power production. But these same environments also create ideal conditions for atmospheric icing.

Most icing events do not occur in extreme cold. Instead, they happen in the temperature range between −15°C and 0°C, when air contains enough moisture for droplets to freeze on contact with surfaces.

Ice build-up on turbine blades can:
- Reduce aerodynamic efficiency and lower power output
- Force turbines to shut down for safety reasons
- Increase mechanical wear and structural fatigue
- Cause ice to fall from height, posing risks to nearby vessels and personnel
- Create mass imbalances that are especially hazardous for floating turbines

For operators, icing can also lead to overly optimistic power forecasts if not properly forecasted.

### The Three Ways Ice Forms on Offshore Structures

Atmospheric icing of offshore structures occurs through three main mechanisms:
1. Sea spray icing: Wind and waves throw super-cooled saltwater droplets into the air. When these droplets strike a cold surface, they freeze instantly. This is often the most severe form of icing for offshore structures.
2. Precipitation icing: Freezing rain or wet snow can accumulate on turbine blades and structures. When temperatures drop slightly below freezing, this wet accumulation hardens into dense, strongly adhered ice.
3. Frost icing: Water vapor in the air can freeze directly onto surfaces. While visually striking, this form of icing is generally light and not considered a major operational concern.

Different combinations of temperature, wind speed, droplet size, and moisture content produce different kinds of ice, such as soft rime, hard rime, or dense glaze ice. These ice types behave very differently: some are light and brittle, while others form heavy, solid layers that are difficult to remove and more damaging to equipment.

## Image Tour <!--{ as="img" mode="tour" position="right"}-->
### 
<!--{ src="https://raw.githubusercontent.com/BlackCA/cif-stories/18ef9abd132764255b7b0ba270e9e591222131fa/assets/BlackCA/IMG_1312-NPI-high-res-scaled.jpg" style="background: #ffe7ef;" }-->

#### Who Needs Structure Icing Information?
Several groups rely on understanding icing risks:
1. **Wind farm operators:** to anticipate power losses, plan turbine shutdowns, and schedule maintenance safely.
2. **Marine operators and service crews:** to assess whether it is safe to approach or work near iced structures.
3. **Design engineers and planners:** to understand long-term icing exposure when planning new offshore installations in cold regions.
4. **Researchers and policymakers:** to evaluate how icing risks change seasonally and geographically as offshore activity expands northward.


## What Data the CIF Dashboard Uses to Predict Icing
Assessing icing risk requires combining several environmental variables that control how quickly ice can form on a surface:
- 2 m air temperature
- Sea surface temperature
- Wind speed
- Sea ice concentration (to determine when sea spray is possible)
- Occurrence of freezing rain or wet snow
- Sea surface salinity (which determines the freezing point of seawater)

These variables are obtained from the European Centre for Medium-Range Weather Forecasts reanalysis and global ocean reanalysis products and are processed into daily spatial averages for the region of interest.

### How the CIF Dashboard Assesses Structure Icing

The CIF Dashboard combines two well-established scientific models:
1. A sea spray icing model, originally developed for vessels and now widely used operationally, which estimates how quickly super-cooled sea spray can freeze onto a structure based on wind speed, air temperature, sea temperature, and seawater freezing point.
2. A precipitation icing model, which estimates ice accumulation from freezing rain and wet snow based on wind speed, droplet size, and the efficiency with which turbine blades collect freezing droplets.

Together, these models estimate how rapidly ice can accumulate on exposed structures such as turbine blades and offshore platforms dependent on environmental conditions.

### What the CIF Dashboard Produces

For a selected location and time period, the CIF Dashboard calculates:
- The potential rate of ice accretion on offshore structures
- Whether icing is likely driven by sea spray or precipitation
- Maps showing where icing risks are low, moderate, or severe
- Inputs for operational planning, forecasting, and long-term risk assessment

These outputs can be viewed as map layers and integrated with other CIF datasets to support decision-making.

## Icing map <!--{as="eox-map" style="width: 100%; height: 500px;" layers='[{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"sx-cat_ortho680500;:;EPSG:3857","title":"Terrain Light Stereographic North"},"source":{"type":"TileWMS","url":"https://sxcat-demo.eox.at/sxcat_maps/wms","projection":"ORTHO:680500","tileGrid":{"tileSize":[512,512]},"attributions":"{ Terrain light: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors and <a href=\"https://maps.eox.at/#data\" target=\"_blank\">others</a>, Rendering &copy; <a href=\"http://eox.at\" target=\"_blank\">EOX</a> }","params":{"LAYERS":"sx-cat_ortho680500","TILED":true}}},{"type":"Tile","properties":{"id":"cloudless-2024;:;EPSG:3857","title":"EOxCloudless 2024"},"source":{"type":"XYZ","url":"https://s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2024_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857","attributions":"{ EOxCloudless 2024: <a href=\"https://s2maps.eu\" target=\"_blank\">Sentinel-2 cloudless - s2maps.eu</a> by <a href=\"https://eox.at\" target=\"_blank\">EOX IT Services GmbH</a> (Contains modified Copernicus Sentinel data 2024) }"}},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain light"},"source":{"type":"XYZ","url":"https://s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857","attributions":"{ Terrain light: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors and <a href=\"https://maps.eox.at/#data\" target=\"_blank\">others</a>, Rendering &copy; <a href=\"http://eox.at\" target=\"_blank\">EOX</a> }"}},{"type":"Tile","properties":{"id":"eox-osm;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"https://s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857","attributions":"{ OSM: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors and <a href=\"https://maps.eox.at/#data\" target=\"_blank\">others</a>, Rendering &copy; <a href=\"http://eox.at\" target=\"_blank\">EOX</a> }"}}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"WebGLTile","properties":{"id":"structureicing_processf989197c-c3d1-11f0-b986-0255ac100045","title":"Results structureicing "},"source":{"type":"GeoTIFF","normalize":false,"sources":[{"url":"https://obs.eu-nl.otc.t-systems.com/gtif-data-cerulean1/output-structure-icing/pygeoapi-job-f989197c-c3d1-11f0-b986-0255ac100045/harshness_2020_2022_icing_moderate_0.4_0.4_-73.75567183840752_38.547950784470686_-39.10000731850119_53.91068379062307_QQ==.tif"}]},"style":{"variables":{"vmin":0,"vmax":19.71},"color":["case",[">",["band",1],0],["interpolate",["linear"],["/",["-",["band",1],["var","vmin"]],["-",["var","vmax"],["var","vmin"]]],0,[12,51,131,1],0.265,[10,136,186,1],0.638,[242,211,56,1],1,[217,30,30,1]],["color",0,0,0,0]]}}]},{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"https://s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857","attributions":"{ Overlay: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors, Made with Natural Earth, Rendering &copy; <a href=\"https://eox.at\" target=\"_blank\">EOX</a> }"}},{"type":"Vector","source":{"type":"Vector","url":"https://workspace-ui-public.cif.gtif.eox.at/api/public/share/public-4wazei3y-02/wind_energy.geojson","format":{"type":"GeoJSON","dataProjection":"EPSG:4326"}},"properties":{"id":"Wind_Energy_Areas","title":"Wind Energy Areas"},"style":{"stroke-color":"#ff0000","fill-color":"#00000000","stroke-width":3}}]}]' zoom="6.311748315004959" center=[-55.106770825093996,48.18588798129247] projection="" }-->

## Try out the Structure Icing Index on the CIF Dashboard
See the application of the [Structure Icing Index capability in the CIF Dashboard](https://cif.eox.at/uc1dashboard/?x=-37.4448&y=59.2537&z=4.3117&template=light&indicator=structureicing&datetime=2026-02-03). Explore historical and real-time icing risk maps, examine how icing potential varies across regions and seasons, and assess how environmental conditions translate into operational risks for offshore wind turbines and other marine structures.

