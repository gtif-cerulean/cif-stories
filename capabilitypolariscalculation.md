
---
title: Capability_POLARIS_Calculation
cover-image: https://github.com/BlackCA/cif-stories/blob/main/assets/BlackCA/OceanImageBank_VivekMehra_14_Antarctica.jpg?raw=true 
---

# CIF Capability: POLARIS and navigating polar waters<!--{ as="video" mode="hero" src="https://raw.githubusercontent.com/BlackCA/cif-stories/BlackCA/cif-projectoverviewstory/assets/BlackCA/BAS-Weddell-Sea-Clip-21-1751546090329.mp4" }-->


## A capability of the CIF Dashboard, the POLARIS algorithm links ship information with up-to-date sea-ice conditions to support safe navigation in polar waters.  

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

As more ships travel through the Arctic and Antarctic, ensuring safe navigation in ice-covered waters has never been more important. The Polar Operational Limit Assessment Risk Indexing System—better known as **POLARIS**—is a tool approved by the International Maritime Organization (IMO) to help mariners understand the risks posed by sea ice and make safer decisions on every voyage.

### Why POLARIS Exists

The Polar Code, adopted by the IMO in 2014, requires all ships operating in polar waters to carry a **Polar Ship Certificate**. This certificate outlines the ship’s limits for operating in ice, based on its structural strength and ice-class rating.

But sea ice isn’t uniform. Conditions can vary widely from place to place and day to day. POLARIS provides a practical way to assess how safe it is for a specific ship to operate in the ice conditions it faces, whether during voyage planning or in real time on the bridge.

### How POLARIS Works

At its core, POLARIS matches two things:
1.  **The ship’s ice class**
2.  **The surrounding ice conditions**, using standard national sea ice charts

Each type of sea ice—new ice, first-year ice, multi-year ice, and so on—is assigned a number that reflects how risky it is for a certain ice-classed ship. POLARIS looks at:

* What types of ice are present  
* How much of each type there is  
* What the ship is built to withstand 

Using these factors, POLARIS produces a score called the **Risk Index Outcome (RIO)**. This score tells mariners whether the ship can proceed normally, should exercise caution, or should avoid an area altogether. POLARIS and RIO scores allow captains and voyage planners to make informed decisions based on ice conditions.

## POLARIS and RIO <!--{as="img" data-fallback-src="https://raw.githubusercontent.com/BlackCA/cif-stories/BlackCA/polaris-calculation-update/assets/BlackCA/1372aa7fcd8f4bce5020a7b5f4bc6b541d0084aad61391b8403b341e47ebb3d4-1770127022639.jpg" src="https://raw.githubusercontent.com/gtif-cerulean/cif-stories/9c31c4f1d205ad9d67765db8d950ac8a42254cbc/assets/1372aa7fcd8f4bce5020a7b5f4bc6b541d0084aad61391b8403b341e47ebb3d4-1770127022639.jpg" style="width: 60%; height: px;"}-->

## Who Uses POLARIS?

POLARIS supports several important needs across the polar marine community:

1. ***Voyage Planning***: 
Shipping companies—such as **FedNav**, one of the world’s largest operators of ice-class carriers—use POLARIS to plan safe routes through ice.
2. ***Long-term Strategic Planning***:
Governments and researchers rely on POLARIS-based analyses to understand how accessibility changes throughout the year. For example, the **Government of Greenland** uses this information when studying new coastal activities such as carbon-sequestration projects.
3. ***Policy and Code Development***:
Organizations like the **Arctic Council’s PAME Working Group** work with the IMO to evaluate and refine how POLARIS supports safe operations and whether future updates are needed.

## What Data the CIF Dashboard Uses to Implement POLARIS

