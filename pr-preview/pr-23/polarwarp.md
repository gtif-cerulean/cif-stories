---
title: SatelliteImageWarping
theme: theme_name
cover-image: https://raw.githubusercontent.com/BlackCA/cif-stories/BlackCA/polarwarp/assets/BlackCA/DSC0294-1770215254818.JPG
date: 2025-01-01
tags: tag1
official: true
---
# CIF Capability: Sea Ice Motion Animation <!--{ as="img" data-fallback-src="https://raw.githubusercontent.com/BlackCA/cif-stories/BlackCA/polarwarp/assets/BlackCA/DSC0294-1770215254818.JPG" mode="hero" src="https://raw.githubusercontent.com/gtif-cerulean/cif-stories/51d15173321d5e6afc08fdff9da1a60e7bb1746d/assets/DSC0294-1770215254818.JPG" }-->
 <!--{ style="font-size:1rem;opacity:0.7;margin-top:1rem;" }-->

## A capability of the CIF Dashboard, Sea Ice Motion Animation forecasts the future position of sea ice by morphing satellite imagery using sea-ice drift and weather model data.
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

In ice-covered waters, satellite images provide a snapshot of where the ice *was* when the satellite passed overhead. For vessels navigating dynamic pack ice, that is often not enough.

CIF's Sea Ice Motion Animation capability addresses this gap by transforming a recent satellite (SAR) image into a forecasted view of where the same ice features are expected to be hours into the future. By combining ice drift estimates from sea-ice and atmospheric models with advanced image warping techniques, the capability produces a predicted future version of the original satellite image.

This allows operators to see not only the current ice situation, but how it is likely to evolve along their route.

### Why Satellite Image Warping Matters

In polar regions, sea ice is constantly in motion due to wind, currents, and internal ice dynamics. Leads open and close, pressure ridges form, and floes shift position over short time scales.

For ship operators, this creates a challenge:
- A satellite image may already be several hours old when received
- Ice conditions may have changed significantly since acquisition
- Tactical navigation decisions depend on anticipating where hazards will move

By forecasting the drift of visible ice structures in the image, Sea Ice Motion Animation turns static imagery into a dynamic planning tool.

## End Users <!--{ as="img" mode="tour" position="right"}-->
### <!--{ src="https://raw.githubusercontent.com/gtif-cerulean/cif-stories/9dfcedbd13917282778b7bc192b3897c97cd6027/assets/BlackCA/IMG1179-NPI-high-res-1770148305979.JPG" style="background: #ffe7ef;" }-->

#### Who Needs Satellite Image Warping Information?
Several groups benefit from this capability:
1. **Ship operators and ice navigators:** for tactical route adjustments in moving pack ice.
2. **Marine service providers:** supporting vessels operating in ice-covered waters.
3. **Research and governmental organizations:** studying sea-ice dynamics and operational risks.
4. **Technology providers and analytics teams:** integrating forecasted imagery into decision-support systems.

## Image Tour <!--{ as="img" mode="tour" position="right"}-->
### <!--{ src="https://raw.githubusercontent.com/gtif-cerulean/cif-stories/9dfcedbd13917282778b7bc192b3897c97cd6027/assets/BlackCA/IMG1179-NPI-high-res-1770148305979.JPG" style="background: #e7f0ff;" }-->

#### Who Needs Forecasted Satellite Ice Movement Information?
Several groups benefit from this capability:
1. **Ship operators and ice navigators:** for tactical route adjustments in moving pack ice.
2. **Marine service providers:** supporting vessels operating in ice-covered waters.
3. **Research and governmental organizations:** studying sea-ice dynamics and operational risks.
4. **Technology providers and analytics teams:** integrating forecasted imagery into decision-support systems.

## What Data the CIF Dashboard Uses to Forecast Ice Motion
This capability combines two key data sources with user-defined parameters.

#### SAR Image Data

Although any georeferenced (GeoTiff) image can be used, the system is optimized for SAR imagery from:
- European Space Agency's **Sentinel-1**
- Canadian Space Agency's **RADARSAT Constellation Mission (RCM)**

These images are pre-processed and provided in polar stereographic projection to ensure geometric correctness near the poles.

#### Model Data for Ice Drift
Two model sources are available to estimate sea-ice drift:
1. **Sea-ice model (neXtSIM)**: A lagrangian sea-ice model using elasto-brittle rheology to simulate fracturing and deformation of Arctic sea ice.

2. **Weather model (ICON)**: Wind fields are converted into ice drift estimates using the Nansen rule (where sea ice typically moves at about 2.5% of the wind speed, and 20-40° to the right in the Northern Hemisphere due to the Coriolis effect).

#### User-Defined Parameters
Users control the behavior of the warping process through:
- Forecast duration (hours into the future)
- Choice of model data (neXtSIM or ICON)
- Ground control point spacing
- Output image resolution

## What the CIF Dashboard Produces

For each forecast timestep, the CIF Dashboard generates:

- A morphed image representing predicted ice positions
- The trajectories of all points within the area of interest defined by the user

The result is a forecasted image showing where the same ice features are expected to be up to **six hours into the future**. These outputs can be layered with other CIF data to support tactical navigation and operational decision-making.

# Example Animation <!--{ as="video" data-fallback-src="" mode="hero" src="https://dlmultimedia.esa.int/download/public/videos/2023/06/010/2306_010_AR_EN.mp4" }-->
#### CAB: Waiting to export an animation from the Dashboard to put here <!--{ style="font-size:1rem;opacity:0.7;margin-top:1rem;" }-->

## Try out Satellite Image Warping on the CIF Dashboard
Explore how recent SAR imagery can be transformed into [forecasted ice maps within the CIF Dashboard](https://cif.eox.at/uc1dashboard/?x=-180.0000&y=-80.0220&z=0.0000&template=light&indicator=polarwarp_sentinel1&datetime=2026-02-04). Compare original and warped images, examine how ice features are expected to drift, and use this information to support safer and more efficient navigation in polar waters.
