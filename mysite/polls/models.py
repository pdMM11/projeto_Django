# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models

from django.utils import timezone

import datetime


# Create your models here.


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class FusionPeptides(models.Model):
    idfusion_peptides = models.IntegerField(db_column='idFusion_Peptides', primary_key=True)  # Field name made lowercase.
    residues = models.CharField(db_column='Residues', max_length=45, blank=True, null=True)  # Field name made lowercase.
    sequence = models.CharField(db_column='Sequence', max_length=10000, blank=True, null=True)  # Field name made lowercase.
    annotation_method = models.CharField(db_column='Annotation_Method', max_length=500, blank=True, null=True)  # Field name made lowercase.
    exp_evidence = models.CharField(db_column='Exp_Evidence', max_length=500, blank=True, null=True)  # Field name made lowercase.
    protein = models.ForeignKey('Protein', models.DO_NOTHING, db_column='Protein', blank=True, null=True)  # Field name made lowercase.

    def __str__(self): return("'%s',' %s',' %s',' %s',' %s',' %s'"
        % (self.idfusion_peptides,self.residues,self.sequence,self.annotation_method,self.exp_evidence,self.protein))

    def fields(self):
        return [ f.name for f in self._meta.fields + self._meta.many_to_many ]

    class Meta:
        managed = False
        db_table = 'fusion_peptides'


class Host(models.Model):
    idhost = models.IntegerField(db_column='idHost', primary_key=True)  # Field name made lowercase.
    host = models.CharField(db_column='Host', max_length=45, blank=True, null=True)  # Field name made lowercase.


    def __str__(self): return("'%s',' %s'"
        % (self.idhost,self.host))

    def fields(self):
        return [ f.name for f in self._meta.fields + self._meta.many_to_many ]

    class Meta:
        managed = False
        db_table = 'host'


class PeptideReferences(models.Model):
    idpeptide = models.ForeignKey(FusionPeptides, models.DO_NOTHING, db_column='idPeptide', primary_key=True)  # Field name made lowercase.
    idreferences = models.ForeignKey('References', models.DO_NOTHING, db_column='idReferences')  # Field name made lowercase.

    def __str__(self): return("'%s',' %s'"
        % (self.idpeptide,self.idreferences))

    def fields(self):
        return [ f.name for f in self._meta.fields + self._meta.many_to_many ]


    class Meta:
        managed = False
        db_table = 'peptide_references'
        unique_together = (('idpeptide', 'idreferences'),)


class PeptideStructure(models.Model):
    idpeptide_structure = models.IntegerField(db_column='idPeptide_Structure', primary_key=True)  # Field name made lowercase.
    idprotein = models.ForeignKey('Protein', models.DO_NOTHING, db_column='idProtein', blank=True, null=True)  # Field name made lowercase.
    idpeptide = models.ForeignKey('FusionPeptides', models.DO_NOTHING, db_column='idPeptide', blank=True, null=True)  # Field name made lowercase.
    idstructure = models.ForeignKey('Structure', models.DO_NOTHING, db_column='idStructure', blank=True, null=True)  # Field name made lowercase.

    def __str__(self): return("'%s',' %s',' %s',' %s'"
        % (self.idpeptide_structure,self.idprotein,self.idpeptide,self.idstructure))

    def fields(self):
        return [ f.name for f in self._meta.fields + self._meta.many_to_many ]


    class Meta:
        managed = False
        db_table = 'peptide_structure'


