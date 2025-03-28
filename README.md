# Join Layer Plugin for QGIS

## Description
This QGIS plugin is designed to split polygon layers using a line layer as the cutting centerline. The plugin identifies polygon and centerline layers loaded in QGIS, then uses GeoPandas and Shapely to process the geometry.

## Features
- Splits polygon layers using a line layer as the cutting centerline
- Works with layers already loaded in QGIS
- Utilizes GeoPandas and Shapely for geometry processing

## Requirements
- QGIS version 3.0 or higher
- Python dependencies:
  - GeoPandas
  - Shapely

## Installation
1. Download the plugin files
2. Place the plugin folder in your QGIS plugins directory (typically `~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/` on Linux or `%APPDATA%\QGIS\QGIS3\profiles\default\python\plugins` on Windows)
3. Restart QGIS or enable the plugin through the Plugin Manager

## Usage
1. Load your polygon layer and line (centerline) layer into QGIS
2. Activate the plugin through the QGIS plugin menu
3. Select your polygon layer and centerline layer from the dropdown menus
4. Run the plugin to split your polygons along the centerline

## Version
Current version: 0.1

## Author
Muhammad Akmalul Iman Liari

## Support
For issues or questions, please contact the author.
