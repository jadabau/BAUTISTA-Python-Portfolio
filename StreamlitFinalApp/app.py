import streamlit as st
import pandas as pd

# Load the CSV
df = pd.read_excel('StreamlitFinalApp/phtravel.xlsx')

# Rename columns for map compatibility
df = df.rename(columns={'Latitude': 'latitude', 'Longitude': 'longitude'})

# Sidebar main navigation
st.sidebar.title("🌺 Navigation")
page = st.sidebar.radio("Go to:", ["🏠 Home", "🌸 Explore by Category"])

# App title (always shown)
st.markdown("<h1 style='text-align: center;'>Travel Pilipinas: Cultural Explorer 🇵🇭🌴✨</h1>", unsafe_allow_html=True)

# Home Page
if page == "🏠 Home":
    st.markdown("<p style='text-align: center;'>Welcome to <b>Travel Pilipinas</b>, your guide to the Philippines' breathtaking destinations! 🌊⛰️🌺</p>", unsafe_allow_html=True)
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/3/3d/Philippines_islands.png",
        caption="Archipelago of Wonders",
        use_container_width=True
    )
    st.markdown("""
        ### 🌟 What You’ll Find Here:
        - Discover **natural wonders** like beaches, mountains, and waterfalls
        - Explore **cultural treasures** from festivals to local crafts
        - Visit **historic landmarks** that shaped Philippine history
        - Get tips, trivia, and beautiful visuals of each destination

        👉 Use the sidebar to start exploring!
    """)
    st.markdown("---")

# Explore by Category Page
elif page == "🌸 Explore by Category":
    st.markdown("<p style='text-align: center;'>Select an experience below to explore recommended destinations.</p>", unsafe_allow_html=True)
    st.markdown("---")

    # Sidebar category selection
    category = st.sidebar.selectbox("Choose your experience:", df['Category'].unique())

    # Filter data by category
    filtered_df = df[df['Category'] == category]

    # Sidebar destination selector
    if not filtered_df.empty:
        destination = st.sidebar.selectbox(
            f"Select a destination in {category}:",
            ["Show All"] + sorted(filtered_df['Place'].unique())
        )
    else:
        st.sidebar.warning("No destinations found for this category.")

    # Show on map (if available)
    if not filtered_df.empty and 'latitude' in df.columns and 'longitude' in df.columns:
        st.subheader(f"🗺️ Map of {category} Destinations")
        st.map(filtered_df[['latitude', 'longitude']])

    # Show destination details
    st.markdown("---")
    if destination != "Show All":
        filtered_df = filtered_df[filtered_df['Place'] == destination]

    if not filtered_df.empty:
        for index, row in filtered_df.iterrows():
            with st.expander(f"🌟 {row['Place']}"):
                if 'ImageURL' in row and pd.notna(row['ImageURL']):
                    st.image(row['ImageURL'], width=500, caption=row['Place'])
                st.write(f"**Description:** {row['Description']}")
                if 'DidYouKnow' in row and pd.notna(row['DidYouKnow']):
                    st.info(f"💡 **Did you know?** {row['DidYouKnow']}")
                if 'SpecialFood' in row and pd.notna(row['SpecialFood']):
                    st.success(f"🍽️ **To Eat in {row['Place']}:** {row['SpecialFood']}")
    else:
        st.warning("No destinations match your current filters.")

# Footer (always shown)
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 12px;'>Made with ❤️ for cultural travelers 🌍 | Streamlit App Demo</p>", unsafe_allow_html=True)
