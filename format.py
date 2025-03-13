#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import sys

def format_github_url(url):
    """
    格式化GitHub URL为指定的输出格式
    
    Args:
        url (str): GitHub仓库URL地址
        
    Returns:
        str: 格式化后的输出
    """
    # 移除可能的前缀（如@符号）
    url = url.lstrip('@')
    
    # 确保URL是GitHub仓库地址
    if not url.startswith('https://github.com/'):
        return f"错误: 不是有效的GitHub仓库地址: {url}"
    
    # 提取仓库地址 (username/repo)
    pattern = r'https://github.com/([^/]+/[^/]+)/?.*'
    match = re.match(pattern, url)
    
    if not match:
        return f"错误: 无法解析仓库地址: {url}"
    
    repo_path = match.group(1)
    
    # 移除URL末尾可能的斜杠
    url = url.rstrip('/')
    
    # 格式化输出
    formatted_output = f"[Code]({url})[![GitHub stars](https://img.shields.io/github/stars/{repo_path})]({url})"
    
    return formatted_output

def main():
    """主函数，处理命令行参数或用户输入"""
    if len(sys.argv) > 1:
        # 从命令行参数获取URL
        url = sys.argv[1]
    else:
        # 从用户输入获取URL
        url = "https://github.com/microsoft/opendatasheets-framework"
    
    formatted_output = format_github_url(url)
    print(formatted_output)

if __name__ == "__main__":
    main()
