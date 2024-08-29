import sys
import time
# Include the path to the custom modules
sys.path.append('C:/Users/rajes/portfolio/projects/dataCut')
import streamlit as st
from extract import reading as rd
from extract import profiling as pf
from load import writing as wt




def main(config_path):
    """
    Main function to process data based on configuration file.
    
    Args:
        config_path (str): Path to the configuration CSV file.
    """
    try:
        # Read configuration CSV file
        config_df = rd.read_from_csv_file(config_path)

        for i in range(len(config_df) - 1):
            input_path = config_df.at[i, 'input_path']
            file_format = config_df.at[i, 'file_format']
            file_name = config_df.at[i, 'file_name']

            # Read data from the specified file
            df = rd.read_data_from_file(file_format, input_path)
            
            # Write data to the output path
            output_path = config_df.at[len(config_df) - 1, 'input_path']
            wt.write_to_csv(output_path, df, file_name)

            # Show success message for writing data
            display_success_message(f"{file_name} collection success")

            # Profile the dataframe and write the profiling data
            df_prof = pf.profile_dataframe(df)
            output_prof_path = output_path.replace("/datafiles", "/profiling")
            wt.write_to_csv(output_prof_path, df_prof, file_name + "_prof")

            # Show success message for profiling
            display_success_message(f"{file_name}_prof profiling success")
            
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")


def display_success_message(message):
    """
    Display a success message with fade-in and fade-out effect.
    
    Args:
        message (str): Message to display.
    """
    # HTML and CSS for fade-in and fade-out effect
    st.markdown(f"""
        <style>
            .fade-in {{
                animation: fadeIn 2s ease-in-out;
                -webkit-animation: fadeIn 2s ease-in-out;
                -moz-animation: fadeIn 2s ease-in-out;
                -o-animation: fadeIn 2s ease-in-out;
                -ms-animation: fadeIn 2s ease-in-out;
            }}
            @keyframes fadeIn {{
                0% {{ opacity: 0; }}
                100% {{ opacity: 1; }}
            }}
        </style>
        <div class="fade-in">
            <p style="color:green; font-size:20px;">&#10004; {message}</p>
        </div>
    """, unsafe_allow_html=True)

    # Wait for some time to simulate fade-out effect
    time.sleep(2)
    st.markdown(f"""
        <style>
            .fade-out {{
                animation: fadeOut 2s ease-in-out;
                -webkit-animation: fadeOut 2s ease-in-out;
                -moz-animation: fadeOut 2s ease-in-out;
                -o-animation: fadeOut 2s ease-in-out;
                -ms-animation: fadeOut 2s ease-in-out;
            }}
            @keyframes fadeOut {{
                0% {{ opacity: 1; }}
                100% {{ opacity: 0; }}
            }}
        </style>
        <div class="fade-out">
            <p style="color:green; font-size:20px;">&#10004; {message}</p>
        </div>
    """, unsafe_allow_html=True)




# Streamlit UI for file upload
config_path = st.file_uploader("Choose config file", type="csv")
if config_path is not None:
    main(config_path)
