from django.db import migrations

def add_default_categories(apps, schema_editor):
    # Get the model
    BlogCategory = apps.get_model('content', 'BlogCategory')
    
    # Create default categories
    default_categories = [
        "Technology",
        "Business",
        "Health",
        "Education",
        "Entertainment"
    ]
    
    for category_name in default_categories:
        BlogCategory.objects.get_or_create(title=category_name)

def remove_default_categories(apps, schema_editor):
    # Function to reverse the migration if needed
    BlogCategory = apps.get_model('content', 'BlogCategory')
    BlogCategory.objects.filter(title__in=[
        "Technology",
        "Business",
        "Health",
        "Education",
        "Entertainment"
    ]).delete()

class Migration(migrations.Migration):
    dependencies = [
        ('content', '0001_initial'),  # Make sure this points to your last migration
    ]

    operations = [
        migrations.RunPython(add_default_categories, remove_default_categories),
    ]