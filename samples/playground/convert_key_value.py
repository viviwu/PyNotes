import json

def convert_json(data):
  """
  将JSON字符串中的键值对进行转换。

  Args:
    data: 要转换的JSON字符串。

  Returns:
    转换后的JSON字符串。
  """

  # 将字符串转换为字典
  data_dict = json.loads(data)

  # 创建一个新的字典来存储转换后的键值对
  new_dict = {}
  for key, value in data_dict.items():
    new_dict[str(value)] = key

  # 将转换后的字典转换为JSON字符串
  new_json = json.dumps(new_dict, ensure_ascii=False)  # 防止中文乱码

  return new_json

# 示例用法
original_json = '''
 {
      "未报": 0,
      "待报": 1,
      "已报": 2,
      "已报待撤": 3,
      "部成待撤": 4,
      "部分撤单": 5,
      "全部撤单": 6,
      "部分成交": 7,
      "全部成交": 8,
      "废单": 9,
      "其他": 65535
    }
'''
new_json = convert_json(original_json)
print(new_json)  # 输出结果：{"1": "普通买入", "2": "普通卖出"}