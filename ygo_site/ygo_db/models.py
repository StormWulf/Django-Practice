from django.db import models

class CardTexts(models.Model):
    """Models the 'texts' table from DB"""
    id = models.IntegerField(primary_key=True)
    name = models.CharField(blank=True, max_length=60)
    desc = models.TextField(blank=True)
    str1 = models.CharField(blank=True, max_length=100)
    str2 = models.CharField(blank=True, max_length=100)
    str3 = models.CharField(blank=True, max_length=100)
    str4 = models.CharField(blank=True, max_length=100)
    str5 = models.CharField(blank=True, max_length=100)
    str6 = models.CharField(blank=True, max_length=100)
    str7 = models.CharField(blank=True, max_length=100)
    str8 = models.CharField(blank=True, max_length=100)
    str9 = models.CharField(blank=True, max_length=100)
    str10 = models.CharField(blank=True, max_length=100)
    str11 = models.CharField(blank=True, max_length=100)
    str12 = models.CharField(blank=True, max_length=100)
    str13 = models.CharField(blank=True, max_length=100)
    str14 = models.CharField(blank=True, max_length=100)
    str15 = models.CharField(blank=True, max_length=100)
    str16 = models.CharField(blank=True, max_length=100)

    class Meta:
        """Link model to the 'texts' table from DB"""
        db_table = 'texts'
        managed = False

    def __str__(self):
        return '%s' % (self.name)

class CardDatas(models.Model):
    """Models the 'datas' table from DB"""
    id = models.ForeignKey('CardTexts', db_column='id', primary_key=True, on_delete=models.CASCADE)
    ot = models.IntegerField(blank=True)
    alias = models.IntegerField(blank=True)
    setcode = models.IntegerField(blank=True)
    card_type = models.IntegerField(db_column='type', default=0)
    attack = models.IntegerField(db_column='atk', default=0)
    defense = models.IntegerField(db_column='def', default=0)
    level = models.IntegerField(blank=True)
    race = models.IntegerField(blank=True)
    ATTRIBUTE_CHOICES = (
        ('0','Null'),
        ('1','EARTH'),
        ('2','WATER'),
        ('4','FIRE'),
        ('8','WIND'),
        ('16','LIGHT'),
        ('32','DARK'),
        ('64','DIVINE')
    )
    attribute = models.CharField(
        max_length=10,
        choices=ATTRIBUTE_CHOICES,
        default='0',
    )
    category = models.IntegerField(blank=True)

    class Meta:
        """Link model to the 'datas' table from DB"""
        db_table = 'datas'
        managed = False