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
    OT_CHOICES = (
        ('1','OCG only'),
        ('2','TCG only'),
        ('3','OCG/TCG'),
        ('4','Anime only')
    )
    ot = models.CharField(
        max_length=20,
        choices=OT_CHOICES,
        default='1',
    )
    alias = models.IntegerField(blank=True)
    setcode = models.IntegerField(blank=True)
    card_type = models.IntegerField(db_column='type', default=0)
    attack = models.IntegerField(db_column='atk', default=0)
    defense = models.IntegerField(db_column='def', default=0)
    level = models.IntegerField(blank=True)
    RACE_CHOICES = (
        ('0','Null'),
        ('1','Warrior'),
        ('2','Spellcaster'),
        ('4','Fairy'),
        ('8','Fiend'),
        ('16','Zombie'),
        ('32','Machine'),
        ('64','Aqua'),
        ('128','Pyro'),
        ('256','Rock'),
        ('512','Winged Beast'),
        ('1024','Plant'),
        ('2048','Insect'),
        ('4096','Thunder'),
        ('8192','Dragon'),
        ('16384','Beast'),
        ('32768','Beast-Warrior'),
        ('65536','Dinosaur'),
        ('131072','Fish'),
        ('262144','Sea-Serpent'),
        ('524288','Reptile'),
        ('1048576','Psychic'),
        ('2097152','Divine-Beast'),
        ('4194304','Creator God'),
        ('8388608','Wyrm'),
        ('16777216','Cyberse')
    )
    race = models.CharField(
        max_length=20,
        choices=RACE_CHOICES,
        default='0',
    )
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