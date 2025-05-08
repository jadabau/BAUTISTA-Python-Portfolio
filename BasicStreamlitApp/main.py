import streamlit as st
import pandas as pd

st.title("🎬 Movie Ratings Viewer")
st.markdown("Go through the top grossed movies between **2007 and 2011**!")

# load the dataset
csv_path = "basicstreamlitapp/data/movies.csv"
df = pd.read_csv(csv_path)

# change 'Audience score %' to numeric
df["Audience score %"] = pd.to_numeric(df["Audience score %"], errors="coerce")

# take out the missing values in 'Audience score %'
df = df.dropna(subset=["Audience score %"])

# fix the typos in the genre column
df["Genre"] = df["Genre"].replace({
    "Romence": "Romance",
    "Comdy": "Comedy",
    "comedy": "Comedy",
    "romance": "Romance"
})

# **display the raw data column**
st.write("### 🍿 Movie Data")
st.dataframe(df)

# **apply interactive filters**
genre = st.selectbox("🔍 Select Genre", ["All"] + sorted(df["Genre"].unique()))

# Audience score slider (from 0 to 100)
score_min, score_max = st.slider(
    "⭐ Filter by Audience Score %",
    min_value=0.0,
    max_value=100.0,
    value=(float(df["Audience score %"].min()), float(df["Audience score %"].max())),
    step=0.1
)

# **sort the options**
st.sidebar.header("🔽 Sorting options")

sort_column = st.sidebar.selectbox("Sort by column", df.columns)

# Sorting order (ascending or descending)
sort_order = st.sidebar.radio("Order", ["Ascending", "Descending"])

filtered_df = df.copy()
if genre != "All":
    filtered_df = filtered_df[filtered_df["Genre"] == genre]
filtered_df = filtered_df[(filtered_df["Audience score %"] >= score_min) & (filtered_df["Audience score %"] <= score_max)]

ascending_order = True if sort_order == "Ascending" else False
filtered_df = filtered_df.sort_values(by=sort_column, ascending=ascending_order)

st.write(f"### Filtered results ({len(filtered_df)} movies)")
st.dataframe(filtered_df)
