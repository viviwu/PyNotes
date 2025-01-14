import json

def struct_to_json(struct_str):
    """
    将结构体数组数据字符串转换为 JSON 字符串

    Args:
        struct_str: 结构体数组数据字符串

    Returns:
        JSON 字符串
    """

    # 定义替换规则，增加对布尔值和数组的支持
    replacements = [
        ('{"', '{"key": "'),
        ('u8"', '"name": "'),
        ('DtString', '"type": "string"'),  # 使用更通用的 "type" 字段
        ('DtInt64', '"type": "bigint"'),
        ('DtInt', '"type": "integer"'),
        ('DtDouble', '"type": "number"'),
        ('DtTime', '"type": "datetime"'),
        ('DtEnumString', '"type": "str_opt"'),
        ('DtEnum', '"type": "num_opt"'),
        ('DtNumBtn', '"type": "num_opt"'),
        ('DtPrivacy', '"type": "string"'),
        # (',', '", '),  # 在逗号后添加空格，提高可读性
        ('false', '"interact": "READ_ONLY"'),  # 处理布尔值
        ('true', '"interact": "READ_WRITE"'),
    ]

    # 处理数组
    # struct_str = struct_str.replace('[', '[{').replace(']', '}]')
    # print(struct_str)
    # 进行替换
    for old, new in replacements:
        struct_str = struct_str.replace(old, new)
    # print(struct_str)
    # 构造 JSON 对象
    json_data = json.loads(struct_str)  # 直接将字符串转换为 JSON 对象

    return json.dumps(json_data, indent=4)  # 格式化输出

# 示例用法
struct_str = '''[ 
{"username", u8"交易员ID", DtString, false},
    {"name", u8"交易员姓名", DtString, true},
    {"cust_code", u8"客户代码", DtString, true},
    {"auth_mac", u8"MAC地址", DtString, true},
    {"auth_ip", u8"IP地址", DtString, true},
    {"state", u8"用户状态", DtEnum, true},
    {"acc_count", u8"绑定账号数", DtNumBtn, false},
    {"update_time", u8"更新时间", DtTime, false},
    {"create_date", u8"创建时间", DtTime, false}, 
    {"password", u8"用户密码", DtPrivacy, false},
    {"id", u8"记录编号", DtInt, false},
    {"cust_id", u8"客户标记", DtInt, false},
    {"institution_id", u8"机构编号", DtString, false}
]'''
result = struct_to_json(struct_str)
print(result)