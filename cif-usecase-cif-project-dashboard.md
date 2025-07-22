---
cover-image: https://raw.githubusercontent.com/gtif-cerulean/cif-stories/main/assets/BlackCA/polaris.png
date: 2025-01-01
theme: shipping
tags: test
official: true
---
# The CIF Dashboard for better navigation: of sea ice data and Arctic waters  <!--{ as="video" data-fallback-src="https://raw.githubusercontent.com/BlackCA/cif-stories/BlackCA/cif-usecases-20250613/assets/BlackCA/BAS-Weddell-Sea-Clip-21-1751546090329.mp4" mode="hero" src="https://raw.githubusercontent.com/gtif-cerulean/cif-stories/d53dd96375849926cc803c12c0771e248cb0f036/assets/BlackCA/BAS-Weddell-Sea-Clip-21-1751546090329.mp4" }-->
####  <!--{ style="font-size:1rem;opacity:0.7;margin-top:1rem;" }-->

#  
<div style="text-align: center;">
  <img src="https://cif.polarview.org/wp-content/uploads/2024/05/CIF-Logo-v3-125.png" style="height: 200px;">
</div>
<br><br>
<table>
  <tr>
    <td style="text-align: left; padding-right: 20px;width: 300px">
      <img src="https://cif.polarview.org/wp-content/uploads/bb-plugin/cache/Shipping-Icon-circle-d3dfaffc3b3ce792813de5d7fdd64fdf-hwxq58bkvn93.png" 
     style="height: 300px; width: 300px ">
    </td>
    <td style="vertical-align: top;">
			<h4>CIF Use Case</h4> Enhancing Arctic shipping decisions using multi-layered Earth observation data<br><br>
      <h4>Sector/Domain</h4> Arctic Shipping<br><br>
      <h4>Primary Stakeholders</h4> Commercial shipping operators, scientific missions, tourism vessels, northern logistics planners, marine analysts<br><br>
			<h4>Description</h4> The Cerulean Information Factory (CIF) Dashboard provides four key layers of sea ice information into a single decision-support cloud-based platform. This layered approach enables users to move between high-level assessments and detailed data, depending on their needs and level of expertise.<br><br>
    </td>
  </tr>
</table>

## Context and Problem <!--{ as="img" mode="tour" }-->

### <!--{ src="https://cif.polarview.org/wp-content/uploads/2024/05/North-Atlantic-Map.png" }-->
#### Context and Challenge 
Ships voyaging through the North Atlantic and Arctic Oceans are required under the *International Maritime Organization’s* **Polar Code** to consult timely and historical ice information to plan the safest possible route.

### <!--{ src="https://cif.polarview.org/wp-content/uploads/2024/05/North-Atlantic-Map.png" }-->
##### Traditional methods
Ship operators rely on **ice charts** manually produced by a handful of nations with ice services. The resultant charts are authoritative, but are limited by being time-consuming to create, often low in resolution – ice charts generalize conditions over large areas, and can miss critical navigational features like polynyas, narrow cracks in the ice that offer passage – and while typically updated daily, sometimes that frequency drops to weekly. 

Ship operators often refer to the raw satellite radar images, called "synthetic aperture radar" or **SAR images**, which are the basis of ice charts, for more immediate and detailed insight, a strategy requiring long experience reading such hard-to-interpret images (for example, rough seas and ice may appear similar).

### <!--{ src="https://cif.polarview.org/wp-content/uploads/bb-plugin/cache/Greenland-Glacier-1024x603-landscape-ed3be4eb55de0f900f71aa38ec37783f-g9bzt50arfkx.png" }-->
#### Navigating safely in the Arctic is high-stakes
A wrong judgment can lead to route delays, excessive fuel use, damage to the vessel, or in severe cases, becoming trapped in ice. In response to these challenges, the CIF Dashboard integrates SAR images and traditional ice charts with new tools to support ship operators to make confident decisions. 

# Four-Layer Sea Ice Intelligence <!--{ as="img" data-fallback-src="https://raw.githubusercontent.com/BlackCA/cif-stories/BlackCA/cif-usecases-20250613/assets/BlackCA/Nordica-Icebreaker-FIMR-1751547468888.JPG" mode="hero" src="https://raw.githubusercontent.com/gtif-cerulean/cif-stories/2d940e2f891a3088e02537609be76ffc9bb1d9d0/assets/BlackCA/Nordica-Icebreaker-FIMR-1751547468888.JPG" }-->
### Nordica Icebreaker (FIMR) traversing ice <!--{ style="font-size:1rem;opacity:0.7;margin-top:1rem;" }-->

