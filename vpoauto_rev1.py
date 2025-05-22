import pandas as pd

 
def create_excel_sheets(input_file, output_file):
    # Read the Excel file into a DataFrame
    data_input = pd.read_excel(input_file)
   
    # Get unique product configuration names
    product_configurations = data_input['product_configuration_name'].unique()
   
    # Create a Pandas Excel writer using XlsxWriter as the engine
    with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
        # Iterate over each unique product configuration name
        for config_name in product_configurations:
            # Filter the DataFrame for the current product configuration name
            filtered_data = data_input[
                (data_input['product_configuration_name'] == config_name) &
                (data_input['my_bucket'] == 'RV')
            ]
           
            # Write the filtered data to a new sheet named after the product configuration name
            filtered_data.to_excel(writer, sheet_name=config_name, index=False)
 
# Usage
create_excel_sheets('prueba1.xlsx', 'output.xlsx')