import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


@st.cache
def load_data():
    data = pd.read_csv('seattle-weather.csv')
    data['date'] = pd.to_datetime(data['date'])
    return data


def plot_distribution(data, column):
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.histplot(data[column], kde=True, ax=ax)
    ax.set_title(f'Distribution of {column}')
    ax.set_xlabel(column)
    ax.set_ylabel('Count')
    st.pyplot(fig)


def plot_pie_chart(data, column):
    fig, ax = plt.subplots(figsize=(8, 6))
    data[column].value_counts().plot.pie(autopct='%1.1f%%', ax=ax)
    ax.set_title(f'Pie Chart of {column}')
    st.pyplot(fig)


def plot_box_plot(data, column):
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.boxplot(x=data[column], ax=ax)
    ax.set_title(f'Box Plot of {column}')
    ax.set_xlabel(column)
    st.pyplot(fig)


def plot_line_chart(data, column):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(x='date', y=column, data=data, ax=ax)
    ax.set_title(f'Line Chart of {column} Over Time')
    ax.set_xlabel('Date')
    ax.set_ylabel(column)
    st.pyplot(fig)


def plot_bar_chart(data, column):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='weather', y=column, data=data, ax=ax)
    ax.set_title(f'Bar Chart of {column} by Weather')
    ax.set_xlabel('Weather')
    ax.set_ylabel(column)
    st.pyplot(fig)


def plot_scatter_plot(data, x_column, y_column):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x=x_column, y=y_column, hue='weather', data=data, ax=ax)
    ax.set_title(f'Scatter Plot of {x_column} vs {y_column}')
    ax.set_xlabel(x_column)
    ax.set_ylabel(y_column)
    st.pyplot(fig)


def main():
    st.title('Seattle Weather Data Visualization')
    st.write('This app visualizes the Seattle weather dataset.')

    data = load_data()

    st.sidebar.header('Options')


    if st.sidebar.checkbox('Show Dataset'):
        st.write(data)


    if st.sidebar.checkbox('Show Data Summary'):
        st.write(data.describe(include='all'))


    st.sidebar.write("""
    ## About the Dataset
    The dataset contains weather data from Seattle, including attributes such as date, precipitation, max and min temperatures, wind, and weather type. We'll explore various insights from this dataset using different visualization charts.
    """)


    visualization_type = st.sidebar.selectbox('Select Visualization Type', [
        'Distribution Plot', 'Pie Chart', 'Box Plot', 'Line Chart', 'Bar Chart', 'Scatter Plot'
    ])

    # Render selected visualization
    if visualization_type == 'Distribution Plot':
        selected_column = st.sidebar.selectbox('Select Column for Distribution Plot', data.columns)
        plot_distribution(data, selected_column)
    elif visualization_type == 'Pie Chart':
        categorical_columns = data.select_dtypes(include=['object', 'category']).columns
        selected_column = st.sidebar.selectbox('Select Column for Pie Chart', categorical_columns)
        plot_pie_chart(data, selected_column)
    elif visualization_type == 'Box Plot':
        selected_column = st.sidebar.selectbox('Select Column for Box Plot', data.columns)
        plot_box_plot(data, selected_column)
    elif visualization_type == 'Line Chart':
        selected_column = st.sidebar.selectbox('Select Column for Line Chart', data.columns)
        plot_line_chart(data, selected_column)
    elif visualization_type == 'Bar Chart':
        selected_column = st.sidebar.selectbox('Select Column for Bar Chart', data.columns)
        plot_bar_chart(data, selected_column)
    elif visualization_type == 'Scatter Plot':
        x_column = st.sidebar.selectbox('Select X Column for Scatter Plot', data.columns)
        y_column = st.sidebar.selectbox('Select Y Column for Scatter Plot', data.columns)
        plot_scatter_plot(data, x_column, y_column)


if __name__ == '__main__':
    main()
