#!/bin/bash

# INSERTAR VARIABLES (FUNCIONA)

# os.system(r'''sed -i '/int VENDOR_Init(void)/i int GetModelNumber(dm_req_t *req, char *buf, int len);\n' vendor.c''')
# sed -i '/int VENDOR_Init(void)/i int GetModelNumber(dm_req_t *req, char *buf, int len);\n' vendor.c

# INSERTAR FUNCIÓN (FUNCIONA)

# sed -i '/int VENDOR_Init(void)/{N;/{/{N;s/$/\tint CardUnlock = USP_REGISTER_DBParam_ReadWrite("Device.SmartLock.Features.CardUnlock", "MyModelNumber", NULL, NULL, DM_STRING);\n\tif (CardUnlock != USP_ERR_OK)\n\t{\n\t\treturn CardUnlock;\n\t}\n/}}' vendor.c

# CREAR FUNCIÓN

# FUNCIONA

# awk '/\/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\/\/\*\*/ {++count} count==2 && /\/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\/\/\*\*/ {print "int GetModelNumber(dm_req_t \*req, char *buf, int len)\n{\n\tstrncpy(buf, \"MyModelNumber\", len);\n\treturn USP_ERR_OK;\n}\n"} 1' vendor.c
# os.system(r'''awk '/\/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\/\/\*\*/ {++count} count==2 && /\/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\/\/\*\*/ {print "int GetModelNumber(dm_req_t *req, char *buf, int len)\n{\n\tstrncpy(buf, \"MyModelNumber\", len);\n\treturn USP_ERR_OK;\n}\n"} 1' vendor.c > tmp_vendor.c && mv tmp_vendor.c vendor.c''')
# find_line="\/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\/\/\*\*"
# os.system(r'''awk '/''' + find_line + r'''/ {++count} count==2 && /''' + find_line + r'''/ {print "int GetModelNumber(dm_req_t *req, char *buf, int len)\n{\n\tstrncpy(buf, \"MyModelNumber\", len);\n\treturn USP_ERR_OK;\n}\n"} 1' vendor.c > tmp_vendor.c && mv tmp_vendor.c vendor.c''')