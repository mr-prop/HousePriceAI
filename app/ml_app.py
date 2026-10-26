import requests
import pandas as pd
import streamlit as st


title = st.title("Real Estate")

caption = st.caption("House price prediction")

df = pd.read_csv("data/real_estate_dataset2.csv")

x = df.drop(["Price" , "ID"] , axis=1)
y = df["Price"]

with st.expander("Feature"):
    st.dataframe(x)

with st.expander("target"):
    st.dataframe(y)

st.sidebar.title("Enter data")

Square_Feet = st.sidebar.slider("Square Feet" ,
                                min_value=float(df["Square_Feet"].min()),
                                max_value=float(df["Square_Feet"].max()),
                                value=float(df["Square_Feet"].mean()))

Num_Bedrooms = st.sidebar.selectbox(
    "Number of Bedrooms",
    sorted(df["Num_Bedrooms"].unique())
)


Num_Bathrooms = st.sidebar.selectbox(
    "Number of Bathrooms",
    sorted(df["Num_Bathrooms"].unique())
)


Num_Floors = st.sidebar.selectbox(
    "Number of Floors",
    sorted(df["Num_Floors"].unique())
)


Year_Built = st.sidebar.slider(
    "Year Built",
    min_value=int(df["Year_Built"].min()),
    max_value=int(df["Year_Built"].max()),
    value=int(df["Year_Built"].median())
)

Has_Garden = st.sidebar.checkbox("Has Garden")

Has_Pool = st.sidebar.checkbox("Has Pool")

Garage_Size = st.sidebar.slider(
    "Garage Size",
    min_value=int(df["Garage_Size"].min()),
    max_value=int(df["Garage_Size"].max()),
    value=int(df["Garage_Size"].median())
)


Location_Score = st.sidebar.slider(
    "Location Score",
    min_value=float(df["Location_Score"].min()),
    max_value=float(df["Location_Score"].max()),
    value=float(df["Location_Score"].mean())
)


Distance_to_Center = st.sidebar.slider(
    "Distance to Center",
    min_value=float(df["Distance_to_Center"].min()),
    max_value=float(df["Distance_to_Center"].max()),
    value=float(df["Distance_to_Center"].mean())
)

button_prediction = st.sidebar.button("Prediction")

if button_prediction:

    input_data = {
        "Square_Feet": float(Square_Feet),
        "Num_Bedrooms": int(Num_Bedrooms),
        "Num_Bathrooms": int(Num_Bathrooms),
        "Num_Floors": int(Num_Floors),
        "Year_Built": int(Year_Built),
        "Has_Garden": int(Has_Garden),
        "Has_Pool": int(Has_Pool),
        "Garage_Size": int(Garage_Size),
        "Location_Score": float(Location_Score),
        "Distance_to_Center": float(Distance_to_Center)
    }

    try:
        response_post = requests.post(
            "http://api:8000/api/v1/predict/",
            json=input_data,
            timeout=15
        )

        response_post.raise_for_status()
        result = response_post.json()

        # Display the exact input selected by the user
        col1, col2 = st.columns(2)

        with col1:
            st.write(f"Square Feet: {input_data['Square_Feet']:,.2f}")
            st.write(f"Bedrooms: {input_data['Num_Bedrooms']}")
            st.write(f"Bathrooms: {input_data['Num_Bathrooms']}")
            st.write(f"Num Floors: {input_data['Num_Floors']}")
            st.write(f"Year Built: {input_data['Year_Built']}")

        with col2:
            st.write(f"Has Garden: {input_data['Has_Garden']}")
            st.write(f"Has Pool: {input_data['Has_Pool']}")
            st.write(f"Garage Size: {input_data['Garage_Size']}")
            st.write(f"Location Score: {input_data['Location_Score']:.2f}")
            st.write(
                f"Distance to Center: "
                f"{input_data['Distance_to_Center']:.3f}"
            )

        st.success(
            f"price prediction-> ${float(result['prediction']):,.2f}"
        )

    except requests.exceptions.RequestException as e:
        st.error(f"Prediction request failed: {e}")

    except (KeyError, ValueError, TypeError):
        st.error("Invalid response received from prediction API.")