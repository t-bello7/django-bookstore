from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_populate_uuid_values'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
