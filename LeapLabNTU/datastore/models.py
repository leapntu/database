from django.db import models
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from address.models import AddressField
from django.core.validators import MinValueValidator, MaxValueValidator
import django
from django.utils.crypto import get_random_string

def slug_save(obj):
	if not obj.slug:
		obj.slug = get_random_string(8)
		slug_is_wrong = True
		while slug_is_wrong:
			slug_is_wrong = False
			other_objs_with_slug = type(obj).objects.filter(slug = obj.slug)
			if len(other_objs_with_slug) > 0:
				slug_is_wrong = True
			if slug_is_wrong:
				obj.slug = get_random_string(8)

class PercentField(models.FloatField):
    """
    Float field that ensures field value is in the range 0-100.
    """
    default_validators = [
        MinValueValidator(0),
        MaxValueValidator(100),
    ]

class DateTimeKeeperModel(models.Model):
	class Meta:
		abstract = True
	last_modified = models.DateTimeField(auto_now = True)
	created_at = models.DateTimeField(auto_now_add = True)
	dateTime = models.DateTimeField(default = django.utils.timezone.now)

class Occupation(models.Model):
	def __str__(self):
		return self.name
	name = models.TextField()

class Person(models.Model):
	last_modified = models.DateTimeField(auto_now = True)
	created_at = models.DateTimeField(auto_now_add = True)
	country_of_birth = CountryField(blank = True, null = True)

class Parent(Person):
	date_of_migration_to_singapore = models.DateField(blank = True, null = True)
	languages_spoken_while_growing_up = models.ManyToManyField('Language', related_name = 'parent', blank = True)
	education = models.TextField(blank = True, null = True)
	occupation = models.ForeignKey(Occupation, null = True, blank = True)
	email_address = models.EmailField(blank = True, null = True)
	contact_number = PhoneNumberField(blank = True, null = True)

class Language(models.Model):
	def __str__(self):
		return self.name
	name = models.CharField(max_length = 35)

class Mother(Parent):
	def __str__(self):
		if self.name:
			return self.name
		babies = Baby.objects.filter(mother__pk = self.pk)
		if not babies.count():
			return 'Mother without any assigned baby'
		else:
			return "Mother of " + babies[0].first_name + (" " + babies[0].last_name if babies[0].last_name else "")
	household = models.ForeignKey('Household', related_name = 'mothers', blank = True, null = True)
	name = models.TextField(blank = True, null = True)

class Father(Parent):
	def __str__(self):
		if self.name:
			return self.name
		babies = Baby.objects.filter(father__pk = self.pk)
		if not babies.count():
			return 'Father without any assigned baby'
		else:
			return "Father of " + babies[0].first_name + (" " + babies[0].last_name if babies[0].last_name else "")
	household = models.ForeignKey('Household', related_name = 'fathers', blank = True, null = True)
	name = models.TextField(blank = True, null = True)

class LanguagesKnownByFatherInOrderOfFluency(models.Model):
	def __str__(self):
		return str(self.father) + " - " + str(self.language) + " - " + str(self.order)
	father = models.ForeignKey(Father)
	language = models.ForeignKey(Language)
	order = models.PositiveSmallIntegerField()

class LanguagesKnownByMotherInOrderOfFluency(models.Model):
	def __str__(self):
		return str(self.mother) + " - " + str(self.language) + " - " + str(self.order)
	mother = models.ForeignKey(Mother)
	language = models.ForeignKey(Language)
	order = models.PositiveSmallIntegerField()

class Baby(Person):
	SEX = [
		("Male", "Male"),
		("Female", "Female"),
	]
	def __str__(self):
		return self.first_name + " " + (self.last_name if self.last_name else "")
	first_name = models.CharField(max_length = 35)
	last_name = models.CharField(max_length = 35, blank = True, null = True)
	date_of_birth = models.DateField(blank = True, null = True)
	has_sight_difficulties = models.NullBooleanField(blank = True, null = True)
	has_hearing_difficulties = models.NullBooleanField(blank = True, null = True)
	father = models.ForeignKey(Father, related_name = 'baby', blank = True, null = True)
	mother = models.ForeignKey(Mother, related_name = 'baby', blank = True, null = True)
	sex = models.CharField(max_length = 6, choices = SEX, blank = True, null = True)
	slug = models.SlugField(max_length = 8, blank = True)
	def save(self, *args, **kwargs):
		slug_save(self)
		super().save(*args, **kwargs)
	household = models.ForeignKey('Household', related_name = 'babies', blank = True, null = True)
	due_date = models.DateField(blank = True, null = True)
	medical_history_notes = models.TextField(blank = True, null = True)

