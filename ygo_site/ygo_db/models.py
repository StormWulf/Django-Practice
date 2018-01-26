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
    legality = models.CharField(
        db_column='ot',
        max_length=20,
        choices=OT_CHOICES,
        default='1',
    )
    alias = models.IntegerField(default=0)
    setcode = models.IntegerField(default=0)
    CARD_TYPE_CHOICES = (
        ('2','Spell / Normal'),
        ('4','Trap / Normal'),
        ('33','Effect'),
        ('65','Fusion'),
        ('97','Fusion / Effect'),
        ('129','Ritual'),
        ('130','Spell / Ritual'),
        ('161','Ritual / Effect'),
        ('545','Spirit'),
        ('673','Ritual / Spirit / Effect'),
        ('1057','Union'),
        ('2081','Gemini / Effect'),
        ('4113','Tuner'),
        ('4129','Tuner / Effect'),
        ('4161','Fusion / Tuner'),
        ('8193','Synchro'),
        ('8225','Synchro / Effect'),
        ('12321','Synchro / Tuner / Effect'),
        ('16401','Token'),
        ('65538','Spell / Quick-Play'),
        ('131074','Spell / Continuous'),
        ('131076','Trap / Continuous'),
        ('262146','Spell / Equip'),
        ('524290','Spell / Field'),
        ('1048580','Trap / Counter'),
        ('2097185','Flip / Effect'),
        ('2101281','Flip / Tuner / Effect'),
        ('4194337','Toon / Effect'),
        ('8388609','Xyz'),
        ('8388641','Xyz / Effect'),
        ('16777233','Pendulum / Normal'),
        ('16777249','Pendulum / Effect'),
        ('16777313','Fusion / Pendulum / Effect'),
        ('16781313','Pendulum / Tuner / Normal'),
        ('16781345','Pendulum / Tuner / Effect'),
        ('16785441','Synchro / Pendulum / Effect'),
        ('18874401','Pendulum / Flip / Effect'),
        ('25165857','Xyz / Pendulum / Effect'),
        ('67108881','Link'),
        ('67108897','Link / Effect')
    )
    card_type = models.CharField(
        db_column='type',
        max_length=50,
        choices=CARD_TYPE_CHOICES,
        default='2',
    )
    attack = models.IntegerField(db_column='atk', default=0)
    defense = models.IntegerField(db_column='def', default=0)
    level = models.IntegerField(default=0)
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
    category = models.IntegerField(default=0)

    class Meta:
        """Link model to the 'datas' table from DB"""
        db_table = 'datas'
        managed = False