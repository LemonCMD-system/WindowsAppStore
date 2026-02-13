import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import requests
import json
import threading
import os
import urllib.request
from urllib.parse import urlparse
import webbrowser

class WindowsAppStore:
    def __init__(self, root):
        self.root = root
        self.root.title("Windows应用商店")
        self.root.geometry("1200x800")
        
        # 应用数据
        self.apps_data = []
        self.current_category = "0"  # 默认全部应用
        self.current_page = 1
        self.items_per_page = 28
        
        # 分类ID和名称对应关系
        self.categories = {
            "0": "全部应用",
            "10": "游戏",
            "20": "视频",
            "30": "浏览器",
            "40": "聊天",
            "50": "输入法",
            "60": "下载",
            "70": "音乐",
            "80": "图片",
            "90": "安全",
            "100": "解压刻录",
            "110": "系统",
            "120": "驱动",
            "130": "办公",
            "140": "编程",
            "150": "股票网银",
            "160": "剪辑",
            "170": "网络",
            "180": "桌面"
        }
        
        # 创建GUI界面
        self.create_widgets()
        
        # 加载初始数据
        self.load_apps()
    
    def create_widgets(self):
        # 顶部搜索栏
        search_frame = ttk.Frame(self.root, padding="10")
        search_frame.pack(fill=tk.X)
        
        ttk.Label(search_frame, text="搜索应用:").pack(side=tk.LEFT, padx=5)
        self.search_entry = ttk.Entry(search_frame, width=50)
        self.search_entry.pack(side=tk.LEFT, padx=5)
        self.search_button = ttk.Button(search_frame, text="搜索", command=self.search_apps)
        self.search_button.pack(side=tk.LEFT, padx=5)
        
        # 分类导航
        category_frame = ttk.Frame(self.root, padding="10")
        category_frame.pack(fill=tk.X)
        
        ttk.Label(category_frame, text="分类:").pack(side=tk.LEFT, padx=5)
        self.category_combobox = ttk.Combobox(category_frame, values=list(self.categories.values()), width=20)
        self.category_combobox.current(0)
        self.category_combobox.bind("<<ComboboxSelected>>", self.on_category_change)
        self.category_combobox.pack(side=tk.LEFT, padx=5)
        
        # 应用列表
        self.apps_frame = ttk.Frame(self.root)
        self.apps_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # 创建树状视图
        self.apps_tree = ttk.Treeview(self.apps_frame, columns=("名称", "版本", "大小", "评分", "更新时间"), show="headings")
        self.apps_tree.heading("名称", text="应用名称")
        self.apps_tree.heading("版本", text="版本")
        self.apps_tree.heading("大小", text="大小")
        self.apps_tree.heading("评分", text="评分")
        self.apps_tree.heading("更新时间", text="更新时间")
        
        self.apps_tree.column("名称", width=300)
        self.apps_tree.column("版本", width=100)
        self.apps_tree.column("大小", width=100)
        self.apps_tree.column("评分", width=100)
        self.apps_tree.column("更新时间", width=150)
        
        self.apps_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # 滚动条
        scrollbar = ttk.Scrollbar(self.apps_frame, orient=tk.VERTICAL, command=self.apps_tree.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.apps_tree.configure(yscrollcommand=scrollbar.set)
        
        # 右键菜单
        self.tree_menu = tk.Menu(self.root, tearoff=0)
        self.tree_menu.add_command(label="查看详情", command=self.show_app_detail)
        self.tree_menu.add_command(label="下载", command=self.download_app)
        self.tree_menu.add_command(label="打开官网", command=self.open_app_website)
        self.apps_tree.bind("<Button-3>", self.show_tree_menu)
        
        # 底部状态栏
        status_frame = ttk.Frame(self.root, padding="10")
        status_frame.pack(fill=tk.X)
        
        self.status_label = ttk.Label(status_frame, text="就绪")
        self.status_label.pack(side=tk.LEFT)
        
        # 分页控制
        pagination_frame = ttk.Frame(status_frame)
        pagination_frame.pack(side=tk.RIGHT)
        
        self.prev_button = ttk.Button(pagination_frame, text="上一页", command=self.prev_page)
        self.prev_button.pack(side=tk.LEFT, padx=5)
        self.page_label = ttk.Label(pagination_frame, text="第1页")
        self.page_label.pack(side=tk.LEFT, padx=5)
        self.next_button = ttk.Button(pagination_frame, text="下一页", command=self.next_page)
        self.next_button.pack(side=tk.LEFT, padx=5)
    
    def show_tree_menu(self, event):
        try:
            self.apps_tree.selection_set(self.apps_tree.identify_row(event.y))
            self.tree_menu.post(event.x_root, event.y_root)
        except:
            pass
    
    def on_category_change(self, event):
        category_name = self.category_combobox.get()
        # 找到对应的分类ID
        for cid, name in self.categories.items():
            if name == category_name:
                self.current_category = cid
                self.current_page = 1
                self.load_apps()
                break
    
    def load_apps(self):
        """加载应用数据"""
        def load_thread():
            try:
                self.status_label.config(text="正在加载应用数据...")
                
                url = "https://s.pcmgr.qq.com/tapi/web/softlistcgi.php"
                params = {
                    "c": self.current_category,
                    "sort": 0,
                    "offset": (self.current_page - 1) * self.items_per_page,
                    "limit": self.items_per_page,
                    "noplugin": 0
                }
                
                response = requests.get(url, params=params)
                # 处理JSONP响应
                response_text = response.text
                if response_text.startswith("loadList(") and response_text.endswith(")"):
                    json_data = json.loads(response_text[9:-1])
                
                if json_data.get("code") == 0:
                    self.apps_data = json_data.get("list", [])
                    self.update_apps_tree()
                    self.page_label.config(text=f"第{self.current_page}页")
                    self.status_label.config(text=f"加载完成，共找到{json_data.get('total', 0)}个应用")
                else:
                    self.status_label.config(text="加载失败")
                    
            except Exception as e:
                self.status_label.config(text=f"加载出错: {str(e)}")
        
        threading.Thread(target=load_thread, daemon=True).start()
    
    def update_apps_tree(self):
        """更新应用列表"""
        # 清空现有数据
        for item in self.apps_tree.get_children():
            self.apps_tree.delete(item)
        
        # 添加新数据
        for app in self.apps_data:
            self.apps_tree.insert("", tk.END, values=(
                app.get("sn", ""),
                app.get("ver", ""),
                app.get("fs", ""),
                f"{app.get('star', 0)}/5.0",
                app.get("ux", "")
            ), iid=app.get("s"))
    
    def search_apps(self):
        """搜索应用"""
        keyword = self.search_entry.get().strip()
        if not keyword:
            messagebox.showwarning("警告", "请输入搜索关键词")
            return
        
        def search_thread():
            try:
                self.status_label.config(text="正在搜索...")
                
                url = "https://s.pcmgr.qq.com/tapi/web/searchcgi.php"
                params = {
                    "type": "search",
                    "keyword": keyword,
                    "page": 1,
                    "pernum": 50,
                    "more": 0
                }
                
                response = requests.get(url, params=params)
                # 处理JSONP响应
                response_text = response.text
                if response_text.startswith("searchCallback(") and response_text.endswith(")"):
                    json_data = json.loads(response_text[15:-1])
                
                if json_data.get("code") == 0:
                    self.apps_data = json_data.get("list", [])
                    self.update_apps_tree()
                    self.status_label.config(text=f"搜索完成，找到{len(self.apps_data)}个相关应用")
                else:
                    self.status_label.config(text="搜索失败")
                    
            except Exception as e:
                self.status_label.config(text=f"搜索出错: {str(e)}")
        
        threading.Thread(target=search_thread, daemon=True).start()
    
    def get_selected_app(self):
        """获取选中的应用"""
        selected_item = self.apps_tree.selection()
        if not selected_item:
            messagebox.showwarning("警告", "请先选择一个应用")
            return None
        
        app_id = selected_item[0]
        for app in self.apps_data:
            if app.get("s") == app_id:
                return app
        
        return None
    
    def show_app_detail(self):
        """显示应用详情"""
        app = self.get_selected_app()
        if not app:
            return
        
        detail_window = tk.Toplevel(self.root)
        detail_window.title(f"{app.get('sn')} - 应用详情")
        detail_window.geometry("800x600")
        
        # 创建详情内容
        detail_frame = ttk.Frame(detail_window, padding="20")
        detail_frame.pack(fill=tk.BOTH, expand=True)
        
        # 应用图标和基本信息
        top_frame = ttk.Frame(detail_frame)
        top_frame.pack(fill=tk.X, pady=10)
        
        # 图标
        if app.get("lg"):
            try:
                # 下载图标
                icon_url = app.get("lg")
                icon_path = f"/tmp/{app.get('s')}_icon.png"
                urllib.request.urlretrieve(icon_url, icon_path)
                
                # 显示图标
                icon_img = tk.PhotoImage(file=icon_path).subsample(2, 2)
                icon_label = ttk.Label(top_frame, image=icon_img)
                icon_label.image = icon_img
                icon_label.pack(side=tk.LEFT, padx=10)
            except:
                pass
        
        # 基本信息
        info_frame = ttk.Frame(top_frame)
        info_frame.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        ttk.Label(info_frame, text=f"应用名称: {app.get('sn')}", font=("Arial", 16, "bold")).pack(anchor=tk.W, pady=5)
        ttk.Label(info_frame, text=f"版本: {app.get('ver')}").pack(anchor=tk.W, pady=2)
        ttk.Label(info_frame, text=f"大小: {app.get('fs')}").pack(anchor=tk.W, pady=2)
        ttk.Label(info_frame, text=f"评分: {app.get('star', 0)}/5.0").pack(anchor=tk.W, pady=2)
        ttk.Label(info_frame, text=f"更新时间: {app.get('ux')}").pack(anchor=tk.W, pady=2)
        ttk.Label(info_frame, text=f"腾讯软件: {'是' if app.get('tx') == 1 else '否'}").pack(anchor=tk.W, pady=2)
        
        # 下载按钮
        download_button = ttk.Button(info_frame, text="下载", command=lambda: self.download_app(app))
        download_button.pack(anchor=tk.W, pady=10)
        
        # 详情描述
        ttk.Label(detail_frame, text="应用介绍:", font=("Arial", 12, "bold")).pack(anchor=tk.W, pady=5)
        
        # 这里应该从详情页获取更多信息，但由于API限制，我们先显示占位符
        detail_text = scrolledtext.ScrolledText(detail_frame, width=80, height=20)
        detail_text.pack(fill=tk.BOTH, expand=True, pady=5)
        detail_text.insert(tk.END, "应用详情请访问官方网站查看...\n\n")
        detail_text.insert(tk.END, f"官方网站: {app.get('detailUrl', '暂无')}")
        detail_text.config(state=tk.DISABLED)
        
        # 打开官网按钮
        if app.get('detailUrl'):
            website_button = ttk.Button(detail_frame, text="打开官网", command=lambda: webbrowser.open(app.get('detailUrl')))
            website_button.pack(anchor=tk.W, pady=5)
    
    def download_app(self, app=None):
        """下载应用"""
        if not app:
            app = self.get_selected_app()
            if not app:
                return
        
        download_url = app.get("url")
        if not download_url:
            messagebox.showerror("错误", "该应用没有下载链接")
            return
        
        def download_thread():
            try:
                self.status_label.config(text=f"正在下载 {app.get('sn')}...")
                
                # 获取文件名
                parsed_url = urlparse(download_url)
                filename = os.path.basename(parsed_url.path)
                if not filename:
                    filename = f"{app.get('s')}.exe"
                
                # 下载文件
                save_path = os.path.join(os.path.expanduser("~"), "Downloads", filename)
                urllib.request.urlretrieve(download_url, save_path, reporthook=self.download_progress)
                
                messagebox.showinfo("下载完成", f"应用已下载完成，保存到:\n{save_path}")
                self.status_label.config(text="下载完成")
                
                # 询问是否打开文件
                if messagebox.askyesno("打开文件", "是否打开下载的文件?"):
                    os.startfile(save_path)
                    
            except Exception as e:
                messagebox.showerror("下载失败", f"下载出错: {str(e)}")
                self.status_label.config(text="下载失败")
        
        threading.Thread(target=download_thread, daemon=True).start()
    
    def download_progress(self, block_num, block_size, total_size):
        """下载进度回调"""
        downloaded = block_num * block_size
        if total_size > 0:
            progress = (downloaded / total_size) * 100
            self.status_label.config(text=f"下载进度: {progress:.1f}%")
    
    def prev_page(self):
        """上一页"""
        if self.current_page > 1:
            self.current_page -= 1
            self.load_apps()
    
    def open_app_website(self):
        """打开应用官网"""
        app = self.get_selected_app()
        if not app:
            return
        
        if app.get("detailUrl"):
            webbrowser.open(app.get("detailUrl"))
        else:
            messagebox.showwarning("警告", "该应用没有官网链接")

    def next_page(self):
        """下一页"""
        self.current_page += 1
        self.load_apps()

if __name__ == "__main__":
    root = tk.Tk()
    app = WindowsAppStore(root)
    root.mainloop()