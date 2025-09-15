import streamlit as st
import pandas as pd
import plotly.express as px

# Load Data
df = pd.read_csv("data/women_in_tech.csv")

# App Title
st.title("👩‍💻 Women in Tech - Ghana Dashboard")
st.write("Insights, trends, and opportunities for women in the Ghanaian tech ecosystem.")

# Sidebar filters
categories = df['category'].unique()
selected_category = st.sidebar.selectbox("Select a category", categories)

# Filtered data
filtered_df = df[df['category'] == selected_category]

# Line Chart
fig = px.line(
    filtered_df,
    x="year",
    y="value",
    markers=True,
    title=f"{selected_category} Over Time",
    labels={"value": "%", "year": "Year"}
)


# --- Education (Bar Chart) ---
st.subheader("🎓 STEM Graduates by Gender")
edu_df = pd.read_csv("data/education.csv")
region = st.selectbox("Select region", edu_df["region"].unique())
filtered_edu = edu_df[edu_df["region"] == region]
fig_bar = px.bar(
    filtered_edu,
    x="year",
    y="graduates",
    color="gender",
    barmode="group",
    title=f"STEM Graduates in {region}"
)
st.plotly_chart(fig_bar, use_container_width=True)

# --- Roles (Pie Chart) ---
st.subheader("💼 Distribution of Women in Tech Roles")
roles_df = pd.read_csv("data/roles.csv")
year_roles = st.selectbox("Select year", roles_df["year"].unique())
filtered_roles = roles_df[roles_df["year"] == year_roles]
fig_pie = px.pie(filtered_roles, names="role", values="percentage",
                 title=f"Women in Tech Roles ({year_roles})")
st.plotly_chart(fig_pie, use_container_width=True)

# --- Leadership (Line Chart by Region) ---
st.subheader("👩‍💼 Women in Leadership by Region")
lead_df = pd.read_csv("data/leadership.csv")
fig_line = px.line(lead_df, x="year", y="percentage", color="region",
                   markers=True, title="Leadership Representation")
st.plotly_chart(fig_line, use_container_width=True)


# --- Communities Map ---
st.subheader("🌍 Women in Tech Communities in Ghana")

comm_df = pd.read_csv("data/communities.csv")

fig_map = px.scatter_mapbox(
    comm_df,
    lat="latitude",
    lon="longitude",
    text="community",
    hover_name="community",
    hover_data=["region", "focus"],
    zoom=6,
    height=500,
    color_discrete_sequence=["purple"]
)

fig_map.update_layout(mapbox_style="open-street-map")
fig_map.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

st.plotly_chart(fig_map, use_container_width=True)


# Fix x-axis ticks (show integers only)
fig.update_xaxes(dtick=1)

st.plotly_chart(fig, use_container_width=True)


# Show Data Table
if st.checkbox("Show Raw Data"):
    st.write(filtered_df)
