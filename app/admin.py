from django.contrib import admin
from .models import BlockHeadingModel, BlockSectionModel, BlockTextModel, BlockFormModel


@admin.register(BlockHeadingModel, BlockSectionModel, BlockTextModel, BlockFormModel)
class BlockAdmin(admin.ModelAdmin):
    pass
