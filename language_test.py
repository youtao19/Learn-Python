import google.generativeai as genai

# 设置 API 密钥
api_key = "AIzaSyBnPjFNuRtZQqHFFRYolx_jXoXdRvgWDQo"
genai.configure(api_key=api_key)

# 选择模型
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# 生成文本
text = input("请输入文本：")
prompt = text
response = model.generate_content(prompt)  # 注意这里使用 generate_text

# 打印结果
print(response.text)