class BabyLanguageProfile(DateTimeKeeperModel):
	def __str__(self):
		return str(self.baby) + " - " + str(self.dateTime)
	LANGUAGE_PREVALENCE_ALL_ENGLISH = 1
	LANGUAGE_PREVALENCE_HALF_ENGLISH_HALF_OTHER_LANGUAGE = 4
	LANGUAGE_PREVALENCE_ALL_SECOND_LANGUAGE = 7
	CHOICES_LANGUAGE_PREVALENCE = (
		(LANGUAGE_PREVALENCE_ALL_ENGLISH, 'All English'),
		(2, '2'),
		(3, '3'),
		(LANGUAGE_PREVALENCE_HALF_ENGLISH_HALF_OTHER_LANGUAGE, 'Half English/half other language'),
		(5, '5'),
		(6, '6'),
		(LANGUAGE_PREVALENCE_ALL_SECOND_LANGUAGE, 'All 2nd Language'),
	)
	baby = models.ForeignKey(Baby, related_name = 'language_profiles')
	language_spoken_in_home_between_parents = models.IntegerField(choices = CHOICES_LANGUAGE_PREVALENCE, blank = True, null = True)
	language_spoken_in_home_between_siblings = models.IntegerField(choices = CHOICES_LANGUAGE_PREVALENCE, blank = True, null = True)
	language_spoken_in_home_between_maternal_grandparents = models.IntegerField(choices = CHOICES_LANGUAGE_PREVALENCE, blank = True, null = True)
	language_spoken_in_home_between_paternal_grandparents = models.IntegerField(choices = CHOICES_LANGUAGE_PREVALENCE, blank = True, null = True)
	language_spoken_in_home_between_parents_and_other_relatives = models.IntegerField(choices = CHOICES_LANGUAGE_PREVALENCE, blank = True, null = True)
	language_spoken_in_home_between_parents_and_other_caregivers = models.IntegerField(choices = CHOICES_LANGUAGE_PREVALENCE, blank = True, null = True)
	language_used_in_home_for_reading = models.IntegerField(choices = CHOICES_LANGUAGE_PREVALENCE, blank = True, null = True)
	language_used_in_home_for_listening_to_radio_or_music = models.IntegerField(choices = CHOICES_LANGUAGE_PREVALENCE, blank = True, null = True)
	language_used_in_home_for_watching_tv_or_video = models.IntegerField(choices = CHOICES_LANGUAGE_PREVALENCE, blank = True, null = True)
	language_used_in_home_for_using_internet_or_smartphones = models.IntegerField(choices = CHOICES_LANGUAGE_PREVALENCE, blank = True, null = True)
	language_used_in_home_for_reading_stories_to_child = models.IntegerField(choices = CHOICES_LANGUAGE_PREVALENCE, blank = True, null = True)
	number_of_weekly_hours_spent_with_child_by_mother = models.FloatField(blank = True, null = True, validators = [MinValueValidator(0), MaxValueValidator(168)])
	number_of_weekly_hours_spent_with_child_by_father = models.FloatField(blank = True, null = True, validators = [MinValueValidator(0), MaxValueValidator(168)])
	number_of_weekly_hours_spent_with_child_by_siblings = models.FloatField(blank = True, null = True, validators = [MinValueValidator(0), MaxValueValidator(168)])
	number_of_weekly_hours_spent_with_maternal_grandparents = models.FloatField(blank = True, null = True, validators = [MinValueValidator(0), MaxValueValidator(168)])
	number_of_weekly_hours_spent_with_paternal_grandparents = models.FloatField(blank = True, null = True, validators = [MinValueValidator(0), MaxValueValidator(168)])
	number_of_weekly_hours_spent_with_child_by_other_relatives = models.FloatField(blank = True, null = True, validators = [MinValueValidator(0), MaxValueValidator(168)])
	number_of_weekly_hours_spent_with_child_by_school = models.FloatField(blank = True, null = True, validators = [MinValueValidator(0), MaxValueValidator(168)])
	language_child_speaks_to_mother = models.IntegerField(choices = CHOICES_LANGUAGE_PREVALENCE, blank = True, null = True)
	language_child_speaks_to_father = models.IntegerField(choices = CHOICES_LANGUAGE_PREVALENCE, blank = True, null = True)
	language_child_speaks_to_siblings = models.IntegerField(choices = CHOICES_LANGUAGE_PREVALENCE, blank = True, null = True)
	language_child_speaks_to_maternal_grandparents = models.IntegerField(choices = CHOICES_LANGUAGE_PREVALENCE, blank = True, null = True)
	language_child_speaks_to_paternal_grandparents = models.IntegerField(choices = CHOICES_LANGUAGE_PREVALENCE, blank = True, null = True)
	language_child_speaks_to_other_relatives = models.IntegerField(choices = CHOICES_LANGUAGE_PREVALENCE, blank = True, null = True)
	language_child_speaks_to_friends = models.IntegerField(choices = CHOICES_LANGUAGE_PREVALENCE, blank = True, null = True)
	language_child_uses_for_reading = models.IntegerField(choices = CHOICES_LANGUAGE_PREVALENCE, blank = True, null = True)
	language_child_uses_for_listening_to_radio_or_music = models.IntegerField(choices = CHOICES_LANGUAGE_PREVALENCE, blank = True, null = True)
	language_child_uses_for_watching_tv_or_video = models.IntegerField(choices = CHOICES_LANGUAGE_PREVALENCE, blank = True, null = True)
	language_child_uses_for_watching_tv_or_video = models.IntegerField(choices = CHOICES_LANGUAGE_PREVALENCE, blank = True, null = True)
	language_child_uses_internet_or_smartphones_in = models.IntegerField(choices = CHOICES_LANGUAGE_PREVALENCE, blank = True, null = True)
	language_child_uses_overall_to_speak_at_home = models.IntegerField(choices = CHOICES_LANGUAGE_PREVALENCE, blank = True, null = True)
	language_child_uses_overall_to_speak_within_your_community = models.IntegerField(choices = CHOICES_LANGUAGE_PREVALENCE, blank = True, null = True)

