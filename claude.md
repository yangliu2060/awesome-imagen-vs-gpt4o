# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 语言和任务管理

- 所有对话使用中文
- 所有任务记录写在 `todo.md` 文件中

## 项目概述

这是一个 **Google AI Studio vs GPT-4o 图像生成对比项目**，将原 [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images) 项目中的100个提示词案例，分别使用两个模型生成图像并进行对比。

## 项目结构

```
awesome-imagen-vs-gpt4o/
├── cases/{001..100}/     # 100个案例目录，存放生成的图像
├── data/
│   ├── prompts.json      # 核心数据：100个提示词的结构化数据
│   ├── original_readme.md
│   └── reference_images_needed.md
├── references/           # 参考图片存放目录
└── scripts/
    └── extract_prompts.py
```

## 常用命令

```bash
# 运行提示词提取脚本
python3 scripts/extract_prompts.py

# 查看提示词数据
cat data/prompts.json | python3 -m json.tool | head -100
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
3. 保存到对应的 `cases/{编号}/google.png`
4. 更新 README.md 中的对比展示
