import streamlit as st
from st_cytoscape import cytoscape

st.set_page_config(layout="wide")

asset_library_tab, network_library_tab = st.tabs(["Asset Tab", "Network Tab"])

elements = [
    {
        "data": {"id": "asset"},
        "position": {"x": 150, "y": 0},
        "classes": "",
    },
    {
        "data": {"id": "product"},
        "position": {"x": 0, "y": 150},
        "classes": "product",
    },
    {
        "data": {"id": "process"},
        "position": {"x": 150, "y": 150},
        "classes": "process",
    },
    {
        "data": {"id": "resource"},
        "position": {"x": 300, "y": 150},
        "classes": "resource",
    },
    {
        "data": {"id": "machine"},
        "position": {"x": 300, "y": 150},
        "classes": "resource",
    },
    {
        "data": {"id": "sensor"},
        "position": {"x": 300, "y": 150},
        "classes": "resource",
    },
    {
        "data": {"id": "actuator"},
        "position": {"x": 300, "y": 50},
        "classes": "resource",
    },
    {
        "data": {"id": "joining"},
        "position": {"x": 300, "y": 50},
        "classes": "process",
    },
    {
        "data": {"id": "welding", "label":"Welding"},
        "position": {"x": 300, "y": 50},
        "classes": "process",
    },
    {"data": {"source": "asset", "target": "product", "id": "asset➞product"}},
    {"data": {"source": "asset", "target": "process", "id": "asset➞process"}},
    {"data": {"source": "asset", "target": "resource", "id": "asset➞resource"}},
    {"data": {"source": "resource", "target": "machine", "id": "resource➞machine"}},
    {"data": {"source": "resource", "target": "actuator", "id": "resource➞actuator"}},
    {"data": {"source": "resource", "target": "sensor", "id": "resource➞sensor"}},
    {"data": {"source": "process", "target": "joining", "id": "process➞joining"}},
    {"data": {"source": "joining", "target": "welding", "id": "joining➞welding"}},
]


stylesheet = [

    {
        "selector": "node",
        "style": {
            "background-color": "light-grey",
            "label": "data(id)",
            "width": 48,
            "height": 30,
            "shape": "rectangle",
            "text-valign": "center",
            "text-halign": "center",
            "font-size": 10,
            "text-wrap": "wrap",  # Wrap the text
            "text-max-width": 48,  # Maximum width before text wraps
        },
    },
    {
        "selector": ".product",
        "style": {
            "background-color": "#AEBFBE",
        },
    },
    {
        "selector": ".process",
        "style": {
            "background-color": "#59554C",
            #"label": "data(label)",
        },
    },
    {
        "selector": ".resource",
        "style": {
            "background-color": "#F2EFDF",
        },
    },
    {
        "selector": ".image",
        "style": {
            "label": "",
            "background-color": "light-grey",
            "background-image": "https://i.imgur.com/74eSogS.png",
            # "background-image":
            "width": 200,
            "height": 500,
        },
    },
    {
        "selector": ".corner",
        "style": {
            "label": "",
            "background-color": "#ffffff",
        },
    },
    {
        "selector": "edge",
        "style": {
            "width": 3,
            "curve-style": "bezier",
            "target-arrow-shape": "triangle",
        },
    },
]

with asset_library_tab:
    st.header("PPR Library")

    selected = cytoscape(
        elements,
        stylesheet,
        key="graph",
        layout={ "name": "klay"},
        user_panning_enabled=True,
        user_zooming_enabled=False,
        selection_type="single",
        min_zoom=1,
        height="50em"
    )

    if len(selected["nodes"]) > 0:
        st.header(selected["nodes"][0])

    st.button("Delete Element", use_container_width=True)
    st.button("Add Child", use_container_width=True, type="primary" )

product_list = ["product"]
process_list = ["process", "welding", "joining"]
resource_list = ["resource", "sensor", "actuator" , "machine"]

with network_library_tab:
    st.info("Here go the networked assets")

    with st.expander("Welding network"):
        input_products = st.multiselect("Input products", options=product_list)
        process = st.multiselect("Process", options=process_list)
        output_products = st.multiselect("Output Products", options=product_list)
        main_resource = st.multiselect("Main Resource", options=resource_list)
        sub_resources = st.multiselect("Sub Resources", options=resource_list)

    st.button("Add new Network", use_container_width=True, type="secondary" )
    st.button("Save configuration", use_container_width=True, type="primary")