POLARIS relies on national sea ice charts and ship-specific information. Key data sources for the [CIF Dashboard](https://cif.eox.at/) include:

- **Greenlandic Ice Service** and **Canadian Ice Service** charts (which include essential “stage of ice development” details)  
- **Ship ice classification** from the vessel’s Polar Ship Certificate  
- **Seasonal information**, such as whether ice is decaying in summer  

## What CIF's Dashboard Produces

Once the algorithm processes a sea ice chart, it calculates **RIO values for every ship class** across the area covered by the chart. These results can be displayed as:

- Vector or raster layers in the CIF Dashboard  
- Map overlays showing areas suitable for different ice-class ships  
- Inputs to other decision-support tools, such as sea-ice datacubes  

## POLARIS in the CIF Dashboard

On the **CIF Dashboard**, users can view sea ice concentration maps, POLARIS RIO results for different ship classes, and real-time or historical scenarios, as demonstrated below.  

## POLARIS <!--{ as="eox-map" mode="tour" }-->

### <!--{ layers='[{"type":"Group","properties":{"id":"BaseLayersGroup","title":"Base Layers"},"layers":[{"type":"Tile","properties":{"id":"eox-osm;:;EPSG:3857","title":"OSM Background"},"source":{"type":"XYZ","url":"//s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg","projection":"EPSG:3857","attributions":"{ OSM: Data &copy; <a href=\"http://www.openstreetmap.org/copyright\" target=\"_blank\">OpenStreetMap</a> contributors and <a href=\"//maps.eox.at/#data\" target=\"_blank\">others</a>, Rendering &copy; <a href=\"http://eox.at\" target=\"_blank\">EOX</a> }"}}]},{"type":"Vector","style":{"fill-color":["match",["get","wmo_concentration"],"Ice Free",[0,100,255,1],"Open Water (< 1/10 ice)",[150,200,255,1],"Bergy Water",[150,200,255,1],"1/10",[140,255,159,1],"2/10",[140,255,159,1],"3/10",[140,255,159,1],"4/10",[255,255,0,1],"5/10",[255,255,0,1],"6/10",[255,255,0,1],"7/10",[255,125,7,1],"8/10",[255,125,7,1],"9/10",[255,0,0,1],"10/10",[255,0,0,1],"9/10 to 10/10 ice, 9+/10",[255,0,0,1],"Unknown/Undetermined",[255,255,255,1],[255,255,255,1]],"stroke-color":"black","stroke-width":1},"source":{"type":"FlatGeoBuf","url":"https://workspace-ui-public.cif.gtif.eox.at/api/public/share/public-4wazei3y-02/output-polaris/202501182050_CentralWest_RIC-processed.fgb","projection":"EPSG:4326"},"properties":{"id":"Polaris_algorithm_dmi_demo;:;2025-01-18T20:50:00Z;:;0","title":"POLARIS"}}]' zoom="6.3231" center=[-55.856266337204524,69.49965576414462]}-->
#### Sea ice concentration maps
Sea ice concentration, as a fraction of area covered by ice, from 1 to 10, with World Meteorological Concentration (WMO) divided into four categories. In the CIF Dashboard, users can select dates and times of interest, ranging from January 1, 2022 to near real-time: 
![](https://github.com/BlackCA/cif-stories/blob/main/assets/BlackCA/POLARIS%E2%80%93icechart%E2%80%93legend.png?raw=true)

### <!--{ layers='[ { "type": "Group", "properties": { "id": "BaseLayersGroup", "title": "Base Layers" }, "layers": [ { "type": "Tile", "properties": { "id": "OSM;:;EPSG:3857", "title": "OSM Background" }, "source": { "type": "XYZ", "url": "https://s2maps-tiles.eu/wmts/1.0.0/osm_3857/default/g/{z}/{y}/{x}.jpeg", "projection": "EPSG:3857" } } ] }, { "type": "Group", "properties": { "id": "AnalysisGroup", "title": "Data Layers" }, "layers": [ { "type": "Vector", "source": { "url": "https://workspace-ui-public.cif.gtif.eox.at/api/public/share/public-4wazei3y-02/dmi-polaris/converted/202602012115_Qaanaaq_RIC-processed.fgb", "type": "FlatGeoBuf", "projection": "EPSG:4326" }, "style":{"fill-color":["case",["==",["get","polygon_type"],"Ice Free"],[0,100,255],["==",["get","polaris_decayed_pc_nis_rio"],"RIO > 20: Normal Operation"],[54,122,74,1],["==",["get","polaris_decayed_pc_nis_rio"],">= 10 RIO < 20: Normal Operation"],[62,150,85,1],["==",["get","polaris_decayed_pc_nis_rio"],">= 0 RIO < 10: Normal Operation"],[102,188,118,1],["==",["get","polaris_decayed_pc_nis_rio"],">= -10 RIO < 0: Operation subject to special consideration"],[252,251,1,1],["==",["get","polaris_decayed_pc_nis_rio"],">= -20 RIO < -10: Operation subject to special consideration"],[227,108,9,1],["==",["get","polaris_decayed_pc_nis_rio"],"RIO < -20: Operation subject to special consideration"],[188,1,6,1],["==",["get","polaris_decayed_pc_nis_rio"],"<= -10 RIO < 0: Elevated operational risk"],[252,251,1,1],[0,0,0,1]],"stroke-color":"black","stroke-width":1}, "properties": { "id": "DMI_polaris;:;2026-02-02;:;0", "title": "POLARIS (DMI)" } } ] } ]' zoom="5.845627417974437" center=[-73.58052908361533,75.78792733012872]}-->
#### POLARIS RIO results for different ship classes  
Maps are colour-coded by RIO scores, and users can select a Ship Class of interest:
![](https://github.com/BlackCA/cif-stories/blob/main/assets/BlackCA/RIO%E2%80%93POLARIS%E2%80%93legend.png?raw=true)
Hovering over the RIO regions on the map in the Dashboard provides information about that area:
![](https://github.com/BlackCA/cif-stories/blob/main/assets/BlackCA/POLARIS%E2%80%93hover.png?raw=true) <!--{width="700" }-->

## Try out the POLARIS capability in the CIF Dashboard
See the application of the [POLARIS capability in the CIF Dashboard](https://cif.eox.at/uc1dashboard/?x=-25.0000&y=69.0715&z=3.4281&template=light&indicator=Polaris_algorithm_dmi_demo&datetime=2025-01-20). Explore historical and real-time POLARIS RIO maps, examine how navigational risk varies across regions and seasons, and assess how sea-ice conditions translate into navigation guidance for vessels in polar waters.



        




