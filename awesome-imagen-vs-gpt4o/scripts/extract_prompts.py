#!/usr/bin/env python3
"""
从 awesome-gpt4o-images 项目提取提示词数据
"""

import json
import re
import os

# 原始 README 内容会从 GitHub 获取
# 这里我们直接定义提取的数据结构

def extract_cases_from_readme(readme_content):
    """从 README 内容中提取案例数据"""
    cases = []

    # 匹配案例模式
    # 格式: ### 案例 X：标题 (by @author)
    case_pattern = r'<a id="cases-(\d+)"></a>\s*### 案例 \d+：(.+?) \(by \[?@?([^\])\n]+)'

    # 查找所有案例
    matches = list(re.finditer(case_pattern, readme_content))

    for i, match in enumerate(matches):
        case_num = int(match.group(1))
        title = match.group(2).strip()
        author = match.group(3).strip()

        # 获取案例内容区域
        start_pos = match.end()
        if i + 1 < len(matches):
            end_pos = matches[i + 1].start()
        else:
            end_pos = len(readme_content)

        case_content = readme_content[start_pos:end_pos]

        # 提取提示词
        prompt = extract_prompt(case_content)

        # 检查是否需要参考图片
        needs_reference = "需上传参考图片" in case_content or "上传" in case_content

        # 提取原文链接
        link_match = re.search(r'\[原文链接\]\((https?://[^\)]+)\)', case_content)
        original_link = link_match.group(1) if link_match else ""

        cases.append({
            "id": case_num,
            "title": title,
            "author": author,
            "prompt": prompt,
            "needs_reference_image": needs_reference,
            "original_link": original_link,
            "generated": False,
            "notes": ""
        })

    return sorted(cases, key=lambda x: x["id"])


def extract_prompt(content):
    """从案例内容中提取提示词"""
    # 查找 ```code block``` 中的提示词
    code_match = re.search(r'\*\*提示词\*\*\s*```[^\n]*\n([\s\S]*?)```', content)
    if code_match:
        return code_match.group(1).strip()

    # 备用：查找提示词段落
    prompt_match = re.search(r'\*\*提示词[：:]\*\*\s*\n+([\s\S]*?)(?=\n\*\*|$)', content)
    if prompt_match:
        return prompt_match.group(1).strip()

    return ""


def main():
    # 读取 README 文件（假设已下载到本地）
    readme_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'original_readme.md')

    if not os.path.exists(readme_path):
        print(f"请先将原项目 README.md 下载到: {readme_path}")
        print("可以运行: curl -o data/original_readme.md https://raw.githubusercontent.com/jamez-bondos/awesome-gpt4o-images/main/README.md")
        return

    with open(readme_path, 'r', encoding='utf-8') as f:
        readme_content = f.read()

    # 提取案例
    cases = extract_cases_from_readme(readme_content)

    # 保存为 JSON
    output_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'prompts.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(cases, f, ensure_ascii=False, indent=2)

    print(f"成功提取 {len(cases)} 个案例")
    print(f"数据已保存到: {output_path}")

    # 统计需要参考图片的案例
    ref_count = sum(1 for c in cases if c["needs_reference_image"])
    print(f"需要参考图片的案例: {ref_count} 个")

    # 输出简要列表
    print("\n案例列表:")
    for case in cases:
        ref_mark = "📷" if case["needs_reference_image"] else "  "
        print(f"  {ref_mark} {case['id']:3d}. {case['title']}")


if __name__ == "__main__":
    main()
