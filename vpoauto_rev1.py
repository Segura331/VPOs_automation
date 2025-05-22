import pandas as pd
from xlsxwriter import workbook
 
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
            data_input = data_input.drop(workweek,site,quantity,eimslot,DECIMA_bucket,program_name,VF_1,VF_2,	VF_3,	VF_4,	VF_5,	VF_6,	RV1,	RV2,	RV3,	RV4,	RV5,DpmBucket	DpmBucket_RV	DpmBucketAccuracy	prod_requestid	rv_requestid	L2RV_Candidate	L2RVRULES	LV2 RV From KX	RV_Type	RUPS_WO,eqa_rv	device_name	qa_wo)
 
# Usage
create_excel_sheets('prueba1.xlsx', 'output.xlsx')