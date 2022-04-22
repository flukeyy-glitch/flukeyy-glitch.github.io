import streamlit as st 
from streamlit_option_menu import option_menu
import streamlit as st
from streamlit_folium import folium_static
import folium

st.set_page_config(page_title="Greta Hall, Keswick", page_icon="gretahall.png", layout="wide")

with st.sidebar:
    selected = option_menu(
        menu_title ="Main Menu",
        options=["Home", "The House", "History", "Gallery", "Bookings", "Location", "Contact"],

    )

if selected == "Home":
    st.title(f" You have selected {selected}")
if selected == "The House":
    st.title(f" You have selected {selected}")
if selected == "History":
    st.title(f" You have selected {selected}")
if selected == "Gallery":
    st.title(f" You have selected {selected}")
if selected == "Bookings":
    st.title(f" You have selected {selected}")
if selected == "Location":
    st.title(f" You have selected {selected}")

"# streamlit-folium"

with st.echo():
    import streamlit as st
    from streamlit_folium import folium_static
    import folium

    # center on Liberty Bell
    m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)

    # add marker for Liberty Bell
    tooltip = "Liberty Bell"
    folium.Marker(
        [39.949610, -75.150282], popup="Liberty Bell", tooltip=tooltip
    ).add_to(m)

    # call to render Folium map in Streamlit
    folium_static(m)
if selected == "Contact":
    st.title(f" You have selected {selected}")

#---- HEADER SECTION ------
with st.container():
    st.subheader("Greta Hall")
    st.title("Premium Self Catering in Keswick, the Lake District")
    st.write("Former home of the Lakes poets Samuel Taylor Coleridge and Robert Southey")
    st.write("Retreat among Lakeland's finest peaks")

# ---- INFORMATION ABOUT GRETA HALL ------
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("The House")
        st.write("##")
        st.write(
            """
            Greta Hall is a stunning historic Georgian house in the heart of Keswick with a large garden and stunning views from every windows. With self catering sleeping for 2-22 guests in three Wings, original features, open fires, large bedrooms, cosy reception rooms, well equipped kitchens and, it is a wonderful place to stay.
            """
        )