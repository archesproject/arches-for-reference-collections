import uuid
from django.db import migrations
from django.utils.translation import gettext as _
import json


class Migration(migrations.Migration):

    initial = True
    dependencies = [
        ("models", "11499_add_editlog_resourceinstance_idx"),
    ]

    def add_map_layers(apps, schema_editor):
        MapSource = apps.get_model("models", "MapSource")
        MapLayer = apps.get_model("models", "MapLayer")

        ofm_positron_light = {
            "maplayerid": uuid.UUID("803829fe-b437-40b2-94a4-8ae10fa25b10"),
            "sortorder": 0,
            "style": {
                "name": "Positron",
                "sources": {
                    "ne2_shaded": {
                    "maxzoom": 6,
                    "tileSize": 256,
                    "tiles": [
                        "https://tiles.openfreemap.org/natural_earth/ne2sr/{z}/{x}/{y}.png"
                    ],
                    "type": "raster"
                    },
                    "openmaptiles": {
                    "type": "vector",
                    "url": "https://tiles.openfreemap.org/planet"
                    }
                },
                "layers": [
                    {
                    "id": "background",
                    "type": "background",
                    "layout": {"visibility": "visible"},
                    "paint": {"background-color": "rgb(242,243,240)"}
                    },
                    {
                    "id": "park",
                    "type": "fill",
                    "source": "openmaptiles",
                    "source-layer": "park",
                    "filter": ["==", ["geometry-type"], "Polygon"],
                    "layout": {"visibility": "none"},
                    "paint": {"fill-color": "rgb(230, 230, 230)"}
                    },
                    {
                    "id": "water",
                    "type": "fill",
                    "source": "openmaptiles",
                    "source-layer": "water",
                    "filter": [
                        "all",
                        ["==", ["geometry-type"], "Polygon"],
                        ["!=", ["get", "brunnel"], "tunnel"]
                    ],
                    "layout": {"visibility": "visible"},
                    "paint": {"fill-antialias": True, "fill-color": "rgb(220, 220, 220)"}
                    },
                    {
                    "id": "landcover_ice_shelf",
                    "type": "fill",
                    "source": "openmaptiles",
                    "source-layer": "landcover",
                    "maxzoom": 8,
                    "filter": [
                        "all",
                        ["==", ["geometry-type"], "Polygon"],
                        ["==", ["get", "subclass"], "ice_shelf"]
                    ],
                    "paint": {"fill-color": "hsl(0,0%,98%)", "fill-opacity": 0.7}
                    },
                    {
                    "id": "landcover_glacier",
                    "type": "fill",
                    "source": "openmaptiles",
                    "source-layer": "landcover",
                    "maxzoom": 8,
                    "filter": [
                        "all",
                        ["==", ["geometry-type"], "Polygon"],
                        ["==", ["get", "subclass"], "glacier"]
                    ],
                    "paint": {
                        "fill-color": "hsl(0,0%,98%)",
                        "fill-opacity": ["interpolate", ["linear"], ["zoom"], 0, 1, 8, 0.5]
                    }
                    },
                    {
                    "id": "landuse_residential",
                    "type": "fill",
                    "source": "openmaptiles",
                    "source-layer": "landuse",
                    "maxzoom": 16,
                    "filter": [
                        "all",
                        ["==", ["geometry-type"], "Polygon"],
                        ["==", ["get", "class"], "residential"]
                    ],
                    "layout": {"visibility": "visible"},
                    "paint": {
                        "fill-color": "rgb(230, 230, 230)",
                        "fill-opacity": [
                        "interpolate",
                        ["exponential", 0.6],
                        ["zoom"],
                        8,
                        0.8,
                        9,
                        0.6
                        ]
                    }
                    },
                    {
                    "id": "landcover_wood",
                    "type": "fill",
                    "source": "openmaptiles",
                    "source-layer": "landcover",
                    "minzoom": 10,
                    "filter": [
                        "all",
                        ["==", ["geometry-type"], "Polygon"],
                        ["==", ["get", "class"], "wood"]
                    ],
                    "layout": {"visibility": "visible"},
                    "paint": {
                        "fill-color": "rgb(220,220,220)",
                        "fill-opacity": ["interpolate", ["linear"], ["zoom"], 8, 0, 12, 1]
                    }
                    },
                    {
                    "id": "waterway",
                    "type": "line",
                    "source": "openmaptiles",
                    "source-layer": "waterway",
                    "filter": ["==", ["geometry-type"], "LineString"],
                    "layout": {"visibility": "visible"},
                    "paint": {"line-color": "hsl(195,17%,78%)"}
                    },
                    {
                    "id": "building",
                    "type": "fill",
                    "source": "openmaptiles",
                    "source-layer": "building",
                    "minzoom": 12,
                    "paint": {
                        "fill-antialias": True,
                        "fill-color": "rgb(234, 234, 229)",
                        "fill-outline-color": "rgb(219, 219, 218)"
                    }
                    },
                    {
                    "id": "tunnel_motorway_casing",
                    "type": "line",
                    "source": "openmaptiles",
                    "source-layer": "transportation",
                    "minzoom": 6,
                    "filter": [
                        "all",
                        ["==", ["geometry-type"], "LineString"],
                        [
                        "all",
                        ["==", ["get", "brunnel"], "tunnel"],
                        ["==", ["get", "class"], "motorway"]
                        ]
                    ],
                    "layout": {"line-cap": "butt", "line-join": "miter"},
                    "paint": {
                        "line-color": "rgb(213, 213, 213)",
                        "line-opacity": 1,
                        "line-width": [
                        "interpolate",
                        ["exponential", 1.4],
                        ["zoom"],
                        5.8,
                        0,
                        6,
                        3,
                        20,
                        40
                        ]
                    }
                    },
                    {
                    "id": "tunnel_motorway_inner",
                    "type": "line",
                    "source": "openmaptiles",
                    "source-layer": "transportation",
                    "minzoom": 6,
                    "filter": [
                        "all",
                        ["==", ["geometry-type"], "LineString"],
                        [
                        "all",
                        ["==", ["get", "brunnel"], "tunnel"],
                        ["==", ["get", "class"], "motorway"]
                        ]
                    ],
                    "layout": {"line-cap": "round", "line-join": "round"},
                    "paint": {
                        "line-color": "rgb(234,234,234)",
                        "line-width": [
                        "interpolate",
                        ["exponential", 1.4],
                        ["zoom"],
                        4,
                        2,
                        6,
                        1.3,
                        20,
                        30
                        ]
                    }
                    },
                    {
                    "id": "aeroway-taxiway",
                    "type": "line",
                    "source": "openmaptiles",
                    "source-layer": "aeroway",
                    "minzoom": 12,
                    "filter": ["match", ["get", "class"], ["taxiway"], True, False],
                    "layout": {"line-cap": "round", "line-join": "round"},
                    "paint": {
                        "line-color": "hsl(0,0%,88%)",
                        "line-opacity": 1,
                        "line-width": [
                        "interpolate",
                        ["exponential", 1.55],
                        ["zoom"],
                        13,
                        1.8,
                        20,
                        20
                        ]
                    }
                    },
                    {
                    "id": "aeroway-runway-casing",
                    "type": "line",
                    "source": "openmaptiles",
                    "source-layer": "aeroway",
                    "minzoom": 11,
                    "filter": ["match", ["get", "class"], ["runway"], True, False],
                    "layout": {"line-cap": "round", "line-join": "round"},
                    "paint": {
                        "line-color": "hsl(0,0%,88%)",
                        "line-opacity": 1,
                        "line-width": [
                        "interpolate",
                        ["exponential", 1.5],
                        ["zoom"],
                        11,
                        6,
                        17,
                        55
                        ]
                    }
                    },
                    {
                    "id": "aeroway-area",
                    "type": "fill",
                    "source": "openmaptiles",
                    "source-layer": "aeroway",
                    "minzoom": 4,
                    "filter": [
                        "all",
                        ["==", ["geometry-type"], "Polygon"],
                        ["match", ["get", "class"], ["runway", "taxiway"], True, False]
                    ],
                    "paint": {
                        "fill-color": "rgba(255, 255, 255, 1)",
                        "fill-opacity": ["interpolate", ["linear"], ["zoom"], 13, 0, 14, 1]
                    }
                    },
                    {
                    "id": "aeroway-runway",
                    "type": "line",
                    "source": "openmaptiles",
                    "source-layer": "aeroway",
                    "minzoom": 11,
                    "filter": [
                        "all",
                        ["match", ["get", "class"], ["runway"], True, False],
                        ["==", ["geometry-type"], "LineString"]
                    ],
                    "layout": {"line-cap": "round", "line-join": "round"},
                    "paint": {
                        "line-color": "rgba(255, 255, 255, 1)",
                        "line-opacity": 1,
                        "line-width": [
                        "interpolate",
                        ["exponential", 1.5],
                        ["zoom"],
                        11,
                        4,
                        17,
                        50
                        ]
                    }
                    },
                    {
                    "id": "road_area_pier",
                    "type": "fill",
                    "source": "openmaptiles",
                    "source-layer": "transportation",
                    "filter": [
                        "all",
                        ["==", ["geometry-type"], "Polygon"],
                        ["==", ["get", "class"], "pier"]
                    ],
                    "paint": {"fill-antialias": True, "fill-color": "rgb(242,243,240)"}
                    },
                    {
                    "id": "road_pier",
                    "type": "line",
                    "source": "openmaptiles",
                    "source-layer": "transportation",
                    "filter": [
                        "all",
                        ["==", ["geometry-type"], "LineString"],
                        ["match", ["get", "class"], ["pier"], True, False]
                    ],
                    "layout": {"line-cap": "round", "line-join": "round"},
                    "paint": {
                        "line-color": "rgb(242,243,240)",
                        "line-width": [
                        "interpolate",
                        ["exponential", 1.2],
                        ["zoom"],
                        15,
                        1,
                        17,
                        4
                        ]
                    }
                    },
                    {
                    "id": "highway_path",
                    "type": "line",
                    "source": "openmaptiles",
                    "source-layer": "transportation",
                    "filter": [
                        "all",
                        ["==", ["geometry-type"], "LineString"],
                        ["==", ["get", "class"], "path"]
                    ],
                    "layout": {"line-cap": "round", "line-join": "round"},
                    "paint": {
                        "line-color": "rgb(234, 234, 234)",
                        "line-opacity": 0.9,
                        "line-width": [
                        "interpolate",
                        ["exponential", 1.2],
                        ["zoom"],
                        13,
                        1,
                        20,
                        10
                        ]
                    }
                    },
                    {
                    "id": "highway_minor",
                    "type": "line",
                    "source": "openmaptiles",
                    "source-layer": "transportation",
                    "minzoom": 8,
                    "filter": [
                        "all",
                        ["==", ["geometry-type"], "LineString"],
                        ["match", ["get", "class"], ["minor", "service", "track"], True, False]
                    ],
                    "layout": {"line-cap": "round", "line-join": "round"},
                    "paint": {
                        "line-color": "hsl(0,0%,88%)",
                        "line-opacity": 0.9,
                        "line-width": [
                        "interpolate",
                        ["exponential", 1.55],
                        ["zoom"],
                        13,
                        1.8,
                        20,
                        20
                        ]
                    }
                    },
                    {
                    "id": "highway_major_casing",
                    "type": "line",
                    "source": "openmaptiles",
                    "source-layer": "transportation",
                    "minzoom": 11,
                    "filter": [
                        "all",
                        ["==", ["geometry-type"], "LineString"],
                        [
                        "match",
                        ["get", "class"],
                        ["primary", "secondary", "tertiary", "trunk"],
                        True,
                        False
                        ]
                    ],
                    "layout": {"line-cap": "butt", "line-join": "miter"},
                    "paint": {
                        "line-color": "rgb(213, 213, 213)",
                        "line-dasharray": [12, 0],
                        "line-width": [
                        "interpolate",
                        ["exponential", 1.3],
                        ["zoom"],
                        10,
                        3,
                        20,
                        23
                        ]
                    }
                    },
                    {
                    "id": "highway_major_inner",
                    "type": "line",
                    "source": "openmaptiles",
                    "source-layer": "transportation",
                    "minzoom": 11,
                    "filter": [
                        "all",
                        ["==", ["geometry-type"], "LineString"],
                        [
                        "match",
                        ["get", "class"],
                        ["primary", "secondary", "tertiary", "trunk"],
                        True,
                        False
                        ]
                    ],
                    "layout": {"line-cap": "round", "line-join": "round"},
                    "paint": {
                        "line-color": "#fff",
                        "line-width": [
                        "interpolate",
                        ["exponential", 1.3],
                        ["zoom"],
                        10,
                        2,
                        20,
                        20
                        ]
                    }
                    },
                    {
                    "id": "highway_major_subtle",
                    "type": "line",
                    "source": "openmaptiles",
                    "source-layer": "transportation",
                    "maxzoom": 11,
                    "filter": [
                        "all",
                        ["==", ["geometry-type"], "LineString"],
                        [
                        "match",
                        ["get", "class"],
                        ["primary", "secondary", "tertiary", "trunk"],
                        True,
                        False
                        ]
                    ],
                    "layout": {"line-cap": "round", "line-join": "round"},
                    "paint": {"line-color": "hsla(0,0%,85%,0.69)", "line-width": 2}
                    },
                    {
                    "id": "highway_motorway_casing",
                    "type": "line",
                    "source": "openmaptiles",
                    "source-layer": "transportation",
                    "minzoom": 6,
                    "filter": [
                        "all",
                        ["==", ["geometry-type"], "LineString"],
                        [
                        "all",
                        ["match", ["get", "brunnel"], ["bridge", "tunnel"], False, True],
                        ["==", ["get", "class"], "motorway"]
                        ]
                    ],
                    "layout": {"line-cap": "butt", "line-join": "miter"},
                    "paint": {
                        "line-color": "rgb(213, 213, 213)",
                        "line-dasharray": [2, 0],
                        "line-opacity": 1,
                        "line-width": [
                        "interpolate",
                        ["exponential", 1.4],
                        ["zoom"],
                        5.8,
                        0,
                        6,
                        3,
                        20,
                        40
                        ]
                    }
                    },
                    {
                    "id": "highway_motorway_inner",
                    "type": "line",
                    "source": "openmaptiles",
                    "source-layer": "transportation",
                    "minzoom": 6,
                    "filter": [
                        "all",
                        ["==", ["geometry-type"], "LineString"],
                        [
                        "all",
                        ["match", ["get", "brunnel"], ["bridge", "tunnel"], False, True],
                        ["==", ["get", "class"], "motorway"]
                        ]
                    ],
                    "layout": {"line-cap": "round", "line-join": "round"},
                    "paint": {
                        "line-color": [
                        "interpolate",
                        ["linear"],
                        ["zoom"],
                        5.8,
                        "hsla(0,0%,85%,0.53)",
                        6,
                        "#fff"
                        ],
                        "line-width": [
                        "interpolate",
                        ["exponential", 1.4],
                        ["zoom"],
                        4,
                        2,
                        6,
                        1.3,
                        20,
                        30
                        ]
                    }
                    },
                    {
                    "id": "highway_motorway_subtle",
                    "type": "line",
                    "source": "openmaptiles",
                    "source-layer": "transportation",
                    "maxzoom": 6,
                    "filter": [
                        "all",
                        ["==", ["geometry-type"], "LineString"],
                        ["==", ["get", "class"], "motorway"]
                    ],
                    "layout": {"line-cap": "round", "line-join": "round"},
                    "paint": {
                        "line-color": "hsla(0,0%,85%,0.53)",
                        "line-width": [
                        "interpolate",
                        ["exponential", 1.4],
                        ["zoom"],
                        4,
                        2,
                        6,
                        1.3
                        ]
                    }
                    },
                    {
                    "id": "railway_transit",
                    "type": "line",
                    "source": "openmaptiles",
                    "source-layer": "transportation",
                    "minzoom": 16,
                    "filter": [
                        "all",
                        ["==", ["geometry-type"], "LineString"],
                        [
                        "all",
                        ["==", ["get", "class"], "transit"],
                        ["match", ["get", "brunnel"], ["tunnel"], False, True]
                        ]
                    ],
                    "layout": {"line-join": "round"},
                    "paint": {"line-color": "#dddddd", "line-width": 3}
                    },
                    {
                    "id": "railway_transit_dashline",
                    "type": "line",
                    "source": "openmaptiles",
                    "source-layer": "transportation",
                    "minzoom": 16,
                    "filter": [
                        "all",
                        ["==", ["geometry-type"], "LineString"],
                        [
                        "all",
                        ["==", ["get", "class"], "transit"],
                        ["match", ["get", "brunnel"], ["tunnel"], False, True]
                        ]
                    ],
                    "layout": {"line-join": "round"},
                    "paint": {
                        "line-color": "#fafafa",
                        "line-dasharray": [3, 3],
                        "line-width": 2
                    }
                    },
                    {
                    "id": "railway_service",
                    "type": "line",
                    "source": "openmaptiles",
                    "source-layer": "transportation",
                    "minzoom": 16,
                    "filter": [
                        "all",
                        ["==", ["geometry-type"], "LineString"],
                        ["all", ["==", ["get", "class"], "rail"], ["has", "service"]]
                    ],
                    "layout": {"line-join": "round"},
                    "paint": {"line-color": "#dddddd", "line-width": 3}
                    },
                    {
                    "id": "railway_service_dashline",
                    "type": "line",
                    "source": "openmaptiles",
                    "source-layer": "transportation",
                    "minzoom": 16,
                    "filter": [
                        "all",
                        ["==", ["geometry-type"], "LineString"],
                        ["==", ["get", "class"], "rail"],
                        ["has", "service"]
                    ],
                    "layout": {"line-join": "round"},
                    "paint": {
                        "line-color": "#fafafa",
                        "line-dasharray": [3, 3],
                        "line-width": 2
                    }
                    },
                    {
                    "id": "railway",
                    "type": "line",
                    "source": "openmaptiles",
                    "source-layer": "transportation",
                    "minzoom": 13,
                    "filter": [
                        "all",
                        ["==", ["geometry-type"], "LineString"],
                        ["all", ["!", ["has", "service"]], ["==", ["get", "class"], "rail"]]
                    ],
                    "layout": {"line-join": "round"},
                    "paint": {
                        "line-color": "#dddddd",
                        "line-width": [
                        "interpolate",
                        ["exponential", 1.3],
                        ["zoom"],
                        16,
                        3,
                        20,
                        7
                        ]
                    }
                    },
                    {
                    "id": "railway_dashline",
                    "type": "line",
                    "source": "openmaptiles",
                    "source-layer": "transportation",
                    "minzoom": 13,
                    "filter": [
                        "all",
                        ["==", ["geometry-type"], "LineString"],
                        ["all", ["!", ["has", "service"]], ["==", ["get", "class"], "rail"]]
                    ],
                    "layout": {"line-join": "round"},
                    "paint": {
                        "line-color": "#fafafa",
                        "line-dasharray": [3, 3],
                        "line-width": [
                        "interpolate",
                        ["exponential", 1.3],
                        ["zoom"],
                        16,
                        2,
                        20,
                        6
                        ]
                    }
                    },
                    {
                    "id": "highway_motorway_bridge_casing",
                    "type": "line",
                    "source": "openmaptiles",
                    "source-layer": "transportation",
                    "minzoom": 6,
                    "filter": [
                        "all",
                        ["==", ["geometry-type"], "LineString"],
                        [
                        "all",
                        ["==", ["get", "brunnel"], "bridge"],
                        ["==", ["get", "class"], "motorway"]
                        ]
                    ],
                    "layout": {"line-cap": "butt", "line-join": "miter"},
                    "paint": {
                        "line-color": "rgb(213, 213, 213)",
                        "line-dasharray": [2, 0],
                        "line-opacity": 1,
                        "line-width": [
                        "interpolate",
                        ["exponential", 1.4],
                        ["zoom"],
                        5.8,
                        0,
                        6,
                        5,
                        20,
                        45
                        ]
                    }
                    },
                    {
                    "id": "highway_motorway_bridge_inner",
                    "type": "line",
                    "source": "openmaptiles",
                    "source-layer": "transportation",
                    "minzoom": 6,
                    "filter": [
                        "all",
                        ["==", ["geometry-type"], "LineString"],
                        [
                        "all",
                        ["==", ["get", "brunnel"], "bridge"],
                        ["==", ["get", "class"], "motorway"]
                        ]
                    ],
                    "layout": {"line-cap": "round", "line-join": "round"},
                    "paint": {
                        "line-color": [
                        "interpolate",
                        ["linear"],
                        ["zoom"],
                        5.8,
                        "hsla(0,0%,85%,0.53)",
                        6,
                        "#fff"
                        ],
                        "line-width": [
                        "interpolate",
                        ["exponential", 1.4],
                        ["zoom"],
                        4,
                        2,
                        6,
                        1.3,
                        20,
                        30
                        ]
                    }
                    },
                    {
                    "id": "boundary_3",
                    "type": "line",
                    "source": "openmaptiles",
                    "source-layer": "boundary",
                    "minzoom": 1,
                    "filter": [
                        "all",
                        [">=", ["get", "admin_level"], 3],
                        ["<=", ["get", "admin_level"], 6],
                        ["!=", ["get", "maritime"], 1],
                        ["!=", ["get", "disputed"], 1],
                        ["!", ["has", "claimed_by"]]
                    ],
                    "layout": {"visibility": "visible"},
                    "paint": {
                        "line-color": "hsl(0,0%,70%)",
                        "line-dasharray": [1, 1],
                        "line-width": ["interpolate", ["linear", 1], ["zoom"], 7, 1, 11, 2]
                    }
                    },
                    {
                    "id": "boundary_2",
                    "type": "line",
                    "source": "openmaptiles",
                    "source-layer": "boundary",
                    "filter": [
                        "all",
                        ["==", ["get", "admin_level"], 2],
                        ["!=", ["get", "maritime"], 1],
                        ["!=", ["get", "disputed"], 1],
                        ["!", ["has", "claimed_by"]]
                    ],
                    "layout": {"line-cap": "round", "line-join": "round"},
                    "paint": {
                        "line-color": "hsl(0,0%,70%)",
                        "line-opacity": ["interpolate", ["linear"], ["zoom"], 0, 0.4, 4, 1],
                        "line-width": ["interpolate", ["linear"], ["zoom"], 3, 1, 5, 1.2, 12, 3]
                    }
                    },
                    {
                    "id": "boundary_disputed",
                    "type": "line",
                    "source": "openmaptiles",
                    "source-layer": "boundary",
                    "filter": [
                        "all",
                        ["!=", ["get", "maritime"], 1],
                        ["==", ["get", "disputed"], 1]
                    ],
                    "paint": {
                        "line-color": "hsl(0,0%,70%)",
                        "line-dasharray": [1, 2],
                        "line-width": ["interpolate", ["linear"], ["zoom"], 3, 1, 5, 1.2, 12, 3]
                    }
                    },
                    {
                    "id": "waterway_line_label",
                    "type": "symbol",
                    "source": "openmaptiles",
                    "source-layer": "waterway",
                    "minzoom": 10,
                    "filter": ["==", ["geometry-type"], "LineString"],
                    "layout": {
                        "symbol-placement": "line",
                        "symbol-spacing": 350,
                        "text-field": [
                        "case",
                        ["has", "name:nonlatin"],
                        ["concat", ["get", "name:latin"], " ", ["get", "name:nonlatin"]],
                        ["coalesce", ["get", "name_en"], ["get", "name"]]
                        ],
                        "text-font": ["Noto Sans Italic"],
                        "text-letter-spacing": 0.2,
                        "text-max-width": 5,
                        "text-size": 14
                    },
                    "paint": {
                        "text-color": "hsl(0,0%,66%)",
                        "text-halo-color": "rgba(255,255,255,0.7)",
                        "text-halo-width": 1.5
                    }
                    },
                    {
                    "id": "water_name_point_label",
                    "type": "symbol",
                    "source": "openmaptiles",
                    "source-layer": "water_name",
                    "filter": ["==", ["geometry-type"], "Point"],
                    "layout": {
                        "text-field": [
                        "case",
                        ["has", "name:nonlatin"],
                        ["concat", ["get", "name:latin"], "\n", ["get", "name:nonlatin"]],
                        ["coalesce", ["get", "name_en"], ["get", "name"]]
                        ],
                        "text-font": ["Noto Sans Italic"],
                        "text-letter-spacing": 0.2,
                        "text-max-width": 5,
                        "text-size": ["interpolate", ["linear"], ["zoom"], 0, 10, 8, 14]
                    },
                    "paint": {
                        "text-color": "#495e91",
                        "text-halo-color": "rgba(255,255,255,0.7)",
                        "text-halo-width": 1.5
                    }
                    },
                    {
                    "id": "water_name_line_label",
                    "type": "symbol",
                    "source": "openmaptiles",
                    "source-layer": "water_name",
                    "filter": ["==", ["geometry-type"], "LineString"],
                    "layout": {
                        "symbol-placement": "line",
                        "symbol-spacing": 350,
                        "text-field": [
                        "case",
                        ["has", "name:nonlatin"],
                        ["concat", ["get", "name:latin"], " ", ["get", "name:nonlatin"]],
                        ["coalesce", ["get", "name_en"], ["get", "name"]]
                        ],
                        "text-font": ["Noto Sans Italic"],
                        "text-letter-spacing": 0.2,
                        "text-max-width": 5,
                        "text-size": 14
                    },
                    "paint": {
                        "text-color": "#495e91",
                        "text-halo-color": "rgba(255,255,255,0.7)",
                        "text-halo-width": 1.5
                    }
                    },
                    {
                    "id": "highway-name-path",
                    "type": "symbol",
                    "source": "openmaptiles",
                    "source-layer": "transportation_name",
                    "minzoom": 15.5,
                    "filter": ["==", ["get", "class"], "path"],
                    "layout": {
                        "symbol-placement": "line",
                        "text-field": [
                        "case",
                        ["has", "name:nonlatin"],
                        ["concat", ["get", "name:latin"], " ", ["get", "name:nonlatin"]],
                        ["coalesce", ["get", "name_en"], ["get", "name"]]
                        ],
                        "text-font": ["Noto Sans Regular"],
                        "text-rotation-alignment": "map",
                        "text-size": ["interpolate", ["linear"], ["zoom"], 13, 12, 14, 13]
                    },
                    "paint": {
                        "text-color": "hsl(30,0%,62%)",
                        "text-halo-color": "#f8f4f0",
                        "text-halo-width": 0.5
                    }
                    },
                    {
                    "id": "highway-name-minor",
                    "type": "symbol",
                    "source": "openmaptiles",
                    "source-layer": "transportation_name",
                    "minzoom": 15,
                    "filter": [
                        "all",
                        ["==", ["geometry-type"], "LineString"],
                        ["match", ["get", "class"], ["minor", "service", "track"], True, False]
                    ],
                    "layout": {
                        "symbol-placement": "line",
                        "text-field": [
                        "case",
                        ["has", "name:nonlatin"],
                        ["concat", ["get", "name:latin"], " ", ["get", "name:nonlatin"]],
                        ["coalesce", ["get", "name_en"], ["get", "name"]]
                        ],
                        "text-font": ["Noto Sans Regular"],
                        "text-rotation-alignment": "map",
                        "text-size": ["interpolate", ["linear"], ["zoom"], 13, 12, 14, 13]
                    },
                    "paint": {
                        "text-color": "#666",
                        "text-halo-blur": 0.5,
                        "text-halo-width": 1
                    }
                    },
                    {
                    "id": "highway-name-major",
                    "type": "symbol",
                    "source": "openmaptiles",
                    "source-layer": "transportation_name",
                    "minzoom": 12.2,
                    "filter": [
                        "match",
                        ["get", "class"],
                        ["primary", "secondary", "tertiary", "trunk"],
                        True,
                        False
                    ],
                    "layout": {
                        "symbol-placement": "line",
                        "text-field": [
                        "case",
                        ["has", "name:nonlatin"],
                        ["concat", ["get", "name:latin"], " ", ["get", "name:nonlatin"]],
                        ["coalesce", ["get", "name_en"], ["get", "name"]]
                        ],
                        "text-font": ["Noto Sans Regular"],
                        "text-rotation-alignment": "map",
                        "text-size": ["interpolate", ["linear"], ["zoom"], 13, 12, 14, 13]
                    },
                    "paint": {
                        "text-color": "#666",
                        "text-halo-blur": 0.5,
                        "text-halo-width": 1
                    }
                    },
                    {
                    "id": "highway-shield-non-us",
                    "type": "symbol",
                    "source": "openmaptiles",
                    "source-layer": "transportation_name",
                    "minzoom": 11,
                    "filter": [
                        "all",
                        ["<=", ["get", "ref_length"], 6],
                        ["==", ["geometry-type"], "LineString"],
                        [
                        "match",
                        ["get", "network"],
                        ["us-highway", "us-interstate", "us-state"],
                        False,
                        True
                        ]
                    ],
                    "layout": {
                        "icon-image": ["concat", "road_", ["get", "ref_length"]],
                        "icon-rotation-alignment": "viewport",
                        "icon-size": 1,
                        "symbol-placement": ["step", ["zoom"], "point", 11, "line"],
                        "symbol-spacing": 200,
                        "text-field": ["to-string", ["get", "ref"]],
                        "text-font": ["Noto Sans Regular"],
                        "text-rotation-alignment": "viewport",
                        "text-size": 10
                    }
                    },
                    {
                    "id": "highway-shield-us-interstate",
                    "type": "symbol",
                    "source": "openmaptiles",
                    "source-layer": "transportation_name",
                    "minzoom": 11,
                    "filter": [
                        "all",
                        ["<=", ["get", "ref_length"], 6],
                        ["==", ["geometry-type"], "LineString"],
                        ["match", ["get", "network"], ["us-interstate"], True, False]
                    ],
                    "layout": {
                        "icon-image": [
                        "concat",
                        ["get", "network"],
                        "_",
                        ["get", "ref_length"]
                        ],
                        "icon-rotation-alignment": "viewport",
                        "icon-size": 1,
                        "symbol-placement": ["step", ["zoom"], "point", 7, "line", 8, "line"],
                        "symbol-spacing": 200,
                        "text-field": ["to-string", ["get", "ref"]],
                        "text-font": ["Noto Sans Regular"],
                        "text-rotation-alignment": "viewport",
                        "text-size": 10
                    }
                    },
                    {
                    "id": "road_shield_us",
                    "type": "symbol",
                    "source": "openmaptiles",
                    "source-layer": "transportation_name",
                    "minzoom": 12,
                    "filter": [
                        "all",
                        ["<=", ["get", "ref_length"], 6],
                        ["==", ["geometry-type"], "LineString"],
                        ["match", ["get", "network"], ["us-highway", "us-state"], True, False]
                    ],
                    "layout": {
                        "icon-image": [
                        "concat",
                        ["get", "network"],
                        "_",
                        ["get", "ref_length"]
                        ],
                        "icon-rotation-alignment": "viewport",
                        "icon-size": 1,
                        "symbol-placement": ["step", ["zoom"], "point", 11, "line"],
                        "symbol-spacing": 200,
                        "text-field": ["to-string", ["get", "ref"]],
                        "text-font": ["Noto Sans Regular"],
                        "text-rotation-alignment": "viewport",
                        "text-size": 10
                    }
                    },
                    {
                    "id": "airport",
                    "type": "symbol",
                    "source": "openmaptiles",
                    "source-layer": "aerodrome_label",
                    "minzoom": 11,
                    "filter": ["all", ["has", "iata"]],
                    "layout": {
                        "icon-image": "airport_11",
                        "icon-size": 1,
                        "text-anchor": "top",
                        "text-field": [
                        "case",
                        ["has", "name:nonlatin"],
                        ["concat", ["get", "name:latin"], "\n", ["get", "name:nonlatin"]],
                        ["coalesce", ["get", "name_en"], ["get", "name"]]
                        ],
                        "text-font": ["Noto Sans Regular"],
                        "text-max-width": 9,
                        "text-offset": [0, 0.6],
                        "text-optional": True,
                        "text-padding": 2,
                        "text-size": 12
                    },
                    "paint": {
                        "text-color": "#666",
                        "text-halo-blur": 0.5,
                        "text-halo-color": "#ffffff",
                        "text-halo-width": 1
                    }
                    },
                    {
                    "id": "label_other",
                    "type": "symbol",
                    "source": "openmaptiles",
                    "source-layer": "place",
                    "minzoom": 8,
                    "filter": [
                        "match",
                        ["get", "class"],
                        ["city", "continent", "country", "state", "town", "village"],
                        False,
                        True
                    ],
                    "layout": {
                        "text-field": [
                        "case",
                        ["has", "name:nonlatin"],
                        ["concat", ["get", "name:latin"], "\n", ["get", "name:nonlatin"]],
                        ["coalesce", ["get", "name_en"], ["get", "name"]]
                        ],
                        "text-font": ["Noto Sans Italic"],
                        "text-letter-spacing": 0.1,
                        "text-max-width": 9,
                        "text-size": ["interpolate", ["linear"], ["zoom"], 8, 9, 12, 10],
                        "text-transform": "uppercase"
                    },
                    "paint": {
                        "text-color": "#333",
                        "text-halo-blur": 1,
                        "text-halo-color": "#fff",
                        "text-halo-width": 1
                    }
                    },
                    {
                    "id": "label_village",
                    "type": "symbol",
                    "source": "openmaptiles",
                    "source-layer": "place",
                    "minzoom": 9,
                    "filter": ["==", ["get", "class"], "village"],
                    "layout": {
                        "icon-allow-overlap": True,
                        "icon-image": ["step", ["zoom"], "circle_11_black", 10, ""],
                        "icon-optional": False,
                        "icon-size": 0.2,
                        "text-anchor": "bottom",
                        "text-field": [
                        "case",
                        ["has", "name:nonlatin"],
                        ["concat", ["get", "name:latin"], "\n", ["get", "name:nonlatin"]],
                        ["coalesce", ["get", "name_en"], ["get", "name"]]
                        ],
                        "text-font": ["Noto Sans Regular"],
                        "text-max-width": 8,
                        "text-size": [
                        "interpolate",
                        ["exponential", 1.2],
                        ["zoom"],
                        7,
                        10,
                        11,
                        12
                        ]
                    },
                    "paint": {
                        "text-color": "#000",
                        "text-halo-blur": 1,
                        "text-halo-color": "#fff",
                        "text-halo-width": 1
                    }
                    },
                    {
                    "id": "label_town",
                    "type": "symbol",
                    "source": "openmaptiles",
                    "source-layer": "place",
                    "minzoom": 6,
                    "filter": ["==", ["get", "class"], "town"],
                    "layout": {
                        "icon-allow-overlap": True,
                        "icon-image": ["step", ["zoom"], "circle_11_black", 10, ""],
                        "icon-optional": False,
                        "icon-size": 0.2,
                        "text-anchor": "bottom",
                        "text-field": [
                        "case",
                        ["has", "name:nonlatin"],
                        ["concat", ["get", "name:latin"], "\n", ["get", "name:nonlatin"]],
                        ["coalesce", ["get", "name_en"], ["get", "name"]]
                        ],
                        "text-font": ["Noto Sans Regular"],
                        "text-max-width": 8,
                        "text-size": [
                        "interpolate",
                        ["exponential", 1.2],
                        ["zoom"],
                        7,
                        12,
                        11,
                        14
                        ]
                    },
                    "paint": {
                        "text-color": "#aaa",
                        "text-halo-blur": 1,
                        "text-halo-color": "#fff",
                        "text-halo-width": 1,
                        "icon-color": "rgba(0, 0, 0, 1)"
                    }
                    },
                    {
                    "id": "label_state",
                    "type": "symbol",
                    "source": "openmaptiles",
                    "source-layer": "place",
                    "minzoom": 5,
                    "maxzoom": 8,
                    "filter": ["==", ["get", "class"], "state"],
                    "layout": {
                        "text-field": [
                        "case",
                        ["has", "name:nonlatin"],
                        ["concat", ["get", "name:latin"], "\n", ["get", "name:nonlatin"]],
                        ["coalesce", ["get", "name_en"], ["get", "name"]]
                        ],
                        "text-font": ["Noto Sans Italic"],
                        "text-letter-spacing": 0.2,
                        "text-max-width": 9,
                        "text-size": ["interpolate", ["linear"], ["zoom"], 5, 10, 8, 14],
                        "text-transform": "uppercase"
                    },
                    "paint": {
                        "text-color": "#333",
                        "text-halo-blur": 1,
                        "text-halo-color": "#fff",
                        "text-halo-width": 1
                    }
                    },
                    {
                    "id": "label_city",
                    "type": "symbol",
                    "source": "openmaptiles",
                    "source-layer": "place",
                    "minzoom": 3,
                    "filter": [
                        "all",
                        ["==", ["get", "class"], "city"],
                        ["!=", ["get", "capital"], 2]
                    ],
                    "layout": {
                        "icon-allow-overlap": True,
                        "icon-image": ["step", ["zoom"], "circle_11_black", 9, ""],
                        "icon-optional": False,
                        "icon-size": 0.4,
                        "text-anchor": "bottom",
                        "text-field": [
                        "case",
                        ["has", "name:nonlatin"],
                        ["concat", ["get", "name:latin"], "\n", ["get", "name:nonlatin"]],
                        ["coalesce", ["get", "name_en"], ["get", "name"]]
                        ],
                        "text-font": ["Noto Sans Regular"],
                        "text-max-width": 8,
                        "text-offset": [0, -0.1],
                        "text-size": [
                        "interpolate",
                        ["exponential", 1.2],
                        ["zoom"],
                        4,
                        11,
                        7,
                        13,
                        11,
                        18
                        ]
                    },
                    "paint": {
                        "text-color": "rgba(153, 153, 153, 1)",
                        "text-halo-blur": 1,
                        "text-halo-color": "#fff",
                        "text-halo-width": 1
                    }
                    },
                    {
                    "id": "label_city_capital",
                    "type": "symbol",
                    "source": "openmaptiles",
                    "source-layer": "place",
                    "minzoom": 3,
                    "filter": [
                        "all",
                        ["==", ["get", "class"], "city"],
                        ["==", ["get", "capital"], 2]
                    ],
                    "layout": {
                        "icon-allow-overlap": True,
                        "icon-image": ["step", ["zoom"], "circle_11_black", 9, ""],
                        "icon-optional": False,
                        "icon-size": 0.5,
                        "text-anchor": "bottom",
                        "text-field": [
                        "case",
                        ["has", "name:nonlatin"],
                        ["concat", ["get", "name:latin"], "\n", ["get", "name:nonlatin"]],
                        ["coalesce", ["get", "name_en"], ["get", "name"]]
                        ],
                        "text-font": ["Noto Sans Bold"],
                        "text-max-width": 8,
                        "text-offset": [0, -0.2],
                        "text-size": [
                        "interpolate",
                        ["exponential", 1.2],
                        ["zoom"],
                        4,
                        12,
                        7,
                        14,
                        11,
                        20
                        ]
                    },
                    "paint": {
                        "text-color": "#000",
                        "text-halo-blur": 1,
                        "text-halo-color": "#fff",
                        "text-halo-width": 1
                    }
                    },
                    {
                    "id": "label_country_3",
                    "type": "symbol",
                    "source": "openmaptiles",
                    "source-layer": "place",
                    "minzoom": 2,
                    "maxzoom": 9,
                    "filter": [
                        "all",
                        ["==", ["get", "class"], "country"],
                        [">=", ["get", "rank"], 3]
                    ],
                    "layout": {
                        "text-field": [
                        "case",
                        ["has", "name:nonlatin"],
                        ["concat", ["get", "name:latin"], "\n", ["get", "name:nonlatin"]],
                        ["coalesce", ["get", "name_en"], ["get", "name"]]
                        ],
                        "text-font": ["Noto Sans Bold"],
                        "text-max-width": 6.25,
                        "text-size": ["interpolate", ["linear"], ["zoom"], 3, 9, 7, 17]
                    },
                    "paint": {
                        "text-color": "#000",
                        "text-halo-blur": 1,
                        "text-halo-color": "#fff",
                        "text-halo-width": 1
                    }
                    },
                    {
                    "id": "label_country_2",
                    "type": "symbol",
                    "source": "openmaptiles",
                    "source-layer": "place",
                    "maxzoom": 9,
                    "filter": [
                        "all",
                        ["==", ["get", "class"], "country"],
                        ["==", ["get", "rank"], 2]
                    ],
                    "layout": {
                        "text-field": [
                        "case",
                        ["has", "name:nonlatin"],
                        ["concat", ["get", "name:latin"], "\n", ["get", "name:nonlatin"]],
                        ["coalesce", ["get", "name_en"], ["get", "name"]]
                        ],
                        "text-font": ["Noto Sans Bold"],
                        "text-max-width": 6.25,
                        "text-size": ["interpolate", ["linear"], ["zoom"], 2, 9, 5, 17]
                    },
                    "paint": {
                        "text-color": "#000",
                        "text-halo-blur": 1,
                        "text-halo-color": "#fff",
                        "text-halo-width": 1
                    }
                    },
                    {
                    "id": "label_country_1",
                    "type": "symbol",
                    "source": "openmaptiles",
                    "source-layer": "place",
                    "maxzoom": 9,
                    "filter": [
                        "all",
                        ["==", ["get", "class"], "country"],
                        ["==", ["get", "rank"], 1]
                    ],
                    "layout": {
                        "text-field": [
                        "case",
                        ["has", "name:nonlatin"],
                        ["concat", ["get", "name:latin"], "\n", ["get", "name:nonlatin"]],
                        ["coalesce", ["get", "name_en"], ["get", "name"]]
                        ],
                        "text-font": ["Noto Sans Bold"],
                        "text-max-width": 6.25,
                        "text-size": ["interpolate", ["linear"], ["zoom"], 1, 9, 4, 17]
                    },
                    "paint": {
                        "text-color": "#000",
                        "text-halo-blur": 1,
                        "text-halo-color": "#fff",
                        "text-halo-width": 1
                    }
                    }
                ],
            },
            "arches_metadata": {"addtomap": True, "icon": "fa fa-globe", "isoverlay": False},
        }

        reference_collections = {
            "maplayerid": uuid.UUID("803829fe-b437-40b2-94a4-8ae10fa25b10"),
            "sortorder": 1,
            "style": {
                "name": "Reference Collections",
                "sources": {
                    "referencecollections": {
                        "type": "vector",
                        "tiles": ["/api-reference-collection-mvt/{z}/{x}/{y}.pbf"],
                        "minzoom": 1,
                    }
                },
                "layers": [
                    {
                        "id": "referencecollections-point-stroke",
                        "source": "referencecollections",
                        "source-layer": "referencecollections",
                        "type": "circle",
                        "filter": ['all',[
                            "==", "$type", "Point"
                        ]],
                        "paint": {
                            "circle-radius": 6,
                            "circle-opacity": 1,
                            "circle-color": "#00f"
                        }
                    }, {
                        "id": "referencecollections-point",
                        "source": "referencecollections",
                        "source-layer": "referencecollections",
                        "type": "circle",
                        "filter": ['all',[
                            "==", "$type", "Point"
                        ]],
                        "paint": {
                            "circle-radius": 3,
                            "circle-color": "#aaf"
                        }
                    },
                    {
                        "id": "referencecollections-line",
                        "type": "line",
                        "paint": {
                            "line-color": "#00f",
                            "line-width": 3
                        },
                        "layout": {
                            "line-cap": "round",
                            "line-join": "round"
                        },
                        "source": "referencecollections",
                        "source-layer": "referencecollections"
                    },
                    {
                        "id": "referencecollections-polygon-line",
                        "type": "line",
                        "paint": {
                            "line-color": "#00f",
                            "line-width": 3
                        },
                        "filter": [
                            "==",
                            "$type",
                            "Polygon"
                        ],
                        "layout": {
                            "line-cap": "round",
                            "line-join": "round"
                        },
                        "source": "referencecollections",
                        "source-layer": "referencecollections"
                    },
                    {
                        "id": "referencecollections-fill",
                        "type": "fill",
                        "paint": {
                            "fill-color": "#00f",
                            "fill-opacity": 0.1,
                            "fill-outline-color": "#0ff"
                        },
                        "filter": [
                            "==",
                            "$type",
                            "Polygon"
                        ],
                        "source": "referencecollections",
                        "source-layer": "referencecollections"
                    },
                    {
                        "id": "referencecollections-labels",
                        "type": "symbol",
                        "paint": {
                            "text-color": "#33d",
                            "text-halo-color": "#fff",
                            "text-halo-width": 2.5
                        },
                        "layout": {
                            "text-font": [
                                "Open Sans Semibold",
                                "Arial Unicode MS Bold"
                            ],
                            "text-size": 18,
                            "text-field": [
                                "get",
                                "quad_name"
                            ],
                            "text-justify": "auto",
                            "text-radial-offset": 0.5,
                            "text-variable-anchor": [
                                "top",
                                "bottom",
                                "left",
                                "right"
                            ]
                        },
                        "source": "referencecollections",
                        "minzoom": 9,
                        "source-layer": "referencecollections"
                    }
                ],
            },
            "arches_metadata": {"addtomap": True, "icon": "fa fa-globe", "isoverlay": True},
        }

        layer_configs = (ofm_positron_light, reference_collections)

        for config in layer_configs:
            try:
                config["style"] = json.loads(config["style"])
            except:
                pass
            layer_name = config["style"]["name"]
            for layer in config["style"]["layers"]:
                if "source" in layer:
                    layer["source"] = layer["source"]
            for source_name, source_dict in config["style"]["sources"].items():
                MapSource.objects.get_or_create(name=source_name, source=source_dict)

            map_layer = MapLayer(
                maplayerid=config["maplayerid"],
                name=layer_name,
                sortorder=config["sortorder"],
                layerdefinitions=config["style"]["layers"],
                **config["arches_metadata"],
            )
            map_layer.save()

    def remove_map_layers(apps, schema_editor):
        MapSource = apps.get_model("models", "MapSource")
        MapLayer = apps.get_model("models", "MapLayer")
        layerids = (
            "803829fe-b437-40b2-94a4-8ae10fa25b10",
        )
        for layerid in layerids:
            mapbox_layer = MapLayer.objects.get(maplayerid=layerid)
            all_sources = [i.get("source") for i in mapbox_layer.layerdefinitions]
            sources = {i for i in all_sources if i}
            for source in sources:
                src = MapSource.objects.get(name=source)
                src.delete()
            mapbox_layer.delete()


    operations = [
        migrations.RunPython(add_map_layers, remove_map_layers),
    ]