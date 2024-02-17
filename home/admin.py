from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import FooterItem
from .models import DishCategory, Dish, Gallery, Reservation

admin.site.register(FooterItem)
admin.site.register(Gallery)
admin.site.register(Reservation)

@admin.register(DishCategory)
class DishCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'position', 'is_visible')
    list_editable = ('name', 'position', 'is_visible')


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('photo_src_tag', 'name', 'slug', 'ingredients', 'description', 'price', 'is_visible', 'position', 'category')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('ingredients', 'price', 'is_visible', 'position')
    list_filter = ('category', 'is_visible')
    search_fields = ('name', 'ingredients', 'description')

    def photo_src_tag(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width=50 height=50>")

    photo_src_tag.short_description = 'Dish photo'



