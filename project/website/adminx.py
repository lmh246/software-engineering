from xadmin import views
import xadmin
from .models import CategoryTable,ForumTable,ArticleTable


# 文章表
class ArticleAdmin(object):
    list_display = ['article_title','created_time','modified_time','article_category','article_user','views']
    search_fields = ['article_title', 'article_category','article_user']
    list_filter = ['article_category']

xadmin.site.register(ArticleTable,ArticleAdmin)

# 类别表
class CategoryAdmin(object):
    list_display = ['category_name']
    search_fields = ['category_name']
    list_filter = ['category_name']


xadmin.site.register(CategoryTable,CategoryAdmin)

# 标签表
class ForumAdmin(object):
    list_display = ['forum_name']
    search_fields = ['forum_name']
    list_filter = ['forum_name']

xadmin.site.register(ForumTable,ForumAdmin)



# 创建xadmin的最基本管理器配置，并与view绑定
class BaseSetting(object):
    # 开启主题功能
    enable_themes = True
    use_bootswatch = True

# 将基本配置管理与view绑定
xadmin.site.register(views.BaseAdminView,BaseSetting)


# 全局修改，固定写法
class GlobalSettings(object):
    # 修改title
    site_title = '网红店管理系统'
    # 修改footer
    site_footer = '网红店'
    # 收起菜单
    menu_style = 'accordion'

# 将title和footer信息进行注册
xadmin.site.register(views.CommAdminView,GlobalSettings)