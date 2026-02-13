#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 由BAT转Python工具自动生成
# 原文件：F:/Users/LemonXC/Desktop/适用于Rindows的脚本应用/Rindows安全应用市场 V2.0.bat
import subprocess
import os
import sys

# 设置当前工作目录为脚本所在目录（模拟BAT的默认行为）
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def main():
    try:
    # 执行原BAT命令：@echo off
result = subprocess.run(r'@echo off', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
result = subprocess.run(r'>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if '%errorlevel%' NEQ '0' (
result = subprocess.run(r'if '%errorlevel%' NEQ '0' (', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    print("Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"")
    print("UAC.ShellExecute "%~s0", "", "", "runas", 1 >> "%temp%\getadmin.vbs"")
    # 执行原BAT命令："%temp%\getadmin.vbs"
result = subprocess.run(r'"%temp%\getadmin.vbs"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：exit /B
result = subprocess.run(r'exit /B', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：)
result = subprocess.run(r')', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if exist "%temp%\getadmin.vbs" (del "%temp%\getadmin.vbs")
result = subprocess.run(r'if exist "%temp%\getadmin.vbs" (del "%temp%\getadmin.vbs")', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：mode con cols=46 lines=30
result = subprocess.run(r'mode con cols=46 lines=30', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：chcp 65001 > nul 2>&1  :: 解决中文乱码问题
result = subprocess.run(r'chcp 65001 > nul 2>&1  :: 解决中文乱码问题', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：color 2F
result = subprocess.run(r'color 2F', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：title Rindows安全应用市场 V2.0 - 下载目录：%USERPROFILE%\Desktop\Rindows安全应用市场下载
result = subprocess.run(r'title Rindows安全应用市场 V2.0 - 下载目录：%USERPROFILE%\Desktop\Rindows安全应用市场下载', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：set "DOWNLOAD_DIR=%USERPROFILE%\Desktop\Rindows安全应用市场下载"
result = subprocess.run(r'set "DOWNLOAD_DIR=%USERPROFILE%\Desktop\Rindows安全应用市场下载"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # :: 自动创建下载目录
    # 执行原BAT命令：if not exist "%DOWNLOAD_DIR%" (
result = subprocess.run(r'if not exist "%DOWNLOAD_DIR%" (', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：md "%DOWNLOAD_DIR%" > nul 2>&1
result = subprocess.run(r'md "%DOWNLOAD_DIR%" > nul 2>&1', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    print("已创建下载目录：%DOWNLOAD_DIR%")
    print(".")
    # 执行原BAT命令：)
result = subprocess.run(r')', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # :: 主菜单函数
    # 执行原BAT命令：:MAIN_MENU
result = subprocess.run(r':MAIN_MENU', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：cls
result = subprocess.run(r'cls', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    print("==============================================")
    print("Rindows安全应用市场 V2.0")
    print("（60+应用，官方安全）")
    print("==============================================")
    print("【1】办公软件（WPS、LibreOffice、思维导图等）")
    print("【2】开发工具（VS Code、Git、Python、Node.js等）")
    print("【3】影音工具（PotPlayer、VLC、格式工厂、剪映等）")
    print("【4】系统工具（7-Zip、Everything、鲁大师、驱动精灵等）")
    print("【5】浏览器工具（Chrome、Edge、Firefox、360浏览器等）")
    print("【6】设计创作（PS便携版、Figma客户端、Snipaste等）")
    print("【7】安全防护（火绒、360安全卫士、腾讯电脑管家等）")
    print("【0】退出应用市场")
    print("==============================================")
    # 执行原BAT命令：set /p "CHOICE=请输入您要选择的分类编号："
result = subprocess.run(r'set /p "CHOICE=请输入您要选择的分类编号："', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%CHOICE%"=="1" goto OFFICE_MENU
result = subprocess.run(r'if "%CHOICE%"=="1" goto OFFICE_MENU', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%CHOICE%"=="2" goto DEV_MENU
result = subprocess.run(r'if "%CHOICE%"=="2" goto DEV_MENU', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%CHOICE%"=="3" goto MEDIA_MENU
result = subprocess.run(r'if "%CHOICE%"=="3" goto MEDIA_MENU', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%CHOICE%"=="4" goto SYS_MENU
result = subprocess.run(r'if "%CHOICE%"=="4" goto SYS_MENU', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%CHOICE%"=="5" goto BROWSER_MENU
result = subprocess.run(r'if "%CHOICE%"=="5" goto BROWSER_MENU', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%CHOICE%"=="6" goto DESIGN_MENU
result = subprocess.run(r'if "%CHOICE%"=="6" goto DESIGN_MENU', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%CHOICE%"=="7" goto SECURITY_MENU
result = subprocess.run(r'if "%CHOICE%"=="7" goto SECURITY_MENU', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%CHOICE%"=="0" goto EXIT_APP
result = subprocess.run(r'if "%CHOICE%"=="0" goto EXIT_APP', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # :: 输入错误处理
    print(".")
    print("！输入错误，请输入0-7之间的有效编号！")
    # 执行原BAT命令：pause > nul
result = subprocess.run(r'pause > nul', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：goto MAIN_MENU
result = subprocess.run(r'goto MAIN_MENU', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # :: ---------------------- 分类1：办公软件菜单（12款） ----------------------
    # 执行原BAT命令：:OFFICE_MENU
result = subprocess.run(r':OFFICE_MENU', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：cls
result = subprocess.run(r'cls', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    print("==============================================")
    print("办公软件分类（12款）")
    print("==============================================")
    print("【1】WPS Office 官方安装版（Windows）")
    print("【2】LibreOffice 免费开源办公套件")
    print("【3】XMind 思维导图便携版")
    print("【4】印象笔记 客户端")
    print("【5】PDF-XChange Editor（PDF编辑）")
    print("【6】金山文档 桌面客户端")
    print("【7】永中Office 免费办公套件")
    print("【8】MindMaster 思维导图免费版")
    print("【9】福昕PDF 阅读器")
    print("【10】OneNote 微软笔记工具")
    print("【11】WPS 表格独立便携版")
    print("【12】有道云笔记 客户端")
    print("【0】返回主菜单")
    print("==============================================")
    # 执行原BAT命令：set /p "SOFT_CHOICE=请输入要下载的软件编号："
result = subprocess.run(r'set /p "SOFT_CHOICE=请输入要下载的软件编号："', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="1" call :DOWNLOAD_SOFT "WPS Office" "https://official-package.wpscdn.cn/wps/download/WPS_Setup_24657.exe"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="1" call :DOWNLOAD_SOFT "WPS Office" "https://official-package.wpscdn.cn/wps/download/WPS_Setup_24657.exe"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="2" call :DOWNLOAD_SOFT "LibreOffice" "https://download.documentfoundation.org/libreoffice/stable/7.6.4/win/x86_64/LibreOffice_7.6.4_Win_x64.msi"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="2" call :DOWNLOAD_SOFT "LibreOffice" "https://download.documentfoundation.org/libreoffice/stable/7.6.4/win/x86_64/LibreOffice_7.6.4_Win_x64.msi"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="3" call :DOWNLOAD_SOFT "XMind便携版" "https://dl.xmind.cn/XMind-ZEN-2023-for-Windows.zip"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="3" call :DOWNLOAD_SOFT "XMind便携版" "https://dl.xmind.cn/XMind-ZEN-2023-for-Windows.zip"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="4" call :DOWNLOAD_SOFT "印象笔记" "https://cdn.yinxiang.com/dist/public/ENWinLatest.exe"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="4" call :DOWNLOAD_SOFT "印象笔记" "https://cdn.yinxiang.com/dist/public/ENWinLatest.exe"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="5" call :DOWNLOAD_SOFT "PDF-XChange Editor" "https://downloads.tracker-software.com/product/pdfxe/10/PDFXEdit10.zip"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="5" call :DOWNLOAD_SOFT "PDF-XChange Editor" "https://downloads.tracker-software.com/product/pdfxe/10/PDFXEdit10.zip"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="6" call :DOWNLOAD_SOFT "金山文档" "https://kdocs.cn/desktop/download/KDocsDesktop.exe"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="6" call :DOWNLOAD_SOFT "金山文档" "https://kdocs.cn/desktop/download/KDocsDesktop.exe"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="7" call :DOWNLOAD_SOFT "永中Office" "https://www.yozosoft.com/downloads/yozoffice2021.exe"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="7" call :DOWNLOAD_SOFT "永中Office" "https://www.yozosoft.com/downloads/yozoffice2021.exe"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="8" call :DOWNLOAD_SOFT "MindMaster" "https://www.edrawsoft.com/download/mindmaster/mindmaster_cn.exe"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="8" call :DOWNLOAD_SOFT "MindMaster" "https://www.edrawsoft.com/download/mindmaster/mindmaster_cn.exe"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="9" call :DOWNLOAD_SOFT "福昕PDF阅读器" "https://www.foxitsoftware.com.cn/downloads/foxit-reader.php"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="9" call :DOWNLOAD_SOFT "福昕PDF阅读器" "https://www.foxitsoftware.com.cn/downloads/foxit-reader.php"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="10" call :DOWNLOAD_SOFT "OneNote" "https://go.microsoft.com/fwlink/?LinkId=2082575"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="10" call :DOWNLOAD_SOFT "OneNote" "https://go.microsoft.com/fwlink/?LinkId=2082575"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="11" call :DOWNLOAD_SOFT "WPS表格便携版" "https://wdl.cache.wps.cn/wps/download/ep/Portable/WPSTable_Portable.zip"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="11" call :DOWNLOAD_SOFT "WPS表格便携版" "https://wdl.cache.wps.cn/wps/download/ep/Portable/WPSTable_Portable.zip"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="12" call :DOWNLOAD_SOFT "有道云笔记" "https://note.youdao.com/download/YoudaoNote.exe"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="12" call :DOWNLOAD_SOFT "有道云笔记" "https://note.youdao.com/download/YoudaoNote.exe"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="0" goto MAIN_MENU
result = subprocess.run(r'if "%SOFT_CHOICE%"=="0" goto MAIN_MENU', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    print(".")
    print("！输入错误，请输入0-12之间的有效编号！")
    # 执行原BAT命令：pause > nul
result = subprocess.run(r'pause > nul', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：goto OFFICE_MENU
result = subprocess.run(r'goto OFFICE_MENU', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # :: ---------------------- 分类2：开发工具菜单（15款） ----------------------
    # 执行原BAT命令：:DEV_MENU
result = subprocess.run(r':DEV_MENU', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：cls
result = subprocess.run(r'cls', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    print("==============================================")
    print("开发工具分类（15款）")
    print("==============================================")
    print("【1】VS Code 官方最新版")
    print("【2】Git for Windows")
    print("【3】Python 3.12.1（64位）")
    print("【4】Node.js 20.10.0（64位）")
    print("【5】Postman 便携版")
    print("【6】Docker Desktop（Windows）")
    print("【7】Notepad++ 最新版")
    print("【8】PyCharm Community 2023.3")
    print("【9】MySQL Installer 8.0.36")
    print("【10】Redis Desktop Manager")
    print("【11】Sublime Text 4")
    print("【12】IntelliJ IDEA Community 2023.3")
    print("【13】GitKraken 便携版")
    print("【14】PostgreSQL 16.1")
    print("【15】VS 2022 Build Tools")
    print("【0】返回主菜单")
    print("==============================================")
    # 执行原BAT命令：set /p "SOFT_CHOICE=请输入要下载的软件编号："
result = subprocess.run(r'set /p "SOFT_CHOICE=请输入要下载的软件编号："', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="1" call :DOWNLOAD_SOFT "VS Code" "https://update.code.visualstudio.com/latest/win32-x64-user/stable"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="1" call :DOWNLOAD_SOFT "VS Code" "https://update.code.visualstudio.com/latest/win32-x64-user/stable"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="2" call :DOWNLOAD_SOFT "Git for Windows" "https://github.com/git-for-windows/git/releases/download/v2.43.0/Git-2.43.0-64-bit.exe"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="2" call :DOWNLOAD_SOFT "Git for Windows" "https://github.com/git-for-windows/git/releases/download/v2.43.0/Git-2.43.0-64-bit.exe"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="3" call :DOWNLOAD_SOFT "Python 3.12.1" "https://www.python.org/ftp/python/3.12.1/python-3.12.1-amd64.exe"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="3" call :DOWNLOAD_SOFT "Python 3.12.1" "https://www.python.org/ftp/python/3.12.1/python-3.12.1-amd64.exe"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="4" call :DOWNLOAD_SOFT "Node.js 20.10.0" "https://nodejs.org/dist/v20.10.0/node-v20.10.0-x64.msi"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="4" call :DOWNLOAD_SOFT "Node.js 20.10.0" "https://nodejs.org/dist/v20.10.0/node-v20.10.0-x64.msi"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="5" call :DOWNLOAD_SOFT "Postman便携版" "https://dl.pstmn.io/download/latest/win64"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="5" call :DOWNLOAD_SOFT "Postman便携版" "https://dl.pstmn.io/download/latest/win64"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="6" call :DOWNLOAD_SOFT "Docker Desktop" "https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="6" call :DOWNLOAD_SOFT "Docker Desktop" "https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="7" call :DOWNLOAD_SOFT "Notepad++" "https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v8.5.8/npp.8.5.8.Installer.exe"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="7" call :DOWNLOAD_SOFT "Notepad++" "https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v8.5.8/npp.8.5.8.Installer.exe"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="8" call :DOWNLOAD_SOFT "PyCharm Community" "https://download.jetbrains.com/python/pycharm-community-2023.3.2.exe"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="8" call :DOWNLOAD_SOFT "PyCharm Community" "https://download.jetbrains.com/python/pycharm-community-2023.3.2.exe"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="9" call :DOWNLOAD_SOFT "MySQL Installer" "https://dev.mysql.com/get/Downloads/MySQLInstaller/mysql-installer-community-8.0.36.0.msi"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="9" call :DOWNLOAD_SOFT "MySQL Installer" "https://dev.mysql.com/get/Downloads/MySQLInstaller/mysql-installer-community-8.0.36.0.msi"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="10" call :DOWNLOAD_SOFT "Redis Desktop Manager" "https://github.com/uglide/RedisDesktopManager/releases/download/2022.5/rdm-2022.5-windows.exe"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="10" call :DOWNLOAD_SOFT "Redis Desktop Manager" "https://github.com/uglide/RedisDesktopManager/releases/download/2022.5/rdm-2022.5-windows.exe"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="11" call :DOWNLOAD_SOFT "Sublime Text 4" "https://download.sublimetext.com/Sublime%20Text%20Build%204169%20x64%20Setup.exe"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="11" call :DOWNLOAD_SOFT "Sublime Text 4" "https://download.sublimetext.com/Sublime%20Text%20Build%204169%20x64%20Setup.exe"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="12" call :DOWNLOAD_SOFT "IntelliJ IDEA Community" "https://download.jetbrains.com/idea/ideaIC-2023.3.2.exe"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="12" call :DOWNLOAD_SOFT "IntelliJ IDEA Community" "https://download.jetbrains.com/idea/ideaIC-2023.3.2.exe"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="13" call :DOWNLOAD_SOFT "GitKraken" "https://release.gitkraken.com/win/GitKrakenSetup.exe"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="13" call :DOWNLOAD_SOFT "GitKraken" "https://release.gitkraken.com/win/GitKrakenSetup.exe"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="14" call :DOWNLOAD_SOFT "PostgreSQL 16.1" "https://get.enterprisedb.com/postgresql/postgresql-16.1-1-windows-x64.exe"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="14" call :DOWNLOAD_SOFT "PostgreSQL 16.1" "https://get.enterprisedb.com/postgresql/postgresql-16.1-1-windows-x64.exe"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="15" call :DOWNLOAD_SOFT "VS 2022 Build Tools" "https://aka.ms/vs/17/release/vs_buildtools.exe"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="15" call :DOWNLOAD_SOFT "VS 2022 Build Tools" "https://aka.ms/vs/17/release/vs_buildtools.exe"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="0" goto MAIN_MENU
result = subprocess.run(r'if "%SOFT_CHOICE%"=="0" goto MAIN_MENU', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    print(".")
    print("！输入错误，请输入0-15之间的有效编号！")
    # 执行原BAT命令：pause > nul
result = subprocess.run(r'pause > nul', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：goto DEV_MENU
result = subprocess.run(r'goto DEV_MENU', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # :: ---------------------- 分类3：影音工具菜单（10款） ----------------------
    # 执行原BAT命令：:MEDIA_MENU
result = subprocess.run(r':MEDIA_MENU', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：cls
result = subprocess.run(r'cls', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    print("==============================================")
    print("影音工具分类（10款）")
    print("==============================================")
    print("【1】PotPlayer 官方版")
    print("【2】VLC 媒体播放器")
    print("【3】格式工厂 免费版")
    print("【4】ScreenToGif（录屏/动图）")
    print("【5】剪映 桌面端")
    print("【6】QQ影音 纯净版")
    print("【7】迅雷 极速版")
    print("【8】网易云音乐 客户端")
    print("【9】爱奇艺 桌面客户端")
    print("【10】Adobe Premiere Rush 免费版")
    print("【0】返回主菜单")
    print("==============================================")
    # 执行原BAT命令：set /p "SOFT_CHOICE=请输入要下载的软件编号："
result = subprocess.run(r'set /p "SOFT_CHOICE=请输入要下载的软件编号："', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="1" call :DOWNLOAD_SOFT "PotPlayer" "https://download1.videohelp.com/PotPlayer/PotPlayerSetup.exe"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="1" call :DOWNLOAD_SOFT "PotPlayer" "https://download1.videohelp.com/PotPlayer/PotPlayerSetup.exe"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="2" call :DOWNLOAD_SOFT "VLC 媒体播放器" "https://get.videolan.org/vlc/3.0.20/win64/vlc-3.0.20-win64.exe"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="2" call :DOWNLOAD_SOFT "VLC 媒体播放器" "https://get.videolan.org/vlc/3.0.20/win64/vlc-3.0.20-win64.exe"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="3" call :DOWNLOAD_SOFT "格式工厂" "https://www.pcfreetime.com/FFSetup5.15.0.exe"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="3" call :DOWNLOAD_SOFT "格式工厂" "https://www.pcfreetime.com/FFSetup5.15.0.exe"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="4" call :DOWNLOAD_SOFT "ScreenToGif" "https://github.com/NickeManarin/ScreenToGif/releases/download/2.39.1/ScreenToGif.2.39.1.Setup.exe"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="4" call :DOWNLOAD_SOFT "ScreenToGif" "https://github.com/NickeManarin/ScreenToGif/releases/download/2.39.1/ScreenToGif.2.39.1.Setup.exe"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="5" call :DOWNLOAD_SOFT "剪映桌面端" "https://www.capcut.cn/desktop/download"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="5" call :DOWNLOAD_SOFT "剪映桌面端" "https://www.capcut.cn/desktop/download"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="6" call :DOWNLOAD_SOFT "QQ影音纯净版" "https://player.qq.com/download/QQPlayer_Setup_3.9.936.0.exe"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="6" call :DOWNLOAD_SOFT "QQ影音纯净版" "https://player.qq.com/download/QQPlayer_Setup_3.9.936.0.exe"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="7" call :DOWNLOAD_SOFT "迅雷极速版" "https://down.sandai.net/thunder9/Thunder9.1.66.928.exe"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="7" call :DOWNLOAD_SOFT "迅雷极速版" "https://down.sandai.net/thunder9/Thunder9.1.66.928.exe"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="8" call :DOWNLOAD_SOFT "网易云音乐" "https://music.163.com/#/download"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="8" call :DOWNLOAD_SOFT "网易云音乐" "https://music.163.com/#/download"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="9" call :DOWNLOAD_SOFT "爱奇艺客户端" "https://www.iqiyi.com/common/download.html"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="9" call :DOWNLOAD_SOFT "爱奇艺客户端" "https://www.iqiyi.com/common/download.html"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="10" call :DOWNLOAD_SOFT "Adobe Premiere Rush" "https://creative.adobe.com/products/download/premiere-rush"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="10" call :DOWNLOAD_SOFT "Adobe Premiere Rush" "https://creative.adobe.com/products/download/premiere-rush"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="0" goto MAIN_MENU
result = subprocess.run(r'if "%SOFT_CHOICE%"=="0" goto MAIN_MENU', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    print(".")
    print("！输入错误，请输入0-10之间的有效编号！")
    # 执行原BAT命令：pause > nul
result = subprocess.run(r'pause > nul', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：goto MEDIA_MENU
result = subprocess.run(r'goto MEDIA_MENU', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # :: ---------------------- 分类4：系统工具菜单（12款） ----------------------
    # 执行原BAT命令：:SYS_MENU
result = subprocess.run(r':SYS_MENU', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：cls
result = subprocess.run(r'cls', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    print("==============================================")
    print("系统工具分类（12款）")
    print("==============================================")
    print("【1】7-Zip 压缩工具（64位）")
    print("【2】Everything 文件搜索工具")
    print("【3】CCleaner 系统清理工具")
    print("【4】Bandizip 免费压缩工具")
    print("【5】TreeSize Free（磁盘分析）")
    print("【6】驱动精灵 万能版")
    print("【7】鲁大师 硬件检测")
    print("【8】火绒剑 系统分析工具")
    print("【9】UltraISO 软碟通")
    print("【10】TeamViewer 远程控制")
    print("【11】傲梅分区助手 免费版")
    print("【12】Windows优化大师 经典版")
    print("【0】返回主菜单")
    print("==============================================")
    # 执行原BAT命令：set /p "SOFT_CHOICE=请输入要下载的软件编号："
result = subprocess.run(r'set /p "SOFT_CHOICE=请输入要下载的软件编号："', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="1" call :DOWNLOAD_SOFT "7-Zip" "https://www.7-zip.org/a/7z2301-x64.msi"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="1" call :DOWNLOAD_SOFT "7-Zip" "https://www.7-zip.org/a/7z2301-x64.msi"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="2" call :DOWNLOAD_SOFT "Everything" "https://www.voidtools.com/Everything-1.4.1.1022.x64.msi"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="2" call :DOWNLOAD_SOFT "Everything" "https://www.voidtools.com/Everything-1.4.1.1022.x64.msi"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="3" call :DOWNLOAD_SOFT "CCleaner" "https://download.ccleaner.com/ccsetup599.exe"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="3" call :DOWNLOAD_SOFT "CCleaner" "https://download.ccleaner.com/ccsetup599.exe"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="4" call :DOWNLOAD_SOFT "Bandizip" "https://dl.bandisoft.com/bandizip/bdzsetup.exe"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="4" call :DOWNLOAD_SOFT "Bandizip" "https://dl.bandisoft.com/bandizip/bdzsetup.exe"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="5" call :DOWNLOAD_SOFT "TreeSize Free" "https://downloads.jam-software.com/treesize_free/TreeSizeFreeSetup.exe"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="5" call :DOWNLOAD_SOFT "TreeSize Free" "https://downloads.jam-software.com/treesize_free/TreeSizeFreeSetup.exe"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="6" call :DOWNLOAD_SOFT "驱动精灵" "https://file.mydrivers.com/DGSetup_v9.61.3708.3002.exe"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="6" call :DOWNLOAD_SOFT "驱动精灵" "https://file.mydrivers.com/DGSetup_v9.61.3708.3002.exe"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="7" call :DOWNLOAD_SOFT "鲁大师" "https://cdn.ludashi.com/ludashi/ludashi_setup.zip"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="7" call :DOWNLOAD_SOFT "鲁大师" "https://cdn.ludashi.com/ludashi/ludashi_setup.zip"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="8" call :DOWNLOAD_SOFT "火绒剑" "https://www.huorong.cn/download/hrj_tool.zip"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="8" call :DOWNLOAD_SOFT "火绒剑" "https://www.huorong.cn/download/hrj_tool.zip"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="9" call :DOWNLOAD_SOFT "UltraISO软碟通" "https://www.ultraiso.com/xiazaizhongxin.html"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="9" call :DOWNLOAD_SOFT "UltraISO软碟通" "https://www.ultraiso.com/xiazaizhongxin.html"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="10" call :DOWNLOAD_SOFT "TeamViewer" "https://download.teamviewer.com/download/TeamViewer_Setup.exe"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="10" call :DOWNLOAD_SOFT "TeamViewer" "https://download.teamviewer.com/download/TeamViewer_Setup.exe"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="11" call :DOWNLOAD_SOFT "傲梅分区助手" "https://www.disktool.cn/download.html"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="11" call :DOWNLOAD_SOFT "傲梅分区助手" "https://www.disktool.cn/download.html"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="12" call :DOWNLOAD_SOFT "Windows优化大师" "https://www.youhua.cn/downloads/youhuadasheng.exe"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="12" call :DOWNLOAD_SOFT "Windows优化大师" "https://www.youhua.cn/downloads/youhuadasheng.exe"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="0" goto MAIN_MENU
result = subprocess.run(r'if "%SOFT_CHOICE%"=="0" goto MAIN_MENU', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    print(".")
    print("！输入错误，请输入0-12之间的有效编号！")
    # 执行原BAT命令：pause > nul
result = subprocess.run(r'pause > nul', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：goto SYS_MENU
result = subprocess.run(r'goto SYS_MENU', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # :: ---------------------- 新增分类5：浏览器工具菜单（8款） ----------------------
    # 执行原BAT命令：:BROWSER_MENU
result = subprocess.run(r':BROWSER_MENU', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：cls
result = subprocess.run(r'cls', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    print("==============================================")
    print("浏览器工具分类（8款）")
    print("==============================================")
    print("【1】Google Chrome 官方版")
    print("【2】Microsoft Edge 最新版")
    print("【3】360安全浏览器 纯净版")
    print("【4】Mozilla Firefox 火狐")
    print("【5】搜狗浏览器 高速版")
    print("【6】QQ浏览器 纯净版")
    print("【7】Brave 隐私安全浏览器")
    print("【8】Opera 欧朋浏览器")
    print("【0】返回主菜单")
    print("==============================================")
    # 执行原BAT命令：set /p "SOFT_CHOICE=请输入要下载的软件编号："
result = subprocess.run(r'set /p "SOFT_CHOICE=请输入要下载的软件编号："', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="1" call :DOWNLOAD_SOFT "Google Chrome" "https://dl.google.com/chrome/install/standalone/ChromeStandaloneSetup64.exe"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="1" call :DOWNLOAD_SOFT "Google Chrome" "https://dl.google.com/chrome/install/standalone/ChromeStandaloneSetup64.exe"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="2" call :DOWNLOAD_SOFT "Microsoft Edge" "https://go.microsoft.com/fwlink/?linkid=2171382"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="2" call :DOWNLOAD_SOFT "Microsoft Edge" "https://go.microsoft.com/fwlink/?linkid=2171382"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="3" call :DOWNLOAD_SOFT "360安全浏览器" "https://dl.360safe.com/se/360se13.1.6220.0.exe"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="3" call :DOWNLOAD_SOFT "360安全浏览器" "https://dl.360safe.com/se/360se13.1.6220.0.exe"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="4" call :DOWNLOAD_SOFT "Mozilla Firefox" "https://download.mozilla.org/?product=firefox-latest&os=win64&lang=zh-CN"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="4" call :DOWNLOAD_SOFT "Mozilla Firefox" "https://download.mozilla.org/?product=firefox-latest&os=win64&lang=zh-CN"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="5" call :DOWNLOAD_SOFT "搜狗浏览器" "https://download.sogou.com/sogou_explorer/SogouExplorer_13.0.0.3380.exe"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="5" call :DOWNLOAD_SOFT "搜狗浏览器" "https://download.sogou.com/sogou_explorer/SogouExplorer_13.0.0.3380.exe"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="6" call :DOWNLOAD_SOFT "QQ浏览器" "https://dl.qq.com/breg/download/QQBrowser_Setup.exe"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="6" call :DOWNLOAD_SOFT "QQ浏览器" "https://dl.qq.com/breg/download/QQBrowser_Setup.exe"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="7" call :DOWNLOAD_SOFT "Brave浏览器" "https://github.com/brave/brave-browser/releases/download/v1.61.109/BraveBrowserSetup.exe"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="7" call :DOWNLOAD_SOFT "Brave浏览器" "https://github.com/brave/brave-browser/releases/download/v1.61.109/BraveBrowserSetup.exe"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="8" call :DOWNLOAD_SOFT "Opera浏览器" "https://net.geo.opera.com/opera/stable/win/Opera_Setup.exe"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="8" call :DOWNLOAD_SOFT "Opera浏览器" "https://net.geo.opera.com/opera/stable/win/Opera_Setup.exe"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="0" goto MAIN_MENU
result = subprocess.run(r'if "%SOFT_CHOICE%"=="0" goto MAIN_MENU', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    print(".")
    print("！输入错误，请输入0-8之间的有效编号！")
    # 执行原BAT命令：pause > nul
result = subprocess.run(r'pause > nul', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：goto BROWSER_MENU
result = subprocess.run(r'goto BROWSER_MENU', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # :: ---------------------- 新增分类6：设计创作工具菜单（7款） ----------------------
    # 执行原BAT命令：:DESIGN_MENU
result = subprocess.run(r':DESIGN_MENU', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：cls
result = subprocess.run(r'cls', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    print("==============================================")
    print("设计创作分类（7款）")
    print("==============================================")
    print("【1】Photoshop 便携版（精简）")
    print("【2】Snipaste 截图贴图工具")
    print("【3】Figma 桌面客户端")
    print("【4】Canva 可画 桌面端")
    print("【5】GIMP 免费图像编辑")
    print("【6】Axure RP 原型设计")
    print("【7】Lightshot 简易截图")
    print("【0】返回主菜单")
    print("==============================================")
    # 执行原BAT命令：set /p "SOFT_CHOICE=请输入要下载的软件编号："
result = subprocess.run(r'set /p "SOFT_CHOICE=请输入要下载的软件编号："', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="1" call :DOWNLOAD_SOFT "Photoshop便携版" "https://www.photoshopcs6.net/xiazai/pscc2024_portable.zip"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="1" call :DOWNLOAD_SOFT "Photoshop便携版" "https://www.photoshopcs6.net/xiazai/pscc2024_portable.zip"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="2" call :DOWNLOAD_SOFT "Snipaste" "https://dl.snipaste.com/Snipaste-2.7.8-x64.zip"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="2" call :DOWNLOAD_SOFT "Snipaste" "https://dl.snipaste.com/Snipaste-2.7.8-x64.zip"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="3" call :DOWNLOAD_SOFT "Figma客户端" "https://www.figma.com/desktop-download"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="3" call :DOWNLOAD_SOFT "Figma客户端" "https://www.figma.com/desktop-download"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="4" call :DOWNLOAD_SOFT "Canva可画" "https://www.canva.cn/download/windows/"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="4" call :DOWNLOAD_SOFT "Canva可画" "https://www.canva.cn/download/windows/"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="5" call :DOWNLOAD_SOFT "GIMP" "https://download.gimp.org/mirror/pub/gimp/v2.10/windows/gimp-2.10.34-setup.exe"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="5" call :DOWNLOAD_SOFT "GIMP" "https://download.gimp.org/mirror/pub/gimp/v2.10/windows/gimp-2.10.34-setup.exe"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="6" call :DOWNLOAD_SOFT "Axure RP" "https://www.axure.com/download/latest-version"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="6" call :DOWNLOAD_SOFT "Axure RP" "https://www.axure.com/download/latest-version"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="7" call :DOWNLOAD_SOFT "Lightshot" "https://app.prntscr.com/en/download.html"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="7" call :DOWNLOAD_SOFT "Lightshot" "https://app.prntscr.com/en/download.html"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="0" goto MAIN_MENU
result = subprocess.run(r'if "%SOFT_CHOICE%"=="0" goto MAIN_MENU', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    print(".")
    print("！输入错误，请输入0-7之间的有效编号！")
    # 执行原BAT命令：pause > nul
result = subprocess.run(r'pause > nul', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：goto DESIGN_MENU
result = subprocess.run(r'goto DESIGN_MENU', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # :: ---------------------- 新增分类7：安全防护工具菜单（6款） ----------------------
    # 执行原BAT命令：:SECURITY_MENU
result = subprocess.run(r':SECURITY_MENU', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：cls
result = subprocess.run(r'cls', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    print("==============================================")
    print("安全防护分类（6款）")
    print("==============================================")
    print("【1】火绒安全软件 免费版")
    print("【2】360安全卫士 纯净版")
    print("【3】腾讯电脑管家 免费版")
    print("【4】Windows Defender 升级工具")
    print("【5】Malwarebytes 恶意软件清理")
    print("【6】360杀毒 独立版")
    print("【0】返回主菜单")
    print("==============================================")
    # 执行原BAT命令：set /p "SOFT_CHOICE=请输入要下载的软件编号："
result = subprocess.run(r'set /p "SOFT_CHOICE=请输入要下载的软件编号："', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="1" call :DOWNLOAD_SOFT "火绒安全软件" "https://www.huorong.cn/download/Huorong_Setup.exe"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="1" call :DOWNLOAD_SOFT "火绒安全软件" "https://www.huorong.cn/download/Huorong_Setup.exe"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="2" call :DOWNLOAD_SOFT "360安全卫士纯净版" "https://guanjia.360.cn/纯净版/"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="2" call :DOWNLOAD_SOFT "360安全卫士纯净版" "https://guanjia.360.cn/纯净版/"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="3" call :DOWNLOAD_SOFT "腾讯电脑管家" "https://pc.qq.com/download.html"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="3" call :DOWNLOAD_SOFT "腾讯电脑管家" "https://pc.qq.com/download.html"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="4" call :DOWNLOAD_SOFT "Windows Defender升级工具" "https://support.microsoft.com/zh-cn/topic/kb5005292-update-to-windows-defender-antivirus-antimalware-platform-to-latest-version"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="4" call :DOWNLOAD_SOFT "Windows Defender升级工具" "https://support.microsoft.com/zh-cn/topic/kb5005292-update-to-windows-defender-antivirus-antimalware-platform-to-latest-version"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="5" call :DOWNLOAD_SOFT "Malwarebytes" "https://downloads.malwarebytes.com/file/mb3_setup"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="5" call :DOWNLOAD_SOFT "Malwarebytes" "https://downloads.malwarebytes.com/file/mb3_setup"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="6" call :DOWNLOAD_SOFT "360杀毒独立版" "https://sd.360.cn/download.html"
result = subprocess.run(r'if "%SOFT_CHOICE%"=="6" call :DOWNLOAD_SOFT "360杀毒独立版" "https://sd.360.cn/download.html"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if "%SOFT_CHOICE%"=="0" goto MAIN_MENU
result = subprocess.run(r'if "%SOFT_CHOICE%"=="0" goto MAIN_MENU', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    print(".")
    print("！输入错误，请输入0-6之间的有效编号！")
    # 执行原BAT命令：pause > nul
result = subprocess.run(r'pause > nul', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：goto SECURITY_MENU
result = subprocess.run(r'goto SECURITY_MENU', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # :: ---------------------- 核心下载函数（保留优化） ----------------------
    # 执行原BAT命令：:DOWNLOAD_SOFT
result = subprocess.run(r':DOWNLOAD_SOFT', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：set "SOFT_NAME=%~1"
result = subprocess.run(r'set "SOFT_NAME=%~1"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：set "DOWNLOAD_URL=%~2"
result = subprocess.run(r'set "DOWNLOAD_URL=%~2"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：set "SAVE_PATH=%DOWNLOAD_DIR%\%SOFT_NAME%.exe"
result = subprocess.run(r'set "SAVE_PATH=%DOWNLOAD_DIR%\%SOFT_NAME%.exe"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # :: 处理非exe格式的文件（如zip、msi、7z），自动提取后缀名
    # 执行原BAT命令：for /f "delims=" %%a in ("%DOWNLOAD_URL%") do (
result = subprocess.run(r'for /f "delims=" %%a in ("%DOWNLOAD_URL%") do (', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：set "FILE_EXT=%%~xa"
result = subprocess.run(r'set "FILE_EXT=%%~xa"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：)
result = subprocess.run(r')', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if not "%FILE_EXT%"=="" set "SAVE_PATH=%DOWNLOAD_DIR%\%SOFT_NAME%%FILE_EXT%"
result = subprocess.run(r'if not "%FILE_EXT%"=="" set "SAVE_PATH=%DOWNLOAD_DIR%\%SOFT_NAME%%FILE_EXT%"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    print(".")
    print("==============================================")
    print("开始下载：%SOFT_NAME%")
    print("下载链接：%DOWNLOAD_URL%")
    print("保存路径：%SAVE_PATH%")
    print("==============================================")
    print(".")
    # :: 检测文件是否已存在
    # 执行原BAT命令：if exist "%SAVE_PATH%" (
result = subprocess.run(r'if exist "%SAVE_PATH%" (', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    print("！检测到该软件已存在于下载目录，是否重新下载？")
    # 执行原BAT命令：set /p "RE_DOWNLOAD=输入 Y 重新下载，其他键取消："
result = subprocess.run(r'set /p "RE_DOWNLOAD=输入 Y 重新下载，其他键取消："', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if /i not "%RE_DOWNLOAD%"=="Y" (
result = subprocess.run(r'if /i not "%RE_DOWNLOAD%"=="Y" (', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    print("已取消下载 %SOFT_NAME%")
    # 执行原BAT命令：pause > nul
result = subprocess.run(r'pause > nul', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：goto MAIN_MENU
result = subprocess.run(r'goto MAIN_MENU', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：)
result = subprocess.run(r')', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：)
result = subprocess.run(r')', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # :: 优先使用curl下载（Win10+自带），备用bitsadmin（Win7兼容）
    # 执行原BAT命令：curl --version > nul 2>&1
result = subprocess.run(r'curl --version > nul 2>&1', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：if %errorlevel%==0 (
result = subprocess.run(r'if %errorlevel%==0 (', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：curl -L -o "%SAVE_PATH%" "%DOWNLOAD_URL%"
result = subprocess.run(r'curl -L -o "%SAVE_PATH%" "%DOWNLOAD_URL%"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：) else (
result = subprocess.run(r') else (', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：bitsadmin /transfer "%SOFT_NAME%_Download" /priority normal "%DOWNLOAD_URL%" "%SAVE_PATH%"
result = subprocess.run(r'bitsadmin /transfer "%SOFT_NAME%_Download" /priority normal "%DOWNLOAD_URL%" "%SAVE_PATH%"', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：)
result = subprocess.run(r')', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # :: 下载结果判断
    # 执行原BAT命令：if %errorlevel%==0 (
result = subprocess.run(r'if %errorlevel%==0 (', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    print(".")
    print("==============================================")
    print("恭喜！%SOFT_NAME% 下载完成！")
    print("文件保存于：%SAVE_PATH%")
    print("==============================================")
    # 执行原BAT命令：) else (
result = subprocess.run(r') else (', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    print(".")
    print("==============================================")
    print("错误！%SOFT_NAME% 下载失败！")
    print("可能原因：网络异常、下载链接失效、部分链接需手动跳转")
    print("==============================================")
    # 执行原BAT命令：)
result = subprocess.run(r')', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：pause > nul
result = subprocess.run(r'pause > nul', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：goto MAIN_MENU
result = subprocess.run(r'goto MAIN_MENU', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # :: ---------------------- 退出脚本 ----------------------
    # 执行原BAT命令：:EXIT_APP
result = subprocess.run(r':EXIT_APP', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：cls
result = subprocess.run(r'cls', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    print("==============================================")
    print("Rindows安全应用市场 V2.0，再见！")
    print("==============================================")
    # 执行原BAT命令：timeout /t 2 /nobreak > nul
result = subprocess.run(r'timeout /t 2 /nobreak > nul', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)
    # 执行原BAT命令：exit /b
result = subprocess.run(r'exit /b', shell=True, encoding='gbk', errors='ignore')
# 检查命令执行结果，非0则退出（模拟BAT的错误行为）
if result.returncode != 0:
    sys.exit(result.returncode)

    except Exception as e:
        print("执行出错：", str(e))
        sys.exit(1)

if __name__ == "__main__":
    main()
