import os
import subprocess
import sys
from pathlib import Path

def launch_minecraft(version):
    """启动Minecraft游戏"""
    try:
        # 获取可执行文件的路径
        if getattr(sys, 'frozen', False):
            # 打包后的环境 - 获取可执行文件所在目录
            executable_dir = Path(sys.executable).parent
        else:
            # 开发环境 - 获取脚本文件所在目录
            executable_dir = Path(__file__).parent.parent
        
        # 构造游戏可执行文件路径
        # 首先尝试在可执行文件同目录的game文件夹中查找
        game_exe_path = executable_dir / "game" / "mc1_8.exe"
        
        # 如果没有找到，尝试在可执行文件同目录中直接查找
        if not game_exe_path.exists():
            game_exe_path = executable_dir / "mc1_8.exe"
            
        # 如果还没有找到，尝试在上一级目录的game文件夹中查找（开发环境）
        if not game_exe_path.exists():
            game_exe_path = executable_dir.parent / "game" / "mc1_8.exe"
            
        # 如果还没有找到，尝试在dist目录中查找（开发环境）
        if not game_exe_path.exists():
            game_exe_path = executable_dir / "dist" / "game" / "mc1_8.exe"
            
        # 检查游戏文件是否存在
        if not game_exe_path.exists():
            return {
                "success": False, 
                "error": f"未找到游戏可执行文件: {game_exe_path}"
            }
        
        # 启动游戏并等待其结束
        launch_and_wait(game_exe_path)
        
        return {
            "success": True,
            "message": f"Minecraft {version} 启动成功"
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

def launch_and_wait(game_exe_path):
    """启动游戏并等待其结束"""
    try:
        # 启动游戏进程
        process = subprocess.Popen([str(game_exe_path)], cwd=game_exe_path.parent)
        
        # 等待游戏进程结束
        process.wait()
        
    except Exception as e:
        raise e

def get_minecraft_versions():
    """获取可用的Minecraft版本列表"""
    # 这里可以实现获取实际可用版本的逻辑
    # 目前返回固定的版本列表
    return ["1.8"]