class PollsChoice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField()
    question = models.ForeignKey('PollsQuestion', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'polls_choice'


class PollsQuestion(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'polls_question'


class Protein(models.Model):
    idprotein = models.IntegerField(db_column='idProtein', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=500, blank=True, null=True)  # Field name made lowercase.
    class_field = models.CharField(db_column='Class', max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    activation = models.CharField(db_column='Activation', max_length=45, blank=True, null=True)  # Field name made lowercase.
    name_fusogenic_unit = models.CharField(db_column='Name_Fusogenic_Unit', max_length=500, blank=True, null=True)  # Field name made lowercase.
    location_fusogenic = models.CharField(db_column='Location_Fusogenic', max_length=500, blank=True, null=True)  # Field name made lowercase.
    sequence_fusogenic = models.CharField(db_column='Sequence_fusogenic', max_length=10000, blank=True, null=True)  # Field name made lowercase.
    uniprotid = models.CharField(db_column='UniProtID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ncbiid = models.CharField(db_column='NcbiID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    idtaxonomy = models.ForeignKey('TaxanomyVirus', models.DO_NOTHING, db_column='idTaxonomy', blank=True, null=True)  # Field name made lowercase.

    def fields(self):
        return [ f.name for f in self._meta.fields + self._meta.many_to_many ]

    def __str__(self): return("'%s',' %s',' %s',' %s',' %s',' %s',' %s',' %s',' %s',' %s'"
        % (self.idprotein,self.name,self.class_field,self.activation,self.name_fusogenic_unit,
            self.location_fusogenic,self.sequence_fusogenic,self.uniprotid,self.ncbiid,self.idtaxonomy))

    class Meta:
        managed = False
        db_table = 'protein'


class ProteinReferences(models.Model):
    idprotein = models.ForeignKey(Protein, models.DO_NOTHING, db_column='idProtein', primary_key=True)  # Field name made lowercase.
    idreferences = models.ForeignKey('References', models.DO_NOTHING, db_column='idReferences')  # Field name made lowercase.

    def __str__(self): return("'%s',' %s'"
        % (self.idprotein,self.idreferences))

    def fields(self):
        return [ f.name for f in self._meta.fields + self._meta.many_to_many ]

    class Meta:
        managed = False
        db_table = 'protein_references'
        unique_together = (('idprotein', 'idreferences'),)


class References(models.Model):
    idreferences = models.IntegerField(db_column='idReferences', primary_key=True)  # Field name made lowercase.
    type_reference = models.CharField(db_column='Type_Reference', max_length=45, blank=True, null=True)  # Field name made lowercase.
    doi = models.CharField(db_column='DOI', max_length=500, blank=True, null=True)  # Field name made lowercase.

    def __str__(self): return("'%s',' %s','%s'"
        % (self.idreferences,self.type_reference,self.doi))

    def fields(self):
        return [ f.name for f in self._meta.fields + self._meta.many_to_many ]

    class Meta:
        managed = False
        db_table = 'references'


class Structure(models.Model):
    idstructure = models.IntegerField(db_column='idStructure', primary_key=True)  # Field name made lowercase.
    exp_method = models.CharField(db_column='Exp_method', max_length=100, blank=True, null=True)  # Field name made lowercase.
    repository = models.CharField(db_column='Repository', max_length=100, blank=True, null=True)  # Field name made lowercase.
    id_repository = models.CharField(db_column='ID_Repository', max_length=45, blank=True, null=True)  # Field name made lowercase.
    reference = models.ForeignKey(References, models.DO_NOTHING, db_column='Reference', blank=True, null=True)  # Field name made lowercase.

    def __str__(self): return("'%s',' %s','%s','%s','%s'"
        % (self.idstructure,self.exp_method,self.repository,self.id_repository, self.reference))

    def fields(self):
        return [ f.name for f in self._meta.fields + self._meta.many_to_many ]

    class Meta:
        managed = False
        db_table = 'structure'


class TaxHost(models.Model):
    idtaxonomy = models.ForeignKey('TaxanomyVirus', models.DO_NOTHING, db_column='idTaxonomy', primary_key=True)  # Field name made lowercase.
    idhost = models.ForeignKey(Host, models.DO_NOTHING, db_column='idHost')  # Field name made lowercase.

    def __str__(self): return("'%s',' %s'"
        % (self.idtaxonomy,self.idhost))

    def fields(self):
        return [ f.name for f in self._meta.fields + self._meta.many_to_many ]

    class Meta:
        managed = False
        db_table = 'tax_host'
        unique_together = (('idtaxonomy', 'idhost'),)


class TaxanomyVirus(models.Model):
    idtaxanomy = models.IntegerField(db_column='idTaxanomy', primary_key=True)  # Field name made lowercase.
    commonname = models.CharField(db_column='CommonName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    family = models.CharField(db_column='Family', max_length=45, blank=True, null=True)  # Field name made lowercase.
    genre = models.CharField(db_column='Genre', max_length=45, blank=True, null=True)  # Field name made lowercase.
    species = models.CharField(db_column='Species', max_length=45, blank=True, null=True)  # Field name made lowercase.
    subspecies = models.CharField(db_column='SubSpecies', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ncbitax = models.CharField(db_column='NcbiTax', max_length=45, blank=True, null=True)  # Field name made lowercase.

    def __str__(self): return("'%s',' %s',' %s',' %s',' %s',' %s',' %s'"
        % (self.idtaxanomy,self.commonname,self.family,self.genre, self.species,self.subspecies,self.ncbitax))

    def fields(self):
        return [ f.name for f in self._meta.fields + self._meta.many_to_many ]
    class Meta:
        managed = False
        db_table = 'taxanomy_virus'



class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self): return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now




class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self): return self.choice_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'