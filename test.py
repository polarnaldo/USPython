import os

transformed_data_clean = "transformed_data_clean"
test = "test"

command = (r'''sed -i "/int VENDOR_Init(void)/{
    N;
    /{/{N;
        s/\$/\n\tint ''' + test + ''' = USP_REGISTER_DBParam_ReadWrite(\\"''' + transformed_data_clean + '''\\", \\"MyModelNumber\\", NULL, NULL, DM_STRING);\\n\\tif (''' + test + ''' != USP_ERR_OK)\\n\\t{\\n\\t\\treturn ''' + test + ''';\\n\\t}\\n/
    }
}" vendor.c''')

os.system(command)