class LanguageProficiencyOfMothersInSpeaking(models.Model):
	def __str__(self):
		return str(self.mother) + " - " + str(self.language)
	mother = models.ForeignKey(Mother)
	language = models.ForeignKey(Language)
	percentage = PercentField()

class LanguageProficiencyOfMothersInUnderstanding(models.Model):
	def __str__(self):
		return str(self.mother) + " - " + str(self.language)
	mother = models.ForeignKey(Mother)
	language = models.ForeignKey(Language)
	percentage = PercentField()

class LanguageProficiencyOfMothersInWriting(models.Model):
	def __str__(self):
		return str(self.mother) + " - " + str(self.language)
	mother = models.ForeignKey(Mother)
	language = models.ForeignKey(Language)
	percentage = PercentField()

class LanguageProficiencyOfMothersInReading(models.Model):
	def __str__(self):
		return str(self.mother) + " - " + str(self.language)
	mother = models.ForeignKey(Mother)
	language = models.ForeignKey(Language)
	percentage = PercentField()

class LanguageProficiencyOfFathersInSpeaking(models.Model):
	def __str__(self):
		return str(self.father) + " - " + str(self.language)
	father = models.ForeignKey(Father)
	language = models.ForeignKey(Language)
	percentage = PercentField()

class LanguageProficiencyOfFathersInUnderstanding(models.Model):
	def __str__(self):
		return str(self.father) + " - " + str(self.language)
	father = models.ForeignKey(Father)
	language = models.ForeignKey(Language)
	percentage = PercentField()

class LanguageProficiencyOfFathersInWriting(models.Model):
	def __str__(self):
		return str(self.father) + " - " + str(self.language)
	father = models.ForeignKey(Father)
	language = models.ForeignKey(Language)
	percentage = PercentField()

class LanguageProficiencyOfFathersInReading(models.Model):
	def __str__(self):
		return str(self.father) + " - " + str(self.language)
	father = models.ForeignKey(Father)
	language = models.ForeignKey(Language)
	percentage = PercentField()

class LanguageSpokenToBabyByMother(models.Model):
	def __str__(self):
		return str(self.language_profile) + " - " + str(self.language) + " - " + str(self.percentage)
	language_profile = models.ForeignKey(BabyLanguageProfile, related_name = 'languages_spoken_to_baby_by_mother')
	language = models.ForeignKey(Language)
	percentage = PercentField()

class LanguageSpokenToBabyByFather(models.Model):
	def __str__(self):
		return str(self.language_profile) + " - " + str(self.language) + " - " + str(self.percentage)
	language_profile = models.ForeignKey(BabyLanguageProfile, related_name = 'languages_spoken_to_baby_by_father')
	language = models.ForeignKey(Language)
	percentage = PercentField()