##

The CIF Dashboard brings together multiple tools, new and well-established, into one cloud-based platform. 

Traditional tools for navigating in the Arctic:

1. Satellite-based radar images (SAR images)
2. Human-made ice charts:
    1. Concentration of sea ice (indicating the fraction of ocean surface covered by ice), 
    2. Stage of sea ice development (ice age ranging from new to multi-year old ice), and 
    3. Floe size (size of individual ice floes, e.g., pancake, brash, medium floe)
3. The POLARIS risk score, which combines ice chart data with a ship’s ice class rating to generate navigational risk scores across a region of interest.

New tools available in the CIF Dashboard include **ship route optimization in ice**, developed by the National Research Council of Canada, and **AI-derived ice charts**, doing the work of analyzing satellite radar images, developed by the Danish Meteorological Institute, as well as other tools such as **structural icing** (the accumulation of ice on marine infrastructure) and **ice dynamics and deformation** (analyzing how the ice is moving, including the creation of pressurized ice), developed by C-CORE, are all available within the [CIF Dashboard](https://cif.eox.at/).   

In this use case, we present *four key data layers for interpreting and navigating sea ice and icebergs*. 

## Map Tour <!--{ as="eox-map" mode="tour" }-->
### <!--{ layers='[{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857","attributions":"{ Overlay: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors, Made with Natural Earth, Rendering &copy; <a href=\"//eox.at\" target=\"_blank\">EOX</a> }"}}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2022;:;EPSG:3857","title":"EOxCloudless 2022"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2022_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857","attributions":"{ EOxCloudless 2022: <a href=\"//s2maps.eu\" target=\"_blank\">Sentinel-2 cloudless - s2maps.eu</a> by <a href=\"//eox.at\" target=\"_blank\">EOX IT Services GmbH</a> (Contains modified Copernicus Sentinel data 2022) }"}}]}]' zoom="3.9319280948873625" center=[-36.413951125436455,65.78910736784152] projection="" animationOptions={duration:500}}-->
#### CIF's Domain: the North Atlantic Ocean
The CIF's domain is the North Atlantic Ocean, connecting Canada and Denmark, the project's partner countries. 

The image you see is derived from optical (colour) images of the Earth collected by satellite and then processed by EOX to create a cloudless view of the earth and ocean.  

Let's zoom in on the east coast of Greenland to view a Sentinel 1 SAR image from January 20, 2025. Here, we'll be able to see fjords, glaciers, icebergs and because it's wintertime, sea ice. 

### <!--{ layers='[{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857","attributions":"{ Overlay: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors, Made with Natural Earth, Rendering &copy; <a href=\"//eox.at\" target=\"_blank\">EOX</a> }"}}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"Sentinel1-EW-HH;:;2025-01-20T00:00:00Z;:;Sentinel1-EW-HH;:;EPSG:3857","title":"Sentinel1-EW-HH"},"source":{"type":"TileWMS","url":"https://services.sentinel-hub.com/ogc/wms/b8c37569-fa44-4f8d-9cfc-0b535ba4e4c3","projection":"EPSG:4326","tileGrid":{"tileSize":[512,512]},"params":{"LAYERS":["EW_HH_DB"],"TILED":true,"TIME":"2025-01-20T00:00:00Z/2025-01-20T23:59:59Z"}}}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"sx-cat_ortho680500;:;EPSG:3857","title":"Terrain Light Stereographic North"},"source":{"type":"TileWMS","url":"//sxcat-demo.eox.at/sxcat_maps/wms","projection":"ORTHO:680500","tileGrid":{"tileSize":[512,512]},"attributions":"{ Terrain light: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors and <a href=\"//maps.eox.at/#data\" target=\"_blank\">others</a>, Rendering &copy; <a href=\"http://eox.at\" target=\"_blank\">EOX</a> }","params":{"LAYERS":"sx-cat_ortho680500","TILED":true}}},{"type":"Tile","properties":{"id":"cloudless-2022;:;EPSG:3857","title":"EOxCloudless 2022"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2022_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857","attributions":"{ EOxCloudless 2022: <a href=\"//s2maps.eu\" target=\"_blank\">Sentinel-2 cloudless - s2maps.eu</a> by <a href=\"//eox.at\" target=\"_blank\">EOX IT Services GmbH</a> (Contains modified Copernicus Sentinel data 2022) }"}},{"type":"Tile","properties":{"id":"terrain-light;:;EPSG:3857","title":"Terrain light"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/terrain-light_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857","attributions":"{ Terrain light: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors and <a href=\"//maps.eox.at/#data\" target=\"_blank\">others</a>, Rendering &copy; <a href=\"http://eox.at\" target=\"_blank\">EOX</a> }"}},{"type":"Tile","properties":{"id":"eox-osm;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857","attributions":"{ OSM: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors and <a href=\"//maps.eox.at/#data\" target=\"_blank\">others</a>, Rendering &copy; <a href=\"http://eox.at\" target=\"_blank\">EOX</a> }"}}]}]' zoom="5.931928094887364" center=[-15.594400090077727,74.42428773417387] projection="" animationOptions={duration:500}}-->
#### Data layer 1: Raw SAR image
The first data layer that we'll look at here, offered by the CIF Dashboard, is a real-time radar image from the Sentinel 1 satellites that offer weather-independent views of sea ice conditions. 

The swaths you see here are about 400 km across. 

These images are the basis for human-derived ice charts. They may also be used by ship operators to get the most recent and detailed ice information available.

Next, we'll look at the ice concentration, one of the maps provided as part of an ice chart. 

### <!--{ layers='[{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857","attributions":"{ Overlay: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors, Made with Natural Earth, Rendering &copy; <a href=\"//eox.at\" target=\"_blank\">EOX</a> }"}}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Tile","properties":{"id":"ice_concentration;:;2025-01-20T00:00:00Z;:;wmts capabilities;:;EPSG:3857","title":"Ice concentration"},"source":{"type":"WMTS","url":"https://wmts.marine.copernicus.eu/teroWmts","layer":"GLOBAL_ANALYSISFORECAST_PHY_001_024/cmems_mod_glo_phy_anfc_0.083deg_P1D-m_202406/siconc","style":"cmap:ice","matrixSet":"EPSG:3857","tileGrid":{"tileSize":[128,128]},"dimensions":{"time":"2025-01-20T00:00:00Z","elevation":"0"}}}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2022;:;EPSG:3857","title":"EOxCloudless 2022"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2022_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857","attributions":"{ EOxCloudless 2022: <a href=\"//s2maps.eu\" target=\"_blank\">Sentinel-2 cloudless - s2maps.eu</a> by <a href=\"//eox.at\" target=\"_blank\">EOX IT Services GmbH</a> (Contains modified Copernicus Sentinel data 2022) }"}}]}]' zoom="5.3227335000352545" center=[-18.98843659860518,76.1554805359965]}-->

#### Data layer 2: Human-made ice charts
Ice charts are expert-drawn maps from national ice services that classify ice by type and concentration. These charts remain a legal reference point under the Polar Code, but are labor-intensive and often lack spatial detail.

Here, we can see sea ice concentration, between 1/10 and 10/10 coverage. 

### <!--{ layers='[{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857","attributions":"{ Overlay: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors, Made with Natural Earth, Rendering &copy; <a href=\"//eox.at\" target=\"_blank\">EOX</a> }"}}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"WebGLTile","source":{"type":"GeoTIFF","normalize":false,"interpolate":false,"sources":[{"url":"https://eox-gtif-public.s3.eu-central-1.amazonaws.com/EOX/sea_ice_concentration/multisensorSeaIce_202501210600.tiff"}]},"properties":{"id":"sea_ice_detections;:;2025-01-21T06:00:00Z;:;0","title":"Sea Ice Detections"},"style":{"variables":{"vmin":60,"vmax":100},"color":["case",[">",["band",1],0],["interpolate",["linear"],["/",["-",["band",1],60],40],0,[12,51,131,1],0.25,[10,136,186,1],0.5,[242,211,56,1],0.75,[242,143,56,1],1,[217,30,30,1]],[0,0,0,0]]}}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2022;:;EPSG:3857","title":"EOxCloudless 2022"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2022_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857","attributions":"{ EOxCloudless 2022: <a href=\"//s2maps.eu\" target=\"_blank\">Sentinel-2 cloudless - s2maps.eu</a> by <a href=\"//eox.at\" target=\"_blank\">EOX IT Services GmbH</a> (Contains modified Copernicus Sentinel data 2022) }"}}]}]' zoom="5.3227335000352545" center=[-18.98843659860518,76.1554805359965]}-->
#### Data layer 3: AI-derived ice charts
Machine learning models developed by the Danish Meteorological Institute (DMI) interpret SAR and meteorological data to produce faster, scalable, and often higher-resolution ice charts. These can be compared side-by-side with traditional products in the CIF Dashboard.

Now on to our final data layer on this tour, to look at how the POLARIS algorithm determines shipping risk in polar waters. 

### <!--{ layers='[{"type":"Group","properties":{"id":"OverlayGroup","title":"Overlay Layers"},"layers":[{"type":"Tile","properties":{"id":"overlay_bright;:;EPSG:3857","title":"Overlay labels"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/overlay_base_bright_3857/default/g/{z}/{y}/{x}.png","projection":"EPSG:3857","attributions":"{ Overlay: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors, Made with Natural Earth, Rendering &copy; <a href=\"//eox.at\" target=\"_blank\">EOX</a> }"}}]},{"type":"Group","properties":{"id":"AnalysisGroup","title":"Data Layers"},"layers":[{"type":"Vector","source":{"type":"FlatGeoBuf","url":"https://workspace-ui-public.cif.gtif.eox.at/api/public/share/public-4WaZei3Y-02/output-polaris/202501200900_SouthEast_RIC-processed.fgb","format":"GeoJSON"}, "style":{"stroke-color":"#000000","stroke-width":1,"fill-color":["case",["==",["get","polygon_type"], "Ice Free"],[0, 100, 255,1],["==", ["get", "polaris_standard_pc_nis_rio"] ,"RIO > 20: Normal Operation"], [54,122,74,1],["==", ["get", "polaris_standard_pc_nis_rio"], ">= 10 RIO < 20: Normal Operation"],[62,150,85,1],["==", ["get", "polaris_standard_pc_nis_rio"], ">= 0 RIO < 10: Normal Operation"],[102,188,118,1],["==", ["get", "polaris_standard_pc_nis_rio"], ">= -10 RIO < 0: Operation subject to special consideration"],[252,251,1,1],["==", ["get", "polaris_standard_pc_nis_rio"], ">= -20 RIO < -10: Operation subject to special consideration"],[227,108,9,1],["==", ["get", "polaris_standard_pc_nis_rio"], "RIO < -20: Operation subject to special consideration"],[188,1,6,1],["==", ["get", "polaris_standard_pc_nis_rio"], "<= -10 RIO < 0: Elevated operational risk"],[252,251,1,1], [0,0,0,1]]}, "properties":{"id":"Polaris_algorithm_dmi_demo;:;2025-01-20T09:00:00Z;:;0","title":"POLARIS"}}]},{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"cloudless-2022;:;EPSG:3857","title":"EOxCloudless 2022"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/s2cloudless-2022_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857","attributions":"{ EOxCloudless 2022: <a href=\"//s2maps.eu\" target=\"_blank\">Sentinel-2 cloudless - s2maps.eu</a> by <a href=\"//eox.at\" target=\"_blank\">EOX IT Services GmbH</a> (Contains modified Copernicus Sentinel data 2022) }"}}]}]' zoom="5.600932974052083" center=[-28.440094657925023,65.85935412612687]}-->
#### Data layer 4: POLARIS risk index with Polar Code integration
The POLARIS algorithm combines ice chart data with a ship’s ice class rating to generate navigational risk scores. These help planners assess whether a ship can safely transit a given area, should proceed with caution, or should avoid it altogether. While not mandatory, POLARIS risk indices are often referenced by insurers in the event of an incident.
Now on to our final data layer on this tour, to look at how the POLARIS algorithm determines shipping risk in polar waters. 

## Who Benefits

CIF’s Arctic shipping tools are designed for a range of users, including:

* **Commercial shipping companies** moving goods into and out of Arctic regions, such as ore from Baffin Island or supplies for remote communities.
* **Tourism vessels**, some of which are among the world’s most ice-capable ships, seeking immersive experiences in ice-covered waters.
* **Fishing fleets**, often small and operating near the ice edge, where accurate, high-resolution ice data is critical.
* **Scientific research expeditions**, including those aiming to reach high-latitude study sites or the North Pole, sometimes with icebreaker support.

## Value and Impact

By integrating multiple types of sea ice information into one tool, the CIF Dashboard supports:

* Improved safety, through clearer information about route-specific ice risks
* Better route planning, reducing delays, fuel use, and emissions
* Compliance with the Polar Code, by providing easy access to required and recommended data
* Faster, more informed decision-making, especially for time-sensitive or high-cost voyages

The CIF Dashboard offers a practical, scalable solution that increases Arctic data availability and accessibility, helping make it more usable by those navigating some of the world’s most challenging waters.

## Use CIF's tools yourself
Visit the CIF’s Beta Dashboard at https://cif.eox.at/ where you can find the above applications and more tools to support Arctic shipping. 

The CIF Dashboard also provides tools for Aquaculture and Off-shore Renewable Energy in the North Atlantic Ocean. 
