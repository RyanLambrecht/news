# articles/admin.py
from django.contrib import admin
from .models import Article, Comment, Ticker

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]
    list_display = [
        "title",
        "body",
        "author",
    ]

admin.site.register(Ticker)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)