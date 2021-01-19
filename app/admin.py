from django.contrib import admin
from .models import BlockHeadingModel, BlockSectionModel, BlockTextModel, BlockFormModel, MailsModel


@admin.register(BlockHeadingModel, BlockSectionModel, BlockTextModel, BlockFormModel, MailsModel)
class BlockAdmin(admin.ModelAdmin):
    pass