class LanguageSpokenToBabyBySiblings(models.Model):
	def __str__(self):
		return str(self.language_profile) + " - " + str(self.language) + " - " + str(self.percentage)
	language_profile = models.ForeignKey(BabyLanguageProfile, related_name = 'languages_spoken_to_baby_by_siblings')
	language = models.ForeignKey(Language)
	percentage = PercentField()

class LanguageSpokenToBabyByMaternalGrandparents(models.Model):
	def __str__(self):
		return str(self.language_profile) + " - " + str(self.language) + " - " + str(self.percentage)
	language_profile = models.ForeignKey(BabyLanguageProfile, related_name = 'languages_spoken_to_baby_by_maternal_grandparents')
	language = models.ForeignKey(Language)
	percentage = PercentField()

class LanguageSpokenToBabyByPaternalGrandparents(models.Model):
	def __str__(self):
		return str(self.language_profile) + " - " + str(self.language) + " - " + str(self.percentage)
	language_profile = models.ForeignKey(BabyLanguageProfile, related_name = 'languages_spoken_to_baby_by_paternal_grandparents')
	language = models.ForeignKey(Language)
	percentage = PercentField()

class LanguageSpokenToBabyByRelatives(models.Model):
	def __str__(self):
		return str(self.language_profile) + " - " + str(self.language) + " - " + str(self.percentage)
	language_profile = models.ForeignKey(BabyLanguageProfile, related_name = 'languages_spoken_to_baby_by_relatives')
	language = models.ForeignKey(Language)
	percentage = PercentField()

class LanguageSpokenToBabyByOtherCaregivers(models.Model):
	def __str__(self):
		return str(self.language_profile) + " - " + str(self.language) + " - " + str(self.percentage)
	language_profile = models.ForeignKey(BabyLanguageProfile, related_name = 'languages_spoken_to_baby_by_other_caregivers')
	language = models.ForeignKey(Language)
	percentage = PercentField()

class LanguageSpokenToBabyInSchool(models.Model):
	def __str__(self):
		return str(self.language_profile) + " - " + str(self.language) + " - " + str(self.percentage)
	language_profile = models.ForeignKey(BabyLanguageProfile, related_name = 'languages_spoken_to_baby_in_school')
	language = models.ForeignKey(Language)
	percentage = PercentField()

class Session(models.Model):
	def __str__(self):
		return str(self.baby) + " - " + str(self.date)
	baby = models.ForeignKey(Baby)
	date = models.DateField(blank = True, null = True)

class Study(models.Model):
	def __str__(self):
		return str(self.session) + " - " + self.study
	CHOICE_STUDY = (
		('NARRATION', 'NARRATION'),
		('PUPPET SHOW', 'PUPPET SHOW'),
		('FORWARD-BACKWARD', 'FORWARD-BACKWARD'),
		('NonAdj', 'NonAdj'),
	)
	study = models.CharField(max_length = 20, choices = CHOICE_STUDY)
	session = models.ForeignKey(Session)
	recording = models.FileField(blank = True, null = True)

class Household(models.Model):
	def __str__(self):
		baby_occupants_string_representation = ', '.join([str(baby) for baby in self.babies.all()])
		father_occupants_string_representation = ', '.join([str(father) for father in self.fathers.all()])
		mother_occupants_string_representation = ', '.join([str(mother) for mother in self.mothers.all()])
		household_members_string_representation = ', '.join([str(household_member) for household_member in self.members.all()])
		return (', '.join(
			([baby_occupants_string_representation] if baby_occupants_string_representation else [])
			+ ([father_occupants_string_representation] if father_occupants_string_representation else [])
			+ ([mother_occupants_string_representation] if mother_occupants_string_representation else [])
			+ ([household_members_string_representation] if household_members_string_representation else [])
		))
	address = AddressField(blank = True, null = True)
	house_phone = PhoneNumberField(blank = True, null = True)
	notes = models.TextField(blank = True, null = True)

class HouseholdMember(models.Model):
	def __str__(self):
		return self.relationship_with_baby
	relationship_with_baby = models.TextField()
	email_address = models.EmailField(blank = True, null = True)
	contact_number = PhoneNumberField(blank = True, null = True)
	household = models.ForeignKey(Household, related_name = 'members', blank = True, null = True)