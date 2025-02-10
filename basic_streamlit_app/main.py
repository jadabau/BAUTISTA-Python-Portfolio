import streamlit as st
import pandas as pd

st.title("🎬 Movie Ratings Viewer!")
st.markdown("Go through the top grossed movies between **2007 and 2011**!")

# load the dataset
csv_path = "basic_streamlit_app/data/your_data.csv"
df = pd.read_csv(csv_path)

# make Audience score % numeric
df["Audience score %"] = pd.to_numeric(df["Audience score %"], errors="coerce")

# make sure to remove missing values in Audience score %
df = df.dropna(subset=["Audience score %"])

# fix typos in the Genre column
df["Genre"] = df["Genre"].replace({
    "Romence": "Romance",
    "Comdy": "Comedy",
    "comedy": "Comedy",
    "romance": "Romance"
})

# show the raw data table
st.write("### 🍿 Movie Data")
st.dataframe(df)

# apply interactive slide filter
genre = st.selectbox("🔍 Select Genre", ["All"] + sorted(df["Genre"].unique()))

score_min, score_max = st.slider(
    "⭐ Filter by Audience Score %",
    min_value=0.0,  # min score (float)
    max_value=100.0,  # max score (float)
    value=(float(df["Audience score %"].min()), float(df["Audience score %"].max())),  # Default range
    step=0.1  # make sure step is a float to match min/max
)

# apply the filter
filtered_df = df.copy()
if genre != "All":
    filtered_df = filtered_df[filtered_df["Genre"] == genre]
filtered_df = filtered_df[(filtered_df["Audience score %"] >= score_min) & (filtered_df["Audience score %"] <= score_max)]

# show the filtered results
st.write(f"### Filtered Results ({len(filtered_df)} movies)")
st.dataframe(filtered_df)
