# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 语言和任务管理

1 在项目根目录下我创建了一个 todo 文件，每次在开发之前，你都应该先将我们商量好的待办任务添加到这个文件中。每完成一个任务时，记得把对应的任务标记为已完成，这样可以方便我们实时跟踪开发进度。
2 合理使用 Task 工具创建多个子代理来提高开发的效率，每个子代理负责一个独立的任务，互不干扰，支持并行开发。
3 每次跟我沟通或者需要获得权限审批时使用中文.

## 项目概述

这是一个 **Google AI Studio vs GPT-4o 图像生成对比项目**，将原 [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images) 项目中的100个提示词案例，分别使用两个模型生成图像并进行对比。

## GitHub 仓库

https://github.com/yangliu2060/awesome-imagen-vs-gpt4o

## 项目结构

```
awesome-imagen-vs-gpt4o/
├── cases/{001..100}/     # 100个案例目录
│   ├── google.jpg        # Google AI Studio 生成的图片（已压缩）
│   └── gpt4o.png         # GPT-4o 原始图片
├── data/
│   ├── prompts.json      # 核心数据：100个提示词的结构化数据
│   ├── original_readme.md
│   └── reference_images_needed.md
├── references/           # 参考图片存放目录
├── scripts/
│   ├── extract_prompts.py
│   ├── batch_generate.py
│   └── test_api.py
└── README.md             # 展示页面，包含100个并排对比
```

## 常用命令

```bash
# 运行提示词提取脚本
python3 awesome-imagen-vs-gpt4o/scripts/extract_prompts.py

# 查看提示词数据
cat awesome-imagen-vs-gpt4o/data/prompts.json | python3 -m json.tool | head -100

# 压缩图片（使用 Pillow）
pip3 install Pillow
# 见 scripts/ 中的压缩脚本示例

# 推送到 GitHub
cd /Users/sky/Desktop/100个bananopro项目
git add awesome-imagen-vs-gpt4o/ && git commit -m "更新内容" && git push
```

## 数据结构

`data/prompts.json` 中每个案例包含：
- `id`: 案例编号 (1-100)
- `title`: 标题
- `author`: 原作者
- `prompt`: 提示词文本
- `needs_reference_image`: 是否需要参考图片
- `original_link`: 原文链接
- `generated`: 是否已生成
- `notes`: 备注

## 工作流程

1. 从 `data/prompts.json` 读取提示词
2. 在 Google AI Studio 中生成图像
3. 压缩图片并保存为 `cases/{编号}/google.jpg`（最大宽度1200px，JPEG质量85%）
4. 下载 GPT-4o 原图保存为 `cases/{编号}/gpt4o.png`
5. 更新 README.md 中的对比展示（并排表格格式，宽度400px）

## README 对比格式

```markdown
| GPT-4o | Google AI Studio |
|:------:|:----------------:|
| <img src="cases/001/gpt4o.png" width="400"> | <img src="cases/001/google.jpg" width="400"> |
```
